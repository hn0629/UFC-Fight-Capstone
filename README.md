# UFC Fight Data Pipeline Project

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-D14836?logo=apache-airflow&logoColor=white)](https://airflow.apache.org/) [![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/) [![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)

End-to-end UFC data engineering capstone using Python, Apache Airflow, SQL, MongoDB, and data visualization to transform raw fight records into validated analytical outputs.

## Overview

This project ingests historical UFC fight data, cleans and transforms it, builds a gold summary layer, loads the curated data into SQLite, and validates the final outputs. It also includes exploratory analysis, MongoDB queries, and relational schema design for a complete portfolio-ready data project.

## Project Demo

A few visuals from the project are shown below to highlight the data model, database design, MongoDB querying, and analysis output.

| Visual | Preview |
|---|---|
| Schema Diagram | ![Schema Diagram](images/UML.jpg) |
| Entity Relationship Diagram | ![Entity Relationship Diagram](images/EER.png) |
| MongoDB Query Example | ![MongoDB Query Example](images/mongodb-lookup-fighter-event.png) |
| Analysis Chart | ![Analysis Chart](images/chart-top-submissions.png) |

## Highlights

- Airflow ETL pipeline for local orchestration.
- Raw, silver, and gold data layers.
- SQLite load and validation checks.
- MongoDB examples for filtering, aggregation, and lookup.
- SQL schema design and database modeling.
- Notebook-based analysis and visualizations.

## Airflow Pipeline

This project uses an Airflow DAG to orchestrate the local ETL workflow. The DAG ingests raw UFC data, transforms it, builds a gold summary layer, loads the curated data into SQLite, and validates the final results.

The DAG code lives in `dags/ufc_pipeline_dag.py`.

### How to Run

Activate your virtual environment and test the DAG locally:

```bash
source .venv/bin/activate
airflow dags test ufc_pipeline_dag 2026-04-27
```

### What It Produces

When the pipeline runs locally, it creates generated CSV files in `output/`. The folder is kept in the repo with a `.gitkeep` file, while the generated files can remain untracked.

## Getting Started

```bash
git clone <your-repo-url>
cd UFC-Fight-Data-Pipeline-Project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
airflow dags test ufc_pipeline_dag 2026-04-27
```

## Output Files

The pipeline can create these files in `output/` when it runs locally:

- `output/raw_fights.csv`
- `output/transformed_fights.csv`
- `output/gold_fighter_summary.csv`
- `output/validated_fights.csv`

The validation file contains 3 rows with the expected columns: `fight_id`, `fighter`, `opponent`, `result`, and `is_win`.

## Analysis and Modeling

The project includes:

- UFC fight trend analysis in a Jupyter notebook.
- MongoDB collection exploration, filtering, regex queries, and `$lookup` joins.
- SQL table design and relational schema work.
- Diagrams and screenshots supporting the data model and analysis.

## Repository Layout

```text
UFC Fight Data Pipeline Project/
├── dags/
│   └── ufc_pipeline_dag.py
├── data/
│   ├── ufc.db
│   ├── raw/
│   ├── silver/
│   └── gold/
├── docs/
├── images/
├── output/
├── presentations/
├── queries/
├── scripts/
├── sql/
├── check_tables.py
├── config.py
├── logging_config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Notes

- `scripts/` contains the executable pipeline code.
- `queries/` contains SQL and MongoDB query files.
- `docs/`, `images/`, and `presentations/` contain project deliverables.
- Generated files in `output/` are created by the pipeline and should be treated as artifacts.