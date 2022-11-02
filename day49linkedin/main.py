from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


import time

from dotenv import load_dotenv

import os

load_dotenv()

chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# URL = "https://en.wikipedia.org/wiki/Main_Page"

URL =  "https://www.linkedin.com/jobs/search/?currentJobId=3321807606&f_AL=true&f_E=1&geoId=92000000&keywords=engineer%20intern%202023&location=Worldwide&refresh=true&sortBy=R/"
driver.get(URL)

time.sleep(4)
driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary").click()
driver.find_element(by=By.ID, value="username").send_keys(os.getenv("USER"))
driver.find_element(by=By.ID, value="password").send_keys(os.getenv("PASS"))
driver.find_element(by=By.CLASS_NAME, value="btn__primary--large").click()

listings = driver.find_elements(by=By.CLASS_NAME, value="job-card-container--clickable")

print(listings)

for listing in listings:
    listing.click()
    time.sleep(2)
    driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button").click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Submit application']").click()
        
    except NoSuchElementException:
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()
        driver.find_element(By.XPATH, "//button[@data-control-name='discard_application_confirm_btn']").click()
    
    else:
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()




