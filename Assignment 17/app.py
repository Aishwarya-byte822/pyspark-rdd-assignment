from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesDataFrameApp").getOrCreate()


df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("Original Data:")
df.show()
 

sorted_df = df.orderBy(col("sales").desc())
print("Products sorted by sales (desc):")
sorted_df.show()


top3 = sorted_df.limit(3)
print("Top 3 products:")
top3.show()


filtered = df.filter(col("sales") > 80000)

print("Products with sales > 80000:")
filtered.show()


filtered.write.mode("overwrite").csv("output/sales_above_80000", header=True)

spark.stop()