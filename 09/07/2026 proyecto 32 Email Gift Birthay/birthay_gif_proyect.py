import csv
import os
import ssl
import smtplib
from pathlib import Path
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "cumples.csv"
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)


def get_env_value(name: str) -> str:
    """Read environment variables and clean common formatting errors."""
    value = os.getenv(name) or os.getenv(f"{name} ") or ""
    # remove spaces, quotes and invisible common characters
    cleaned = value.strip().strip('"').strip("'")
    cleaned = cleaned.replace("\u200b", "").replace("\ufeff", "").replace("\u00a0", "")
    return cleaned

EMAIL_SENDER = get_env_value("EMAIL_SENDER")
PASSWORD = get_env_value("GMAIL_PASSWORD").replace(" ", "")
TZ = get_env_value("TZ") or "America/Santiago"

if not EMAIL_SENDER or not PASSWORD:
    raise ValueError("EMAIL_SENDER or GMAIL_PASSWORD missing in .env file")

print(f"Using .env file: {ENV_FILE}")
print(f"CSV_FILE resolved to: {CSV_FILE}")
print(f"EMAIL_SENDER: {EMAIL_SENDER}")
print(f"GMAIL_PASSWORD length: {len(PASSWORD)}")

try:
    today = datetime.now(ZoneInfo(TZ))
except Exception as e:
    raise ValueError(f"Invalid timezone in TZ: {TZ}") from e

month_today, day_today = today.month, today.day


def email_valid(email: str) -> bool:
    """Validate email"""
    return "@" in email and "." in email.split("@")[-1]


birthdays_today = []

try:
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_columns = {"nombre", "email", "mes", "dia"}
        if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
            raise ValueError("The CSV must have columns: name,email,month,day")

        for row in reader:
            try:
                nombre = row["nombre"].strip()
                email = row["email"].strip()
                mes = int(row["mes"])
                dia = int(row["dia"])
            except (KeyError, ValueError, AttributeError):
                print("Malformed row, it is skipped.")
                continue

            if not nombre:
                print("Empty name, the row is skipped.")
                continue

            if not email_valid(email):
                print(f"Invalid email ({email}), the row is skipped.")
                continue

            if not (1 <= mes <= 12) or not (1 <= dia <= 31):
                print(f"Invalid date ({mes}/{dia}) for {nombre}, the row is skipped.")
                continue

            if mes == month_today and dia == day_today:
                birthdays_today.append((nombre, email))

except FileNotFoundError:
    raise FileNotFoundError(f"File not found {CSV_FILE}")

if not birthdays_today:
    print("Today there are no birthdays.")
    raise SystemExit

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, PASSWORD)

        for nombre, email in birthdays_today:
            msg = EmailMessage()
            msg["From"] = EMAIL_SENDER
            msg["To"] = email
            msg["Subject"] = f"For {nombre} on their unique and special day 🎉🌙💛🌻🌸"
            msg.set_content(
                f"Hello {nombre},\n\n"
                f"Happy birthday, {nombre}! 🎉🎂\n\n"
                f"Have a wonderful day and that all your wishes come true.\n\n"
                f"With love, Jesus\n"
            )

            smtp.send_message(msg)
            print(f"Sent to {nombre} <{email}>")

except smtplib.SMTPAuthenticationError:
    raise ValueError(
        "SMTP authentication error. Check EMAIL_SENDER and GMAIL_PASSWORD (application password)."
    )
except smtplib.SMTPException as e:
    raise RuntimeError(f"Error sending emails: {e}") from e