from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello Airflow Docker is working!")

with DAG(
    dag_id="hello_airflow_docker",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["learning"],
) as dag:

    PythonOperator(
        task_id="say_hello",
        python_callable=hello
    )
