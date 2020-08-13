# ANCHOR streamingcontext
# 연속된 데이터를 사용하기 위한 모듈
# 얼마만큼의 시간 간격을 두고 배치 처리를 수행할지에 대한 정보

import findspark
from pyspark import SparkContext, SparkConf, StorageLevel
from pyspark.streaming.context import StreamingContext
import queue

findspark.init()
conf = SparkConf()
conf.set("spark.driver.host","127.0.0.1")

sc = SparkContext(master="local",appName="StreamingSample",conf=conf)
ssc = StreamingContext(sc,3)

rdd1 = sc.parallelize(["Spark Streaming Sample ssc"])
rdd2 = sc.parallelize(["Spark Queue Spark API"])

inputQueue = [rdd1,rdd2]
lines = ssc.queueStream(inputQueue, True)
words = lines.flatMap(lambda v : v.split(" "))
words.countByValue().pprint()

ssc.start()
ssc.awaitTermination()

# REVIEW output
# ('Spark',1),('Streaming',1),('Sample',1),('scc',1)
#  ('Spark',2),('Queue',1),('API',1)
# 