import findspark
from pyspark import SparkContext, SparkConf, storagelevel
from pyspark.streaming.context import StreamingContext

# NOTE pyspark version
# pyspark 3.0 부터는 kafka 없음
# pyspark 2.0대 사용
from pyspark.streaming.kafka import KafkaUtils

findspark.init()
conf = SparkConf()
sc = SparkContext(master="local[*]",appName="KafkaSample",conf=conf)
ssc = StreamingContext(sc,3)

ds1 = KafkaUtils.createStream(ssc,"localhost:2181","testGroup",{"test":3})

ds2 = KafkaUtils.createDirectStream(ssc,["test"],{"metadata.broker.list":"localhost:9092"})

ds1.pprint()
ds2.pprint()

ssc.start()
ssc.awaitTermination()