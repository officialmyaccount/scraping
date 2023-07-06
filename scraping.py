import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

soup = BeautifulSoup(rest.text, "html.parser")

data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for data in data_list:
    print(data.span.string)
    print(data.attrs["href"])
