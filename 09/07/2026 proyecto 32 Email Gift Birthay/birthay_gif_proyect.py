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
    """Lee variables de entorno y limpia errores comunes de formato."""
    value = os.getenv(name) or os.getenv(f"{name} ") or ""
    # Quita espacios, comillas y caracteres invisibles comunes
    cleaned = value.strip().strip('"').strip("'")
    cleaned = cleaned.replace("\u200b", "").replace("\ufeff", "").replace("\u00a0", "")
    return cleaned

EMAIL_SENDER = get_env_value("EMAIL_SENDER")
PASSWORD = get_env_value("GMAIL_PASSWORD").replace(" ", "")
TZ = get_env_value("TZ") or "America/Santiago"

if not EMAIL_SENDER or not PASSWORD:
    raise ValueError("Faltan EMAIL_SENDER o GMAIL_PASSWORD en el archivo .env")

print(f"Usando .env en: {ENV_FILE}")
print(f"CSV_FILE resuelto a: {CSV_FILE}")
print(f"EMAIL_SENDER: {EMAIL_SENDER}")
print(f"GMAIL_PASSWORD length: {len(PASSWORD)}")

try:
    hoy = datetime.now(ZoneInfo(TZ))
except Exception as e:
    raise ValueError(f"Zona horaria inválida en TZ: {TZ}") from e

mes_hoy, dia_hoy = hoy.month, hoy.day


def email_valido(email: str) -> bool:
    """Validación simple de email."""
    return "@" in email and "." in email.split("@")[-1]


cumples_hoy = []

try:
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        columnas_requeridas = {"nombre", "email", "mes", "dia"}
        if not reader.fieldnames or not columnas_requeridas.issubset(set(reader.fieldnames)):
            raise ValueError("El CSV debe tener columnas: nombre,email,mes,dia")

        for row in reader:
            try:
                nombre = row["nombre"].strip()
                email = row["email"].strip()
                mes = int(row["mes"])
                dia = int(row["dia"])
            except (KeyError, ValueError, AttributeError):
                print("Fila malformada, se omite.")
                continue

            if not nombre:
                print("Nombre vacío, se omite fila.")
                continue

            if not email_valido(email):
                print(f"Email inválido ({email}), se omite fila.")
                continue

            if not (1 <= mes <= 12) or not (1 <= dia <= 31):
                print(f"Fecha inválida ({mes}/{dia}) para {nombre}, se omite fila.")
                continue

            if mes == mes_hoy and dia == dia_hoy:
                cumples_hoy.append((nombre, email))

except FileNotFoundError:
    raise FileNotFoundError(f"No se encontró el archivo {CSV_FILE}")

if not cumples_hoy:
    print("Hoy no hay cumpleaños.")
    raise SystemExit

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, PASSWORD)

        for nombre, email in cumples_hoy:
            msg = EmailMessage()
            msg["From"] = EMAIL_SENDER
            msg["To"] = email
            msg["Subject"] = f"Para {nombre} en su dia unico y especial 🎉🌙💛🌻🌸"
            msg.set_content(
                f"Hola {nombre},\n\n"
                f"Happy birthday, {nombre}! 🎉🎂\n\n"
                f"Que tengas un día maravilloso y que todos tus deseos se cumplan.\n\n"
                f"Con cariño, Jesus\n"
            )

            smtp.send_message(msg)
            print(f"Enviado a {nombre} <{email}>")

except smtplib.SMTPAuthenticationError:
    raise ValueError(
        "Error de autenticación SMTP. Revisa EMAIL_SENDER y GMAIL_PASSWORD (App Password)."
    )
except smtplib.SMTPException as e:
    raise RuntimeError(f"Error al enviar correos: {e}") from e