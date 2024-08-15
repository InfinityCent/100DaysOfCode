import datetime as dt
import smtplib
from random import choice

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()

random_quote = choice(quotes)
today = dt.datetime.now().weekday()

if today == 4:
    my_email = "pereeia@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="iaogmdvamqbsddpi")
        connection.sendmail(from_addr=my_email, to_addrs="alexdaiejavad@gmail.com",
                            msg=f"Subject:Inspirational Quote\n\n{random_quote}")

