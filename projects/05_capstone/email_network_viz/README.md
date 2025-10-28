# 🌐 Capstone Project: Email Network Analysis

This project represents the complete data pipeline developed during the Capstone course of the Python for Everybody Specialization. It focuses on using Python and SQL to analyze a large corpus of email data.

## Goal and Methodology

The primary goal is to retrieve, process, and visualize the organization's communication patterns (who emails whom) from a publicly available dataset (the Sakai archive).

The project workflow covers key areas of a data science pipeline:

1.  **Data Retrieval & Cleaning (`gmane.py` / `mbox.py`):** Scripts parse email headers from a large `.mbox` file to extract sender organizations and normalized email addresses.
2.  **Database Storage (SQLite):** Normalized data (emails, senders, and counts) is loaded into a dedicated SQLite database (`org_network.sqlite`) using Python's `sqlite3` library. This step demonstrates **SQL** and efficient data storage.
3.  **Visualization Preparation (`gbasic.py`):** The Python script queries the SQL database to process and output the data in the necessary format for JavaScript visualization.
4.  **Network Visualization (D3.js):** The resulting data is used by the **`gline.js`** or **`gbasic.js`** file to render an interactive force-directed graph (using D3.js) that maps organizational connections and message timelines.

## Technologies and Skills Demonstrated

| Category | Skills & Tools |
| :--- | :--- |
| **Data Flow** | Complete Data Pipeline (ETL: Extract, Transform, Load) |
| **Database** | **SQLite3**, **SQL** Queries (`SELECT`, `INSERT`), Database Schema Design |
| **Python** | `sqlite3`, File I/O, Data Normalization |
| **Visualization** | Interactive Web Visualization (D3.js / JavaScript) |

## Setup and Execution

To replicate the project:
1.  Run the Python script (e.g., **`gbasic.py`**) to process the data and create the necessary `.js` output files.
2.  Open the visualization file (**`gline.htm`** or **`gbasic.htm`**) in a web browser to view the network graph and timeline.
