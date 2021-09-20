import boto3
import pandas as pd

#Criar um cliente Cliente para interagir com AWS S3
s3_cliente = boto3.client('s3')

s3_cliente.download_file("datalake-kelson-igti-edc","data/FLUXO DE CAIIXA NACIONAL 18-08-21.csv","data/Fluxo_Caixa_Nacional.csv")
                       


df = pd.read_csv("data\Fluxo_Caixa_Nacional.csv", sep=";")

#print(df)
s3_cliente.upload_file("data/Fluxo_Caixa_Nacional.csv",
                        "datalake-kelson-igti-edc",
                        "data/arquivo.csv")