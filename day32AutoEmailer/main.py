#
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "<insert email>@gmail.com"
MY_PASSWORD = "<insert app password>"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#print(birthdays_dict)

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
