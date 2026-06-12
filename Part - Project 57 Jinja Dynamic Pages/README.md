# Jinja Dynamic Pages with API Integration

## Project Overview
A Flask web application demonstrating dynamic content generation using Jinja2 templating with external API integration. This project combines Flask routing, template rendering, and real-time data from external APIs to create interactive web pages.

## Technologies Used
- Python 3.x
- Flask web framework
- Jinja2 templating engine
- External APIs (Genderize, Agify, custom blog API)
- Requests library
- HTML/CSS
- datetime module

## Project Structure
```
Part - Project 57 Jinja Dynamic Pages/
├── server.py                # Main Flask application
├── templates/
│   ├── index.html          # Home page template
│   ├── guess.html          # Name guessing template
│   └── blog.html           # Blog posts template
└── README.md               # This file
```

## Features
- Dynamic content rendering with Jinja2
- External API integration for real-time data
- Multiple template pages with shared layout
- Template variable passing and manipulation
- Date formatting and timezone handling
- Blog post rendering from external API

## Prerequisites
1. Python 3.x installed
2. Required libraries:
   ```
   pip install flask requests
   ```

## How to Run
```
python server.py
```

Access the application at: `http://127.0.0.1:5000`

## API Endpoints Used

### 1. **Genderize API**
- URL: `https://api.genderize.io`
- Predicts gender from first name
- Returns: `gender`, `probability`, `count`

### 2. **Agify API**
- URL: `https://api.agify.io`
- Predicts age from first name
- Returns: `age`, `count`

### 3. **Custom Blog API**
- URL: `https://api.npoint.io/c790b4d5cab58020d391`
- Sample blog posts in JSON format
- Returns: Array of blog post objects

## Code Explanation

### Main Application (`server.py`)
```python
from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    name = "Jesus"
    current_year = datetime.now().year
    return render_template("index.html", name=name, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    # Gender prediction
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    # Age prediction
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    year = datetime.now().year
    return render_template("guess.html", name=name, gender=gender, age=age, year=year)

@app.route("/get_blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
```

## Template Examples

### `index.html` (Home Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Pages</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>Current year: {{ year }}</p>
    
    <h2>Try these links:</h2>
    <ul>
        <li><a href="/guess/John">Guess info for "John"</a></li>
        <li><a href="/guess/Maria">Guess info for "Maria"</a></li>
        <li><a href="/get_blog">View Blog Posts</a></li>
    </ul>
</body>
</html>
```

### `guess.html` (Name Guessing Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Name Guessing</title>
</head>
<body>
    <h1>Name Analysis for: {{ name }}</h1>
    
    <h2>Predicted Gender: {{ gender|title }}</h2>
    <h2>Predicted Age: {{ age }}</h2>
    
    <p>Year: {{ year }}</p>
    
    <a href="/">Back to Home</a>
</body>
</html>
```

### `blog.html` (Blog Posts Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
    <style>
        .post {
            border: 1px solid #ddd;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .title {
            color: #333;
            font-size: 1.5em;
        }
        .author {
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
    
    {% for post in posts %}
    <div class="post">
        <h2 class="title">{{ post.title }}</h2>
        <p class="author">By {{ post.author }}</p>
        <p>{{ post.content }}</p>
    </div>
    {% endfor %}
    
    <a href="/">Back to Home</a>
</body>
</html>
```

## Key Jinja2 Features Demonstrated

### 1. **Variable Rendering**
```html
<p>Name: {{ name }}</p>
<p>Year: {{ year }}</p>
```

### 2. **Filters**
```html
<!-- String manipulation -->
<p>Gender: {{ gender|title }}</p>  <!-- Capitalizes first letter -->
<p>Name: {{ name|upper }}</p>      <!-- Converts to uppercase -->
```

### 3. **Control Structures**
```html
<!-- Loops -->
{% for post in posts %}
    <div class="post">{{ post.title }}</div>
{% endfor %}

<!-- Conditionals -->
{% if age > 18 %}
    <p>Adult</p>
{% else %}
    <p>Minor</p>
{% endif %}
```

### 4. **Template Inheritance** (Concept)
```html
<!-- base.html -->
<html>
<body>
    {% block content %}{% endblock %}
    <footer>Year: {{ year }}</footer>
</body>
</html>

<!-- child.html -->
{% extends "base.html" %}
{% block content %}
    <h1>Page Content Here</h1>
{% endblock %}
```

## API Integration Patterns

### 1. **Synchronous API Calls**
```python
response = requests.get(api_url)
data = response.json()
return render_template("page.html", data=data)
```

### 2. **Error Handling**
```python
try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()  # Raise exception for HTTP errors
    data = response.json()
except requests.exceptions.RequestException as e:
    # Handle network errors
    data = {"error": str(e)}
```

### 3. **Caching API Responses**
```python
import time

cache = {}
cache_timeout = 300  # 5 minutes

def get_cached_data(api_url):
    now = time.time()
    if api_url in cache:
        data, timestamp = cache[api_url]
        if now - timestamp < cache_timeout:
            return data
    
    # Fetch fresh data
    response = requests.get(api_url)
    data = response.json()
    cache[api_url] = (data, now)
    return data
```

## Dynamic Routing Examples

### 1. **URL Parameters**
```python
@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"
```

### 2. **Type Conversion**
```python
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"
```

### 3. **Multiple Parameters**
```python
@app.route("/profile/<username>/<int:age>")
def profile(username, age):
    return render_template("profile.html", username=username, age=age)
```

## Template Context Enhancement

### 1. **Context Processor**
```python
@app.context_processor
def inject_global_vars():
    return {
        'current_year': datetime.now().year,
        'site_name': 'Dynamic Pages App'
    }
```
Now `current_year` and `site_name` are available in all templates.

### 2. **Template Functions**
```python
@app.template_filter('format_date')
def format_date_filter(value, format='%Y-%m-%d'):
    return value.strftime(format)
```
```html
<p>Date: {{ some_date|format_date('%B %d, %Y') }}</p>
```

## Testing Dynamic Content

### Manual Testing
1. Visit home page: `/`
2. Test name guessing: `/guess/John`, `/guess/Maria`
3. View blog posts: `/get_blog`
4. Test edge cases: `/guess/123`, `/guess/verylongname`

### Automated Testing
```python
import unittest
from server import app
import json

class TestDynamicPages(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)
    
    def test_guess_route(self):
        response = self.app.get('/guess/John')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)
    
    def test_blog_route(self):
        response = self.app.get('/get_blog')
        self.assertEqual(response.status_code, 200)
        # Assuming blog API returns JSON
        self.assertIn(b'Blog', response.data)
```

## Performance Considerations

### 1. **API Rate Limits**
- Genderize API: 1000 names/day free
- Agify API: 1000 names/day free
- Implement caching to reduce API calls
- Consider fallback data for API failures

### 2. **Async API Calls** (Advanced)
```python
import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def get_user_data(name):
    async with aiohttp.ClientSession() as session:
        gender_task = fetch_data(session, f"https://api.genderize.io?name={name}")
        age_task = fetch_data(session, f"https://api.agify.io?name={name}")
        
        gender_data, age_data = await asyncio.gather(gender_task, age_task)
        return gender_data, age_data
```

## Security Considerations

### 1. **API Input Validation**
```python
import re

def validate_name(name):
    # Only allow letters, spaces, and hyphens
    if not re.match(r'^[A-Za-z\s\-]+$', name):
        return False
    # Limit length
    if len(name) > 50:
        return False
    return True
```

### 2. **Error Handling in Templates**
```html
{% if gender %}
    <p>Gender: {{ gender }}</p>
{% else %}
    <p>Gender: Not available</p>
{% endif %}

{% if age %}
    <p>Age: {{ age }}</p>
{% else %}
    <p>Age: Not available</p>
{% endif %}
```

## Project Purpose
This project demonstrates:
- Dynamic web content generation with Flask and Jinja2
- External API integration for real-time data
- Template variable passing and manipulation
- Multiple page routing with shared context
- Practical web application patterns
- Error handling and user experience considerations