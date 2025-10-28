# 🌐 Capstone Project: Email Network Analysis (Sakai Archive)

This project showcases a comprehensive **Data Pipeline (ETL)** built using Python and SQLite, processing over 1GB of real-world email data from the Sakai developer mailing list.

## Goal and Methodology

The primary goal is to retrieve, clean, and visualize the organizational communication patterns within the email corpus. This demonstrates mastery over network access, SQL normalization, and data analysis.

The entire workflow is split into three distinct, professional stages:

### 1. Data Retrieval and Spidering
* **Script:** `gmane.py` is used to download emails and store the raw data.

### 2. Data Cleaning and Normalization
* **Script:** `gmodel.py` reads the raw data, performs cleaning and normalization, outputting the results into the final analysis database (`index.sqlite`).

### 3. Analysis and Visualization
* **Script:** `gbasic.py` queries the clean database (`index.sqlite`) to prepare data for the interactive force-directed graph.
* **Visualization:** The results feed into D3.js scripts (`gline.js`) to generate network graphs and message timelines.

## Technologies and Skills Demonstrated

| Category | Skills & Tools |
| :--- | :--- |
| **Data Flow** | **Full Data Pipeline (ETL)**, API Consumption, Resumable Spidering |
| **Database** | **SQLite3 / SQL**, **Database Normalization**, Schema Design |
| **Python** | `gmane.py`, `gmodel.py`, `gbasic.py`, `sqlite3` |
| **Visualization** | D3.js / JavaScript |
