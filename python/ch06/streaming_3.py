from pyspark import SparkConf, SparkContext
from pyspark.streaming.context import StreamingContext
import os

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext(master="local[*]",appName="Streaming",conf=conf)
ssc = StreamingContext(sc,1)

rdd1 = ssc.sparkContext.parallelize(["a", "b", "c", "c", "c"])
rdd2 = ssc.sparkContext.parallelize(["1,2,3,4,5"])

q1 = [rdd1]
q2 = [rdd2]

ds1 = ssc.queueStream(q1, True)
ds2 = ssc.queueStream(q2, True)

# ANCHOR 3.1 print()
# ds1.pprint()

# ANCHOR 3.2 map(func)
'''
NOTE Dstream map()연산
Dstream에 포함된 RDD에 map()연산을 적용한 것과 같음
'''
# ds1.map(lambda v: (v,1)).pprint()

# ANCHOR 3.3 flatmap(func)
'''
NOTE flatmap()
입력과 출력이 1:1로 매핑되는 map() 연산과는 달리
하나의 입력이 0~N개의 출력으로 변환
'''
# ds2.flatMap(lambda v:v.split(",")).pprint()

# ANCHOR 3.4 count(),countByValue()
'''
NOTE count()
Dstream에 포함된 요소의 개수
Dstream에 포함된 요소(요소, 해당요소의 개수)
'''
# ds1.count().pprint()
# ds1.countByValue().pprint()

# ANCHOR 3.5 reduce(func),reduceByKey(func)
'''
NOTE reduce()
RDD값들을 집계해서 최종적으로 하나의 값으로 변환
reduceByKey()
RDD의 값들이 튜플 타입일 경우
연산을 사용해 각 키별로 집계
'''
# ds1.reduce(lambda v1,v2: v1 + ',' + v2).pprint()
# ds1.map(lambda v:(v,1)).reduceByKey(lambda v1,v2:v1+v2).pprint()

# ANCHOR 3.6 filter(func)
# ds1.filter(lambda v: v != "c").pprint()

# ANCHOR 3.7 union()
# ds1.union(ds2).pprint()

# ANCHOR 3.8 join()
# ds1.union(ds2).pprint()

ssc.start()
ssc.awaitTermination()
