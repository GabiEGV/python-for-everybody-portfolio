# 🕸️ Project: HTML Comment Scraper (PY4E)

This project demonstrates foundational **web scraping** and **data extraction** skills using pure Python libraries.

## Goal

The script prompts the user for a specific HTML URL, then fetches the page content. It uses the `BeautifulSoup` library to parse the HTML structure, locate all numerical values embedded within `<span>` tags that have the class `comments`, and calculates the total sum of these numbers.

This exercise showcases the ability to handle network requests, parse semi-structured data (HTML), and perform basic data aggregation.

## Technologies Used

* **Python 3**
* **BeautifulSoup4:** For efficient HTML parsing and data location.
* **urllib.request:** For making network requests (fetching the HTML content).
* **ssl:** To handle and ignore SSL certificate errors during the request.
