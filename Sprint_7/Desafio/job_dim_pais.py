import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, explode


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

trusted_db = "filmes_trusted_db"
trusted_table = "tmdb_movies"

df_tmdb = glueContext.create_dynamic_frame.from_catalog(
    database=trusted_db,
    table_name=trusted_table
).toDF()

df_origin = (
    df_tmdb
    .select("origin_country")
    .withColumn("id_pais", explode(col("origin_country")))
    .select("id_pais")
    .dropDuplicates()
)

df_prod = (
    df_tmdb
    .selectExpr("explode(production_countries) as pais")
    .selectExpr("pais.iso_3166_1 as id_pais", "pais.name as nome_pais")
    .dropna(subset=["id_pais"])
    .dropDuplicates()
)

df_dim_pais = (
    df_origin
    .join(df_prod, on="id_pais", how="left")
    .dropDuplicates(["id_pais", "nome_pais"])
)

df_dim_pais.write.mode("overwrite").format("parquet").save("s3://data-compass-ana/Refined/DimPais/")