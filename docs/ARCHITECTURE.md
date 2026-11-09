# Kiến trúc project (v1.0 — cập nhật Phần 1)

## 1. Nguyên tắc kiến trúc: bền vững 10 năm

Mọi quyết định kỹ thuật đều trả lời câu hỏi: **"Cái này còn chạy đúng sau 10 năm không, nếu không ai bảo trì?"**

| Quyết định | Lý do bền vững |
| --- | --- |
| **Static HTML, không framework, không build step** | Không phụ thuộc vòng đời của JS framework; file HTML mở được bằng mọi trình duyệt + MS Word, offline. |
| **Mỗi bài = 1 file tự chứa** (CSS inline, không CDN, không JS bắt buộc) | Không bị chết link CDN; người học tải 1 file là có trọn bài, mãi mãi. |
| **Nội dung lõi = Unicode Hy Lạp + HTML thuần** | Không phụ thuộc script/render engine; sao chép, in, xuất Word đều ổn. |
| **Dữ liệu meta tách khỏi nội dung** (`lessons.json`) | Portal sinh mục lục từ data, thêm bài chỉ cần thêm 1 dòng JSON. |
| **GitHub Pages** cho hosting | Miễn phí, tài khoản GitHub là "chìa khóa" duy nhất; rủi ro lệ thuộc gần 0. |
| **License rõ ràng** (CC BY-SA 4.0 nội dung, MIT code) | Ai cũng biết được phép làm gì; project sống sót kể cả khi chủ repo nghỉ. |

## 2. Kiến trúc organization (3 repo, mở dần)

```
github.com/<tài-khoản / org>
│
├── graecum-vn          ← REPO NÀY: portal + bài giảng + readings + vocab
│
├── greek-toolkit-vn    ← (Phần sau) "grill me with ancient greek"
│                          hub tools (Logeion, Perseus/Scaife, Morpheus, Alpheios…),
│                          so sánh tài liệu/ngữ pháp, bộ Anki, quiz tự luyện
│
└── satzanalyse-vn      ← (Phần sau) platform phân tích câu:
│                          dán văn bản cổ → tách câu → morphological tagging →
│                          render bản phân tích 7 bước (morphology/syntax/semantics)
```

Rationale tách repo: nội dung giáo dục (portal) đổi theo nhịp biên soạn; curated links (toolkit) đổi theo nhịp công cụ bên ngoài; sản phẩm kỹ thuật (satzanalyse) đổi theo nhịp phần mềm. Ba nhịp khác nhau = ba repo, để một repo "chậm" không bị kéo theo nhịp "nhanh".

Liên kết: mỗi repo link 2 chiều với 2 repo còn lại + dùng chung style guide.

## 3. Layout repo portal (repo này)

```
graecum-vn/
├── index.html                  # Portal landing (tiếng Việt)
├── lessons.json                # Meta index: id, title, level, topics, vocab, status
├── lessons/
│   ├── _template/
│   │   └── lesson.html        # Template chuẩn (quy ước mới)
│   └── 01-foundations/        # mỗi bài 1 thư mục, index.html + (sau này) readings
├── readings/
│   ├── README.md              # Nguồn văn bản PD + cổng đọc online
│   └── (sau này) từng đoạn đọc: greek/ + simplified/ + notes.md
├── vocab/
│   └── (sau này) vocab-01.tsv, decks Anki (apkg source csv)
├── docs/
│   ├── ARCHITECTURE.md         # file này
│   ├── ROADMAP.md              # lộ trình phát triển + continuation notes
│   ├── STYLE-AND-CONVENTIONS.md
│   ├── CURRICULUM.md           # bản đồ 48 bài (chủ đề + bài đọc)
│   └── COPYRIGHT.md             # chính sách bản quyền
├── toolkit.md                  # stub; sẽ tách thành repo riêng
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## 4. Đường ống sản xuất một bài giảng (lesson pipeline)

```
[1] Chọn chủ đề grammar + bài đọc theo CURRICULUM.md
[2] Soạn thảo (template _template/lesson.html, quy ước STYLE-AND-CONVENTIONS.md)
    — ví dụ tự viết, KHÔNG lấy từ giáo trình có bản quyền
    — bài đọc: bản simplified tự biên soạn từ văn bản PD + bản gốc kèm nguồn
[3] Audit bản quyền (COPYRIGHT.md checklist)
[4] QA HTML (checklist trong STYLE-AND-CONVENTIONS.md: span/li cân bằng,
    không ký tự lạ, không lỗi tiếng Việt)
[5] Thêm dòng vào lessons.json (status: draft → published)
[6] Portal tự cập nhật (đọc lessons.json)
[7] Liên kết bài học trước/sau trong TOC mỗi bài
```

Mỗi bài sau khi publish là **ổn định vĩnh viễn** (không rewrite trừ khi có sửa lỗi) — nguyên tắc "đã phát hành thì không đổi URL", để link trong Anki decks/ghi chú người học không bao giờ chết.

## 5. Điểm mở rộng (extension points)

- **lessons.json** có trường `tools` (rỗng ban đầu): sau này mỗi bài có thể link tới exercise tương tác, quiz, hoặc analyzer online mà không sửa HTML bài.
- **readings/** có cấu trúc 3 lớp (greek/simplified/notes) cho phép thêm lớp "interlinear" hay audio sau này.
- **vocab/** theo format TSV chuẩn để sinh Anki deck bằng script, không đổi cấu trúc bài.
- **Bản dịch**: cột tiếng Việt trong bảng ví dụ được thiết kế để thêm cột thứ 5, 6 (tiếng Pháp, Đức…) nếu cộng đồng muốn, mà không phá cấu trúc.

## 6. Decision log (ADR rút gọn)

- **ADR-001 — Không SSG (Hugo/Astro/…)**: giữ static thuần. Bù lại portal đơn giản hơn, nhưng không chết theo framework. Chấp nhận: portal ít tính năng; giải pháp: lessons.json + ít JS tùy chọn.
- **ADR-002 — Duy trì bản "xưởng biên soạn"**: quá trình biên soạn vẫn qua công cụ nội bộ, repo giữ bản chuẩn hóa cuối. Rationale: tách "xưởng" khỏi "kho xuất bản".
- **ADR-003 — Thuật ngữ tiếng Anh thay tiếng Đức** (quyết định từ người sở hữu project): bản thảo L1–6 đang dùng thuật ngữ Đức → phải chuyển hóa khi publish (xem ROADMAP Phần 3).
- **ADR-004 — Phiên âm La tinh hóa bắt buộc ở cấp I**: scheme trong STYLE-AND-CONVENTIONS.md. Cấp II (từ L25) giảm dần, cấp đọc văn bản gốc bỏ hẳn để người học quen chữ Hy Lạp.
- **ADR-005 — Cấu trúc giáo trình thương mại 2018 chỉ làm inspiration**: danh mục bài đọc của ta lấy từ các tác giả gốc (citations là sự thật, không thuộc bản quyền), nhưng trình tự chủ đề grammar và mọi văn bản simplified là của ta. Không bao giờ lưu text adapted/translation của giáo trình.
