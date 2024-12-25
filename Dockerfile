# Sử dụng Python 3.10-slim làm hình ảnh cơ sở
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các tệp yêu cầu và cài đặt các gói Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . .

# Mở cổng 8000
EXPOSE 8000

# Đặt biến môi trường cho Flask
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Khởi chạy ứng dụng Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]