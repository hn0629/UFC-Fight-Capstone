\# UFC Fight Capstone Case Study



\*\*Course:\*\* IE 6700 Data Management for Analytics  

\*\*Group No.:\*\* 12  

\*\*Student Name:\*\* Hoang Nguyen



\## Project Overview



This project analyzes historical UFC fight data from 1993 to 2021 to better understand how fighting styles and fight outcomes have changed over time. The analysis focuses on submissions, knockouts, takedowns, fight finish types by weight class, and fighter-level performance patterns.



The goal is to identify trends that show how the sport has evolved and how performance metrics can support training and strategy.



\## Dataset Source



The dataset used in this project comes from Kaggle and contains historical UFC fight data from 1993 until March 2021.



\## Research Questions



The main research questions for this project are:



\- How has the proportion of submissions changed over time?

\- How many fights occurred each year?

\- Which fighters recorded the most submissions?

\- How do fight finish types vary by weight class?

\- How have takedown-related statistics changed over time?



\## Database Design



The original source data was structured as a wide table with many columns for red-corner and blue-corner statistics. For the database project, the data was organized into smaller logical entities to make querying and analysis easier.



The main entities used in the design are:



\- `fighter`

\- `fighter\_details`

\- `event`

\- `ufc\_fight`



The EER and UML diagrams show how these entities are related through shared identifiers such as `Fighter\_ID` and `Event\_ID`.



\## SQL Work



The SQL portion of the project was developed and tested in MySQL Workbench. I used SQL joins and filters to explore relationships between fighters, fight details, and events.



Example SQL tasks included:



\- joining `fighter` with `fighter\_details`,

\- joining `ufc\_fight` with `event`,

\- and filtering for fighters in southpaw stance with weight over 200 lbs.



\## MongoDB Work



The NoSQL portion of the project was completed in MongoDB using aggregation and `$lookup` to compare fighter, fight, and event data across collections.



Example MongoDB tasks included:



\- counting fighters in the Middleweight class,

\- finding distinct stance values,

\- filtering fighters whose names begin with a specific letter,

\- limiting query output,

\- and joining collections using `$lookup`.



\## Python Analysis



The notebook includes Python-based analysis for exploring the UFC dataset. The analysis looks at:



\- yearly fight counts,

\- finish type trends over time,

\- fighter submission counts,

\- and finish type distribution by weight class.



The presentation includes visualizations such as:



\- Most Frequent Finish Type by Weight Class,

\- Top 15 Fighters with the Most Submissions.



\## Tools Used



\- MySQL Workbench for SQL queries.

\- MongoDB for NoSQL queries.

\- Python in Jupyter Notebook for data cleaning, analysis, and visualization.

\- EER and UML diagrams for database design.



\## Conclusion



This project combines SQL, MongoDB, and Python to analyze UFC fight data from multiple perspectives. The results show how the sport has evolved over time and how different database tools can be used to study the same dataset in different ways.



The project also demonstrates the difference between relational querying in MySQL Workbench and document-based querying in MongoDB. Both approaches were useful for understanding fighter performance, fight outcomes, and trends across years.

