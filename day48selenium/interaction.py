from selenium import webdriver

chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)
count = driver.find_element("id","articlecount")

print("There are", count.text)




driver.quit()