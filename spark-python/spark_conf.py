import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("value").setMaster("spark://localhost:7077")
sc = SparkContext.getOrCreate(conf = conf)

# spark master from docker network inspect project_default 172.18.0.5:7077

# df = spark.sql("Select 'spark' as hello")

# df.show()

# import pyspark
# conf = pyspark.SparkConf().setAppName('MyApp').setMaster('spark://172.18.0.4:7077')
# sc = pyspark.SparkContext(conf=conf)