'''
Making a function more widely reusable


With the best intentions, one of your team mates chopped up a small Spark transformation pipeline, chinese_provinces.py, into smaller functions that can be used in different locations, chinese_provinces_improved.py. That’s great! Your team mate even wrote a test for one of those new functions. However, the test fails. You could verify this by running pipenv run pytest . when you are in the chinese_demographics folder, if you wanted, but that’s not the point of this exercise. You’ll learn more about pytest in the next lesson anyway.

In this exercise, you need to focus only on the ~/workspace/spark_pipelines/chinese_demographics folder.

Instructions
100XP

- Edit chinese_provinces_improved.py so that the unit test would pass. To do so, read the unit test, which you’ll find in test_improvements.py, in the chinese_demographics folder. There’s a large multi-line comment there that gives a good hint about what you would need to alter.

'''
# You need to change spark_pipelines/chinese_province_improved.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, sum

from .catalog import catalog


def extract_demographics(sparksession, catalog):
    return sparksession.read.parquet(catalog["clean/demographics"])


def store_chinese_demographics(frame, catalog):
    frame.write.parquet(catalog["business/chinese_demographics"])


# Improved aggregation function, grouped by country and province
def aggregate_inhabitants_by_province(frame):
    return (frame
            .groupBy("country", "province")
            .agg(sum(col("inhabitants")).alias("inhabitants"))
            )


def main():
    spark = SparkSession.builder.getOrCreate()
    frame = extract_demographics(spark, catalog)
    chinese_demographics = frame.filter(lower(col("country")) == "china")
    aggregated_demographics = aggregate_inhabitants_by_province(
        chinese_demographics)
    store_chinese_demographics(aggregated_demographics, catalog)


if __name__ == "__main__":
    main()
