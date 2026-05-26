import os
import locale
from datetime import datetime, date

import requests
from babel.dates import format_datetime
from twilio.rest import Client

# =========================
# CONFIG
# =========================
CITY_QUERY = "San Juan de los Morros, Guarico, VE"

# Plan B: resumen de hoy (varios horarios en un solo WhatsApp)
MODE = "B"

# Twilio WhatsApp
SMS_FROM = "+12183187447"  # tu número de Twilio / sandbox
SMS_TO = "+584122446504"

# Credenciales (PowerShell, ejemplo):
#   $env:OPENWEATHER_API_KEY = "tu_key"
#   $env:TWILIO_ACCOUNT_SID = "AC..."
#   $env:TWILIO_AUTH_TOKEN = "..."
# IMPORTANTE: no hardcodear secretos en el repo.
# Define estas variables de entorno antes de ejecutar el script, por ejemplo:
#   $env:OPENWEATHER_API_KEY = "tu_key"
#   $env:TWILIO_ACCOUNT_SID = "AC..."
#   $env:TWILIO_AUTH_TOKEN = "..."
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", "").strip()
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "").strip()
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "").strip()

# Si prefieres solo variables de entorno, deja los defaults arriba vacíos y define:
# OPENWEATHER_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
if not OPENWEATHER_API_KEY:
    raise ValueError("Falta OPENWEATHER_API_KEY (variable de entorno o edita el script).")
if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
    raise ValueError("Faltan TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN.")
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except locale.Error:
    for loc in ("Spanish_Spain.1252", "es_ES", "es_CL", "Spanish_Chile.1252"):
        try:
            locale.setlocale(locale.LC_TIME, loc)
            break
        except locale.Error:
            pass
def parse_dt(txt: str) -> datetime:
    return datetime.strptime(txt, "%Y-%m-%d %H:%M:%S")
def format_when(dt: datetime) -> str:
    when = format_datetime(dt, "EEEE dd/MM/yyyy hh:mm a", locale="es").lower()
    return (
        when.replace("a. m.", "am")
            .replace("p. m.", "pm")
            .replace("\u202f", " ")
            .replace("\u00a0", " ")
    )
def build_4_lines(hour_data: dict) -> str:
    w = hour_data["weather"][0]
    dt = parse_dt(hour_data["dt_txt"])
    when = format_when(dt)
    desc = w["description"]
    temp = hour_data["main"]["temp"]
    humidity = hour_data["main"]["humidity"]
    return (
        f"{when}\n"
        f"{desc}\n"
        f"Temperatura: {temp}°C\n"
        f"Humedad: {humidity}%"
    )
# =========================
# OPENWEATHER API
# =========================
geo = requests.get(
    "https://api.openweathermap.org/geo/1.0/direct",
    params={"q": CITY_QUERY, "limit": 1, "appid": OPENWEATHER_API_KEY},
)
geo.raise_for_status()
places = geo.json()
if not places:
    raise ValueError("No se encontró la ubicación. Revisa CITY_QUERY.")
lat = places[0]["lat"]
lon = places[0]["lon"]
forecast = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params={
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "es",
    },
)
forecast.raise_for_status()
data = forecast.json()
items = data["list"]
# =========================
# PLAN B: resumen de hoy (un solo texto)
# =========================
today = date.today()
today_items = [it for it in items if parse_dt(it["dt_txt"]).date() == today]
if not today_items:
    body = build_4_lines(items[0])
else:
    blocks = [build_4_lines(it) for it in today_items]
    body = "\n\n".join(blocks)
# =========================
# SMS con Twilio (mensaje normal)
# =========================
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body=body,
    from_=SMS_FROM,
    to=SMS_TO,
)
print(message.body)