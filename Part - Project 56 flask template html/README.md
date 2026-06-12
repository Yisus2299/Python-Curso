# Flask Template HTML

## Project Overview
A Flask web application demonstrating template rendering with HTML files. This project introduces Flask's template system, separating Python logic from HTML presentation using Jinja2 templating engine.

## Technologies Used
- Python 3.x
- Flask web framework
- Jinja2 templating engine
- HTML5
- CSS (optional)
- Template inheritance

## Project Structure
```
Part - Project 56 flask template html/
├── main.py                    # Flask application
├── templates/
│   └── index.html            # HTML template file
└── README.md                 # This file
```

## Features
- Template rendering with `render_template()`
- Separation of concerns (logic vs presentation)
- Basic template variable passing
- Static file serving concept
- Template inheritance foundation

## Prerequisites
1. Python 3.x installed
2. Flask installation:
   ```
   pip install flask
   ```

## How to Run
```
python main.py
```

Access the application at: `http://127.0.0.1:5000`

## Code Explanation

### Main Application (`main.py`)
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### Template File (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Template Example</title>
</head>
<body>
    <h1>Welcome to Flask Templates</h1>
    <p>This HTML is rendered from a template file.</p>
</body>
</html>
```

## Key Concepts

### 1. **Template Rendering**
```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```
- `render_template()` looks for files in `templates/` folder
- Automatically handles HTML escaping for security
- Supports template inheritance and includes

### 2. **Template Directory Structure**
Flask expects this structure by default:
```
project/
├── main.py
├── templates/     # HTML template files
│   ├── base.html
│   ├── index.html
│   └── about.html
└── static/        # CSS, JS, images (optional)
    ├── style.css
    └── logo.png
```

### 3. **Template Variable Passing**
```python
@app.route("/")
def home():
    user_name = "John"
    return render_template("index.html", name=user_name)
```
```html
<!-- In template -->
<h1>Welcome, {{ name }}!</h1>
```

## Template Features

### 1. **Variable Substitution**
```html
<p>Hello, {{ username }}!</p>
<p>Your score: {{ score }}/100</p>
<p>Today is {{ date }}</p>
```

### 2. **Control Structures**
```html
{% if user_logged_in %}
    <p>Welcome back!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### 3. **Template Inheritance**
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- index.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h1>Welcome to the Home Page</h1>
{% endblock %}
```

## Project Structure Best Practices

### Minimal Structure
```
flask_template_project/
├── main.py
├── templates/
│   └── index.html
└── requirements.txt
```

### Recommended Structure
```
flask_template_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── layout.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Template Configuration

### Custom Template Folder
```python
app = Flask(__name__, template_folder='views')
# Now looks for templates in 'views/' folder
```

### Auto-reload Templates (Debug Mode)
```python
app.run(debug=True)  # Templates auto-reload when changed
```

## Static Files

### Serving Static Files
```python
# Flask automatically serves files from 'static/' folder
# Access at: /static/filename
```

### In Templates
```html
<!-- Link to CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<!-- Link to JavaScript -->
<script src="{{ url_for('static', filename='script.js') }}"></script>

<!-- Link to Image -->
<img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
```

## Template Context

### Default Context Variables
Flask automatically provides:
- `config`: Application configuration
- `request`: Current request object
- `session`: Session object (if enabled)
- `g`: Global request object

### Adding Custom Context
```python
@app.context_processor
def inject_user():
    return dict(current_user=get_current_user())
```
Now `current_user` is available in all templates.

## Template Filters

### Built-in Filters
```html
<!-- String manipulation -->
<p>{{ text|upper }}</p>
<p>{{ text|lower }}</p>
<p>{{ text|title }}</p>

<!-- List operations -->
<p>Total: {{ items|length }}</p>
<p>First: {{ items|first }}</p>
<p>Last: {{ items|last }}</p>

<!-- Default values -->
<p>{{ value|default("Not specified") }}</p>
```

### Custom Filters
```python
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]
```
```html
<p>{{ text|reverse }}</p>
```

## Template Testing

### Manual Testing
1. Start server: `python main.py`
2. Visit: `http://127.0.0.1:5000`
3. Check HTML output in browser
4. View page source to verify template rendering

### Automated Testing
```python
import unittest
from main import app

class TemplateTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_template(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Flask Templates', response.data)
```

## Common Issues & Solutions

### 1. **Template Not Found Error**
```python
# Ensure templates/ folder exists
# Check template filename spelling
# Verify render_template() parameters
```

### 2. **Template Syntax Errors**
```html
<!-- Missing closing tags -->
{% if condition %}  <!-- Missing {% endif %} -->

<!-- Incorrect variable syntax -->
{{ variable }}  <!-- Correct -->
{ variable }    <!-- Incorrect -->
```

### 3. **Static Files Not Loading**
- Check `static/` folder exists
- Use `url_for('static', filename='...')`
- Verify file permissions

## Security Considerations

### 1. **Auto-escaping**
```html
<!-- Flask auto-escapes HTML by default -->
<p>{{ user_input }}</p>  <!-- Safe from XSS -->

<!-- Use |safe filter only for trusted content -->
<p>{{ trusted_html|safe }}</p>
```

### 2. **Template Injection Prevention**
- Never render untrusted templates
- Validate template variables
- Use appropriate escaping

### 3. **Directory Traversal Prevention**
Flask's template loader prevents:
```python
# This is safe - cannot access outside templates/
render_template('../../../etc/passwd')  # Returns 404
```

## Project Purpose
This project demonstrates:
- Flask template rendering fundamentals
- Separation of Python logic and HTML presentation
- Basic Jinja2 template syntax
- Template file organization
- Foundation for more complex Flask applications
- Best practices for web application structure