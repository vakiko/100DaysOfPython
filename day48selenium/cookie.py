from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)


cookie = driver.find_element(by=By.ID, value="cookie")

hasCursor = False
hasGrandma = False
hasFactory = False
hasMine = False
hasShipment = False
hasLab = False
hasPortal = False

while(True):
    price = int((driver.find_element(by=By.ID, value="money")).text)
    cookie.click()
    if not hasCursor and price == 15:
        driver.find_element(by=By.ID, value="buyCursor").click()
        hasCursor = True
    elif not hasGrandma and price == 100:
        driver.find_element(by=By.ID, value="buyGrandma").click()
        hasGrandma = True
    elif not hasFactory and price == 500: 
        driver.find_element(by=By.ID, value="buyFactory").click()
        hasCursor = True
    elif not hasMine and price == 2000:
        driver.find_element(by=By.ID, value="buyMine").click()
        hasGrandma = True
    elif not hasShipment and price == 7000: 
        driver.find_element(by=By.ID, value="buyShipment").click()
        hasGrandma = True
    elif not hasLab and price == 50000: 
        driver.find_element(by=By.ID, value="buyAlchemy lab").click()
        hasCursor = True
    elif not hasPortal and price == 1000000:
        driver.find_element(by=By.ID, value="buyPortal").click()
        hasGrandma = True
    elif price >= 123456789: 
        driver.find_element(by=By.ID, value="buyTime machine").click()
    


