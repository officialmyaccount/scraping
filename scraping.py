import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)

soup = BeautifulSoup(rest.text, "html.parser")

data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

headline_link_list = [data.attrs["href"] for data in data_list]
for headline_link in headline_link_list:
    summary = requests.get(headline_link)
    summary_soup = BeautifulSoup(summary.text, "html.parser")
    summary_soup_a = summary_soup.select("a:contains('続きを読む')")[0]
    
    news_body_link = summary_soup_a.attrs["href"]
    news_body = requests.get(news_body_link)
'''
for data in data_list:
    print(data.span.string)
    print(data.attrs["href"])
'''
