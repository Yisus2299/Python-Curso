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
                f"Ejem, Holis {nombre},\n\n"
                "Ya dejando las formalidades. FELIZ CUMPLEAÑOOOOS MI NIÑA PRECIOSAAA HOY EN TU DIA ESPECIAAAAL\n"
                "La fecha en la que escribi este correo fue el 15-04-2026 (jsj si, si lo recuerdas yo programe este correo en codigo) no se cuantas cosas hayan pasado desde entonces, espero hayamos conseguido gran parte de lo que queremos y que todo sea mejor, se que es y sera asi.\n"
                "Solo el universo entero sabe perfectamente cuando te amo y lo mucho que todos los dias le pido por ti. Todo lo que mi vida ha cambiado desde que te conoci para bien y lo mucho que haces girar mi mundo entero, y lo mucho que deseo que formes parte de el eternamente. Se que sera asi.\n"
                "Me encanta pasar todos los dias contigo, cada momento es un regalo, cada hora/minuto/segundo. Amo cada parte de ti, cada pensamiento, cada observacion, cada punto. Quizas cosas que pienses que no le gustarian a nadie de ti, a mi me encantan\n"
                "Tus entidades me parecen unas personas muy agradables, son simplemente geniales y agradezco haber conocido a muchas en lo que va de tiempo. Espero que cuando lean esto, haya conocido a mas y mas; por mientras, que les puedo decir que ya no les haya dicho de momento, son personas magnificas con un universo entero por explorar que espero jamas dejar de conocer y que tengan plena confianza en nosotros. Los aprecio a todos sin igual\n"
                "Se que quizas haya momentos en donde nada sea como pensamos, donde quizas muchas veces pensemos que no podremos y que realmente no sabemos como continuar. Pero si eso sucede, quiero que sepas que siempre sere tu piedra de apoyo y si no sabes que hacer tratare de ayudarte guiandote, dando opiniones o estando alli para ti incluso cuando sientas que no hay nadie que puede entenderte y estes sola en tu cuarto. Alli estare sin importar que\n"
                "Es ironico que muchas cosas se pudieran haber adelantado incluso por mucho tiempo si tan solo nos hubieramos pedido un consejo de amor; pero, no me arrepiento de nada, ahora estamos juntos y siempre estare para ti\n"
                "Gracias por todos los regalos, las palabras, los pensamientos, las opiniones, los momentos y los recuerdos que nos quedan y hemos creado en todo este tiempo. Son cosas que mejoraran en un futuro\n"
                "Aunque quisiera poder adelantar el tiempo, el orden de las cosas pasa por algo. Tal como dice anteriormente, solo Dios y el universo saben cuanto pido por ti, por tu salud, por tus logros/metas/deseos. Estare alli para lograr todo juntos y para crear eso que siempre quisimos; una famikia, romper el molde, ser diferentes, tener nuestras empresas y poder lograr todo lo que algun dia todos nos dieron la espalda.\n"
                "Sin nada mas que decir, Te amo Alekk, mi Isis, my Moon. Feliz cupleaños mi niña preciosa y espero lo pases y estes pasando excelente cuando recibas este correo algo simple quizas jsj. Gracias por todo y te lo recompenzare siempre\n\n"
                "Nuestro amor es como el viento, no puedo verlo, pero sí sentirlo — Nicholas Sparks\n"
                "Quiero hacer contigo lo que la primavera hace con los cerezos. Querer renovarte, llenarte de vida y belleza por la eternidad - Pablo Nebura\n\n"
                "Con cariño, tu Zyran<3\n"
            )

            smtp.send_message(msg)
            print(f"Enviado a {nombre} <{email}>")

except smtplib.SMTPAuthenticationError:
    raise ValueError(
        "Error de autenticación SMTP. Revisa EMAIL_SENDER y GMAIL_PASSWORD (App Password)."
    )
except smtplib.SMTPException as e:
    raise RuntimeError(f"Error al enviar correos: {e}") from e