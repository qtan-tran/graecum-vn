# Quy ước biên soạn (STYLE-AND-CONVENTIONS) v1.0

Áp dụng cho **mọi bài giảng** trong repo. Mục đích: người học mở bất kỳ bài nào cũng thấy cùng một cấu trúc, cùng thuật ngữ, cùng cách trình bày — và biên soạn viên mới có thể đóng góp mà không phá hệ thống.

## 1. Ngôn ngữ

- **Ngôn ngữ giải thích: tiếng Việt.**
- **Thuật ngữ ngôn ngữ học: tiếng Anh**, kèm chú thích tiếng Việt lần đầu xuất hiện.
  - Viết: *noun* (danh từ), *genitive* (cách sở hữu), *participle* (phân từ), *subjunctive* (thức giả định)…
  - Rationale: người học sẽ tra cứu tiếp bằng tiếng Anh (LSJ, Wiktionary, Perseus) — thuật ngữ Anh là "cầu nối" đến hệ sinh thái tài liệu thế giới. **Không dùng thuật ngữ Đức** trong bản publish (ghi chú: các bản thảo đầu tiên L1–6 dùng thuật ngữ Đức — phải chuyển hóa khi publish, xem ROADMAP Phần 3).
- **Văn bản Hy Lạp: Unicode polytonic** (ὁ ἄνθρωπος, ἐστιν, εἶναι), font-family serif Hy Lạp trong CSS.

## 2. Ví dụ minh họa

- Bảng ví dụ chuẩn **4 cột**:

| Greek | Transliteration | English | Tiếng Việt |
| --- | --- | --- | --- |
| ὁ ἄνθρωπος θεραπεύει τοὺς θεούς | ho ánthrōpos therapeúei toùs theoús | The human being worships the gods. | Con người tôn thờ các vị thần. |

- Rationale 2 cột dịch: tiếng **Anh** cho thấy pattern ngữ pháp tương đương (article, case, word order), tiếng **Việt** cho nghĩa tự nhiên. Người học nhìn cả hai để hiểu cả cấu trúc lẫn nghĩa.
- Trong phần giải thích văn (không phải bảng), có thể dùng ví dụ tiếng Việt hoặc tiếng Anh, chọn cái nào **làm pattern rõ hơn**.
- **Latin corner** (mục phụ, tùy chọn "so sánh Latin"): mỗi khi Hy Lạp và Latin có điểm tương ứng gần (declension endings, infinitive construction, subjunctive), cho 1 ví dụ Latin đơn giản (amō, amāre, amāvisse…) trong callout `.latin`. Không lạm dụng: chỉ khi so sánh thực sự giúp ghi nhớ.

## 3. Phiên âm La tinh hóa (bắt buộc ở Graecum I, L1–24)

- Xuất hiện trong: bảng từ vựng, lần đầu mỗi cụm Hy Lạp trong bài đọc.
- Scheme (academic, có dấu trường âm và dấu trọng âm):

| Greek | Latin | Ghi chú |
| --- | --- | --- |
| α, ἀ, ἁ | a, a, ha | rough breathing → h |
| ε, η | e, ē | macron cho nguyên âm dài |
| ι, ῑ | i, ī | |
| ο, ω | o, ō | |
| υ, ῠ, ῡ | y, y, ȳ | giữ y (người Việt đọc "i"-nhẹ được) |
| οι, ει, υι, αυ, ευ | oi, ei, yi, au, eu | |
| γγ, γκ | ng, nk | |
| trọng âm ά έ ί ό ύ ώ | á é í ó ý ó | dấu á kiểu tiếng Việt quen thuộc |

- Ví dụ: ὁ ἄνθρωπος → *ho ánthrōpos*; τῷ ἀνθρώπῳ → *tōi anthrṓpōi*; εἶναι → *eînai*; θεραπεύειν → *therapeúein*.
- Quy tắc vàng: **đọc được là đủ** — đây là công cụ đọc, không phải hệ thống ký âm học thuật hoàn hảo; chọn cách đọc quen với người Việt (chữ cái Latin như tiếng Việt đọc).
- Từ L25 (Graecum II) giảm dần; các bài đọc văn bản gốc không phiên âm nữa.

## 4. Cấu trúc một bài giảng (lesson anatomy)

Thứ tự cố định (khớp template `lessons/_template/lesson.html`):

1. `<h1>` tiêu đề: `Lesson N: <chủ đề chính>`.
2. **TOC** (mục lục, link anchor).
3. **Box "Mục tiêu"** (.tipp): sau bài học bạn có thể… (dạng checklist kiến thức năng lực).
4. Các mục `<h2>` đánh số 1..n: mỗi chủ đề có (a) giải thích từng bước, (b) bảng ví dụ 4 cột, (c) **pattern để vận dụng** (box .tipp) — người học phải thấy được "công thức" tái sử dụng cho ví dụ khác, (d) tự kiểm tra (self-check).
5. Box **"Watch out"** (.achtung, nền #FFF8E1 viền #C62828): các lỗi thường gặp + vì sao chúng xảy ra + cách tự kiểm tra.
6. Bảng từ vựng: ★ = trọng tâm; cột: Greek | Translit. | English | Tiếng Việt | Ghi chú.
7. **Bảng tổng hợp so sánh các điểm dễ nhầm** (confusables) — luôn có ở cuối bài.
8. **Bài tập tự luyện** (Exercises) + **đáp án** (ẩn trên màn hình, hiện khi in — CSS `.answer { display:none }` + `@media print`).
9. Footer: `Bài giảng Lesson N — Graecum VN · CC BY-SA 4.0 · Đáp án hiện khi in (Ctrl+P → Save as PDF)`.

Box phụ: `.latin` (so sánh Latin), `.info` (ghi chú ngôn ngữ/lịch sử liên hệ — chỉ khi phục vụ việc học).

## 5. Quy ước kỹ thuật HTML

- 1 bài = 1 thư mục `lessons/NN-slug/index.html`; slug kebab-case, ASCII, không dấu (VD: `01-foundations`).
- File **tự chứa**: CSS inline trong `<style>`, không CDN, không JS bắt buộc; JS (nếu có) chỉ là tùy chọn trang trí.
- Cấu trúc semantic cho MS Word: `h1/h2/h3`, `table > thead`, `div` callout.
- Giữ bảng ≤5 cột.
- In ấn: `@media print` hiện đáp án, bỏ nền màu, tránh ngắt trang trong bảng.
- Mọi anchor id: `#s1, #s2 … #vocab, #confusables, #exercises`.

## 6. QA checklist (chạy trước khi publish mỗi bài)

- [ ] Cân bằng thẻ: `<span>`=`</span>`, `<li>`=`</li>`, `<table>`=`</table>`, `<p>`=`</p>`, `<div>`=`</div>`, `<ol>`=`</ol>`.
- [ ] Không ký tự lạ (TQ/Hàn/Nga), không từ tiếng Đức sót trong bản publish (trừ tên riêng như "Graecum").
- [ ] Không text sau `</li>` trong `<ol>`; không `</span>` lẻ.
- [ ] Mọi thuật ngữ Anh lần đầu có chú thích tiếng Việt.
- [ ] Mọi từ vựng cấp I có phiên âm; ★ đã đánh dấu.
- [ ] Có bảng confusables + bài tập + đáp án; đáp án thật sự ẩn khi xem web.
- [ ] Bài đọc (nếu có): ghi rõ nguồn gốc PD (tác giả, tác phẩm, đoạn) + cổng đọc.
- [ ] Footer CC BY-SA đúng chuẩn; không có bất kỳ dấu vết nguồn biên soạn nào (giáo trình/trường/giảng viên).
- [ ] Đã thêm dòng vào `lessons.json`.

## 7. Quy ước đặt tên & phiên bản

- Bài: `NN-kebab-slug` (01-foundations, 02-verbs-present-vocative…). Đổi tên thư mục = phá link → **cấm** sau khi publish.
- Sửa lỗi nội dung: sửa tại chỗ, tăng `rev` trong `lessons.json` (VD `"rev": 2`), ghi chú ngắn trong commit.
- Chính tả tiếng Việt: dùng Unicode tiếng Việt chuẩn; giữ nhất quán cách viết "i/y" theo quy tắc chính tả phổ thông.
