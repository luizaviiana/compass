from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand, floor, when, col, expr

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("../Exercício1/nomes_aleatorios.txt")
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes = df_nomes.withColumn("rand_num", floor(rand(seed=42) * 3))
df_nomes = df_nomes.withColumn("Escolaridade",
    when(col("rand_num") == 0, "Fundamental")
    .when(col("rand_num") == 1, "Médio")
    .otherwise("Superior")
).drop("rand_num")

paises = [
    "Brasil", "Argentina", "Uruguai", "Paraguai", "Chile",
    "Bolívia", "Peru", "Equador", "Colômbia", "Venezuela",
    "Guiana", "Suriname", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn("rand_pais", floor(rand(seed=123) * len(paises)))

case_expr = "CASE "
for i, pais in enumerate(paises):
    case_expr += f"WHEN rand_pais = {i} THEN '{pais}' "
case_expr += "END"

df_nomes = df_nomes.withColumn("Pais", expr(case_expr)).drop("rand_pais")

df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand(seed=456) * 66) + 1945)

df_nomes.createOrReplaceTempView("pessoas")

df_select = spark.sql("""
    SELECT Nomes, AnoNascimento
    FROM pessoas
    WHERE AnoNascimento >= 2001
""")

df_nomes.createOrReplaceTempView("pessoas")

millennials_sql = spark.sql("""
    SELECT COUNT(*) as qtd_millennials
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

df_nomes.createOrReplaceTempView("pessoas")

query_geracoes = """
SELECT
    Pais,
    CASE
        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
        WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        ELSE 'Outros'
    END AS Geracao,
    COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
"""

df_geracoes_por_pais = spark.sql(query_geracoes)

df_geracoes_por_pais.show(truncate=False)
