# UFC Fight Capstone

This capstone project analyzes historical UFC fight data from 1993 to 2021 using database design, SQL, MongoDB, and Python-based exploratory analysis. It combines a Jupyter notebook, a NoSQL milestone, schema diagrams, an SQL source file, and a presentation into one GitHub repository.

## Project overview

The main purpose of this project is to study how UFC fighting styles and fight outcomes evolved over time. The project focuses on trends in submissions, KO/TKO outcomes, takedowns, finish types by weight class, and fighter-level performance insights.

## Dataset source

The dataset used in this project comes from the UFC historical dataset published on Kaggle by Rajeev Wagh and covers fights from 1993 through March 2021.

## Repository contents

- `UFC-Fight-Data-1993-2021-1.ipynb` — main analysis notebook based on UFC fight data.
- `docs/milestone-4-5.md` — cleaned MongoDB milestone queries and explanations.
- `docs/case-study-report.md` — polished case study report.
- `queries/mongodb-queries.js` — runnable MongoDB query examples.
- `schema/EER-Fight.jpg` — EER diagram of the project entities.
- `schema/UML.jpg` — UML-style entity relationship diagram.
- `schema/UFC.sql` — source SQL schema showing the wide-table origin of the dataset.
- `presentations/UFC-FIGHT-ANALYSIS.pdf` — project presentation summarizing goals, schema, tools, queries, and visualizations.

## Database design

The project models the UFC data around four main entities:

- `fighter`
- `fighter_details`
- `event`
- `ufc_fight`

The EER and UML diagrams show the intended relationships between general fighter information, fighter detail records, fight-level results, and event-level records.

The SQL file shows that the original source data was arranged as a single wide table with many columns for red-corner and blue-corner statistics, while the MongoDB work reorganizes the data into smaller logical collections for querying and lookup operations.

## SQL work

The SQL portion of this project was developed and tested in MySQL Workbench to explore relationships between fighters, fight details, and events. MySQL Workbench provides a SQL editor for writing and executing queries, which makes it useful for relational analysis and joins.

Examples shown in the presentation include:
- joining `fighter` with `fighter_details`,
- joining `ufc_fight` with `event`,
- and filtering for fighters in southpaw stance with weight over 200 lbs.

## MongoDB work

The NoSQL portion of the project was completed in MongoDB using aggregation and `$lookup` to compare fighter, fight, and event data across collections. MongoDB’s `$lookup` stage performs a left outer join between collections, which makes it useful for combining related documents in one result.

The NoSQL milestone demonstrates:
- counting documents,
- finding distinct values,
- regex-based filtering,
- conditional filtering,
- and joining collections with `$lookup`.

See `docs/milestone-4-5.md` and `queries/mongodb-queries.js` for the cleaned MongoDB version.

## Python analysis and visualization

The notebook and presentation show a Python-based analysis workflow that explores fight outcomes over time, weight-class-level finish patterns, and fighter-level submission counts.

Examples shown in the project include:
- Most Frequent Finish Type by Weight Class,
- Top 15 Fighters with the Most Submissions,
- yearly fight frequency analysis,
- and finish-type trend analysis across years.

## Project presentation

The presentation file summarizes the project goals, conceptual data model, sample SQL and MongoDB queries, and selected visual outputs. It is included in the repository under `presentations/UFC-FIGHT-ANALYSIS.pdf`.

## Repo structure

```text
UFC-Fight-Capstone/
├── README.md
├── UFC-Fight-Data-1993-2021-1.ipynb
├── docs/
│   ├── milestone-4-5.md
│   ├── case-study-report.md
│   └── powershell-github-steps.md
├── queries/
│   └── mongodb-queries.js
├── schema/
│   ├── EER-Fight.jpg
│   ├── UML.jpg
│   └── UFC.sql
├── presentations/
│   └── UFC-FIGHT-ANALYSIS.pdf
└── images/
    ├── mongodb-show-dbs.png
    ├── mongodb-count-middleweight.png
    ├── mongodb-distinct-stance.png
    ├── mongodb-fighter-f-query.png
    ├── mongodb-usa-events.png
    ├── mongodb-lightweight-red.png
    ├── mongodb-lookup-fighter-event.png
    ├── chart-weight-class-finish-type.png
    └── chart-top-submissions.png
```