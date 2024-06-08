FROM apache/airflow:2.9.1-python3.11

USER root
RUN apt-get update
RUN apt install -y default-jdk
RUN apt-get autoremove -yqq --purge
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   
USER airflow

COPY ./requirement.txt .
RUN pip install -r requirement.txt

RUN mkdir /opt/airflow/jars

# RUN curl -O https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar \
#     && curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar
    # && mv delta-core_2.12-2.4.0.jar /opt/airflow/jars \
    # && mv hadoop-aws-3.3.6.jar /opt/airflow/jars 

# wget https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
# wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar