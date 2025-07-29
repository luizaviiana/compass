import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

trusted_db = "filmes_trusted_db"
trusted_table = "csv_movies"

df_csv = glueContext.create_dynamic_frame.from_catalog(
    database=trusted_db,
    table_name=trusted_table
).toDF()

df_tempo = (
    df_csv
    .select("anolancamento")
    .withColumn("anolancamento", col("anolancamento").cast("int"))
    .filter((col("anolancamento").isNotNull()) & (col("anolancamento") >= 1950))
    .dropDuplicates()
    .withColumnRenamed("anolancamento", "id_tempo")
    .withColumn("ano", col("id_tempo").cast("int"))
    .withColumn("decada", ((col("id_tempo") / 10).cast("int") * 10).cast("int"))
)

df_tempo.write.mode("overwrite").format("parquet").save("s3://data-compass-ana/Refined/DimTempo/")
