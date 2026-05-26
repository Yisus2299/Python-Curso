from flask import Flask
import random

app = Flask(__name__)

# Store the random number globally - this will be regenerated on server restart
# Note: In production, you'd use sessions or database for this
random_number = random.randint(0, 9)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Higher-Lower Game</title>
    </head>
    <body style="text-align: center; padding: 50px;">
        <h1 style="color: purple;">Guess a number between 0 and 9</h1>
        
        <p>Click on a number below to make your guess!</p>
        
        <div style="margin-top: 20px;">
            <a href="/0">0</a> |
            <a href="/1">1</a> |
            <a href="/2">2</a> |
            <a href="/3">3</a> |
            <a href="/4">4</a> |
            <a href="/5">5</a> |
            <a href="/6">6</a> |
            <a href="/7">7</a> |
            <a href="/8">8</a> |
            <a href="/9">9</a>
        </div>
        
        <!-- Add your image here later -->
        <img src="YOUR_IMAGE_URL_HERE" alt="Game Image" width="300">
    </body>
    </html>
    '''

@app.route("/<int:guess>")
def check_guess(guess):
    global random_number
    
    if guess < random_number:
        # Too low - show orange text
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Too Low!</title>
        </head>
        <body style="text-align: center; padding: 50px;">
            <h1 style="color: orange;">Too low! Try again!</h1>
            <p>You guessed {guess}, but the number is higher.</p>
            <img src="YOUR_TOO_LOW_IMAGE_HERE" alt="Too Low" width="300">
            <p><a href="/">Go back and try again</a></p>
        </body>
        </html>
        '''
    elif guess > random_number:
        # Too high - show red text
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Too High!</title>
        </head>
        <body style="text-align: center; padding: 50px;">
            <h1 style="color: red;">Too high! Try again!</h1>
            <p>You guessed {guess}, but the number is lower.</p>
            <img src="YOUR_TOO_HIGH_IMAGE_HERE" alt="Too High" width="300">
            <p><a href="/">Go back and try again</a></p>
        </body>
        </html>
        '''
    else:
        # Correct! Show green text and generate a new random number
        random_number = random.randint(0, 9)  # Generate new number for next game
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>You Won!</title>
        </head>
        <body style="text-align: center; padding: 50px;">
            <h1 style="color: green;">You found it! The number was {guess}!</h1>
            <p>Congratulations! A new number has been generated.</p>
            <img src="YOUR_WIN_IMAGE_HERE" alt="Winner" width="300">
            <p><a href="/">Play again with a new number</a></p>
        </body>
        </html>
        '''

if __name__ == "__main__":
    app.run(debug=True)
