# FaceXFormer Pipeline - Age, Gender & Race Detection

## 📌 Giới Thiệu

Đây là một ứng dụng sử dụng OpenCV và mô hình **FaceXFormer Pipeline** để nhận diện **tuổi, giới tính và chủng tộc** từ camera.

📷 **Chức năng chính:**

-   Mở camera và phát video trực tiếp.
-   Chụp một frame, xử lý nhận diện tuổi, giới tính và chủng tộc.
-   Hiển thị kết quả trực tiếp trên video.
-   Nhấn 'q' để thoát chương trình.

## 📂 Cấu Trúc Thư Mục

```
facexformer_app/
│── 📂 services                  # Chứa các service cần thiết
│── 📂 public                    # Chứa các ảnh test, các ảnh dùng cho việc viết docs và file readme
│── 📂 constant                  # Chứa các constant như age, gender, race để mapping cho dữ liệu đầu ra
│── 📂 result                    # Chứa các kết quả test các tính năng của faceXformer
│── 📂 test                      # Chứa các file test cho từng tính năng
│── main.py                    # File main thực hiện chương trình
│── requirements.txt           # Danh sách thư viện cài đặt
│── README.md                  # Tài liệu hướng dẫn
```

## 🚀 Hướng Dẫn Cài Đặt & Chạy

### 1️⃣ Cài Đặt Môi Trường & Thư Viện

**Yêu cầu:** Python 3.8+ và OpenCV

```bash
# Tạo môi trường ảo (khuyến khích)
python -m venv venv
source venv/bin/activate  # Trên macOS/Linux
venv\Scripts\activate     # Trên Windows

# Cài đặt thư viện
pip install facexformer_pipeline image_input_handler
```

### 2️⃣ Chạy Chương Trình

```bash
python main.py
```

## 📌 Phím Tắt

-   Nhấn **'c'** để chụp ảnh và dự đoán tuổi.
-   Nhấn **'q'** để thoát chương trình.

## 📧 Liên Hệ

Nếu có bất kỳ vấn đề nào, hãy liên hệ qua email: `huyhoangnguyen301202@gmail.com`
