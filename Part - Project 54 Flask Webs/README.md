# Flask Web Development Fundamentals

## Project Overview
An introduction to Flask web framework with basic web server setup and route definitions. This project covers Flask fundamentals including route creation, basic HTTP responses, and simple web application structure.

## Technologies Used
- Python 3.x
- Flask web framework
- Basic HTTP protocol concepts
- Route definitions and decorators
- Development server setup

## Project Structure
```
Part - Project 54 Flask Webs/
├── step1.py              # Basic Flask application
├── ejercicio.py          # Flask exercises and practice
└── README.md            # This file
```

## Features
- Basic Flask web server setup
- Route definitions with decorators
- HTTP response handling
- Development server configuration
- Simple web application structure
- Debug mode implementation

## Prerequisites
1. Python 3.x installed
2. Flask installation:
   ```
   pip install flask
   ```

## File Descriptions

### `step1.py`
Basic Flask application demonstrating:
- Minimal Flask app structure
- Route definitions (`@app.route` decorators)
- String response handling
- Development server startup
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route('/bye')
def bye():
    return "Goodbye"

if __name__ == "__main__":
    app.run()
```

### `ejercicio.py`
Flask exercises and additional practice:
- Multiple route examples
- Route parameter experimentation
- Different response types
- Application configuration options

## Code Examples

### Basic Flask Application
```python
from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Root route - home page
@app.route('/')
def home():
    return 'Welcome to the Home Page'

# About page route
@app.route('/about')
def about():
    return 'About Us Page'

# Contact page route  
@app.route('/contact')
def contact():
    return 'Contact Us Page'

# Dynamic route with parameter
@app.route('/user/<username>')
def show_user(username):
    return f'User Profile: {username}'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

## How to Run Flask Applications

### Method 1: Python Script Execution
```
python step1.py
```
or
```
python -m flask run
```

### Method 2: Command Line Interface
```bash
# Set Flask app environment variable
export FLASK_APP=step1.py  # Linux/Mac
set FLASK_APP=step1.py     # Windows

# Run Flask development server
flask run

# Enable debug mode
flask run --debug
```

## Development Server Output
When running, you'll see output similar to:
```
 * Serving Flask app 'step1.py'
 * Debug mode: off
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Access your application at: `http://127.0.0.1:5000`

## Flask Concepts Covered

### 1. **Application Instance**
```python
app = Flask(__name__)
```
- `__name__` helps Flask find resources
- Creates the WSGI application instance
- Required for all Flask applications

### 2. **Route Decorators**
```python
@app.route('/path')
def function_name():
    return 'response'
```
- Maps URL paths to Python functions
- Uses decorator syntax (`@app.route`)
- Function name becomes view function name

### 3. **View Functions**
- Functions that handle HTTP requests
- Return HTTP responses (usually strings)
- Can return HTML, JSON, or other content types

### 4. **Development Server**
```python
app.run(debug=True, port=8080, host='0.0.0.0')
```
- `debug=True`: Auto-reload on code changes, error pages
- `port`: Change default port (5000)
- `host`: Make server accessible on network

## Common Route Patterns

### 1. **Static Routes**
```python
@app.route('/about')
def about():
    return 'Static About Page'
```

### 2. **Dynamic Routes**
```python
@app.route('/user/<username>')
def profile(username):
    return f'User: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'
```

### 3. **Multiple HTTP Methods**
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login POST request'
    return 'Login GET form'
```

## Configuration Options

### Basic Configuration
```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['TESTING'] = False
```

### Development vs Production
```python
if __name__ == '__main__':
    # Development settings
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5000,
        threaded=True
    )
```

## Error Handling Basics

### 404 Not Found
Flask automatically returns 404 for undefined routes.

### Custom Error Pages
```python
@app.errorhandler(404)
def page_not_found(error):
    return 'Custom 404 Page', 404
```

## Project Structure Best Practices

### Minimal Structure
```
flask_app/
├── app.py
├── requirements.txt
└── README.md
```

### Recommended Structure
```
flask_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Testing Your Application

### 1. **Manual Testing**
```bash
# Test root route
curl http://127.0.0.1:5000/

# Test about route
curl http://127.0.0.1:5000/about

# Test dynamic route
curl http://127.0.0.1:5000/user/john
```

### 2. **Browser Testing**
1. Open browser to `http://127.0.0.1:5000`
2. Navigate to different routes
3. Test error handling (visit non-existent routes)

## Common Issues & Solutions

### 1. **Port Already in Use**
```python
app.run(port=5001)  # Change to different port
```

### 2. **Module Not Found**
```bash
# Ensure Flask is installed
pip install flask

# Check Python path
python -c "import flask; print(flask.__version__)"
```

### 3. **Auto-reload Not Working**
```python
app.run(debug=True)  # Enable debug mode
```

## Security Considerations

### 1. **Never Use in Production**
```python
# Development only - not for production!
app.run(debug=True)
```

### 2. **Production Deployment Options**
- Gunicorn
- uWSGI
- Waitress
- Deploy to: Heroku, AWS, DigitalOcean, etc.

### 3. **Basic Security**
```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
```

## Project Purpose
This project demonstrates:
- Flask web framework fundamentals
- Basic web server setup and configuration
- Route definition and URL mapping
- Development server usage
- Simple web application structure
- Foundation for more complex Flask projects