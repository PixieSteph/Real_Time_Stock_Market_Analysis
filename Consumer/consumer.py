from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
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
      .option("subscribe", "stock-data")
      .option("startingOffsets", "latest")
      .option('failOnDataLoss', 'false')  
      .load()
      )



parsed_df = df.selectExpr( 'CAST(value AS STRING)')\
              .select(from_json(col("value"), kafka_data_schema).alias("data"))\
              .select("data.*")
              
              

processed_df = parsed_df.select(
    col("date").cast(TimeStampType()).alias("date"),
    col("hifh").alias("high"),
    col("low").alias("low"),  
    col("open").alias("open"),
    col("close").alias("close"),
    col("symbol").alias("symbol")
)              


query = (processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("checkpointLocation", checkpoint_dir) \
    .options(truncate=False) \
    .start()
)


query.awaitTermination()