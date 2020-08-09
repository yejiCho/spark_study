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