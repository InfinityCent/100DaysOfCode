import pandas
import smtplib
import datetime as dt
import os
from random import choice


todays_date = (dt.datetime.now().month, dt.datetime.now().day)
birthdays = pandas.read_csv("birthdays.csv")
birthdays['month_day'] = list(zip(birthdays.month, birthdays.day))

for _, row in birthdays.iterrows():
    if todays_date == row["month_day"]:
        template = choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{template}") as letter_template:
            letter = letter_template.readlines()
            letter[0] = letter[0].replace("[NAME]", row["name"])

        my_email = "pereeia@gmail.com"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="iaogmdvamqbsddpi")
            connection.sendmail(from_addr=my_email, to_addrs="alexdaiejavad@gmail.com",
                                msg=f"Subject:Happy Birthday!\n\n{''.join(letter)}")

