import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Alekk Trecanao,kae97dm@gmail.com,7,9

load_dotenv()

email_sender = "jmzm08@gmail.com"
password = os.getenv("GMAIL_PASSWORD")
email_reciver = "kae97dm@gmail.com"

if not password:
    raise ValueError(
        "Falta GMAIL_PASSWORD en .env. Crea una contraseña de aplicación en Google y pégala ahí."
    )

subject = "Para mi noviecita hermosa Alekk<3"
body = """
   Test about sending email
"""


em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
