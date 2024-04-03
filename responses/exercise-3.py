import pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("local-de-test") \
    .getOrCreate()

table_history_df = spark.read.csv("table-history.csv")
status_changes_df = spark.read.csv("status_changes_dataset.csv")

combined_df = status_changes_df.join(table_history_df,"customer_id")


WindowFunc = Window.partitionBy("customer_id").orderBy("start_date")

combined_df = combined_df.withColumn("next_start_date", lead("start_date").over(windowSpec))
combined_df = combined_df.withColumn("end_reason", lead("status").over(windowSpec))


combined_df = combined_df.withColumn(
    "membership_period_end_reason",
    when(col("status") == "FREEZE", "freeze").when(col("status") == "TERMINATE", "termination")
) # time constraint - add other checks

# use this to format history table
def parse_ledger(ledger_str):
