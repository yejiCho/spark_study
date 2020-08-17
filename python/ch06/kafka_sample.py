# import findspark
from pyspark import SparkContext, SparkConf, storagelevel
from pyspark.streaming.context import StreamingContext

# NOTE pyspark version
# pyspark 3.0 부터는 kafka 없음
# pyspark 2.0대 사용
# from pyspark.streaming.kafka import KafkaUtils

from pyspark.streaming.kafka import KafkaUtils
import os

# Spark2.3에서는 spark-streaming-kafka-0-8 API가deprecated 되었습니다.
# 하지만 spark-streaming-kafka-0-10 API는 파이썬에서 사용할 수 없습니다.
# 따라서 아래 예제는 spark-streaming-kafka-0-8 API 를 사용하여 작성되었습니다. 
   

## pyspark에서 실행할 경우 sparkContext는 생성하지 않습니다!
## ./pyspark --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.0.2


# findspark.init()
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext(master="local",appName="KafkaSample",conf=conf)
ssc = StreamingContext(sc,3)

# localhost:2181 주키퍼 쿼럼 정보
# testgroup 컨슈머 그룹명
# Map 매개변수 : 수신할 토픽의 이름,수신에 사용할 스레드의 수

# 리시버를 사용하는 방법 (spark-streaming-kafka-0-8 API)
ds1 = KafkaUtils.createStream(ssc,"localhost:2181","testGroup",{"test":3})
# DirectStream을 사용하는 방법 (spark-streaming-kafka-0-8 API)
ds2 = KafkaUtils.createDirectStream(ssc,["test"],{"metadata.broker.list":"localhost:9092"})

ds1.pprint()
ds2.pprint()

ssc.start()
ssc.awaitTermination()