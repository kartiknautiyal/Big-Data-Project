import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("value").setMaster("local")
sc = SparkContext.getOrCreate(conf = conf)



# df = spark.sql("Select 'spark' as hello")

# df.show()

# import pyspark
# conf = pyspark.SparkConf().setAppName('MyApp').setMaster('spark://172.18.0.4:7077')
# sc = pyspark.SparkContext(conf=conf)