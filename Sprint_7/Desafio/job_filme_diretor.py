import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode
from pyspark.sql import SparkSession

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

trusted_db = "filmes_trusted_db"
trusted_table = "tmdb_movies"

df_tmdb = glueContext.create_dynamic_frame.from_catalog(
    database=trusted_db,
    table_name=trusted_table
).toDF()

df_diretores = (
    df_tmdb
    .select(col("imdb_id"), explode(col("credits.crew")).alias("crew"))
    .filter(col("crew.job") == "Director")
    .select(
        col("imdb_id").alias("id_filme"),
        col("crew.id").cast("string").alias("id_diretor")
    )
    .dropDuplicates(["id_filme", "id_diretor"])
)

df_diretores.write.mode("overwrite").format("parquet").save("s3://data-compass-ana/Refined/FilmeDiretor/")
