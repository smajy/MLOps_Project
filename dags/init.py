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

dag = DAG('job', default_args=default_args, description='A simple DAG to run a Spark job', schedule=None)

# Define tasks as operators
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Task 1: Extract data"',
    dag=dag,
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=ExtractData,  # Call your Spark job function
    dag=dag,
)

task3 = BashOperator(
    task_id='task3',
    bash_command='echo "Task 3: Data transformation"',
    dag=dag,
)


task4 = PythonOperator(
    task_id='task4',
    python_callable=TransformData,  # Call your Spark job function
    dag=dag,
)

task5 = BashOperator(
    task_id='task5',
    bash_command='echo "Task 4: Load data"',
    dag=dag,
)

task6 = PythonOperator(
    task_id='task4',
    python_callable=LoadData,  # Call your Spark job function
    dag=dag,
)

# Define task dependencies
task1 >> task2 >> task3 >> task4 >> task5 >> task6
