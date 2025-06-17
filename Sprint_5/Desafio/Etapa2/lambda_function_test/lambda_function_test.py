import os
import json
import uuid
import boto3
import datetime
from dotenv import load_dotenv
from tmdb_client import buscar_ids_filmes_guerra, buscar_detalhes_filme

load_dotenv()

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client('s3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

def salvar_em_json_s3(dados, max_por_arquivo=100):
    for i in range(0, len(dados), max_por_arquivo):
        lote = dados[i:i + max_por_arquivo]
        nome_arquivo = f"{uuid.uuid4()}.json"
        
        json_bytes = json.dumps(lote, ensure_ascii=False, indent=2).encode('utf-8')
        
        now = datetime.datetime.now(datetime.timezone.utc)
        prefixo = f"Raw/TMDB/JSON/movies/{now.year}/{now.month:02d}/{now.day:02d}/"
        s3_key = prefixo + nome_arquivo

        s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=json_bytes)
        print(f"Enviado para S3: {s3_key} ({len(lote)} filmes)")

def lambda_handler(event=None, context=None):
    print("Buscando IDs de filmes de guerra...")
    ids = buscar_ids_filmes_guerra()
    print(f"Total de filmes encontrados: {len(ids)}")

    detalhes = []
    for idx, id_filme in enumerate(ids):
        print(f"({idx+1}/{len(ids)}) Buscando detalhes do filme ID: {id_filme}")
        dados = buscar_detalhes_filme(id_filme)
        if dados:
            detalhes.append(dados)

    print("Enviando arquivos JSON para o S3...")
    salvar_em_json_s3(detalhes, max_por_arquivo=100)
    return {"statusCode": 200, "body": f"{len(detalhes)} filmes enviados para o S3."}


if __name__ == "__main__":
    resultado = lambda_handler()
    print("Resultado:", resultado)

