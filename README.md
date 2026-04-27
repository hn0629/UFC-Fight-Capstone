# UFC Fight Data Pipeline Project

This repository contains a UFC fight data capstone project built around historical UFC fight records from 1993 to 2021. It combines SQL, MongoDB, Python analysis, Airflow orchestration, database design diagrams, documentation, and presentation materials in one organized repo.

## Overview

The project explores how UFC fighting styles and fight outcomes changed over time. The analysis focuses on submissions, knockout trends, takedowns, finish types by weight class, and fighter-level performance patterns.

## Project Highlights

- Exploratory analysis in a Jupyter notebook.
- MongoDB queries for collections, filtering, joins, and aggregation.
- SQL and schema work for relational modeling.
- Airflow pipeline for ETL-style processing.
- Charts, screenshots, reports, and presentation assets.

## Repository Structure

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
│   ├── case-study-report.md
│   └── milestone-4-5.md
├── images/
│   ├── EER.png
│   ├── UML.jpg
│   ├── chart-top-submissions.png
│   ├── chart-weight-class-finish-type.png
│   ├── mongodb-count-middleweight.png
│   ├── mongodb-distinct-stance.png
│   ├── mongodb-fighter-f-query.png
│   ├── mongodb-lookup-fighter-event.png
│   ├── mongodb-show-dbs.png
│   └── mongodb-usa-events.png
├── output/
├── presentations/
├── queries/
│   ├── mongodb-queries.js
│   └── UFC.sql
├── scripts/
│   ├── build_gold.py
│   ├── ingest.py
│   ├── load.py
│   ├── transform.py
│   ├── utils.py
│   └── validate.py
├── sql/
│   └── create_tables.sql
├── airflow_home/
├── check_tables.py
├── config.py
├── logging_config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Data Sources

The project uses historical UFC fight data originally published on Kaggle and also includes MongoDB, SQL, and schema-based modeling work. The notebook covers fights from 1993 through 2021.

## Main Analysis

The notebook explores:
- yearly fight counts,
- finish types over time,
- fighter submission counts,
- finish type distribution by weight class,
- and supporting visualizations such as the “Most Frequent Finish Type by Weight Class” and “Top 15 Fighters with the Most Submissions” charts.

## MongoDB Work

The MongoDB portion of the project demonstrates:
- listing databases and collections,
- counting documents,
- finding distinct values,
- regex-based filtering,
- and joining collections with `$lookup`.

## SQL and Schema Work

The SQL portion includes a source table definition and database modeling work. The schema diagrams show how the entities connect, including fighter, fighter details, event, UFC fights, winner, referee, title bout, and weight class.

### Analysis screenshots

![MongoDB show dbs](./images/mongodb-show-dbs.png)

![MongoDB count middleweight](./images/mongodb-count-middleweight.png)

![MongoDB distinct stance](./images/mongodb-distinct-stance.png)

![MongoDB fighter F query](./images/mongodb-fighter-f-query.png)

![MongoDB USA events](./images/mongodb-usa-events.png)

![MongoDB lightweight red](./images/mongodb-lightweight-red.png)

![MongoDB lookup fighter event](./images/mongodb-lookup-fighter-event.png)

![Chart weight class finish type](./images/chart-weight-class-finish-type.png)

![Chart top submissions](./images/chart-top-submissions.png)

### Database diagrams

![EER Diagram](./images/EER.png)

![UML Diagram](./images/UML.jpg)

## Airflow Pipeline

The Airflow DAG orchestrates the local ETL flow:
1. ingest raw data,
2. transform it,
3. validate it,
4. build the gold summary,
5. and load or verify the final result.

## Environment Setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Outputs

Pipeline outputs are written to the local project output folder and should be treated as generated artifacts.

## Notes

- Keep `scripts/` for executable pipeline code.
- Keep `queries/` for SQL and MongoDB query files only.
- Keep `docs/`, `images/`, and `presentations/` for project deliverables.
- Ignore local runtime files, cache folders, and virtual environments.
