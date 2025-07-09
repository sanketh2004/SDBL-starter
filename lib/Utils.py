from pyspark.sql import SparkSession

def get_spark_session(env):
    builder = SparkSession.builder \
        .appName(f"SBDL_{env}") \
        .config("spark.sql.warehouse.dir", "file:///tmp/spark-warehouse") \
        .config('spark.driver.extraJavaOptions', '-Dlog4j.configuration=file:log4j.properties') \
        .master("local[2]")

    # Only enable Hive if Hive is properly configured
    try:
        spark = builder.enableHiveSupport().getOrCreate()
    except Exception as e:
        print("⚠️ Warning: Hive support failed. Starting SparkSession without it.")
        print("Error details:", str(e))
        spark = builder.getOrCreate()

    return spark


