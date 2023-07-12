FROM python:3.11.4

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src

ENTRYPOINT python src/main.py