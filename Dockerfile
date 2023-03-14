FROM python:3.8

WORKDIR /app
COPY . /app

EXPOSE 80/tcp

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN ["python", "server.py", "&"]

CMD ["python", "main.py"]