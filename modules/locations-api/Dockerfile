FROM python:3.7-alpine

WORKDIR .

RUN apk add gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5003

COPY . .
CMD ["python3", "-u", "main.py"]
