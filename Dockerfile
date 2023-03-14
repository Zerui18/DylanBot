FROM python:3.8

WORKDIR /app
COPY . /app

EXPOSE 80/tcp

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN ["httpserver", "-p 80", "-a 0.0.0.0", "&"]

CMD ["python", "main.py"]