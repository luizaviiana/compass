FROM python:3.11-slim

WORKDIR /app

COPY csv_limpo.csv /app/csv_limpo.csv

COPY job.py /app/job.py

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

VOLUME /app/volume

CMD ["python", "job.py"]