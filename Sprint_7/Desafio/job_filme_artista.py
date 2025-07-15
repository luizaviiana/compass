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

df_filme_artista = (
    df_tmdb
    .select("imdb_id", explode(col("credits.cast")).alias("cast"))
    .select(
        col("imdb_id").alias("id_filme"),
        col("cast.id").cast("string").alias("id_artista"),
        col("cast.character").alias("papel"),
        col("cast.order").cast("int").alias("ordem_elenco")
    )
    .dropna(subset=["id_filme", "id_artista"])
)

df_filme_artista.write.mode("overwrite").format("parquet").save("s3://data-compass-ana/Refined/FilmeArtista/")
