import sys
from awsglue.transforms import *
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

movies_csv_path = "s3://data-compass-ana/Raw/Local/CSV/Movies/2025/06/15/movies.csv"

movies_output_path = "s3://data-compass-ana/Trusted/Local/Parquet/Movies/"

movies_df = spark.read.option("header", "true").option("sep", "|").csv(movies_csv_path)

print("CSV lido com sucesso.")
print("Total de linhas lidas:", movies_df.count())
print("Caminho de gravação:", movies_output_path)

movies_df.write.mode("overwrite").parquet(movies_output_path)

job.commit()
