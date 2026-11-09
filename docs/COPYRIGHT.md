# Chính sách bản quyền (COPYRIGHT) v1.0

Project này miễn phí cho người học, và phải **sạch bản quyền để tồn tại 10 năm**. Bản quyền không phải là vấn đề đạo đức trừu tượng ở đây: nếu repo host nội dung sao chép, nó sẽ bị DMCA gỡ — và toàn bộ "hub tiêu chuẩn" sụp đổ. Vì vậy chính sách này là **ràng buộc kỹ thuật**, không phải khẩu hiệu.

## 1. Ba tầng nội dung

### Tầng A — An toàn tuyệt đối
- **Sự thật ngôn ngữ**: bảng chia (paradigms), đuôi từ, chức năng cách, thuật ngữ, trình tự chủ đề ngữ pháp. Kiến thức chung của nhân loại, không thể có bản quyền.
- **Văn bản gốc tiếng Hy Lạp cổ**: Homer, Plato, Xenophon, Kinh Thánh Hy Lạp, Aesop, inscriptions… Tác giả đã mất hơn 2000 năm → public domain.
- **Ngữ pháp public domain**: Smyth (1920), Goodwin, Hadley-Allen, Veitch… chọn đúng nguồn PD.
- **Chính nội dung project tự biên soạn**: giải thích, ví dụ, bài tập, bản simplified, bảng so sánh — viết bởi project, cấp license CC BY-SA 4.0.

### Tầng B — Phải làm sạch / không bao giờ xuất bản
- ❌ **Text adapted (Lektionstext) của giáo trình bản quyền** (Kantharos, Athenaze, JACT, Hansen & Quinn…): không trích, không dịch lại, không tái tạo "đúng bản giáo trình".
- ❌ **Bài tập gốc** của các giáo trình đó.
- ❌ **Trình tự 1:1 chương trình giáo trình** khi publish: curriculum của ta tự thiết kế (danh mục *citations* tác giả/tác phẩm/đoạn là sự thật, được phép tham khảo làm inspiration — nhưng grammar progression, cách biên soạn, toàn bộ simplified texts là của ta).
- ❌ **Host file PDF/scans** của bất kỳ tài liệu bản quyền nào.
- ❌ Bản dịch tiếng Việt của người khác nếu không có phép.

### Tầng C — Link thoải mái (không host, chỉ dẫn)
- Review/so sánh giáo trình bản quyền: **được phép**, miễn là chỉ có (a) nhận định của ta, (b) metadata, (c) link mua/borrow chính thống.
- Tool miễn phí (Logeion, Perseus/Scaife, Morpheus…): link + hướng dẫn dùng.

## 2. Quy tắc cho văn bản đọc (readings)

Mỗi bài đọc trong `readings/` phải tuân thủ pipeline:

1. **Bản gốc** (Greek text): chỉ từ nguồn public domain (Perseus, Scaife, PHI, Wikisource el, Theoi, die-bibel.de cho NT, packhum cho inscriptions). Ghi rõ: tác giả, tác phẩm, đoạn, cổng đọc, link.
2. **Bản simplified** (cho người mới): **tự biên soạn từ bản gốc PD** — giảm cấu trúc khó, thay từ hiếm bằng từ trong danh mục bài học, giữ tinh thần đoạn văn. Không "biên tập lại" theo bản adapted của bất kỳ giáo trình nào. Mức đơn giản hóa ghi rõ (VD: "simplified ~80% từ vựng thuộc L1–L6").
3. **Phân tích + dịch**: của project.
4. **Citations**: ghi dạng chuẩn "Plato, Apology 33a–b (Perseus)" — citations là sự thật, luôn an toàn.

Self-check trước khi publish một reading: *"Nếu một luật sư của nhà xuất bản X đọc đoạn này, họ có thể chỉ ra dòng nào là sao chép từ sách của họ không?"* Nếu câu trả lời là "có", viết lại.

## 3. Quy tắc cho từ vựng

- Danh sách từ vựng theo bài: **của project** (chọn từ theo văn bản đọc của ta).
- Danh sách tần suất: chỉ dùng nguồn mở (VD: Dickinson College Commentaries Greek Core Vocabulary, CC BY-SA; Logeion open data) + ghi nguồn.
- Nghĩa tiếng Việt: tự biên soạn; khi đối chiếu từ điển có bản quyền thì chỉ lấy *sự thật nghĩa*, không sao chép định dạng/ví dụ của từ điển.

## 4. License của project

- **Nội dung bài giảng, readings, vocab, tài liệu**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Lý do chọn BY-SA (không NC): muốn người khác được học, chia sẻ, dịch, xây tool lên trên — với điều kiện ghi công và chia sẻ lại cùng license. NC sẽ chặn chính các use case ta muốn khuyến khích.
- **Code (script sinh Anki, template, sau này platform)**: MIT.
- Mỗi file bài giảng ghi license ở footer; repo có file `LICENSE`.

## 5. Checklist audit bản quyền mỗi lần publish

- [ ] Mọi câu ví dụ Hy Lạp: tự viết HOẶC từ văn bản PD có citation.
- [ ] Mọi bài tập: tự biên soạn.
- [ ] Mọi bản dịch tiếng Việt/Anh trong ví dụ: tự biên soạn (bản dịch cũng có bản quyền!).
- [ ] Không dùng bảng biểu, minh họa, layout đặc trưng sao chép từ giáo trình.
- [ ] Không nhắc tên giáo trình/trường/giảng viên trong nội dung bài học (giữ tính độc lập biên soạn).
- [ ] Sources section: chỉ chứa nguồn PD và tool mở.
