# Graecum VN — Ancient Greek cho người Việt

**Một hub tự học tiếng Hy Lạp cổ (Ancient Greek / Altgriechisch) hoàn toàn miễn phí, bằng tiếng Việt**, cho người học từ con số không đến đọc được Plato, Xenophon, Kinh Thánh Hy Lạp (Koine) và các văn bản trung–khó khác.

> Tất cả nội dung: **CC BY-SA 4.0** · Code: **MIT** · Biên soạn bởi **Trần Quốc Tân** · Không quảng cáo, không paywall, không thu thập dữ liệu.

**Bản tiếng Anh:** [README.en.md](README.en.md) · [Portal tiếng Anh](https://qtan-tran.github.io/graecum-vn/en/)

## Vì sao có project này?

- Gần như **không có tài liệu tiếng Việt chất lượng cao** để tự học tiếng Hy Lạp cổ; người Việt phải học qua tiếng Đức, Anh, Pháp — một rào cản kép (học ngôn ngữ cổ bằng ngôn ngữ thứ ba).
- Tài liệu miễn phí trên mạng (Perseus, Scaife, Logeion, ngữ pháp public domain) rất tốt nhưng **rải rác, bằng tiếng Anh**, và không có lộ trình.
- Project này là **lộ trình + bài giảng + văn bản đọc + công cụ** nối tất cả lại, để người tự học tiếng Việt có **một nơi duy nhất để bắt đầu và duy trì việc học**.

## Lộ trình 48 bài (2 cấp)

| Cấp | Bài | Mục tiêu đầu ra |
| --- | --- | --- |
| **Graecum I** (tương đương trình độ chứng chỉ Graecum) | 1–24 | Nắm toàn bộ hình thái (declension, động từ các thì/thức) + cú pháp nền tảng; đọc văn xuôi Attic đơn giản (Xenophon adapted) với từ điển. |
| **Graecum II** | 25–48 | Cú pháp nâng cao (participle, optative, indirect speech, articular infinitive…) và đọc văn bản gốc trung–khó: Plato, Xenophon, Euripides, NT, Homer, Herodot. |

Xem chi tiết: [docs/CURRICULUM.md](docs/CURRICULUM.md)

## Cấu trúc repo

```
├── index.html              # Portal (GitHub Pages) — bắt đầu từ đây
├── lessons/                # 48 bài giảng, mỗi bài 1 file HTML tự chứa
├── readings/               # Văn bản đọc public domain + bản đơn giản hóa kèm phân tích
├── vocab/                  # Từ vựng theo bài, có phiên âm La tinh hóa; Anki decks
├── docs/                   # Kiến trúc, quy ước biên soạn, bản quyền, roadmap
└── toolkit.md              # Trỏ sang repo riêng ancient-greek-toolkit (hub công cụ EN, đã tách)
```

## Cách dùng bài giảng

1. Đọc trực tiếp trên web (GitHub Pages) hoặc **Download** file HTML.
2. Học offline: mở file HTML bằng bất kỳ trình duyệt nào — không cần mạng, không phụ thuộc bên thứ ba.
3. Muốn in: mở file → **Ctrl+P → Save as PDF** — đáp án bài tập tự hiện khi in.

## Nguyên tắc biên soạn (tóm tắt)

- Giải thích bằng **tiếng Việt**; thuật ngữ quen thuộc dùng tiếng Việt, chỉ khái niệm khó mới mở ngoặc thêm thuật ngữ Anh để tra cứu (*hiatus*, *vocative*, *ablative*…).
- Ví dụ dùng **tiếng Anh hoặc tiếng Việt** để nhìn thấy pattern; thỉnh thoảng có **so sánh Latin** (hai ngôn ngữ rất gần nhau).
- Từ vựng cấp I luôn kèm **phiên âm La tinh hóa** (VD: ὁ ἄνθρωπος → *ho ánthrōpos*) để người Việt đọc được ngay.
- Mỗi bài: bảng ví dụ 4 cột (Hy Lạp – phiên âm – English – Việt), mục "Watch out" cho điểm dễ nhầm, bảng tổng hợp so sánh cuối bài, bài tập + đáp án ẩn (hiện khi in).

Chi tiết: [docs/STYLE-AND-CONVENTIONS.md](docs/STYLE-AND-CONVENTIONS.md)

## Chính sách bản quyền

Nội dung biên soạn **độc lập**. Chỉ dùng: ngữ pháp/sự thật ngôn ngữ (không thuộc bản quyền), văn bản gốc **public domain** (tác giả cổ, ngữ pháp cổ điển), và tự viết ví dụ/bài tập/văn bản đọc đơn giản hóa. Không lưu trữ hoặc sao chép bất kỳ giáo trình có bản quyền nào. Chi tiết: [docs/COPYRIGHT.md](docs/COPYRIGHT.md).

## Cách ghi công (bắt buộc khi tái sử dụng)

Mọi nội dung do **Trần Quốc Tân** biên soạn và phát hành miễn phí theo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Khi cite, trích dẫn, dịch, in lại, dạy lại hoặc xây dựng material trên nội dung này, **phải ghi công rõ ràng**:

> Nguồn: **Graecum VN** — biên soạn bởi **Trần Quốc Tân**, https://github.com/qtan-tran/graecum-vn, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

This repository is developed and maintained by **Quoc-Tan Tran**, **Postdoctoral Researcher** at the **Institute for Studies of Science, Bielefeld University**.

Nếu có chỉnh sửa, ghi thêm "có chỉnh sửa". Trường hợp thương mại/trường học/dịch thuật, nguyên tắc không đổi. Chi tiết: [docs/COPYRIGHT.md](docs/COPYRIGHT.md) mục 4.

## Trạng thái

| Hạng mục | Trạng thái |
| --- | --- |
| Kiến trúc + tài liệu nền | ✅ Phần 1 |
| Template bài giảng chuẩn | ✅ Phần 1 |
| Bài 1–6 (nhập môn) | 🔄 dạng bản thảo tiếng Việt (đang chuyển sang quy ước mới) |
| Bài 7–24 (Graecum I) | 📋 trong roadmap |
| Graecum II (25–48) | 📋 trong roadmap |
| Toolkit repo + Anki + platform phân tích câu | 📋 trong roadmap |

Xem: [docs/ROADMAP.md](docs/ROADMAP.md)

## Đóng góp

Mọi đóng góp đều chào đón: soát lỗi tiếng Việt, viết bài tập, biên soạn văn bản đọc, làm Anki deck. Bắt đầu từ [docs/ROADMAP.md](docs/ROADMAP.md), [CONTRIBUTING.md](CONTRIBUTING.md) và Issues.
