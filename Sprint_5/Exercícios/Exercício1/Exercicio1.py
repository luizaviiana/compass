from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower, trim, regexp_replace

spark = SparkSession.builder.appName("ContagemPalavras").getOrCreate()

df = spark.read.text("./work/README.md")

df_limpo = df.withColumn(
    "linha_limpa",
    regexp_replace(col("value"), r"[^a-zA-ZÀ-ÿ\s-–—]", " ")  
)


df_limpo = df_limpo.withColumn(
    "linha_limpa",
    regexp_replace(col("linha_limpa"), r"[-–—]", " ")
)

palavras = (
    df_limpo
    .select(explode(split(col("linha_limpa"), r"\s+")).alias("palavra")) 
    .select(lower(trim(col("palavra"))).alias("palavra"))                
    .filter(col("palavra") != "")                                         
)

contagem_palavras = palavras.groupBy("palavra").count().orderBy(col("count").desc())

contagem_palavras.show(truncate=False)
