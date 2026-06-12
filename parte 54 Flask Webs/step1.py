from flask import Flask
app = Flask(__name__)

# to run: py -m flask run

# print(__name__)

# The @app.route decorator registers a URL route for the function below

@app.route('/')  # python decorators
def hello_world():
    return 'Hello, world'
# Visiting http://127.0.0.1:5000/ will return "Hello, world"

@app.route('/bye')
def bye():
    return "Goodbye"

# Visiting http://127.0.0.1:5000/bye will return "Goodbye"

if __name__ == "__main__":
    app.run()
