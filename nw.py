import requests
from bs4 import BeautifulSoup
import re
import json
url="https://journal.un.org/en/new-york/meeting/officials/97250ac0-e677-4b83-80b5-08da00cb1115/2022-08-01/statements"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

scrap_tag = soup.find("script",src=None)
pattern = "var data = (.*?);\n"
raw_data = re.findall(pattern,scrap_tag.string,re.S )
if raw_data:
    data = json.load(raw_data[0])
    print(data)




