# spark_study

위키북스에서 제작한 빅데이터 분석을 위한 스파크2 프로그래밍 정리하였습니다. 

## 정의

```
하둡과 유사한 클러스터 기반의 분산 처리 기능을 제공하는 오픈소스 프레임워크

처리 결과를 항상 파일시스템에 유지하는 하둡과 달리 메모리에 저장하고 관리할 수 있는
기능을 제공함으로써 머신러닝 등 반복적인 데이터를 처리하는 데 뛰어난 성능을 보입니다.
하둡과 하이브를 비롯한 기존의 여러 솔루션과의 연동을 지원하고
마이크로 배치 방식의 실시간 처리 및 머신러닝 라이브러리를 비롯해 빅데이터 처리와
관련된 다양한 라이브러리를 지원합니다.
```

## 설치과정

- ubuntu에 java 설치

```
java -version

sudo apt-get install openjdk-8-jdk 

wget  http://mirror.navercorp.com/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz

tar -xvzf spark-2.4.0-bin-hadoop2.7.tgz

ln -s spark-2.4.0-bin-hadoop2.7.tgz spark

${SPARK_HOME}/bin/spark-shell


spark 환경변수

sudo gedit /etc/profile

export (spark 설치위치)

```

## ERROR

- Constructor org.apache.spark.api.python.PythonAccumulatorV2([class java.lang.String, class java.lang.Integer]) does not exist

- pyspark -- or spark-submit

- ./pyspark --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.0.2(python파일 경로)

- bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.2.0 (python파일 경로)

- bin/spark-submit --jars yourjarfile.jar --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.3 (python파일 경로)

```
'pyspark' is not supported as of Spark 2.0

Spark 2점대 이후로는 spark-submit 사용

```

- [카프카 실행안될때](https://stackoverflow.com/questions/52040384/spark-unable-to-download-kafka-library)
- [pyspark](https://github.com/YBIGTA/EngineeringTeam/wiki/02.-PySpark-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95)