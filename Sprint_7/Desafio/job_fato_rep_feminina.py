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

df_filtrado = df_filmes_unicos.select(
    col("csv.id").alias("id_filme"),
    col("csv.tituloPincipal").alias("titulo_principal"),
    col("tmdb.original_title").alias("titulo_original"),
    col("csv.anolancamento").alias("ano_lancamento"),
    element_at(col("tmdb.origin_country"), 1).alias("id_pais"),
    col("csv.notamedia").alias("nota_media"),
    col("csv.numerovotos").alias("numero_votos"),
    col("tmdb.popularity").alias("popularidade")
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
        col("f.ano_lancamento"),
        col("id_pais"),
        col("f.nota_media"),
        col("f.numero_votos"),
        col("f.popularidade"),
        col("dt.id_tempo")
    )
)

df_filme_diretor = glueContext.create_dynamic_frame.from_catalog(
    database=refined_db,
    table_name="filmediretor"
).toDF()

df_diretores_agg = (
    df_filme_diretor
    .groupBy("id_filme")
    .agg(collect_list("id_diretor").alias("id_diretores"))
)

df_fato_final = (
    df_fato.alias("fato")
    .join(df_diretores_agg.alias("dir"), col("fato.id_filme") == col("dir.id_filme"), "left")
    .select("fato.*", col("dir.id_diretores"))
)

df_fato_final.write.mode("overwrite").format("parquet").save(
    "s3://data-compass-ana/Refined/FatoRepresentacaoFeminina/"
)
