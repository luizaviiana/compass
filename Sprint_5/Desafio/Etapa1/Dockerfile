FROM python:3.10-slim

WORKDIR /app

COPY upload_s3.py .

RUN pip install boto3 python-dotenv

CMD ["python", "upload_s3.py"]
