# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "dbc9ce2b-8fbb-4fc7-8867-d9e92c8aa79e",
# META       "default_lakehouse_name": "lh_test",
# META       "default_lakehouse_workspace_id": "d326e254-873b-47bd-b46a-10fb99dc8c9d",
# META       "known_lakehouses": [
# META         {
# META           "id": "dbc9ce2b-8fbb-4fc7-8867-d9e92c8aa79e"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# Este Notebook es de Desarrollo

# CELL ********************

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
from datetime import date

# Spark session (en Fabric ya viene inicializada como "spark")
spark = SparkSession.builder.getOrCreate()

# Definir el esquema
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("nombre", StringType(), True),
    StructField("categoria", StringType(), True),
    StructField("valor", DoubleType(), True),
    StructField("fecha", DateType(), True)
])

# Datos dummy
data = [
    (1, "Producto A", "Categoria 1", 100.50, date(2024, 1, 15)),
    (2, "Producto B", "Categoria 2", 250.75, date(2024, 2, 10)),
    (3, "Producto C", "Categoria 1", 75.20,  date(2024, 3, 5)),
    (4, "Producto D", "Categoria 3", 320.00, date(2024, 4, 20)),
    (5, "Producto E", "Categoria 2", 150.30, date(2024, 5, 12)),
]

# Crear DataFrame
df = spark.createDataFrame(data, schema)

df.write.format("delta").mode("overwrite").saveAsTable("tabla_dummy")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
