import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: ['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# A partir daqui exatamente igual executamos no EMR
# Ler os dados do enem 2019
enem = (

    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-kelson-igti-edc/raw-data/enem/MICRODADOS_ENEM_2019.csv")
)

# Escrita dos dados no formato parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-kelson-igti-edc/staging/enem-glue/")
)