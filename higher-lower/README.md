# Higher-Lower Game with Flask

A web-based number guessing game built with Flask where users try to guess a randomly generated number between 0 and 9.

## Features

- Random number generation between 0 and 9
- Interactive web interface with clickable number buttons
- Visual feedback with different colored messages for each result
- Animated GIFs for different game states
- Responsive design

## How to Play

1. The computer generates a random number between 0 and 9
2. Click on any number from 0 to 9 to make your guess
3. Get feedback:
   - **Too low** (orange): Your guess is lower than the random number
   - **Too high** (red): Your guess is higher than the random number  
   - **Correct** (green): You guessed the right number!

## Installation

1. Make sure you have Python installed (Python 3.6 or higher)
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the project directory
2. Run the Flask application:
   ```bash
   python server.py
   ```
3. Open your web browser and go to: `http://127.0.0.1:5000`

## Project Structure

- `server.py` - Main Flask application with game logic
- `requirements.txt` - Python dependencies
- `README.md` - This documentation file

## Code Explanation

The application consists of two main routes:

1. **Home Route (`/`)**: Displays the game interface with number buttons
2. **Guess Route (`/<int:number>`)**: Checks the guessed number against the random number and provides feedback

The game uses:
- Flask for web framework
- Random module for number generation
- HTML/CSS for the user interface
- External GIFs for visual feedback

## Customization

You can easily modify:
- The number range by changing `random.randint(0, 9)` in server.py
- The colors by modifying the CSS styles
- The GIFs by changing the URLs in the result messages
- The styling by editing the HTML/CSS in the return statements