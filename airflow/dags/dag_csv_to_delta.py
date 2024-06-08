from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'spark',
    'retries': 0,
}

with DAG(
    dag_id="csv_to_delta",
    description='A Spark job to convert CSV files to Delta Lake tables',
    default_args=default_args,
    start_date=datetime.now(),
    catchup=False, 
    schedule_interval=None,
) as dag:

    start = DummyOperator(task_id="start", dag=dag)

    spark_task = SparkSubmitOperator(
        task_id='spark_task',
        application='/opt/airflow/dags/spark_job/csv_to_delta.py',  # Caminho para o arquivo do job Spark
        conn_id='spark_default',  # ID da conexão do Spark definida no Airflow
        # py_files='/path/to/delta/lake/delta-lake-0.7.0-spark2.4-s_2.11.jar',
        py_files='/opt/airflow/jars/delta-core_2.12-2.4.0.jar,/opt/airflow/jars/hadoop-aws-3.3.6.jar',
        conf={
            'spark.executor.cores': '2',
            'spark.cores.max': '4'
        },
        name='csv_to_delta',  # Nome do job Spark
        dag=dag,
    )

    end = DummyOperator(task_id="end", dag=dag)

start >> spark_task >> end