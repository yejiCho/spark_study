from pyspark import SparkContext, SparkConf
from pyspark.streaming.context import StreamingContext
import os

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()

conf.set("spark.app.name","StreamingOps")
conf.set("spark.master","local[*]")
conf.set("spark.ui.port","36000")

sc = SparkContext(master ="local[*]",appName="StreamingOps", conf=conf)
ssc = StreamingContext(sc,1)

rdd1 = ssc.sparkContext.parallelize(["a", "b", "c", "c", "c"])
rdd2 = ssc.sparkContext.parallelize(["1,2,3,4,5"])
rdd3 = ssc.sparkContext.parallelize([("k1", "r1"), ("k2", "r2"), ("k3", "r3")])
rdd4 = ssc.sparkContext.parallelize([("k1", "s1"), ("k2", "s2")])
rdd5 = ssc.sparkContext.range(1, 6)

q1 = [rdd1]
q2 = [rdd2]
q3 = [rdd3]
q4 = [rdd4]
q5 = [rdd5]

ds1 = ssc.queueStream(q1, True)
ds2 = ssc.queueStream(q2, True)
ds3 = ssc.queueStream(q3, True)
ds4 = ssc.queueStream(q4, True)
ds5 = ssc.queueStream(q5, True)

# ANCHOR transform(func)
'''
NOTE transform(func)

RDD연산에서 자주 사용되는 연산들을 Dstream API에 포함시킨 것

Dstream이 제공하던 메소드 뿐만아니라 subtract()같이 RDD클래스 타입에서만
제공되던 메소드도 사용가능
1 2 3 4 5 
1 2 
'''
# other = ssc.sparkContext.range(1,3)
# ds5.transform(lambda v: v.subtract(other)).pprint()

# ANCHOR updateStateByKey()

checkpointDir = './checkpoints/streamingops/python'
# ssc = StreamingContext(sc,3)

t1 = ssc.sparkContext.parallelize(["a","b","c"])
t2 = ssc.sparkContext.parallelize(["b","c"])
t3 = ssc.sparkContext.parallelize(["a","a","a"])

q6 = [t1,t2,t3]
ds6 = ssc.queueStream(q6,True)

ssc.checkpoint(checkpointDir)

def updateFunc(newValues,currentValue):
    if currentValue is None:
        currentValue = 0
    return sum(newValues, currentValue)

# ds6.map(lambda c: (c,1)).updateStateByKey(updateFunc).pprint()

# ANCHOR 4.3윈도우 연산

sc = ssc.sparkContext
input = [sc.parallelize([i]) for i in range(1,100)]
ds7 = ssc.queueStream(input)

# ANCHOR 4.4 window(windowLength,slideInterval)
'''
NOTE
slideInterval 지정한 시간마다 windowLength에 지정한 크기만큼의
발생된 데이터를 포함한 Dstream생성
'''
# ds7.window(3,2).pprint()

# ANCHOR 4.5 countByWindow(windowLength,sideInterval)
'''
NOTE
윈도우에 포함된 요소의 개수를 포함한 DStream생성
'''
# ds7.countByWindow(3,2).pprint()

# ANCHOR 4.6 reduceByWindow(func,windowLength,slideInterval)
'''
윈도우에 포함된 요소에 func함수를 적용한 결과로 구성된 Dstream생성
'''
def invFnc(v1,v2):
    return v1 - v2

def reduceFnc(v1,v2):
    return v1 + v2

ds7.reduceByWindow(reduceFunc=reduceFnc, invReduceFunc=invFnc, windowDuration=3, slideDuration=2).pprint()
# ds7.map(lambda v: ("sum", v)).reduceByKeyAndWindow(reduceFnc, invFnc, 3, 2).pprint()

# ANCHOR countByValueAndWindow(windowLength,slideInterval,[numTasks])
# ds7.countByValueAndWindow(3,2).pprint()

ssc.start()
ssc.awaitTermination()