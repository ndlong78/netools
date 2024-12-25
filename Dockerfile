FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cài đặt traceroute
RUN apt-get update && apt-get install -y traceroute

COPY . .

EXPOSE 8000

CMD ["python", "run.py"]