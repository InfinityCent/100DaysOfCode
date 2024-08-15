import requests
import re
import smtplib
import time
from datetime import datetime

MY_LAT = 43.77123808449964
MY_LNG = -79.41289236378145


def iss_overhead(margin_of_error):
    global MY_LAT, MY_LNG

    # ISS position
    request_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = request_iss.json()
    latlng = (float(iss_data["iss_position"]["latitude"]),
              float(iss_data["iss_position"]["longitude"]))

    if abs(MY_LAT - latlng[0]) <= margin_of_error \
            and abs(MY_LNG - latlng[1]) <= margin_of_error:
        return True
    return False


def is_dark():
    global MY_LAT, MY_LNG

    # Time of sunrise and sunset at location
    parameters = {"lat": MY_LAT,
                  "lng": MY_LNG,
                  "formatted": 0}
    request_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    request_sun.raise_for_status()

    sun_data = request_sun.json()
    sunrise = re.split("T|\+", sun_data["results"]["sunrise"])
    sunset = re.split("T|\+", sun_data["results"]["sunset"])
    sunrise_sunset = (sunrise[1], sunset[1])

    current_hour = datetime.now().hour + 4  # accounting for fact at sunrise/sunset
    # times are in UTC

    if current_hour > int(re.split(":", sunrise_sunset[1])[0]) or current_hour < int(re.split(":", sunrise_sunset[1])[1]):
        return True
    return False


while True:
    time.sleep(60)
    if iss_overhead(5) and is_dark():
        my_email = "pereeia@gmail.com"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="iaogmdvamqbsddpi")
            connection.sendmail(from_addr=my_email, to_addrs="alexdaiejavad@gmail.com",
                                msg=f"Subject:ISS\n\nThe ISS was above you at {datetime.now()}.")

