import requests
from bs4 import BeautifulSoup
import urllib3

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_site = response.text

soup = BeautifulSoup(empire_site, "html.parser")
#soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))from_encoding="utf-8"


titles = soup.find_all(name="h3", class_="title")

with open("top100movies.txt", "w", encoding="utf-8") as f:
    for title in reversed(titles):
        f.write(title.getText())
        f.write('\n')
