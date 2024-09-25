FROM python:3.11.5

# Çıktıları tamponlama ve root kullanımı için ayarlar
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=true

# Uygulama dizinini oluştur ve içine kopyala
WORKDIR /car
COPY . .

# Gerekli paketlerin yüklenmesi
RUN apt update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        python3-dev \
        graphviz \
        unixodbc-dev \
        default-libmysqlclient-dev \
        libaio1 && \
    python -m pip install --upgrade pip && \
    pip install pkginfo virtualenv poetry && \
    poetry config cache-dir /car/cache && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev -vvv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Komut
CMD ["poetry", "run", "python", "main.py"]
