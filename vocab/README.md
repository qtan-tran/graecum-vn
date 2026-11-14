# Vocab TSV & Anki – Graecum VN (Bài 1–24 + file import cho bài ôn tập)

Từ vựng trọng tâm của **Lesson 1–24**, trích từ mục "Từ vựng trọng tâm" của từng bài giảng, đóng gói thành hai định dạng:

| File | Nội dung |
| --- | --- |
| `vocab-01-10.tsv` | 186 dòng từ vựng, TSV (UTF-8, tab-separated) – xem chi tiết cột bên dưới |
| `anki-01-05.txt` | File import Anki (định dạng text đơn giản) cho **Ôn tập #1** (Bài 1–5): 114 thẻ (102 từ + 12 **thẻ chia dạng**) |
| `anki-06-10.txt` | File import Anki (định dạng text đơn giản) cho **Ôn tập #2** (Bài 6–10): 84 thẻ (69 từ + 15 **thẻ chia dạng**) |
| `vocab-11-15.tsv` | 111 dòng (96 từ + 15 **thẻ chia dạng**), TSV (UTF-8, tab-separated) – cùng định dạng 8 cột như `vocab-01-10.tsv` |
| `anki-11-15.txt` | File import Anki (định dạng text đơn giản) cho **Ôn tập #3** (Bài 11–15): 111 thẻ (96 từ + 15 **thẻ chia dạng**) |
| `vocab-11-20.tsv` | 216 dòng (từ vựng Bài 11–20: 90 từ mới của Bài 16–20 + 15 **thẻ chia dạng** cộng vào cụm 10 bài 11–20), TSV (UTF-8, tab-separated) – cùng định dạng 8 cột như `vocab-01-10.tsv` |
| `anki-16-20.txt` | File import Anki (định dạng text đơn giản) cho **Ôn tập #4** (Bài 16–20): 104 thẻ (89 từ, từ trùng giữa các bài đã gộp + 15 **thẻ chia dạng**) |
| `vocab-21-24.tsv` | 88 dòng (từ vựng Bài 21–24: 72 từ của Bài 21–24 + 15 **thẻ chia dạng**), TSV (UTF-8, tab-separated) – cùng định dạng 8 cột như `vocab-01-10.tsv` |
| `anki-21-24.txt` | File import Anki (định dạng text đơn giản) cho **Ôn tập #5** (Bài 21–24, kết Graecum I): 87 thẻ (72 từ + 15 **thẻ chia dạng**) |
| `../tools/gen_anki_deck.py` | Script sinh Anki deck `.apkg` (169 thẻ, từ trùng giữa các bài đã gộp, tag theo bài) từ TSV – thuần thư viện chuẩn Python, không cần cài gói ngoài |

Deck `.apkg` không commit dạng binary vào repo; thay vào đó được nhúng base64 ngay trong trang bài ôn tập tương ứng, trình duyệt dựng lại file thật khi người đọc bấm tải về (repo vẫn giữ đúng triết lý "toàn text, inspect được").

## Cách học bằng Anki

**Hướng nhanh (cần Python bất kỳ phiên bản ≥ 3.6):** chạy 1 lệnh rồi mở file kết quả bằng Anki (nhấp đúp, hoặc Anki → File → Import):

```bash
python3 tools/gen_anki_deck.py
```

Deck `Graecum VN – Graecum I (Bài 1–10)` xuất hiện với 169 thẻ mặt trước là từ Hy Lạp, mặt sau là phiên âm + nghĩa Anh + nghĩa Việt + ghi chú + số bài.

Tag gợi ý khi lọc học:

- `bài-01` … `bài-15` – học theo bài (một từ xuất hiện ở nhiều bài mang nhiều tag này).
- `ưu-tiên` – 102 từ ★ "bắt buộc nhớ" trong bài giảng.
- `graecum-1` – toàn bộ cấp Graecum I (sẽ cộng dồn ở các bản sau).

**Không có Python?** TSV import trực tiếp được vào Anki (File → Import, separator Tab, bỏ dòng header, map cột: `greek` → mặt trước, `phiên âm` + `english` + `tiếng việt` + `ghi chú` → mặt sau) – bạn mất template đẹp của script nhưng vẫn học được; hoặc dùng template kiểu "Basic (type in the answer)" tùy ý.

## File import cho bài ôn tập (Wiederholung)

Cứ sau mỗi 5 bài, portal xuất bản một **bài ôn tập** (Ôn tập #1 sau Bài 5, Ôn tập #2 sau Bài 10…), mỗi bài kèm **hai file import Anki** cho từ vựng nhóm 5 bài, tùy người học chọn:

- **File đóng gói `.apkg`** (tải trực tiếp từ trang bài ôn tập tương ứng): deck dựng sẵn, **bảo lưu HTML và mã màu** của template – nhấp đúp là import được ngay.
- **File text `anki-01-05.txt`, `anki-06-10.txt`, `anki-11-15.txt`, `anki-16-20.txt`…**: định dạng đơn giản, mở xem được bằng mọi editor trước khi import vào note type Basic.

Cả hai đều dựng sẵn thẻ (mặt trước = từ Hy Lạp, mặt sau = phiên âm Latin + nghĩa tiếng Việt/Anh) và một nhóm nhỏ **thẻ chia dạng**: mặt trước là một dạng đã biến cách/chia (ví dụ `θεραπεύεις`, `σώμασι(ν)`), mặt sau nêu đúng cách, số/ngôi + dạng từ điển + nghĩa.

**Import vào Anki:**

- **File `.apkg`:** tải về từ trang bài ôn tập → nhấp đúp file (hoặc Anki → **File → Import…**) – deck xuất hiện với đầy đủ template màu.
- **File `.txt`:** tải về (nhấp chuột phải vào link → *Lưu đích dưới dạng…*) → Anki → **File → Import…** (hoặc kéo-thả file vào cửa sổ Anki) → Anki đọc sẵn mọi cài đặt từ các dòng đầu file (dấu tab, HTML, deck đích, tag) – bấm **Import** là xong. Deck chưa có sẽ được tạo tự động.

Tag khi lọc học: `bài-01`… `bài-24` (học theo bài), `ưu-tiên` (từ ★), `chia-dạng` (thẻ chia dạng), `graecum-1` (toàn cấp).

**Quy tắc học thẻ (cô đọng, áp dụng cho mọi nhóm):**

- Mỗi thẻ một mặt là từ Hy Lạp, một mặt là phiên âm Latin + nghĩa tiếng Việt/Anh.
- Phần lớn thẻ dùng để nhớ **Grundform und -bedeutung** (dạng từ điển + nghĩa): khi lật thẻ, nêu ít nhất một trong các nghĩa khả dĩ (Genannt werden muss jeweils mindestens eine der möglichen Bedeutungen).
- Một số thẻ về **biến cách của từ** (chia dạng): nêu đúng cách, số/ngôi + Grundform + nghĩa – dùng để phục vụ việc nhớ cách chia từ (deklination, conjugation).
- **Kasus**: khi bị hỏi phải nêu kèm cách đi kèm của từ – luôn với giới từ (ἐν + Dativ, εἰς + Akkusativ, ἐκ + Genitiv, ὑπό + Genitiv – tác nhân), đôi khi với động từ (κατηγορέω + Genitiv, πιστεύω + Dativ, δέομαι + Genitiv).

File mới nhất: `anki-21-24.txt` ra cùng **Ôn tập #5** (Bài 21–24, kết thúc Graecum I). File tiếp theo: `anki-25-29.txt` sẽ ra cùng **Ôn tập #6** (sau khi Bài 29 xuất bản).

## Định dạng TSV

8 cột, tab-separated, dòng 1 là header:

| Cột | Ý nghĩa |
| --- | --- |
| `bài` | Số bài (1–24) |
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

Script đọc `vocab-01-10.tsv` (mặc định) và ghi `graecum-vn-01-10.apkg`. GUID của thẻ được tính bền từ headword nên sinh lại nhiều lần **không tạo thẻ trùng** trong bộ sưu tập đã import. Script chỉ dùng thư viện chuẩn Python (`sqlite3`, `zipfile`, `hashlib`) – không cần `pip install` gì cả, chạy được offline. Tham số tùy chọn: `--tsv <đường dẫn>`, `--out <file.apkg>`, `--deck <tên deck>` (cho deck nhóm 5 bài, ví dụ `--deck "Graecum VN 01-05"`; ID deck được suy ra bền từ tên nên sinh lại nhiều lần không trùng).

## Bản quyền & ghi công

Nội dung TSV và deck: **CC BY-SA 4.0**; code script: MIT. Biên soạn bởi **Trần Quốc Tân**. Khi cite hoặc tái sử dụng, vui lòng ghi: "Graecum VN – Trần Quốc Tân, https://github.com/qtan-tran/graecum-vn".
