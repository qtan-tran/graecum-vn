#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_anki_deck.py – sinh Anki deck (.apkg) cho Graecum VN từ vocab TSV.

Thuần thư viện chuẩn Python (sqlite3, zipfile, hashlib, json, csv) – không cần
cài gói ngoài. File .apkg theo định dạng schema 11 (collection.anki2) mà Anki
Desktop / AnkiDroid / AnkiMobile import trực tiếp.

Cách chạy:
    python3 tools/gen_anki_deck.py
    python3 tools/gen_anki_deck.py --tsv vocab/vocab-01-10.tsv --out vocab/graecum-vn-01-10.apkg

Sau đó mở file .apkg bằng Anki: File > Import (hoặc nhấp đúp file).

Nguồn dữ liệu: vocab TSV trích từ mục "Từ vựng trọng tâm" của Lesson 1–10
(portal Graecum VN). Từ trùng headword giữa các bài (từ ôn tập) được gộp
thành một note, mang tag của mọi bài chứa nó. GUID ổn định theo headword:
sinh lại deck nhiều lần không tạo note trùng trong bộ sưu tập.

License: code MIT; nội dung TSV/deck CC BY-SA 4.0.
Credit: Graecum VN – Trần Quốc Tân, https://github.com/qtan-tran/graecum-vn
"""

import argparse
import csv
import hashlib
import itertools
import json
import os
import sqlite3
import sys
import tempfile
import time
import zipfile
from collections import OrderedDict

DECK_ID = 1746801951   # ID cố định: deck ổn định qua mỗi lần sinh lại
MODEL_ID = 1746801952   # ID cố định của note type "Graecum VN Vocabulary"
DECK_NAME = "Graecum VN – Graecum I (Bài 1–10)"
DECK_DESCRIPTION = (
    "Khi cite hoặc tái sử dụng, vui lòng ghi: "
    "\"Graecum VN – Trần Quốc Tân, https://github.com/qtan-tran/graecum-vn\"."
)


def configure_deck(name):
    """Đổi tên deck đích và suy ra ID bền (md5) – cho deck nhóm 5 bài (Ôn tập)."""
    global DECK_ID, DECK_NAME
    DECK_NAME = name
    digest = hashlib.md5(("graecum-vn-deck:" + name).encode("utf-8")).digest()
    DECK_ID = int.from_bytes(digest[:3], "big") | (1 << 23)

LATEX_PRE = (
    "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n"
    "\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n"
    "\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n"
)
LATEX_POST = "\\end{document}"

MODEL_CSS = """
.card { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 20px;
        text-align: center; color: #1f2937; background-color: #f8fafc; }
.gk { font-family: 'Palatino Linotype', 'Book Antiqua', Gentium, 'Times New Roman', serif;
      font-size: 1.35em; color: #14532d; }
.tr { font-style: italic; color: #475569; }
.en { color: #166534; }
.vi { color: #1f2937; }
.note { font-size: 0.85em; color: #64748b; }
.badge { display: inline-block; font-size: 0.75em; color: #b45309;
         border: 1px solid #cbd5e1; border-radius: 8px; padding: 1px 8px; margin-top: 8px; }
"""

QFMT = '<div class="gk">{{Greek}}</div>'
AFMT = """
<div class="gk">{{Greek}}</div>
<div class="tr">{{Translit}}</div>
<div class="en">{{English}}</div>
<div class="vi">{{Vietnamese}}</div>
{{#Note}}<div class="note">{{Note}}</div>{{/Note}}
<div class="badge">bài {{Lessons}}</div>
"""

# Schema 11 của collection.anki2 (định dạng legacy mà mọi phiên bản Anki import được)
APKG_SCHEMA = """
CREATE TABLE col (
    id              integer primary key,
    crt             integer not null,
    mod             integer not null,
    scm             integer not null,
    ver             integer not null,
    dty             integer not null,
    usn             integer not null,
    ls              integer not null,
    conf            text not null,
    models          text not null,
    decks           text not null,
    dconf           text not null,
    tags            text not null
);
CREATE TABLE notes (
    id              integer primary key,
    guid            text not null,
    mid             integer not null,
    mod             integer not null,
    usn             integer not null,
    tags            text not null,
    flds            text not null,
    sfld            text not null,
    csum            integer not null,
    flags           integer not null,
    data            text not null
);
CREATE TABLE cards (
    id              integer primary key,
    nid             integer not null,
    did             integer not null,
    ord             integer not null,
    mod             integer not null,
    usn             integer not null,
    type            integer not null,
    queue           integer not null,
    due             integer not null,
    ivl             integer not null,
    factor          integer not null,
    reps            integer not null,
    lapses          integer not null,
    left            integer not null,
    odue            integer not null,
    odid            integer not null,
    flags           integer not null,
    data            text not null
);
CREATE TABLE revlog (
    id              integer primary key,
    cid             integer not null,
    usn             integer not null,
    ease            integer not null,
    ivl             integer not null,
    lastIvl         integer not null,
    factor          integer not null,
    time            integer not null,
    type            integer not null
);
CREATE TABLE graves (
    usn             integer not null,
    oid             integer not null,
    type            integer not null
);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
"""

COL_CONF = {
    "activeDecks": [1], "addToCur": True, "collapseTime": 1200, "curDeck": 1,
    "curModel": None, "dueCounts": True, "estTimes": True, "newBury": True,
    "newSpread": 0, "nextPos": 1, "sortBackwards": False, "sortType": "noteFld",
    "timeLim": 0,
}

DEFAULT_DCONF = {
    "1": {
        "autoplay": True, "id": 1,
        "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8,
                  "minInt": 1, "mult": 0},
        "maxTaken": 60, "mod": 0, "name": "Default",
        "new": {"bury": True, "delays": [1, 10], "initialFactor": 2500,
                "ints": [1, 4, 7], "order": 1, "perDay": 20, "separate": True},
        "replayq": True,
        "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1,
                "maxIvl": 36500, "minSpace": 1, "perDay": 100},
        "timer": 0, "usn": 0,
    }
}

# Bảng chữ base91 của Anki (xem genanki/util.py, MIT)
BASE91_TABLE = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':',
    ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']


def guid_for(*values):
    """GUID base91 từ 8 byte đầu SHA256 – cùng thuật toán Anki/genanki dùng."""
    hash_str = '__'.join(str(v) for v in values)
    m = hashlib.sha256()
    m.update(hash_str.encode('utf-8'))
    hash_int = 0
    for b in m.digest()[:8]:
        hash_int <<= 8
        hash_int += b
    rv_reversed = []
    while hash_int > 0:
        rv_reversed.append(BASE91_TABLE[hash_int % len(BASE91_TABLE)])
        hash_int //= len(BASE91_TABLE)
    return ''.join(reversed(rv_reversed))


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = [dict(r) for r in csv.DictReader(f, delimiter="\t")]
    required = ["bài", "greek", "phiên âm", "english", "tiếng việt", "ưu tiên"]
    for r in rows:
        for col in required:
            if col not in r:
                sys.exit(f"Lỗi: thiếu cột '{col}' trong TSV (kiểm tra header).")
        if ' ' in r['greek'] and False:
            pass
    return rows


def merge_duplicates(rows):
    """Headword trùng giữa các bài: giữ lần đầu, gộp số bài, ưu tiên ★."""
    merged = OrderedDict()
    for r in rows:
        key = r["greek"]
        if key in merged:
            m = merged[key]
            if r["bài"] not in m["bài"].split(","):
                m["bài"] += "," + r["bài"]
            if r["ưu tiên"] == "1":
                m["ưu tiên"] = "1"
            if not m.get("ghi chú", "") and r.get("ghi chú", ""):
                m["ghi chú"] = r["ghi chú"]
        else:
            merged[key] = dict(r)
    return list(merged.values())


def model_json(timestamp):
    """Note type JSON – cấu trúc mirror model.to_json() của genanki/Anki."""
    return {
        str(MODEL_ID): {
            "id": str(MODEL_ID),
            "name": "Graecum VN Vocabulary",
            "type": 0,
            "mod": int(timestamp),
            "usn": -1,
            "sortf": 0,
            "did": DECK_ID,
            "tmpls": [{
                "name": "Greek -> Meaning",
                "ord": 0,
                "qfmt": QFMT,
                "afmt": AFMT,
                "bqfmt": "",
                "bafmt": "",
                "bfont": "",
                "bsize": 0,
                "did": None,
            }],
            "flds": [
                {"name": name, "ord": i, "sticky": False, "rtl": False,
                 "font": "Liberation Sans", "size": 20, "media": []}
                for i, name in enumerate(
                    ["Greek", "Translit", "English", "Vietnamese", "Note", "Lessons"])
            ],
            "css": MODEL_CSS,
            "latexPre": LATEX_PRE,
            "latexPost": LATEX_POST,
            "latexsvg": False,
            "req": [[0, "all", [0]]],   # mặt trước chỉ cần field Greek
            "tags": [],
            "vers": [],
        }
    }


def deck_json():
    return {
        str(DECK_ID): {
            "id": DECK_ID,
            "name": DECK_NAME,
            "mod": 0,
            "usn": -1,
            "lrnToday": [0, 0],
            "revToday": [0, 0],
            "newToday": [0, 0],
            "timeToday": [0, 0],
            "collapsed": False,
            "browserCollapsed": False,
            "desc": DECK_DESCRIPTION,
            "dyn": 0,
            "extendNew": 10,
            "extendRev": 50,
            "conf": 1,
        }
    }


def build_db(db_path, notes_raw, timestamp):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript(APKG_SCHEMA)

    default_deck = {
        "1": {"id": 1, "name": "Default", "mod": 0, "usn": 0, "lrnToday": [0, 0],
              "revToday": [0, 0], "newToday": [0, 0], "timeToday": [0, 0],
              "collapsed": False, "browserCollapsed": False, "desc": "",
              "dyn": 0, "extendNew": 10, "extendRev": 50, "conf": 1}
    }
    default_deck.update(deck_json())

    cur.execute(
        "INSERT INTO col VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);",
        (1, int(timestamp), int(timestamp * 1000), int(timestamp * 1000) - 4,
         11, 0, 0, 0,
         json.dumps(COL_CONF),
         json.dumps(model_json(timestamp)),
         json.dumps(default_deck),
         json.dumps(DEFAULT_DCONF),
         "{}"))

    id_gen = itertools.count(int(timestamp * 1000))
    n_star = 0
    for r in notes_raw:
        lessons = ",".join(sorted(set(r["bài"].split(",")), key=int))
        tags = ["graecum-vn", "graecum-1"] + [f"bài-{int(b):02d}" for b in r["bài"].split(",")]
        if r["ưu tiên"] == "1":
            tags.append("ưu-tiên")
            n_star += 1
        if r.get("nhóm", "") == "chia dạng":
            tags.append("chia-dạng")
        fields = [r["greek"], r["phiên âm"], r["english"], r["tiếng việt"],
                  r.get("ghi chú", "") or "", lessons]
        cur.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?);", (
            next(id_gen),                          # id
            guid_for("graecum-vn-vocab", r["greek"]),  # guid
            MODEL_ID,                              # mid
            int(timestamp),                        # mod
            -1,                                    # usn (local)
            ' ' + ' '.join(tags) + ' ',            # tags
            '\x1f'.join(fields),                   # flds
            r["greek"],                            # sfld (sort field)
            0,                                     # csum (Anki tự tính lại khi import)
            0,                                     # flags
            '',                                    # data
        ))
        note_id = cur.lastrowid
        cur.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (
            next(id_gen),   # id
            note_id,        # nid
            DECK_ID,        # did
            0,              # ord (template 0)
            int(timestamp), # mod
            -1,             # usn
            0,              # type (new)
            0,              # queue (new)
            0,              # due
            0,              # ivl
            0,              # factor
            0,              # reps
            0,              # lapses
            0,              # left
            0,              # odue
            0,              # odid
            0,              # flags
            '',             # data
        ))
    conn.commit()
    conn.close()
    return n_star


def main():
    ap = argparse.ArgumentParser(description="Sinh Anki deck (.apkg) từ vocab TSV của Graecum VN")
    ap.add_argument("--tsv", default="vocab/vocab-01-10.tsv", help="đường dẫn TSV đầu vào")
    ap.add_argument("--out", default="vocab/graecum-vn-01-10.apkg", help="file .apkg đầu ra")
    ap.add_argument("--deck", default=None,
                    help='tên deck đích, ví dụ: "Graecum VN 01-05" (mặc định: bộ Bài 1–10)')
    args = ap.parse_args()
    if args.deck:
        configure_deck(args.deck)

    rows = read_tsv(args.tsv)
    notes_raw = merge_duplicates(rows)

    timestamp = time.time()
    dbfile, dbname = tempfile.mkstemp()
    os.close(dbfile)
    n_star = build_db(dbname, notes_raw, timestamp)

    with zipfile.ZipFile(args.out, 'w', zipfile.ZIP_DEFLATED) as outzip:
        outzip.write(dbname, 'collection.anki2')
        outzip.writestr('media', '{}')  # không có file media
    os.remove(dbname)

    # verify nhanh: mở lại sqlite trong zip và đếm
    with zipfile.ZipFile(args.out) as z:
        with tempfile.TemporaryDirectory() as td:
            z.extract('collection.anki2', td)
            conn = sqlite3.connect(os.path.join(td, 'collection.anki2'))
            n_notes = conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
            n_cards = conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
            n_gconf = conn.execute("SELECT json_valid(models) FROM col").fetchone()[0]
            conn.close()
    assert n_notes == len(notes_raw) and n_cards == len(notes_raw) and n_gconf == 1

    print(f"Đã sinh {len(notes_raw)} notes / {n_cards} cards "
          f"({n_star} từ ưu tiên ★) -> {args.out} [deck: {DECK_NAME}]")


if __name__ == "__main__":
    main()
