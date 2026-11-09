# ROADMAP phát triển project — cập nhật lần 4 (giữa Phần 3)

> **Quy ước làm việc**: công việc chia thành **Phần (Part)**; cuối mỗi Phần ghi **Continuation notes** vào file này. Cứ **6–7 steps** thì bản roadmap này được cập nhật và báo cáo lại cho người sở hữu project. Tốc độ không quan trọng — tính bền vững và chất lượng mới quyết định.

## Nguyên tắc sustainability (đứng sau mọi quyết định)

1. Không phụ thuộc công nghệ sẽ lỗi thời (static HTML, Unicode, không build).
2. Không phụ thuộc một người duy nhất: tài liệu hóa đầy đủ (docs/), license cho phép fork tiếp tục.
3. Không phụ thuộc nội dung không được phép giữ: chỉ PD + tự biên soạn.
4. Không phụ thuộc hosting trả phí: GitHub Pages + export offline (MS Word/PDF).
5. Mỗi bài publish là ổn định vĩnh viễn (URL không đổi).

## Trạng thái các Phần

| Phần | Nội dung | Trạng thái |
| --- | --- | --- |
| **1** | Kiến trúc + tài liệu nền (README, ARCHITECTURE, STYLE, COPYRIGHT, CURRICULUM 48 bài, ROADMAP) + portal skeleton + lesson template | ✅ XONG |
| **2** | Tạo repo GitHub + push Phần 1 + bật GitHub Pages; chuẩn hóa pilot: chuyển hóa **Lesson 1** sang quy ước mới (thuật ngữ tiếng Việt là chính, bảng 4 cột có phiên âm, Latin corner) | ✅ XONG (còn chờ user xác nhận bật Pages) |
| **3** | Chuyển hóa Lesson 2–6 sang quy ước mới, audit bản quyền từng bài; kèm yêu cầu mới: **ghi công tác giả (BY) trên COPYRIGHT + footer mọi bài giảng** | 🔄 ĐANG LÀM (L2, L3 ✅; còn L4–6) |
| **4** | Repo `greek-toolkit-vn` (hub tools + so sánh tài liệu) | ☐ |
| **5** | Lesson 7–10 mới hoàn chỉnh (bắt đầu phần curriculum chưa có bản thảo) + readings pipeline (bản simplified đầu tiên) | ☐ |
| **6** | Vocab TSV + script sinh Anki deck cho L1–10 (CC BY-SA) | ☐ |
| **7–12** | Lesson 11–24 (hoàn thành Graecum I); cập nhật roadmap giữa chừng | ☐ |
| **13+** | Graecum II (L25–48) + satzanalyse platform + cộng đồng | ☐ |

## Continuation notes — Phần 3 (đang làm)

**Yêu cầu mới của người sở hữu (đã ghi thành quy ước):**
- Project miễn phí nhưng phải ghi rõ: các bài giảng **biên soạn bởi Tân**; ai cite hoặc tái sử dụng material **phải ghi công**: (1) tên tác giả, (2) tên project + link repo, (3) license CC BY-SA 4.0.
- Đã cập nhật 6 chỗ: `docs/COPYRIGHT.md` (§4 "License & ghi công tác giả": 3 yêu cầu tối thiểu + dòng ghi công mẫu VN/EN), `README.md` (blockquote "Biên soạn bởi Tân" + section "Cách ghi công (bắt buộc khi tái sử dụng)"), `index.html` (footer), `docs/STYLE-AND-CONVENTIONS.md` (mục 9: footer spec), `lessons/_template/lesson.html` (footer chuẩn), footer Lesson 1. Commit: `36764b8`.
- **Footer chuẩn mọi bài** (đã định hình, L1+L2+template đồng bộ): `Bài giảng Lesson N — Graecum VN · Biên soạn bởi Tân · CC BY-SA 4.0 · Khi cite hoặc tái sử dụng, ghi công: "Graecum VN — Tân, https://github.com/qtan-tran/graecum-vn, CC BY-SA 4.0" · Đáp án bài tập chỉ hiện khi in (Ctrl+P → Save as PDF)` (+ dòng "Bản đọc đối chiếu: …" nếu bài có bài đọc).

**Đã làm:**
- **Lesson 2 publish** — `lessons/02-verbs-present-vocative/index.html` (~61KB, 13 mục): hiện tại chủ động đủ 6 ngôi (paradigm θεραπεύω + πείθω), hô cách + ngoại lệ đực -ος → -ε (ὦ ἄνθρωπε), nguyên mẫu làm chủ ngữ (δεῖ) vs tân ngữ (ἐθέλω) + cảnh báo AcI (bài 4), đối cách kép 2 loại (διδάσκω "dạy ai cái gì" / νομίζω "coi là": tân ngữ có mạo từ + biểu ngữ không mạo từ), οὐ/οὐκ/οὐχ + ngoại lệ οὐκ ἔστι, τί/τι + ἆρα (mũ, hỏi) vs ἄρα (sắc, kết luận) + bộ ba ἤ/ἡ/ἦ, βασιλεύς chỉ chủ cách (chia đủ bài 18), động từ kéo theo cách riêng (κατηγορέω + Gen.), né vực nguyên âm: ν di động + lược âm (ἀλλ' ἐγώ, μεθ' ἡμῶν τ→θ, nhóm không elide περί/πρό/ὅτι/τι/τί), bài đọc simplified **tự biên soạn** theo Platon Apologie 26c–27a ("Socrates trước tòa", 4 câu: ὦ ἄνθρωπε + οὐ/οὐκ + ἄρα sắc + đối cách kép), Latin corners (amo↔θεραπεύω, dominus→domine, a/an↔οὐ/οὐκ, puto Socratem sapientem↔νομίζω), confusables 14 hàng, 7 bài tập + đáp án ẩn. lessons.json: L2 `published, rev 2`. Commit: `5c34b2a`.
- **Audit bản quyền L2**: mọi câu ví dụ + bài đọc tự biên soạn; câu lấy từ Lektionstext gốc (như "πολλὰ διδάσκει με ὁ βίος") đều đã viết lại theo khung của project; chỉ dẫn nguồn: Platon, Apologie 26c–27a (Perseus, PD).
- **QA L2** (checklist đầy đủ): bắt và vá được 2 ký tự TQ lọt vào ("辩护", "原告"), 3× typo "mảo từ", "động tự", translit sai "ethélōi" → "ethélei", tiểu từ hỏi sai dấu ἄρα → **ἆρα** (mũ), mô tả ἦ/ἡ phân biệt qua dấu hơi; cân bằng thẻ, không còn thuật ngữ Đức. Verify push bằng diff raw file theo commit-sha (CDN raw `main` cache chậm ~5 phút).
- **Chuẩn hóa ghi công theo yêu cầu người sở hữu**: bỏ "(Quoc-Tan Tran)", chỉ ghi **"Tân"** mọi chỗ (COPYRIGHT, README, portal, STYLE, template, ROADMAP, footer L1–L3, KNOWLEDGE.md) — commit `e791e17` (kèm homepage overhaul).
- **GitHub Pages đã bật và xác nhận live** (`https://qtan-tran.github.io/graecum-vn/`). Vấn đề phát hiện: link `docs/*.md` trên Pages chỉ hiện text thô (static site không render Markdown) + homepage cũ (tiêu đề Anh, link bài 3–6 bị 404). Đã sửa: mọi link tài liệu trỏ sang giao diện GitHub blob (render đẹp, zero-maintenance); homepage bảng bài giảng chuyển tiêu đề tiếng Việt + trạng thái đúng thực tế (1–3 "đã xuất bản", 4–6 "đang biên soạn" không link); CURRICULUM sửa 2 link `docs/READINGS.md` → `readings/README.md` (file không tồn tại).
- **Lesson 3 publish** — `lessons/03-ellipsis-neuter-plural/index.html` (~38KB, 8 mục): lược từ (ellipsis) + câu danh ngữ (nominal sentence), chủ ngữ trung tính số nhiều → động từ số ít (+ liên hệ Ấn-Âu/Hittite/Latin cổ), **trạng từ** (mục CURRICULUM yêu cầu, bản thảo canvas thiếu — tự biên soạn: -ος → -ως, ἀγαθός→ἀγαθῶς, ταχέως), bài đọc simplified tự biên soạn theo chủ đề Anaxagoras DK 59A42 + Aristoteles Magna Moralia 1,1 ("các ngôi sao của Anaxagoras": 3 câu danh ngữ), Latin corners (ars longa vita brevis; bonus→bene), confusables 9 hàng, 6 bài tập + đáp án ẩn. lessons.json L3 `published, rev 2`. Commit: `d6b34f8`.
- **Chuẩn hóa vị trí dấu thanh Hy Lạp (quy ước publish mới, ghi vào STYLE)**: oxytone cuối câu/nghỉ → dấu sắc; trước từ Hy Lạp kế tiếp → dấu huyền (ἐστίν. nhưng ἐστιν ἐν τῷ οὐρανῷ; λαμπρὰ ἐστίν; πολλὰ γάρ). Sửa đồng loạt L1 (19 chỗ ἐστιν huyền sai vị trí → sắc; ἀδελφοὶ ε…; ἐστι(ν) notation thiếu dấu) + L2 (μετά citations) + L3. Script chuẩn hóa dùng NFD-swap, mọi biến thể codepoint (U+03AF/U+1F77/U+1F76).

**Ghi chú vận hành mới (Phần 3):**
- `github_app.get_file_contents` không đọc được text programmatically trong sandbox (object mờ, chỉ hiện qua echo) → lấy file từ repo bằng `curl` (môi trường upgraded) + `diff` theo URL kèm commit-sha; push vẫn qua `push_files` (đọc file durable bằng `file_system.read_file`, nối vòng lặp truncation).
- File scratch `/home/user/graecum-vn/` không bền (remount xóa) — sau push, repo GitHub là nguồn chuẩn; nếu cần lại file thì curl về.

**Còn trong Phần 3 (pipeline mỗi bài: đọc canvas → chuyển hóa → QA → lessons.json → push riêng):**
1. L4: đại từ nhân xưng + mệnh lệnh + phủ định οὐ/μή + AcI bước đầu + tặng cách các dụng pháp (bản đọc: Diogenes Laertios 7,7; Epikur, Brief an Menoikeus 128; 131–132).
2. L5: trung/bị động hiện tại + động từ khuất (deponent) + tính từ danh từ hóa + τις/τι đầy đủ.
3. L6: δύναμαι + đại từ chỉ định (ὅδε/οὗτος); εἶ vs εἰ.

**Quy ước dấu thanh cần ghi thêm vào STYLE-AND-CONVENTIONS khi có dịp**: vị trí huyền/sắc theo quy tắc trên; notation paradigm dùng ἐστί(ν)/εἰσί(ν) (sắc + ν tùy chọn).

## Continuation notes — Phần 2 (kết thúc)

**Đã làm:**
- Repo `qtan-tran/graecum-vn` (public) được tạo bởi người sở hữu; push Phần 1 (14 file) — commit `3b4d527`.
- **Chuyển hướng thuật ngữ (quyết định người sở hữu, ADR-003 cập nhật):** bản publish dùng **tiếng Việt là chính**; chỉ khái niệm khó mới mở ngoặc thuật ngữ Anh (hiatus, vocative, ablative, attributive position, dative of possession…). Bộ tên cách chuẩn: chủ cách (Nom.), sở hữu cách (Gen.), tặng cách (Dat.), đối cách (Acc.), hô cách (Voc.). Không dùng tiếng Đức.
- Cập nhật chính sách vào: STYLE-AND-CONVENTIONS.md, ARCHITECTURE.md (ADR-003), README.md, index.html (portal), KNOWLEDGE.md.
- Viết lại `docs/CURRICULUM.md` → **"Đề cương giáo án 48 bài"** (thuật ngữ tiếng Việt; cột bài đọc giữ nguyên).
- **Pilot Lesson 1 đã publish**: `lessons/01-foundations/index.html` (~61KB): 16 mục, bảng 4 cột có phiên âm, Latin corner, bài đọc simplified tự biên soạn theo chủ đề Homer Ilias 15.187–193 ("Ba anh em thần": tặng cách sở hữu + μέν…δέ, câu hoàn toàn tự viết), từ vựng ★ có phiên âm, bảng confusables 13 hàng, 7 bài tập + đáp án ẩn hiện khi in. Audit bản quyền: mọi câu ví dụ tự biên soạn; chỉ dẫn nguồn: Homer Ilias 15.187–193 (Perseus, PD). lessons.json: L1 `status: published, rev: 2`.
- Commit Phần 2: `83a038d` (docs + curriculum + lessons.json + Lesson 1) + commit vá typo tiếng Việt.
- QA checklist đã chạy: cân bằng thẻ, không ký tự lạ (CJK/Cyrillic), không thuật ngữ Đức, không source-identifying info.

**Còn treo trong Phần 2:**
- GitHub Pages: người sở hữu bật thủ công (Settings → Pages → Deploy from branch → `main` / `(root)` → Save) → URL `https://qtan-tran.github.io/graecum-vn/`. Chưa xác nhận đã bật.

**Bước tiếp theo (Phần 3):**
1. Chuyển hóa Lesson 2–6 (bản thảo canvas) sang quy ước mới theo đúng template pilot L1: thuật ngữ VN-là-chính, bảng 4 cột phiên âm, Latin corner thay ví dụ Đức, viết lại câu lấy từ Lektionstext gốc thành câu tự biên soạn, audit bản quyền từng bài.
2. Thứ tự đề xuất: L2 (Verben đủ ngôi + vocative) → L3 (ellipsis + trung tính nhiều) → L4 (đại từ + mệnh lệnh) → L5 (medium/passiv) → L6 (δύναμαι + demonstrativa).
3. Sau mỗi bài: QA checklist + cập nhật lessons.json (published, rev 2) + push riêng từng commit.

## Continuation notes — Phần 1 (kết thúc)

**Đã làm:**
- Quyết định kiến trúc: 3 repo (portal / toolkit / satzanalyse), static HTML, lessons.json, license CC BY-SA 4.0 + MIT (ADR-001→005 trong ARCHITECTURE.md).
- Quy ước biên soạn mới: thuật ngữ tiếng Anh, bảng 4 cột (Greek/Translit/English/Việt), Latin corner, phiên âm La tinh hóa cấp I, QA checklist.
- Bản đồ curriculum 48 bài v0.1: chủ đề grammar draft + bài đọc PD theo từng bài (Mimnermos, Homer, Plato, Xenophon, NT, Aesop, Lukian, biên khắc…).
- Chính sách bản quyền 3 tầng + pipeline readings + audit checklist.
- Portal skeleton + lesson template: đã soạn, lưu trong kho bền vững của project.

**Ghi chú vận hành:**
- Connector GitHub không có quyền tạo repo mới (403 by design) → người sở hữu tạo repo `graecum-vn` (public) trên GitHub; sau đó push qua connector.
- Bản sao repo Phần 1 được lưu bền vững trong kho project (khung 14 file + bản đồ ánh xạ đường dẫn).

**Bước tiếp theo (Phần 2 — chi tiết):**
1. Người sở hữu tạo repo public `graecum-vn` trên GitHub.
2. Push Phần 1 lên GitHub qua connector, bật GitHub Pages.
3. Chuyển hóa Lesson 1 (bản thảo canvas hiện có) sang quy ước mới — pilot để chuẩn hóa template lần cuối.
4. QA theo checklist, cập nhật lessons.json, publish bài đầu tiên.

**Câu hỏi mở (cần trả lời trước Phần 4):**
- Có cần "About" tiếng Anh song song (cho donor quốc tế/schools) hay chỉ tiếng Việt? (Khuyến nghị: README tiếng Việt, thêm README.en.md sau.)
- Anki decks: dùng scheduler nào (Anki desktop/apkg) — quyết định format ở Phần 6.

## Lịch sử cập nhật roadmap

- Lần 1 (Phần 1): tạo file; trạng thái ban đầu; connector GitHub không tạo được repo — chuyển bước tạo repo về người sở hữu.
- Lần 2 (Phần 2): pilot Lesson 1 publish thành công; ADR-003 cập nhật sang chính sách "thuật ngữ tiếng Việt là chính"; CURRICULUM đổi tên thành "Đề cương giáo án 48 bài"; bước tiếp theo = Phần 3 (chuyển hóa L2–6).
- Lần 3 (giữa Phần 3): yêu cầu ghi công tác giả (BY) triển khai đầy đủ (COPYRIGHT §4, README, portal footer, template, footer L1) — commit `36764b8`; Lesson 2 publish + lessons.json — commit `5c34b2a`; footer chuẩn mọi bài định hình; còn L3–6.
- Lần 4 (giữa Phần 3): Pages xác nhận live; chuẩn hóa ghi công chỉ còn "Tân" + homepage overhaul (link docs sang GitHub blob, tiêu đề VN, trạng thái đúng) — commit `e791e17`; Lesson 3 publish — commit `d6b34f8`; quy ước vị trí dấu thanh Hy Lạp áp dụng cho L1–L3; còn L4–6.
