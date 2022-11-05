import lxml
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

import time

from dotenv import load_dotenv

import os

load_dotenv()

APT_URL = "https://www.apartments.com/college-station-tx-77840/"

USER_AGENT = "Mozilla/5.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

FORM_URL = "https://forms.gle/1GSQ9UeDvDopBqmF6"
chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"


headers = requests.utils.default_headers()

headers.update({
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent': USER_AGENT
})

response = requests.get(url=APT_URL, headers=headers)

#apartment scraping
apartments_site = response.text

soup = BeautifulSoup(apartments_site, "lxml")
apartment_names = soup.find_all("span", {"class": "js-placardTitle title"})
apartment_placards = soup.find_all("article", {"class": "placard placard-option-diamond has-header js-diamond"})
apartment_prices = soup.find_all("p", {"class": "property-pricing"})
apartment_bedrooms = soup.find_all("p", {"class": "property-beds"})

# i = 0
# for apartment_placard in apartment_placards:
#     print(apartment_placard[i]["data-url"])
#     i += 1


for apartment in apartment_names:
   print(apartment.getText())

#selenium part
driver = webdriver.Chrome(executable_path=chrome_driver_path)

input_boxes = driver.find_elements(By.XPATH, "//input[@type='text']") # size of 4

driver.get(FORM_URL)

for i in range(0, 10):
    form = driver.find_elements(By.XPATH, "//input[@type='text']")
    form[0].send_keys(apartment_names[i].getText())
    form[1].send_keys(apartment_placards[i]["data-streetaddress"])
    #calculate the min price per bedroom
    price = int(apartment_prices[i].getText().replace(',','').split(" - ")[-1])/float(str(apartment_bedrooms[i].getText()).replace('Beds','').replace('Studio','').split("-")[-1])
    form[2].send_keys(price)
    form[3].send_keys(apartment_placards[i]["data-url"])
    button = driver.find_element(By.XPATH, "//div[@role='button']")
    button.click()
    driver.find_element(By.XPATH, "//a[@href]").click()
    time.sleep(2)
    
    

    