from flask import Flask
app = Flask(__name__)

# para ejecutar: py -m flask run

# print(__name__)

#basicamente eso que vemos de @app.route es lo que pasara si el usuario en la web usa lo que le asignamos en los parentesis

@app.route('/') #python decorators
def hello_world():
    return 'Hello, world'
# si ponemos en el link: http://127.0.0.1:5000 un /
# nos va a mostrar Hello World

@app.route('/bye')
def bye():
    return "Goodbye"

# si ponemos en el link: http://127.0.0.1:5000 un /bye
# nos va a mostrar Goodbye

if __name__ == "__main__":
    app.run()


    