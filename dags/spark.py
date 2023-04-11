from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark session
spark = SparkSession.builder.appName("DataControlling").getOrCreate()

def read_csv():
    # Load data from CSV file
    df = spark.read.csv("data.csv", header=True)
    return df
# def 
# Perform data transformations
# df = df.select("name", "age", "gender")  # Select specific columns
# df = df.filter(col("age") >= 18)  # Filter data based on a condition
# df = df.groupBy("gender").agg(avg("age"), count("*"))  # Perform aggregations

# # Save transformed data to a Parquet file
# df.write.parquet("output.parquet", mode="overwrite")
