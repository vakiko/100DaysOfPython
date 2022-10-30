from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# URL = "https://en.wikipedia.org/wiki/Main_Page"

URL =  "https://secure-retreat-92358.herokuapp.com/"
driver.get(URL)
# count = driver.find_element("id","articlecount")
first_name = driver.find_element("name","fName")
first_name.send_keys("Victoria")

first_name = driver.find_element("name","lName")
first_name.send_keys("Chen")

first_name = driver.find_element("name","email")
first_name.send_keys("email@email.com")

submit = driver.find_element(by=By.CLASS_NAME, value="btn")
print("Form submission successful!")

submit.click()

print("Form submission successful!")

driver.quit()

# print("There are", count.text)




# driver.quit()