import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode, when
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

df_artistas = (
    df_tmdb
    .select(explode(col("credits.cast")).alias("cast"))
    .select(
        col("cast.id").cast("string").alias("id_artista"),
        col("cast.name").cast("string").alias("nome_artista"),
        when(col("cast.gender") == 0, None)
            .otherwise(col("cast.gender"))
            .cast("int")
            .alias("genero")
    )
    .dropDuplicates(["id_artista"])
)

df_artistas.write.mode("overwrite").format("parquet").save(
    "s3://data-compass-ana/Refined/DimArtista/"
)