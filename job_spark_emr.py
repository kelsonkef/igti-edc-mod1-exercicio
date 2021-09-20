from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, max, min, col, count, lit

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#Ler um arquivo do S3
enem = (

    spark
    .read
    .format("csv")
    .option("delimiter",";")
    .option("header", True)
    .option("inferSchema", True)
    .load("s3://datalake-kelson-igti-edc/raw-data/enem/")
)

#salva o arquivo em parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-kelson-igti-edc/raw-data/staging/enem")

)