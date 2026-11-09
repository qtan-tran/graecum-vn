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
| **2** | Tạo repo GitHub + push Phần 1 + bật GitHub Pages; chuẩn hóa pilot: chuyển hóa **Lesson 1** sang quy ước mới (thuật ngữ Anh, bảng 4 cột có transliteration, Latin corner) | ▶ ĐANG LÀM: push xong (commit 3b4d527); chờ bật Pages (user) + pilot Lesson 1 |
| **3** | Chuyển hóa Lesson 2–6 sang quy ước mới, audit bản quyền từng bài | ☐ |
| **4** | Repo `greek-toolkit-vn` (hub tools + so sánh tài liệu) | ☐ |
| **5** | Lesson 7–10 mới hoàn chỉnh (bắt đầu phần curriculum chưa có bản thảo) + readings pipeline (bản simplified đầu tiên) | ☐ |
| **6** | Vocab TSV + script sinh Anki deck cho L1–10 (CC BY-SA) | ☐ |
| **7–12** | Lesson 11–24 (hoàn thành Graecum I); cập nhật roadmap giữa chừng | ☐ |
| **13+** | Graecum II (L25–48) + satzanalyse platform + cộng đồng | ☐ |

## Continuation notes — Phần 2 (đang làm)

**Đã làm:**
- Repo `qtan-tran/graecum-vn` (public) được tạo bởi người sở hữu; push Phần 1 (14 file) lên `main` thành công — commit `3b4d527`.
- GitHub Pages: connector không có tool bật Pages → người sở hữu bật thủ công: Settings → Pages → Source "Deploy from a branch" → `main` / `(root)` → Save. URL dự kiến: `https://qtan-tran.github.io/graecum-vn/`.

**Bước tiếp theo trong Phần 2:**
1. Chuyển hóa Lesson 1 (bản thảo canvas hiện có) sang quy ước mới: thuật ngữ Anh, bảng 4 cột có phiên âm, Latin corner thay ví dụ Đức, ví dụ EN/VI; viết lại các câu ví dụ lấy từ Lektionstext gốc thành câu tự biên soạn (audit bản quyền).
2. Bài đọc Lesson 1: bản simplified tự biên soạn theo chủ đề Iliad 15.187–193 (chia ba vương quốc); bản gốc PD tích hợp sau ở readings pipeline (Phần 5) khi fetch text chính xác từ Perseus.
3. QA theo checklist → cập nhật lessons.json (`status: published`, `rev: 2`) → push → portal live.

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
