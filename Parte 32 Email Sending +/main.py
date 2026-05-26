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
    Esto es para mi esposita hermosa. Se que muchas veces no te sientes muy bien, quizas pienses muchas veces que no puedes pero; quiero que sepas que eres la mejor en todo. Eres una hija excepcional, 
    eres la mejor amiga que alguien puede tener, la mejor novia que existe en este mundo y seras la mejor esposa que existira en el universo entero y asi podria seguir. Adoro cada cosa de ti, todos tus conocimientos, todos tus gustos
    todo lo que realmente pienses que jamas a nadie le podria gustar de ti, a mi me encanta. Y si, eso incluyen tus gustos en toda la palabra (kajsaj aunque algunos me den cosa, los respeto), tus canciones, tus dibujos, tu carrera, tus pensamientos, tu sonrisa/ojos/cabello, simplemente todo.
    Nunca olvides quien eres, lo que eres y jamas dudes de ti, y si eso pasa, siempre te lo recordare de alguna manera, por algo somos un equipo. Y para todas tus entidades, a todas las que conozco les tengo aprecio, perdonen que este mensaje vaya mas enfocado para Isis de antemano jsjs. Quiero mucho
    a Ryo (gracias por ser ese amigo/hermano que siempre quise), a Nana (gracias por ser alguien muy espontanea y que dice las cosas de manera directa), A Solene (me encanta tu arte y tus gustos segun he visto en pinterest), a Kafffy (jaja eres muy chistosa y me gusta como eres) y asi podria seguir.
    Asi que si o si debemos de casarnos dentro de poco relaticamente, que no se te olvide y JAMAS SE TE OCURRA RENDIRTE, TU PUEDES<33. Muak. Att: Zyran.
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
