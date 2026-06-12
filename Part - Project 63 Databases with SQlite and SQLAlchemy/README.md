# Book Database with SQLite and SQLAlchemy

## Project Overview
A Flask web application for managing a personal book collection using SQLite database and SQLAlchemy ORM. This project demonstrates full CRUD (Create, Read, Update, Delete) operations with a modern web interface.

## Technologies Used
- Python 3.x
- Flask web framework
- SQLAlchemy ORM (Object-Relational Mapping)
- SQLite database
- HTML/CSS with Bootstrap
- WTForms for form handling
- SQL database operations

## Project Structure
```
Part - Project 63 Databases with SQlite and SQLAlchemy/
├── main.py              # Flask application with SQLAlchemy
├── books-collection.db  # SQLite database file
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── index.html      # Home page with book list
│   ├── add.html        # Add new book form
│   └── edit.html       # Edit book rating form
└── README.md           # This file
```

## Features
- **Book Management**: Complete CRUD operations for book collection
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **Rating System**: Decimal-based rating system (0.0-10.0)
- **Responsive Design**: Bootstrap-styled interface
- **Form Validation**: Server-side validation with WTForms
- **Search & Sort**: Display books in customizable order
- **Data Persistence**: Proper database transactions and error handling

## Installation
1. Clone the repository and navigate to the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
```bash
python main.py
```
The application will be available at: `http://127.0.0.1:5000`

## Database Schema
### Book Table Structure
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) UNIQUE NOT NULL,
    author VARCHAR(250) NOT NULL,
    rating FLOAT NOT NULL
);
```

### SQLAlchemy Model
```python
class Book(db.Model):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
```

## Application Routes
- `/`: Home page displaying all books
- `/add`: Add new book form (GET/POST)
- `/edit/<int:book_id>`: Edit book rating (GET/POST)
- `/delete/<int:book_id>`: Delete book (GET/POST with confirmation)

## Code Structure
### Main Application (`main.py`)
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Database initialization with sample data
with app.app_context():
    db.create_all()
    if db.session.query(Book).first() is None:
        db.session.add(Book(title="Harry Potter", author="J. K. Rowling", rating=9.3))
        db.session.commit()

@app.route("/")
def home():
    books = Book.query.order_by(Book.id).all()
    return render_template("index.html", books=books)
```

## CRUD Operations
### Create (Add New Book)
```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form.get("title", "").strip(),
            author=request.form.get("author", "").strip(),
            rating=float(request.form.get("rating", "0"))
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")
```

### Read (Display Books)
```python
@app.route("/")
def home():
    books = Book.query.order_by(Book.id).all()
    return render_template("index.html", books=books)
```

### Update (Edit Rating)
```python
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.session.get(Book, book_id)
    if request.method == "POST":
        book.rating = float(request.form.get("rating", "0"))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)
```

### Delete (Remove Book)
```python
@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book = db.session.get(Book, book_id)
    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("delete.html", book=book)
```

## Database Operations
### SQLAlchemy Query Examples
```python
# Get all books
books = Book.query.all()

# Get book by ID
book = db.session.get(Book, book_id)

# Filter books by author
books_by_author = Book.query.filter_by(author="J. K. Rowling").all()

# Order books by rating (descending)
top_books = Book.query.order_by(Book.rating.desc()).all()

# Search books by title
search_results = Book.query.filter(Book.title.contains("Potter")).all()

# Update a record
book.rating = 9.5
db.session.commit()

# Delete a record
db.session.delete(book)
db.session.commit()
```

## Form Handling
### Add Book Form
- **Title**: Required text field (unique constraint)
- **Author**: Required text field
- **Rating**: Decimal field (0.0-10.0)

### Edit Book Form
- **Rating**: Decimal field for updating existing book rating
- **Confirmation**: POST request for updates

### Delete Confirmation
- **Confirmation Page**: Prevents accidental deletions
- **POST Request**: Required for deletion action

## Database Configuration
### SQLite Connection
```python
import os
from pathlib import Path

_base_dir = Path(__file__).parent.absolute()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{_base_dir}/books-collection.db"
```

### SQLAlchemy Settings
```python
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disables modification tracking overhead
```

## Data Validation
### Form Input Validation
```python
def _parse_rating(raw: str) -> float:
    """Parse and validate rating input."""
    try:
        rating = float((raw or "0").strip())
        return max(0.0, min(10.0, rating))  # Clamp between 0-10
    except ValueError:
        return 0.0
```

### Database Constraints
- **Title**: Unique constraint prevents duplicate entries
- **Author**: Required field (NOT NULL)
- **Rating**: Float type with range validation

## Error Handling
### Database Errors
```python
try:
    db.session.add(book)
    db.session.commit()
except IntegrityError:
    db.session.rollback()
    # Handle duplicate title error
except SQLAlchemyError as e:
    db.session.rollback()
    # Handle other database errors
```

### Form Validation Errors
- Required field validation
- Rating range validation (0-10)
- Unique title validation

## Bootstrap Integration
### Template Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Collection</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### Bootstrap Components Used
- **Tables**: Responsive table for book listings
- **Forms**: Bootstrap-styled form controls
- **Buttons**: Primary/secondary action buttons
- **Alerts**: Success/error message displays
- **Cards**: Book information cards

## Database Migration (Advanced)
### Alembic Integration
For production applications, consider adding database migrations:
```python
# Install Alembic
pip install alembic

# Initialize migrations
alembic init migrations

# Configure Alembic
# In alembic.ini, update sqlalchemy.url
# In migrations/env.py, import your models

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

## Testing
### Unit Tests Example
```python
import unittest
from main import app, db, Book

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_add_book(self):
        response = self.app.post('/add', data={
            'title': 'Test Book',
            'author': 'Test Author',
            'rating': '8.5'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
    
    def test_book_count(self):
        with app.app_context():
            count = Book.query.count()
            self.assertGreaterEqual(count, 1)  # At least the sample book
```

## Performance Considerations
### Database Optimization
1. **Indexing**: Add indexes for frequently queried columns
   ```python
   class Book(db.Model):
       # ... existing fields
       __table_args__ = (
           db.Index('idx_author', 'author'),
           db.Index('idx_rating', 'rating'),
       )
   ```

2. **Query Optimization**: Use selective queries instead of loading all data
   ```python
   # Instead of: Book.query.all()
   # Use: Book.query.with_entities(Book.title, Book.author).all()
   ```

3. **Session Management**: Proper session handling for concurrent requests

## Security Considerations
### Input Sanitization
```python
def sanitize_input(text: str) -> str:
    """Remove potentially harmful characters from input."""
    import html
    return html.escape(text.strip())
```

### SQL Injection Prevention
SQLAlchemy provides protection against SQL injection through parameterized queries:
```python
# Safe - SQLAlchemy handles parameterization
Book.query.filter(Book.title.contains(user_input)).all()

# Unsafe - Direct string concatenation (DO NOT USE)
f"SELECT * FROM books WHERE title = '{user_input}'"
```

### Database Security
1. **File Permissions**: Restrict access to database file
2. **Backup Strategy**: Regular database backups
3. **Connection Security**: Use SSL for remote database connections

## Deployment
### Production Database
Consider migrating from SQLite to:
- **PostgreSQL**: Advanced features and better concurrency
- **MySQL**: Widely used with good tooling
- **SQL Server**: Enterprise features (Windows environments)

### Environment Configuration
```python
import os

# Use environment variable for database URI
database_uri = os.environ.get('DATABASE_URL', 'sqlite:///books-collection.db')
if database_uri.startswith("postgres://"):
    database_uri = database_uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
```

## Project Purpose
This project demonstrates:
- Full CRUD operations with Flask and SQLAlchemy
- SQLite database integration and management
- Modern web application architecture
- Database schema design and modeling
- Form handling and validation patterns
- Bootstrap integration for responsive design
- Production-ready database practices
- Error handling and data validation techniques