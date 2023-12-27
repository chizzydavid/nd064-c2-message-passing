FROM python:3.9.6

WORKDIR .

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5002

ENV PYTHONUNBUFFERED=1

COPY . .
CMD ["python3", "-u", "main.py"]

