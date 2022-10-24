from selenium import webdriver

chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://www.amazon.com/Spy-Family-Vol-Tatsuya-Endo/dp/1974717240/ref=sr_1_9?keywords=spy+x+family&qid=1666497734"

driver.get(URL)
price = driver.find_element("id","price")
print("This is the price", price.text)




driver.quit()