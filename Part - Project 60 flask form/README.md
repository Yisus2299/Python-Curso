# Flask Web Form with Email Submission

## Project Overview
A Flask web application featuring a contact form that collects user information and sends it via email using SMTP. This project demonstrates form handling, email automation, environment variable management, and template rendering in Flask.

## Technologies Used
- Python 3.x
- Flask web framework
- SMTP (email sending)
- HTML forms
- Jinja2 templating
- dotenv (environment variables)
- SSL/TLS encryption
- Pathlib (file path handling)

## Project Structure
```
Part - Project 60 flask form/
├── main.py                    # Flask application
├── templates/
│   ├── index.html            # Contact form page
│   ├── success.html          # Success confirmation page
│   ├── error.html            # Error page
│   └── .env                  # Environment variables (in templates folder)
├── venv/                     # Virtual environment
└── README.md                 # This file
```

## Features
- Web form with multiple input fields
- Email submission via Gmail SMTP
- Environment variable security
- Form validation and error handling
- Success/error page routing
- SSL/TLS encrypted email transmission
- Template rendering with Flask

## Prerequisites
1. Python 3.x installed
2. Gmail account with 2-factor authentication
3. App password generated from Google Account
4. Required Python libraries:
   ```
   pip install flask python-dotenv
   ```

## Setup Instructions

### 1. **Environment Configuration**
Create a `.env` file in the `templates/` folder with:
```
EMAIL_SENDER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password_here
EMAIL_TO=recipient_email@gmail.com  # Optional, defaults to EMAIL_SENDER
```

### 2. **Security Notes**
⚠️ **IMPORTANT:**
- Never commit `.env` files to version control
- Use app passwords, not regular passwords
- Store `.env` outside project root in production
- Use environment variables on deployment platforms

## How to Run
```
python main.py
```

Access the application at: `http://127.0.0.1:5000`

## Code Explanation

### Main Application (`main.py`)
```python
from flask import Flask, render_template, request
import os
import ssl
import smtplib
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from templates/.env
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / "templates" / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

app = Flask(__name__)

def get_env_value(name: str) -> str:
    """Read and clean environment variable values."""
    value = os.getenv(name) or ""
    cleaned = value.strip().strip('"').strip("'")
    cleaned = cleaned.replace("\u200b", "").replace("\ufeff", "").replace("\u00a0", "")
    return cleaned

# Load email configuration
EMAIL_SENDER = get_env_value("EMAIL_SENDER")
GMAIL_PASSWORD = get_env_value("GMAIL_PASSWORD").replace(" ", "")
EMAIL_TO = get_env_value("EMAIL_TO") or EMAIL_SENDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        # Get form data
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        message_text = request.form.get("message", "").strip()
        
        # Basic validation
        if not all([name, email, message_text]):
            return render_template("error.html", 
                                 error="Please fill in all required fields")
        
        # Send email
        send_form_email(name, email, password, message_text)
        
        return render_template("success.html", name=name)
        
    except Exception as e:
        return render_template("error.html", error=str(e))

def send_form_email(name: str, email: str, password: str, message_text: str) -> None:
    """Send form submission via email."""
    if not EMAIL_SENDER or not GMAIL_PASSWORD:
        raise ValueError("EMAIL_SENDER or GMAIL_PASSWORD missing in .env file")
    
    # Create email message
    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "New submission from web form"
    
    # Email body
    body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Password (form): {password}\n"
        f"Message:\n{message_text}\n"
    )
    msg.set_content(body)
    
    # Send email with SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, GMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
```

## Template Files

### `templates/index.html` (Contact Form)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Contact Form</h1>
    <form action="/submit" method="POST">
        <div class="form-group">
            <label for="name">Full Name *</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email Address *</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="password">Password (for demonstration)</label>
            <input type="password" id="password" name="password">
        </div>
        
        <div class="form-group">
            <label for="message">Message *</label>
            <textarea id="message" name="message" rows="5" required></textarea>
        </div>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### `templates/success.html` (Success Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submission Successful</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .success {
            color: #28a745;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div class="success">✅</div>
    <h1>Thank You, {{ name }}!</h1>
    <p>Your form has been submitted successfully.</p>
    <p>We have received your message and will respond shortly.</p>
    <a href="/">Back to Form</a>
</body>
</html>
```

### `templates/error.html` (Error Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        .error {
            color: #dc3545;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div class="error">❌</div>
    <h1>Something Went Wrong</h1>
    <p>{{ error }}</p>
    <a href="/">Back to Form</a>
</body>
</html>
```

## Key Features Explained

### 1. **Form Handling**
```python
# GET request shows the form
@app.route("/")
def home():
    return render_template("index.html")

# POST request processes form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    # ... process data
```

### 2. **Environment Variable Management**
```python
from dotenv import load_dotenv

# Load from specific file
ENV_FILE = BASE_DIR / "templates" / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

# Get and clean values
def get_env_value(name: str):
    value = os.getenv(name) or ""
    cleaned = value.strip().strip('"').strip("'")
    return cleaned
```

### 3. **Email Sending with SSL**
```python
def send_form_email(name, email, password, message_text):
    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_TO
    msg["Subject"] = "New form submission"
    msg.set_content(f"Name: {name}\nEmail: {email}\n...")
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, GMAIL_PASSWORD)
        smtp.send_message(msg)
```

## Form Validation

### 1. **Server-Side Validation**
```python
# Basic required field validation
if not all([name, email, message_text]):
    return render_template("error.html", 
                         error="Please fill in all required fields")

# Email format validation
import re
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if not re.match(email_regex, email):
    return render_template("error.html", 
                         error="Please enter a valid email address")
```

### 2. **Client-Side Validation** (HTML5)
```html
<!-- Required fields -->
<input type="text" name="name" required>

<!-- Email format validation -->
<input type="email" name="email" required>

<!-- Minimum length -->
<input type="password" name="password" minlength="8">

<!-- Maximum length -->
<textarea name="message" maxlength="1000"></textarea>
```

## Security Considerations

### 1. **Password Field Note**
The password field in this form is for demonstration purposes only. In production:
- Never store passwords in emails
- Use password hashing (bcrypt, Argon2)
- Implement proper authentication systems
- Use HTTPS for all form submissions

### 2. **Input Sanitization**
```python
# Basic input sanitization
def sanitize_input(text: str) -> str:
    """Remove potentially harmful characters."""
    # Remove HTML tags
    import re
    clean = re.sub(r'<[^>]*>', '', text)
    # Remove excessive whitespace
    clean = ' '.join(clean.split())
    return clean[:1000]  # Limit length
```

### 3. **CSRF Protection**
For production, add CSRF protection:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
```

## Email Configuration Options

### 1. **Different Email Providers**
```python
# Gmail
smtp_server = "smtp.gmail.com"
port = 465  # SSL
# port = 587  # TLS

# Outlook/Hotmail
smtp_server = "smtp-mail.outlook.com"
port = 587

# Yahoo
smtp_server = "smtp.mail.yahoo.com"
port = 465
```

### 2. **HTML Email Support**
```python
# Send HTML email
msg = EmailMessage()
msg.add_alternative(f"""
<html>
<body>
    <h1>New Form Submission</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong><br>{message_text}</p>
</body>
</html>
""", subtype='html')
```

## Error Handling

### 1. **SMTP Connection Errors**
```python
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.send_message(msg)
except smtplib.SMTPAuthenticationError:
    return "Authentication failed - check email/password"
except smtplib.SMTPException as e:
    return f"SMTP error: {str(e)}"
except Exception as e:
    return f"Unexpected error: {str(e)}"
```

### 2. **File Attachment Support**
```python
# Add file attachment
if 'attachment' in request.files:
    attachment = request.files['attachment']
    if attachment.filename:
        msg.add_attachment(
            attachment.read(),
            maintype='application',
            subtype='octet-stream',
            filename=attachment.filename
        )
```

## Deployment Considerations

### 1. **Production Environment Variables**
Never hardcode credentials. Use:
- Platform environment variables (Heroku, AWS, etc.)
- Docker secrets
- Kubernetes ConfigMaps/Secrets
- CI/CD pipeline variables

### 2. **Database Integration** (Advanced)
```python
# Store submissions in database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

# Save to database
submission = Submission(name=name, email=email, message=message_text)
db.session.add(submission)
db.session.commit()
```

## Testing the Application

### 1. **Manual Testing**
1. Start server: `python main.py`
2. Visit: `http://127.0.0.1:5000`
3. Fill out form and submit
4. Check email inbox for submission
5. Test validation by leaving fields empty

### 2. **Automated Testing**
```python
import unittest
from main import app

class FormTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Form', response.data)
    
    def test_form_submission(self):
        response = self.app.post('/submit', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 200)
```

## Project Purpose
This project demonstrates:
- Flask web form handling and processing
- Email automation with SMTP
- Environment variable management for security
- Template rendering and routing
- Form validation and error handling
- Production-ready application patterns
- Secure credential management practices