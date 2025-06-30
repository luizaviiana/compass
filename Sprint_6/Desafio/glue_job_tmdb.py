import sys
import re
from pyspark.sql.functions import lit, input_file_name
from pyspark.sql.types import *

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

tmdb_json_path = "s3://data-compass-ana/Raw/TMDB/JSON/movies/2025/06/17/"

match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", tmdb_json_path)
if match:
    year, month, day = match.group(1), match.group(2), match.group(3)
else:
    raise ValueError("Data não encontrada no caminho do S3.")

tmdb_output_path = f"s3://data-compass-ana/Trusted/TMDB/Parquet/Movies/{year}/{month}/{day}/"

tmdb_schema = StructType([
    StructField("adult", BooleanType()),
    StructField("backdrop_path", StringType()),
    StructField("belongs_to_collection", StructType([
        StructField("id", LongType()),
        StructField("name", StringType()),
        StructField("poster_path", StringType()),
        StructField("backdrop_path", StringType()),
    ])),
    StructField("budget", LongType()),
    StructField("genres", ArrayType(StructType([
        StructField("id", LongType()),
        StructField("name", StringType()),
    ]))),
    StructField("homepage", StringType()),
    StructField("id", LongType()),
    StructField("imdb_id", StringType()),
    StructField("origin_country", ArrayType(StringType())),
    StructField("original_language", StringType()),
    StructField("original_title", StringType()),
    StructField("overview", StringType()),
    StructField("popularity", DoubleType()),
    StructField("poster_path", StringType()),
    StructField("production_companies", ArrayType(StructType([
        StructField("id", LongType()),
        StructField("logo_path", StringType()),
        StructField("name", StringType()),
        StructField("origin_country", StringType())
    ]))),
    StructField("production_countries", ArrayType(StructType([
        StructField("iso_3166_1", StringType()),
        StructField("name", StringType())
    ]))),
    StructField("release_date", StringType()),
    StructField("revenue", LongType()),
    StructField("runtime", IntegerType()),
    StructField("spoken_languages", ArrayType(StructType([
        StructField("english_name", StringType()),
        StructField("iso_639_1", StringType()),
        StructField("name", StringType())
    ]))),
    StructField("status", StringType()),
    StructField("tagline", StringType()),
    StructField("title", StringType()),
    StructField("video", BooleanType()),
    StructField("vote_average", DoubleType()),
    StructField("vote_count", IntegerType()),
    StructField("credits", StructType([
        StructField("cast", ArrayType(StructType([
            StructField("adult", BooleanType()),
            StructField("gender", IntegerType()),
            StructField("id", LongType()),
            StructField("known_for_department", StringType()),
            StructField("name", StringType()),
            StructField("original_name", StringType()),
            StructField("popularity", DoubleType()),
            StructField("profile_path", StringType()),
            StructField("cast_id", IntegerType()),
            StructField("character", StringType()),
            StructField("credit_id", StringType()),
            StructField("order", IntegerType()),
        ]))),
        StructField("crew", ArrayType(StructType([
            StructField("adult", BooleanType()),
            StructField("gender", IntegerType()),
            StructField("id", LongType()),
            StructField("known_for_department", StringType()),
            StructField("name", StringType()),
            StructField("original_name", StringType()),
            StructField("popularity", DoubleType()),
            StructField("profile_path", StringType()),
            StructField("credit_id", StringType()),
            StructField("department", StringType()),
            StructField("job", StringType()),
        ]))),
    ])),
    StructField("keywords", StructType([
        StructField("keywords", ArrayType(StructType([
            StructField("id", LongType()),
            StructField("name", StringType())
        ])))
    ])),
    StructField("release_dates", StructType([
        StructField("results", ArrayType(StructType([
            StructField("certification", StringType(), nullable=True),
            StructField("iso_3166_1", StringType()),
            StructField("release_date", StringType())
        ])))
    ])),
])

tmdb_df = (
    spark.read
    .schema(tmdb_schema)
    .option("multiline", True)
    .option("recursiveFileLookup", "true")
    .json(tmdb_json_path)
)

print("Leitura finalizada com schema definido.")
print("Total de registros:", tmdb_df.count())

tmdb_df.write.mode("overwrite").parquet(tmdb_output_path)

print("Dados gravados com sucesso em:", tmdb_output_path)

job.commit()

