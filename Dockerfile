FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY app /app
COPY docker/start.sh /docker/start.sh
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip==22.1.1
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/docker/start.sh"]
