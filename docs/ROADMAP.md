# ROADMAP phát triển project — cập nhật lần 1 (sau Phần 1)

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
| **3** | Chuyển hóa Lesson 2–6 sang quy ước mới, audit bản quyền từng bài | ☐ |
| **4** | Repo `greek-toolkit-vn` (hub tools + so sánh tài liệu) | ☐ |
| **5** | Lesson 7–10 mới hoàn chỉnh (bắt đầu phần curriculum chưa có bản thảo) + readings pipeline (bản simplified đầu tiên) | ☐ |
| **6** | Vocab TSV + script sinh Anki deck cho L1–10 (CC BY-SA) | ☐ |
| **7–12** | Lesson 11–24 (hoàn thành Graecum I); cập nhật roadmap giữa chừng | ☐ |
| **13+** | Graecum II (L25–48) + satzanalyse platform + cộng đồng | ☐ |

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
