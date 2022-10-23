import lxml
from bs4 import BeautifulSoup
import requests
import time
import smtplib
import os

URL = "https://www.amazon.com/Spy-Family-Vol-Tatsuya-Endo/dp/1974717240/ref=sr_1_9?keywords=spy+x+family&qid=1666497734"
USER_AGENT = "Mozilla/5.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

headers = requests.utils.default_headers()

headers.update({
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent': USER_AGENT
})

response = requests.get(url=URL, headers=headers)

amazon_site = response.text

soup = BeautifulSoup(amazon_site, "lxml")

price = soup.find(id="price")
name = soup.find(id="productTitle")

oldPrice = float(price.getText().strip('$'))

while(True):
    time.sleep(2)
    price = soup.find(id="price")
    oldPrice = 20
    if float(price.getText().strip('$')) < oldPrice:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            contents = "The item" + str(name.getText()) + "has dropped in price from " + str(oldPrice) + " to " + str(price.getText().strip('$')) + ". \n Buy this item at " + URL
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon Price Drop!\n\n{contents}"
            )
    


