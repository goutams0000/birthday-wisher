import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
# print(today)

# HINT 2: Use pandas to read the data.csv
data = pandas.read_csv("birthdays.csv")
# print(data)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as sample_letter:
        letter_template = sample_letter.read()
        letter_template = letter_template.replace("[NAME]", birthday_person["name"])
        # print(letter_template)

MY_EMAIL = ""
MY_PASSWORD = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday\n\n{letter_template}"
                        )



