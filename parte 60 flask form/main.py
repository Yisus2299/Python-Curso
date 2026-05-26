from flask import Flask, render_template, request
import os
import ssl
import smtplib
from pathlib import Path
from email.message import EmailMessage

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
# Tu .env está en templates/; si lo pasas a la raíz del proyecto, usa: BASE_DIR / ".env"
ENV_FILE = BASE_DIR / "templates" / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

app = Flask(__name__)


def get_env_value(name: str) -> str:
    """Lee variables de entorno y limpia formato habitual (.env con espacios, comillas, BOM)."""
    value = os.getenv(name) or ""
    cleaned = value.strip().strip('"').strip("'")
    cleaned = cleaned.replace("\u200b", "").replace("\ufeff", "").replace("\u00a0", "")
    return cleaned


EMAIL_SENDER = get_env_value("EMAIL_SENDER")
GMAIL_PASSWORD = get_env_value("GMAIL_PASSWORD").replace(" ", "")
# Opcional en .env: EMAIL_TO=tuotro@correo.com  Si no existe, se envía a ti mismo (EMAIL_SENDER).
EMAIL_TO = get_env_value("EMAIL_TO") or EMAIL_SENDER


def enviar_correo_formulario(nombre: str, email: str, password: str, mensaje: str) -> None:
    if not EMAIL_SENDER or not GMAIL_PASSWORD:
        raise ValueError("Faltan EMAIL_SENDER o GMAIL_PASSWORD en el archivo .env")

    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Nuevo envío desde el formulario web"

    cuerpo = (
        f"Name: {nombre}\n"
        f"Email: {email}\n"
        f"Password (formulario): {password}\n"
        f"Message:\n{mensaje}\n"
    )
    msg.set_content(cuerpo)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, GMAIL_PASSWORD)
        smtp.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        nombre = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        mensaje = request.form.get("message", "").strip()

        print(nombre)
        print(email)
        print(password)
        print(mensaje)

        try:
            enviar_correo_formulario(nombre, email, password, mensaje)
        except (ValueError, smtplib.SMTPException, OSError) as e:
            print("Error al enviar correo:", e)
            error = "No se pudo enviar el correo. Revisa la consola del servidor y el archivo .env."
            return render_template("index.html", exito=False, error=error)

        return render_template("index.html", exito=True, error=None)

    return render_template("index.html", exito=False, error=None)


if __name__ == "__main__":
    app.run(debug=True)