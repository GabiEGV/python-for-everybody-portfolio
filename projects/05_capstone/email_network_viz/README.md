# 🌐 Capstone Project: Email Network Analysis (Sakai Archive)

This project represents the complete **Data Pipeline (ETL)** developed during the Capstone course of the Python for Everybody Specialization. It focuses on using Python and SQL to analyze a large corpus of email data.

## Goal and Methodology

The primary goal is to retrieve, process, and visualize the organization's communication patterns (who emails whom) from a publicly available dataset (the Sakai archive). The entire workflow covers the key areas of a data science pipeline:

1.  **Data Retrieval:** The `gmane.py` script accesses the external API to download and store the raw email data.
2.  **Transformation & Normalization:** The `gmodel.py` script reads the raw data, performs essential cleaning, and normalizes the output into an efficient relational database.
3.  **Analysis & Storage (SQLite):** Normalized data is loaded into the dedicated SQLite database (**index.sqlite**), which is optimized for fast querying. This step demonstrates **SQL** and database normalization.
4.  **Visualization Preparation:** The `gbasic.py` script queries **index.sqlite** to process and output the data in the necessary JavaScript format.
5.  **Network Visualization (D3.js):** The resulting data is used by the `gline.js` or `gbasic.js` file to render an interactive force-directed graph that maps organizational connections and message timelines.

## Technologies and Skills Demonstrated

| Category | Skills & Tools |
| :--- | :--- |
| **Data Flow** | **Complete Data Pipeline (ETL: Extract, Transform, Load)** |
| **Database** | **SQLite3**, **SQL** Queries, **Database Normalization** |
| **Python** | `gmane.py`, `gmodel.py`, `sqlite3`, File I/O |
| **Visualization** | Interactive Web Visualization (**D3.js / JavaScript**) |

## Setup and Execution

To replicate the project, you must run the scripts sequentially to build the final database:

1.  Run the Python spider (`gmane.py`) to download data.
2.  Run the model script (`gmodel.py`) to clean and normalize the data, creating **index.sqlite**.
3.  Run the analysis script (`gbasic.py`) to generate the output files (e.g., `gbasic.js`).
4.  Open the visualization file (`gline.htm` or `gbasic.htm`) in a web browser to view the final network graph.
