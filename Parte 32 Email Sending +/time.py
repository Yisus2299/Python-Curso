# enviar frases motivacionales dependiendo del dia (en este caso le quite esa restriccion)

from pathlib import Path
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from datetime import date, datetime
from zoneinfo import ZoneInfo
import random

load_dotenv()

email_sender = "jmzm08@gmail.com"
password = os.getenv("GMAIL_PASSWORD")
email_reciver = "kenzu603@gmail.com"

if not password:
    raise ValueError("GMAIL_PASSWORD missing in .env file")


tz = ZoneInfo("America/Caracas")
now = datetime.now(tz)
weekday = now.weekday()


enviar_solo_miercoles = False
if enviar_solo_miercoles and weekday != 2:
    print("Today is not Wednesday in Caracas. No email is sent.")
    raise SystemExit

quotes_path = Path(__file__).with_name("quotes.txt")
with quotes_path.open(encoding="utf-8") as quote_file:
    all_quotes = [line.strip() for line in quote_file if line.strip()]

if not all_quotes:
    raise ValueError("quotes.txt is empty or only has blank lines.")

quote = random.choice(all_quotes)
print(f'Selected quote: "{quote}"')

subject = "Motivational quote of the day"
body = quote

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())

print("Email sent successfully.")







