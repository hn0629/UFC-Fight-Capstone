from datetime import datetime
from pathlib import Path
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

PROJECT_DIR = Path(r"C:\Users\harry\UFC Project")
if str(PROJECT_DIR) not in sys.path:
    sys.path.append(str(PROJECT_DIR))

from scripts.ingest import main as ingest_main
from scripts.transform import main as transform_main
from scripts.build_gold import main as build_gold_main
from scripts.load import main as load_main
from scripts.validate import main as validate_main

default_args = {
    "owner": "harry",
    "depends_on_past": False,
}

with DAG(
    dag_id="ufc_pipeline_dag",
    default_args=default_args,
    description="UFC Fight Data Pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ufc", "etl", "sqlite"],
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_raw_data",
        python_callable=ingest_main,
    )

    transform_task = PythonOperator(
        task_id="transform_to_silver",
        python_callable=transform_main,
    )

    build_gold_task = PythonOperator(
        task_id="build_gold_layer",
        python_callable=build_gold_main,
    )

    load_task = PythonOperator(
        task_id="load_to_sqlite",
        python_callable=load_main,
    )

    validate_task = PythonOperator(
        task_id="validate_outputs",
        python_callable=validate_main,
    )

    ingest_task >> transform_task >> build_gold_task >> load_task >> validate_task