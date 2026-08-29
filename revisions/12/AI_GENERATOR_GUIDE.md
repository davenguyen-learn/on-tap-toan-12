# 🚀 HƯỚNG DẪN SỬ DỤNG SCRIPT SINH KHO BÀI TẬP FLASHCARD BẰNG GEMINI AI

Script [**`generate_flashcards_ai.py`**](file:///c:/Users/Admin/Code/Test/toan-12/revisions/12/generate_flashcards_ai.py) cho phép bạn sử dụng API của **Google Gemini** để tự động sinh **hàng ngàn câu hỏi bài tập chất lượng cao**, bám sát 100% chương trình SGK Toán 12 GDPT 2018.

---

## 🔑 1. Lấy API Key miễn phí từ Google
Nếu bạn chưa có API Key:
1. Truy cập [Google AI Studio (aistudio.google.com)](https://aistudio.google.com/app/apikey).
2. Đăng nhập tài khoản Google và bấm **"Create API Key"**.
3. Copy đoạn mã key (bắt đầu bằng `AIzaSy...`).

---

## 💻 2. Các lệnh chạy linh hoạt

### 🔹 Cách 1: Chạy trực tiếp truyền API Key (Khuyên dùng)
```bash
python generate_flashcards_ai.py --api-key "AIzaSy..."
```

### 🔹 Cách 2: Thiết lập biến môi trường (Không cần gõ lại key)
* **Trên PowerShell (Windows):**
  ```powershell
  $env:GEMINI_API_KEY="AIzaSy..."
  python generate_flashcards_ai.py
  ```
* **Trên Command Prompt (CMD):**
  ```cmd
  set GEMINI_API_KEY=AIzaSy...
  python generate_flashcards_ai.py
  ```

---

## ⚙️ 3. Các tùy chọn mở rộng & Nâng cao

| Lệnh | Ý nghĩa |
| :--- | :--- |
| `python generate_flashcards_ai.py --target 1000` | Sinh đủ mục tiêu 1.000 câu hỏi (mặc định) |
| `python generate_flashcards_ai.py --target 500` | Đặt mục tiêu 500 câu hỏi |
| `python generate_flashcards_ai.py --chapter c1 --target 200` | Chỉ sinh riêng cho **Chương 1 (Khảo sát hàm số)** |
| `python generate_flashcards_ai.py --chapter c6 --target 200` | Chỉ sinh chuyên sâu cho **Chương 6 (Xác suất Bayes)** |
| `python generate_flashcards_ai.py --reset` | Xóa database cũ và bắt đầu sinh mới từ con số 0 |

---

## ✨ 4. Điểm đặc biệt của Script

1. **Chống lặp đề & Bám sát ma trận:**
   * Script tích hợp bản đồ chuyên đề gồm **hơn 50 dạng toán nhỏ** phân chia tỉ mỉ cho cả 6 chương. Mỗi lần gọi API sẽ yêu cầu AI tạo câu hỏi theo từng phân nhánh bài toán cụ thể.
2. **Tự động lưu & Khả năng tiếp tục (Resume):**
   * Sau mỗi mẻ (batch 5 câu), script sẽ lưu ngay vào SQLite Database.
   * Nếu đang chạy mà bạn bấm `Ctrl + C` hoặc mạng bị gián đoạn, lần sau bạn chỉ cần chạy lại lệnh, script sẽ tự động nhận biết số câu đã có và **tiếp tục sinh tiếp mà không bị trùng lặp**.
3. **Xử lý giới hạn tần suất (Rate Limit 429):**
   * Tự động nghỉ (exponential backoff) và thử lại nếu vượt quá số lượt gọi/phút của API free-tier.
4. **Đồng bộ tự động lên Web:**
   * Ngay khi sinh xong, dữ liệu được tự động nạp vào file giao diện [`index.html`](file:///c:/Users/Admin/Code/Test/toan-12/revisions/12/index.html) để bạn mở lên học ngay.
