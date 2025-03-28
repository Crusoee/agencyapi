
import json
from collections import defaultdict


import requests
from bs4 import BeautifulSoup


# title = "title-12/ECFR-title12.xml"

# data = requests.get("https://www.govinfo.gov/bulkdata/ECFR/" + title)

# soup = BeautifulSoup(data.content, 'xml')

# print(soup.get_text())

data = requests.get(f"https://www.ecfr.gov/api/versioner/v1/full/2023-10-01/title-48.xml")

soup = BeautifulSoup(data.content, 'xml')

print(soup.get_text().count(' '))