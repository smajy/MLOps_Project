from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from spark import read_csv
import os
os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

# Define default_args for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('spark_job', default_args=default_args, description='A simple DAG to run a Spark job', schedule=None)

# Define tasks as operators
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Task 1: Load data from CSV"',
    dag=dag,
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=read_csv,  # Call your Spark job function
    dag=dag,
)

task3 = BashOperator(
    task_id='task3',
    bash_command='echo "Task 3: Data transformation"',
    dag=dag,
)

task4 = BashOperator(
    task_id='task4',
    bash_command='echo "Task 4: Save transformed data"',
    dag=dag,
)

# Define task dependencies
task1 >> task2 >> task3 >> task4

# t1 = BashOperator(
#     task_id='print_date',
#     bash_command='date',
#     dag=dag,
# )
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
# t2 = SparkSubmitOperator(
#     task_id='run_spark_job',
#     application='/path/to/spark/job.jar',
#     name='Spark Job',
#     conn_id='spark_default',
#     conf={'master': 'yarn', 'deploy-mode': 'cluster'},
#     executor_memory='2g',
#     executor_cores=1,
#     num_executors=2,
#     application_args=['input.csv', 'output.parquet'],
#     dag=dag,
# )
# t1 >> t2