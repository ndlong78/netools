# Sử dụng Python 3.9 làm hình ảnh cơ sở
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các tệp yêu cầu và cài đặt các gói Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . .

# Mở cổng 10000
EXPOSE 10000

# Khởi chạy ứng dụng Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=10000"]