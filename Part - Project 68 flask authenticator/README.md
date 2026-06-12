# Flask Authenticator

A Flask-based web application demonstrating user authentication with registration, login, and protected routes using Flask-Login.

## Overview

This project implements a complete authentication system with user registration, login functionality, session management, and protected pages that require authentication. It uses secure password hashing and Flask's session management.

## Features

- **User Registration**: Create new accounts with email, password, and name
- **User Login**: Authenticate existing users with email and password
- **Session Management**: Persistent login sessions using Flask-Login
- **Protected Routes**: Certain pages only accessible to authenticated users
- **Password Security**: PBKDF2-SHA256 hashing with salt
- **Flash Messages**: User feedback for errors and status updates
- **File Download**: Protected download functionality for registered users

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Security**: Werkzeug password hashing
- **Session Management**: Flask-Login user loader

## Project Structure

```
Part - Project 68 flask authenticator/
├── main.py                 # Main Flask application
├── templates/              # HTML templates
│   ├── index.html         # Home page
│   ├── register.html      # Registration form
│   ├── login.html         # Login form
│   ├── secrets.html       # Protected page (requires login)
│   └── ...                # Other templates
├── static/                # Static assets
│   └── files/
│       └── cheat_sheet.pdf  # Downloadable file
├── instance/              # SQLite database location
├── requirements.txt       # Python dependencies
└── .DS_Store             # macOS metadata
```

## Database Schema

### User Table

| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Unique identifier |
| email | String(100) | User email (unique) |
| password | String(100) | Hashed password |
| name | String(1000) | User's display name |

## Installation & Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-login
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access in browser**:
   Navigate to `http://localhost:5000`

## How It Works

### Authentication Flow

1. **Registration** (`/register`):
   - Validate email is not already registered
   - Hash password using PBKDF2-SHA256
   - Create new User record in database
   - Auto-login after successful registration

2. **Login** (`/login`):
   - Verify email exists in database
   - Check password hash against provided password
   - Create session using Flask-Login

3. **Session Management**:
   - User loader callback: `@login_manager.user_loader`
   - Decorator: `@login_required` for protected routes

### Password Security

```python
from werkzeug.security import generate_password_hash, check_password_hash

# Hashing a password
hash_and_salted_password = generate_password_hash(
    password,
    method='pbkdf2:sha256',
    salt_length=8
)

# Verifying a password
check_password_hash(stored_hash, provided_password)
```

### Routes

| Route | Method | Description | Access |
|-------|--------|-------------|--------|
| `/` | GET | Home page | Public |
| `/register` | GET/POST | Registration | Public |
| `/login` | GET/POST | Login | Public |
| `/secrets` | GET | Protected content | Requires login |
| `/download` | POST | Download file | Requires login |
| `/logout` | GET | Logout | Requires login |

## Key Components

### Flask-Login Setup

```python
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
```

### Protected Route

```python
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)
```

### Current User

In templates, access current user with:
- `current_user.is_authenticated` - Boolean for login status
- `current_user.name` - User's name
- `current_user.email` - User's email

## Flash Messages

The application uses Flask flash messages for feedback:
- "You've already signed up with that email, log in instead!"
- "That email does not exist, please try again."
- "Password incorrect, please try again."

Display in template with:
```jinja2
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      {{ message }}
    {% endfor %}
  {% endif %}
{% endwith %}
```

## Customization

### Adding User Roles

Add a role field to the User model:
```python
role: Mapped[str] = mapped_column(String(50), default="user")
```

### Remember Me Functionality

Enable persistent sessions:
```python
login_user(user, remember=True)
```

### Changing Secret Key

Update the secret key in main.py:
```python
app.config['SECRET_KEY'] = 'your-secure-secret-key'
```

## Security Notes

- Never store plain-text passwords (this project hashes them)
- Change the SECRET_KEY in production
- Use HTTPS in production environments
- Consider adding email verification
- Implement rate limiting for login attempts

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)