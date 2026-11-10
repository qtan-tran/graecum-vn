# Vocab TSV & Anki deck – Graecum VN (Bài 1–10)

Từ vựng trọng tâm của **Lesson 1–10**, trích từ mục "Từ vựng trọng tâm" của từng bài giảng, đóng gói thành hai định dạng:

| File | Nội dung |
| --- | --- |
| `vocab-01-10.tsv` | 186 dòng từ vựng, TSV (UTF-8, tab-separated) – xem chi tiết cột bên dưới |
| `../tools/gen_anki_deck.py` | Script sinh Anki deck `.apkg` (169 thẻ, từ trùng giữa các bài đã gộp, tag theo bài) từ TSV – thuần thư viện chuẩn Python, không cần cài gói ngoài |

Deck `.apkg` không commit vào repo (file binary, sinh lại chỉ cần 1 lệnh – repo giữ đúng triết lý "toàn text, inspect được").

## Cách học bằng Anki

**Hướng nhanh (cần Python bất kỳ phiên bản ≥ 3.6):** chạy 1 lệnh rồi mở file kết quả bằng Anki (nhấp đúp, hoặc Anki → File → Import):

```bash
python3 tools/gen_anki_deck.py
```

Deck `Graecum VN – Graecum I (Bài 1–10)` xuất hiện với 169 thẻ mặt trước là từ Hy Lạp, mặt sau là phiên âm + nghĩa Anh + nghĩa Việt + ghi chú + số bài.

Tag gợi ý khi lọc học:

- `bài-01` … `bài-10` – học theo bài (một từ xuất hiện ở nhiều bài mang nhiều tag này).
- `ưu-tiên` – 102 từ ★ "bắt buộc nhớ" trong bài giảng.
- `graecum-1` – toàn bộ cấp Graecum I (sẽ cộng dồn ở các bản sau).

**Không có Python?** TSV import trực tiếp được vào Anki (File → Import, separator Tab, bỏ dòng header, map cột: `greek` → mặt trước, `phiên âm` + `english` + `tiếng việt` + `ghi chú` → mặt sau) – bạn mất template đẹp của script nhưng vẫn học được; hoặc dùng template kiểu "Basic (type in the answer)" tùy ý.

## Định dạng TSV

8 cột, tab-separated, dòng 1 là header:

| Cột | Ý nghĩa |
| --- | --- |
| `bài` | Số bài (1–10) |
| `greek` | Từ Hy Lạp đúng như bảng từ vựng trong bài giảng (kèm mạo từ, paradigm rút gọn) |
| `phiên âm` | Phiên âm La-tinh hóa có dấu thanh |
| `english` | Nghĩa tiếng Anh |
| `tiếng việt` | Nghĩa tiếng Việt |
| `ghi chú` | Ghi chú ngữ pháp của bài giảng (giống cách, nhóm động từ, …), có thể rỗng |
| `nhóm` | Nhóm con trong bảng từ vựng (Động từ, Danh từ, …), có thể rỗng |
| `ưu tiên` | `1` = từ ★ ưu tiên học trước, `0` = còn lại |

## Quy ước gộp từ trùng

Từ ôn tập xuất hiện lại ở bài sau (ví dụ ὁ ἐχθρός, -οῦ gặp ở bài 1, 3, 6, 7) được gộp thành **một** thẻ Anki: nội dung giữ theo lần xuất hiện đầu, thẻ mang tag của mọi bài chứa nó. Vì vậy 186 dòng TSV → 169 thẻ. Headword giữ nguyên như trong từng bài giảng (ví dụ bài 1 ghi `θεραπεύω, -ει, -ουσι(ν), -ειν`, bài 2–5 ghi `θεραπεύω` – hai headword khác nhau nên thành hai thẻ riêng).

## Sinh lại deck

```bash
python3 tools/gen_anki_deck.py
```

Script đọc `vocab-01-10.tsv` (mặc định) và ghi `graecum-vn-01-10.apkg`. GUID của thẻ được tính bền từ headword nên sinh lại nhiều lần **không tạo thẻ trùng** trong bộ sưu tập đã import. Script chỉ dùng thư viện chuẩn Python (`sqlite3`, `zipfile`, `hashlib`) – không cần `pip install` gì cả, chạy được offline. Tham số tùy chọn: `--tsv <đường dẫn>`, `--out <file.apkg>`.

## Bản quyền & ghi công

Nội dung TSV và deck: **CC BY-SA 4.0**; code script: MIT. Biên soạn bởi **Trần Quốc Tân**. Khi cite hoặc tái sử dụng, ghi công: "Graecum VN – Trần Quốc Tân, https://github.com/qtan-tran/graecum-vn, CC BY-SA 4.0".
