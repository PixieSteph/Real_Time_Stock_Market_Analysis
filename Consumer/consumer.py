from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType
import os




checkpoint_dir = "/tmp/checkpoint/kafka_to_postgres"
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)
    



kafka_data_schema = StructType([
    StructField("date", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("open", DoubleType(), True),
    StructField("high", DoubleType(), True),
    StructField("low", DoubleType(), True),
    StructField("close", DoubleType(), True)
])


spark = (SparkSession.builder
         .appName("KafkaSparkStreaming") 
         .getOrCreate() 
)   



df = (spark.readStream.format("kafka")
      .option("kafka.bootstrap.servers", "kafka:9092")
      .option("subscribe", "stock_analysis")
      .option("startingOffsets", "latest")
      .option('failOnDataLoss', 'false')  
      .load()
      )



parsed_df = df.selectExpr( 'CAST(value AS STRING)')\
              .select(from_json(col("value"), kafka_data_schema).alias("data"))\
              .select("data.*")
              
              

processed_df = parsed_df.select(
    col("date").cast(TimestampType()).alias("date"),
    col("symbol").alias("symbol"),
    col("open").cast("double").alias("open"),
    col("high").cast("double").alias("high"),
    col("low").cast("double").alias("low"),
    col("close").cast("double").alias("close")
)            


def write_to_postgres(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://postgres:5432/stock_market") \
        .option("dbtable", "stock_prices") \
        .option("user", "admin") \
        .option("password", "admin123") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    print(f"Batch {batch_id} written to PostgreSQL")


query = processed_df.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_postgres) \
    .option("checkpointLocation", checkpoint_dir) \
    .start()

query.awaitTermination()