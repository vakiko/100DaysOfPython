import requests
from bs4 import BeautifulSoup
import datetime

#portion of getting date from user input

month = str(input("Please enter the month you would like to search for: "))
date = str(input("Please enter the date you would like to search for: "))
year = str(input("Please enter the year you would like to search for: "))

unformattedDate = year + "-" + month + "-" + date

datetime_object = datetime.datetime.strptime(unformattedDate, "%Y-%m-%d")

URL = "https://www.billboard.com/charts/hot-100/" + datetime_object.strftime("%Y-%m-%d")

request = requests.get(URL)

