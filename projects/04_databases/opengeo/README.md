Markdown
# 📍 Project: Geospatial Data Mapper (API & SQLite)

This project, part of the "Using Databases with Python" course, demonstrates the full pipeline for retrieving, structuring, and visualizing geospatial data using a geocoding API and a SQLite database.

## Goal and Methodology

The primary goal is to use an external API (e.g., OpenStreetMap) to geocode (retrieve latitude and longitude) a list of addresses, store the results in a relational database, and visualize the data on a web map.

The workflow follows a robust data persistence process:

1.  **API Retrieval & Storage (`geoload.py`):** The script reads addresses from a data file (`where.data`), communicates with an external geocoding API, and stores the resulting JSON data (latitude, longitude, formatted address) directly into the SQLite database.
2.  **Database Persistence:** All data is stored in **`opengeo.sqlite`**, demonstrating the use of the `sqlite3` library for structured data persistence and efficient querying.
3.  **Data Extraction & Transformation (`geodump.py`):** The script queries the **`opengeo.sqlite`** database, extracts the stored coordinates, and formats this clean data into a JavaScript file (**`where.js`**).
4.  **Map Visualization:** The web page **`where.html`** loads the JavaScript data to display the geocoded locations as pins on an interactive map.

## Technologies and Skills Demonstrated

| Category | Skills & Tools |
| :--- | :--- |
| **Data Flow** | **API Integration**, **JSON** Parsing, Data Persistence |
| **Database** | **SQLite3**, **SQL** Queries (`INSERT`, `SELECT`), Database Schema Design |
| **Python** | `urllib`, `json`, `sqlite3` |
| **Visualization** | Basic Web Visualization (HTML/JavaScript Mapping) |

## Setup and Execution

To replicate the project, run the scripts sequentially:

1.  Run the **`geoload.py`** script to call the API and populate the **`opengeo.sqlite`** file.
2.  Run the **`geodump.py`** script to generate the **`where.js`** output file.
3.  Open **`where.html`** in a web browser to view the map with all the geocoded locations.
