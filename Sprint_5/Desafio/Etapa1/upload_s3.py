import os
import boto3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")  
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = "data-compass-ana"

today = datetime.today()
year = str(today.year)
month = f"{today.month:02d}"
day = f"{today.day:02d}"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,  
    region_name=AWS_REGION
)

def upload_file_to_s3(file_path, data_type):

    file_name = os.path.basename(file_path)

    s3_key = f"Raw/Local/CSV/{data_type}/{year}/{month}/{day}/{file_name}"

    print(f"Fazendo upload de {file_name} para s3://{BUCKET_NAME}/{s3_key}")

    try:
        s3.upload_file(
            Filename=file_path,
            Bucket=BUCKET_NAME,
            Key=s3_key
        )
        print(f"Upload de {file_name} concluído com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar {file_name}: {e}")

if __name__ == "__main__":
    upload_file_to_s3("movies.csv", "Movies")
    upload_file_to_s3("series.csv", "Series")
