import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list, element_at
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

trusted_db = "filmes_trusted_db"
refined_db = "filmes_refined_db"

df_csv = glueContext.create_dynamic_frame.from_catalog(
    database=trusted_db,
    table_name="csv_movies"
).toDF()

df_tmdb = glueContext.create_dynamic_frame.from_catalog(
    database=trusted_db,
    table_name="tmdb_movies"
).toDF()

df_csv = df_csv.withColumn("id", col("id").cast("string"))
df_tmdb = df_tmdb.withColumn("imdb_id", col("imdb_id").cast("string"))

df_join = (
    df_csv.alias("csv")
    .join(
        df_tmdb.select("imdb_id", "original_title", "origin_country", "popularity").alias("tmdb"),
        col("csv.id") == col("tmdb.imdb_id"),
        "inner"
    )
)

janela = Window.partitionBy("csv.id").orderBy(desc("csv.numerovotos"))
df_filmes_unicos = (
    df_join
    .withColumn("rn", row_number().over(janela))
    .filter(col("rn") == 1)
    .drop("rn")
)

df_filtrado = (
    df_filmes_unicos
    .filter(col("csv.notamedia") >= 6)
    .filter(col("csv.numerovotos") >= 100)
    .filter(col("csv.anolancamento") >= 1950)
    .select(
        col("csv.id").alias("id_filme"),
        col("csv.tituloPincipal").alias("titulo_principal"),
        col("tmdb.original_title").alias("titulo_original"),
        col("csv.anolancamento").alias("ano_lancamento"),
        element_at(col("tmdb.origin_country"), 1).alias("id_pais"),
        col("csv.notamedia").cast("double").alias("nota_media"),      
        col("csv.numerovotos").cast("int").alias("numero_votos"),     
        col("tmdb.popularity").alias("popularidade")
    )
)

df_dim_tempo = glueContext.create_dynamic_frame.from_catalog(
    database=refined_db,
    table_name="dimtempo"
).toDF()

df_fato = (
    df_filtrado.alias("f")
    .join(df_dim_tempo.alias("dt"), col("f.ano_lancamento") == col("dt.ano"), "left")
    .select(
        col("f.id_filme"),
        col("f.titulo_principal"),
        col("f.titulo_original"),
        col("id_pais"),
        col("f.nota_media"),
        col("f.numero_votos"),
        col("f.popularidade"),
        col("dt.id_tempo").cast("int").alias("id_tempo")   
    )
)

df_fato.write.mode("overwrite").format("parquet").save(
    "s3://data-compass-ana/Refined/FatoRepresentacaoFeminina/"
)
