# Python temel imaji
FROM python:3.10-slim

# Terminal ciktilarini anlik goster
ENV PYTHONUNBUFFERED=1

# Konteyner icindeki calisma klasoru
WORKDIR /app

# Gerekli kutuphaneleri kopyala
COPY requirements.txt .

# Python kutuphanelerini yukle
RUN pip install --no-cache-dir -r requirements.txt

# Simulator kodlarini kopyala
COPY simulator/ ./simulator/

# Simulatoru baslat
CMD ["python", "simulator/main.py"]