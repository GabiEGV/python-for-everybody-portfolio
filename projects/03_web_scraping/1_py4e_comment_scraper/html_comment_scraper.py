"""
Web Scraper to Sum Comments (Python for Everybody)

This script uses urllib and BeautifulSoup to fetch HTML from a user-provided URL,
extracts all numerical values from <span> tags with the class 'comments',
and calculates the total sum of these numbers.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt user for the URL (e.g., http://py4e-data.dr-chuck.net/comments_2283179.html)
url = input('Enter URL: ') 

# Read the HTML content
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


count = 0
total = 0

# Find all <span> tags with the class "comments"
tags = soup('span', class_="comments")
for tag in tags:
    # Extract the number from the tag's text, convert to integer, and sum
    number = int(tag.text)
    total += number
    count += 1

print("Count:", count)
print("Sum:", total)