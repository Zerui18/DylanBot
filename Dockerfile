FROM python:3.8

WORKDIR /app
COPY . /app

EXPOSE 80/tcp

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "(python -m http.server 80 -b 0.0.0.0 < /dev/null) & python main.py"]