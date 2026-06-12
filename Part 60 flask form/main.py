from flask import Flask, render_template, request
import os
import ssl
import smtplib
from pathlib import Path
from email.message import EmailMessage

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
# Your .env file is stored in templates/ in this project; if you move it to the project root use: BASE_DIR / ".env"
ENV_FILE = BASE_DIR / "templates" / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

app = Flask(__name__)


def get_env_value(name: str) -> str:
    """Read environment variables and clean common .env formatting issues."""
    value = os.getenv(name) or ""
    cleaned = value.strip().strip('"').strip("'")
    cleaned = cleaned.replace("\u200b", "").replace("\ufeff", "").replace("\u00a0", "")
    return cleaned


EMAIL_SENDER = get_env_value("EMAIL_SENDER")
GMAIL_PASSWORD = get_env_value("GMAIL_PASSWORD").replace(" ", "")
# Optional in .env: EMAIL_TO=other@domain.com. If not set, messages are sent to EMAIL_SENDER.
EMAIL_TO = get_env_value("EMAIL_TO") or EMAIL_SENDER


def send_form_email(name: str, email: str, password: str, message_text: str) -> None:
    if not EMAIL_SENDER or not GMAIL_PASSWORD:
        raise ValueError("EMAIL_SENDER or GMAIL_PASSWORD missing in .env file")

    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "New submission from web form"

    body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Password (form): {password}\n"
        f"Message:\n{message_text}\n"
    )
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, GMAIL_PASSWORD)
        smtp.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        message_text = request.form.get("message", "").strip()

        print(name)
        print(email)
        print(password)
        print(message_text)

        try:
            send_form_email(name, email, password, message_text)
        except (ValueError, smtplib.SMTPException, OSError) as e:
            print("Error sending email:", e)
            error = "Unable to send email. Check server console and .env file."
            return render_template("index.html", success=False, error=error)

        return render_template("index.html", success=True, error=None)

    return render_template("index.html", success=False, error=None)


if __name__ == "__main__":
    app.run(debug=True)