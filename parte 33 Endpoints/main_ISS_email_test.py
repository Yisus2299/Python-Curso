import os
import ssl
import smtplib
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = "jmzm08@gmail.com"
MY_PASSWORD = os.getenv("GMAIL_PASSWORD")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465  # SSL

MY_LAT = 51.507351
MY_LONG = -0.127758


def is_iss_overhead() -> bool:
    response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)


def is_night() -> bool:
    params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    sunrise_hour_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now_hour_utc = datetime.utcnow().hour
    return now_hour_utc >= sunset_hour_utc or now_hour_utc <= sunrise_hour_utc


while True:
    try:
        if True:  # <- temporal para enviarlo ya
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context, timeout=20) as connection:
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="kenzu603@gmail.com",
                    msg="Subject:Look up\n\nLook up, the ISS is not right there where you think",
                )
            break  # <- This is for sending it only once and it ends
    except Exception as e:
        print("Error:", e)
        break