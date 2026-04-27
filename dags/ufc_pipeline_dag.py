from datetime import datetime
from pathlib import Path
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

PROJECT_DIR = Path(r"C:\Users\harry\UFC Project")
if str(PROJECT_DIR) not in sys.path:
    sys.path.append(str(PROJECT_DIR))

from scripts.ingest import ingest_source_csv
from scripts.transform import transform_raw_to_silver
from scripts.load import load_silver_to_sqlite
from scripts.build_gold import build_gold_layer
from scripts.validate import validate_pipeline_outputs


default_args = {
    "owner": "harry",
    "depends_on_past": False,
}


def run_ingest():
    source_file = PROJECT_DIR / "UFC-Fight-Data-1993-2021-1.csv"
    ingest_source_csv(source_file)


with DAG(
    dag_id="ufc_pipeline_dag",
    default_args=default_args,
    description="UFC Fight Data Pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["ufc", "etl", "sqlite"],
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_raw_data",
        python_callable=run_ingest,
    )

    transform_task = PythonOperator(
        task_id="transform_to_silver",
        python_callable=transform_raw_to_silver,
    )

    load_task = PythonOperator(
        task_id="load_to_sqlite",
        python_callable=load_silver_to_sqlite,
    )

    gold_task = PythonOperator(
        task_id="build_gold_layer",
        python_callable=build_gold_layer,
    )

    validate_task = PythonOperator(
        task_id="validate_outputs",
        python_callable=validate_pipeline_outputs,
    )

    ingest_task >> transform_task >> load_task >> gold_task >> validate_task