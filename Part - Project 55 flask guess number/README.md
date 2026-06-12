# Flask Number Guessing Game

## Project Overview
An interactive web-based number guessing game built with Flask. Users guess a number between 0-9 through URL parameters, with visual feedback and images indicating if their guess is too high, too low, or correct.

## Technologies Used
- Python 3.x
- Flask web framework
- HTML/CSS inline styling
- Random number generation
- Dynamic routing with parameters
- Image integration

## Project Structure
```
Part - Project 55 flask guess number/
├── guess_number.py       # Main Flask application
└── README.md            # This file
```

## Features
- Random number generation (0-9)
- Dynamic URL route handling
- Visual feedback with images
- Inline CSS styling for responsive design
- Game logic with comparison operators
- User-friendly interface

## Prerequisites
1. Python 3.x installed
2. Flask installation:
   ```
   pip install flask
   ```

## How to Run
```
python guess_number.py
```

The application will start at: `http://127.0.0.1:5000`

## Game Rules
1. A secret number between 0 and 9 is generated when the server starts
2. Users guess by visiting URLs like `/3`, `/7`, `/0`
3. The application provides feedback:
   - "Too low, try again!" if guess < secret number
   - "Too high, try again!" if guess > secret number  
   - "You found me!" if guess == secret number

## Code Explanation

### Main Application
```python
from flask import Flask
import random

app = Flask(__name__)

# Generate secret number when server starts
SECRET_NUMBER = random.randint(0, 9)

@app.route("/")
def home():
    return '''
    <h1 style="color: black; text-align:center;">
        Guess a number between 0 and 9
    </h1>
    <p style="text-align:center;">
        Type a number in the URL, for example: /3
    </p>
    <div style="text-align:center;">
        <img src="https://via.placeholder.com/300" width="300">
    </div>
    '''

@app.route("/<int:guess>")
def check_guess(guess: int):
    if guess < SECRET_NUMBER:
        return '''
        <h1 style="color: purple; text-align:center;">
            Too low, try again!
        </h1>
        <div style="text-align:center;">
            <img src="https://i.pinimg.com/736x/20/00/1e/20001eaddc88c53cc0f5f2d149c39375.jpg" width="300">
        </div>
        '''
    elif guess > SECRET_NUMBER:
        return '''
        <h1 style="color: red; text-align:center;">
            Too high, try again!
        </h1>
        <div style="text-align:center;">
            <img src="https://i.pinimg.com/736x/ef/3c/67/ef3c67f967e2db531984640a0c3161b5.jpg" width="300">
        </div>
        '''
    else:
        return '''
        <h1 style="color: green; text-align:center;">
            You found me!
        </h1>
        <div style="text-align:center;">
            <img src="https://i.pinimg.com/736x/f4/c6/27/f4c627261335050f44778ef550cc9553.jpg" width="300">
        </div>
        '''

if __name__ == "__main__":
    app.run(debug=True)
```

## Key Concepts Demonstrated

### 1. **Random Number Generation**
```python
import random
SECRET_NUMBER = random.randint(0, 9)  # Generate once at startup
```

### 2. **Dynamic Route with Type Conversion**
```python
@app.route("/<int:guess>")
def check_guess(guess: int):
    # Flask converts URL parameter to integer
    # Invalid inputs (non-numbers) return 404
```

### 3. **Conditional Logic**
```python
if guess < SECRET_NUMBER:
    # Too low response
elif guess > SECRET_NUMBER:
    # Too high response
else:
    # Correct guess response
```

### 4. **Inline CSS Styling**
```python
return '''
<h1 style="color: purple; text-align:center;">
    Too low, try again!
</h1>
'''
```

## Game Interface

### Home Page (`/`)
- Instructions for playing
- Placeholder image
- Clean, centered layout

### Game Responses
1. **Too Low Response** (`guess < secret`):
   - Purple colored text
   - "Too low, try again!" message
   - Encouraging image

2. **Too High Response** (`guess > secret`):
   - Red colored text  
   - "Too high, try again!" message
   - Different encouraging image

3. **Correct Guess** (`guess == secret`):
   - Green colored text
   - "You found me!" success message
   - Celebration image

## Customization Options

### 1. **Change Number Range**
```python
# Generate number between 1-100
SECRET_NUMBER = random.randint(1, 100)
```

### 2. **Custom Images**
```python
# Replace image URLs with your own
too_low_img = "https://your-domain.com/too-low.jpg"
too_high_img = "https://your-domain.com/too-high.jpg"
correct_img = "https://your-domain.com/correct.jpg"
```

### 3. **Add Attempt Counter**
```python
attempts = 0

@app.route("/<int:guess>")
def check_guess(guess: int):
    global attempts
    attempts += 1
    
    if guess < SECRET_NUMBER:
        return f'Too low! Attempt #{attempts}'
    # ... rest of logic
```

### 4. **Add Game Statistics**
```python
game_stats = {
    'games_played': 0,
    'wins': 0,
    'average_attempts': 0
}

@app.route("/stats")
def stats():
    return f'''
    Games Played: {game_stats['games_played']}<br>
    Wins: {game_stats['wins']}<br>
    Average Attempts: {game_stats['average_attempts']}
    '''
```

## Enhanced Features (Optional)

### 1. **Session Management**
```python
from flask import session
import secrets

app.secret_key = secrets.token_hex(16)

@app.route("/")
def home():
    session['secret_number'] = random.randint(0, 9)
    session['attempts'] = 0
    # ... rest of home page
```

### 2. **Form-Based Input**
```python
from flask import request

@app.route("/guess", methods=['POST'])
def guess_form():
    guess = int(request.form['guess'])
    # Process guess
```

### 3. **AJAX API Endpoint**
```python
@app.route("/api/check/<int:guess>")
def api_check_guess(guess):
    result = {
        'guess': guess,
        'secret': SECRET_NUMBER,
        'status': 'low' if guess < SECRET_NUMBER else 'high' if guess > SECRET_NUMBER else 'correct'
    }
    return jsonify(result)
```

## Testing the Game

### Manual Testing
1. Start the server: `python guess_number.py`
2. Open browser to: `http://127.0.0.1:5000`
3. Try different guesses:
   - `http://127.0.0.1:5000/0`
   - `http://127.0.0.1:5000/5`
   - `http://127.0.0.1:5000/9`

### Automated Testing
```python
import unittest
from guess_number import app

class TestGame(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Guess a number', response.data)
```

## Common Issues & Solutions

### 1. **Images Not Loading**
- Check image URLs are accessible
- Use absolute URLs (https://)
- Consider hosting images locally

### 2. **Random Number Changes on Refresh**
- Ensure `SECRET_NUMBER` is generated once at startup
- Don't regenerate inside route functions

### 3. **Type Conversion Errors**
- Flask's `<int:guess>` ensures parameter is integer
- Non-integer URLs return 404 automatically

## Security Considerations

### 1. **Input Validation**
- Flask's type converter handles basic validation
- Additional validation for edge cases if needed

### 2. **Image Security**
- Use HTTPS image URLs
- Consider content security policy for external images
- Host images locally for production

### 3. **Session Security**
- For enhanced features, use Flask sessions with secret key
- Never expose sensitive information in URLs

## Project Purpose
This project demonstrates:
- Interactive web applications with Flask
- Dynamic routing with parameters
- Game logic implementation
- Visual feedback with images and CSS
- User input handling via URL
- Random number generation for games