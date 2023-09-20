# Primeros pasos (SDK for Python (Boto3)) : https://docs.aws.amazon.com/es_es/personalize/latest/dg/getting-started-python.html
# Conceder a Amazon Personalize el acceso a su bucket de Amazon S3.
# Amazon Personalize:  Es un servicio de ML q ayuda a los desarrolladores a crear e implementar rápidamente un motor de recomendaciones 

# Requisitos previos de introducción: debes crear un cuenta de AWS y IAM (Identity and Access Management)
# AWS : cuenta de Amazon.
# IAM : politicas de permisos, desde AWS Management Console (https://console.aws.amazon.com/iam/), 
#       luego (https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies), opcion "crear politicas"

# Doc de Perzonalize:
# https://docs.aws.amazon.com/es_es/personalize/latest/dg/getting-started-python.html#:~:text=Complete%20el-,Requisitos%20previos%20de%20introducci%C3%B3n,-para%20configurar%20los
# En los siguientes pasos, verifica tu entorno y crea el SDK para clientes de Python (Boto3) para Amazon Personalize. 

# Summary:
# Después de completar los requisitos previos, ejecute el siguiente ejemplo de Python para confirmar que su entorno está configurado correctamente. Este código también crea los clientes boto3 de Amazon Personalize que utilizas en este tutorial. Si su entorno está configurado correctamente, se muestra una lista de las recetas disponibles y puede ejecutar los demás ejemplos de este tutorial.
import boto3
import sys
print(f"Ver Python = {sys.version}")                    # 3.7.13 (default, Mar 28 2022, 08:03:21) [MSC v.1916 64 bit (AMD64)]

personalizeRt = boto3.client('personalize-runtime')         
personalize = boto3.client('personalize')               # Could not connect to the endpoint URL: "https://personalize.us-west-1.amazonaws.com/"

response = personalize.list_recipes()                   # Could not connect to the endpoint URL: "https://personalize.us-west-1.amazonaws.com/"

for recipe in response['recipes']:
    print (recipe)