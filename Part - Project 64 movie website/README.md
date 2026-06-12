# Movie Database Website

## Project Overview
A comprehensive movie database website built with Flask and SQLAlchemy that allows users to manage a personal movie collection with ratings, reviews, and rankings. This project demonstrates advanced web application patterns with database relationships and user interfaces.

## Technologies Used
- Python 3.x
- Flask web framework
- SQLAlchemy ORM
- SQLite database
- Flask-Bootstrap5 (frontend framework)
- Flask-WTF (form handling)
- WTForms validation
- HTML/CSS/JavaScript
- Responsive web design

## Project Structure
```
Part - Project 64 movie website/
├── main.py              # Flask application with routes
├── movies.db           # SQLite database file
├── requirements.txt    # Python dependencies
├── static/             # Static assets (CSS, images, JS)
├── templates/          # HTML templates
│   ├── index.html     # Home page with movie rankings
│   ├── add.html       # Add new movie form
│   ├── edit.html      # Edit movie rating/review
│   └── select.html    # Movie selection interface
└── README.md          # This file
```

## Features
- **Movie Management**: Full CRUD operations for movie collection
- **Rating System**: Decimal-based ratings (0.0-10.0) with reviews
- **Ranking System**: Numeric ranking for top movie lists
- **Image Support**: Movie poster URLs with responsive display
- **Search & Filter**: Database queries with sorting options
- **Form Validation**: Comprehensive server-side validation
- **Responsive Design**: Mobile-friendly Bootstrap interface
- **Database Relations**: Proper SQLAlchemy model relationships

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
### Movie Table Structure
```sql
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) UNIQUE NOT NULL,
    year INTEGER NOT NULL,
    description TEXT NOT NULL,
    rating FLOAT,
    ranking INTEGER,
    review VARCHAR(250),
    img_url VARCHAR(500) NOT NULL DEFAULT ''
);
```

### SQLAlchemy Model
```python
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False, default="")
```

## Application Routes
- `/`: Home page displaying ranked movies
- `/add`: Add new movie form (GET/POST)
- `/edit`: Edit movie rating and review (GET/POST)
- `/select`: Movie selection interface
- `/delete/<int:movie_id>`: Delete movie with confirmation

## Code Structure
### Main Application (`main.py`)
```python
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Database initialization
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)
```

## Movie Management Features
### Add New Movie
```python
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Year e.g. 2022", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data.strip(),
            year=int(form.year.data),
            description=form.description.data.strip(),
            img_url="",  # Default empty, can be updated later
            rating=None,
            ranking=None,
            review=None,
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)
```

### Edit Movie Rating
```python
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data.strip()
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit.html", form=form, movie=movie)
```

### Movie Ranking System
```python
def update_movie_rankings():
    """Update movie rankings based on ratings."""
    movies = Movie.query.filter(Movie.rating.isnot(None))\
                       .order_by(Movie.rating.desc())\
                       .all()
    
    for rank, movie in enumerate(movies, start=1):
        movie.ranking = rank
    
    db.session.commit()
```

## Database Operations
### Advanced Queries
```python
# Get top 10 rated movies
top_movies = Movie.query.filter(Movie.rating.isnot(None))\
                        .order_by(Movie.rating.desc())\
                        .limit(10)\
                        .all()

# Search movies by year range
recent_movies = Movie.query.filter(Movie.year >= 2020)\
                           .order_by(Movie.year.desc())\
                           .all()

# Get movies without ratings
unrated_movies = Movie.query.filter(Movie.rating.is_(None))\
                            .order_by(Movie.title)\
                            .all()

# Complex query with multiple conditions
action_movies = Movie.query.filter(
    Movie.description.ilike('%action%'),
    Movie.rating >= 7.0,
    Movie.year >= 2010
).order_by(Movie.rating.desc()).all()
```

### Database Transactions
```python
from sqlalchemy.exc import SQLAlchemyError

def safe_movie_update(movie_id, updates):
    """Safely update movie with transaction rollback on error."""
    try:
        movie = db.session.get(Movie, movie_id)
        if not movie:
            return False, "Movie not found"
        
        for key, value in updates.items():
            if hasattr(movie, key):
                setattr(movie, key, value)
        
        db.session.commit()
        return True, "Movie updated successfully"
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
```

## Form Validation
### Custom Validators
```python
from wtforms.validators import ValidationError

def validate_year(form, field):
    """Validate movie year is reasonable."""
    try:
        year = int(field.data)
        if year < 1888:  # First movie year
            raise ValidationError("Year is too early for movies")
        if year > 2100:  # Reasonable future limit
            raise ValidationError("Year is too far in the future")
    except ValueError:
        raise ValidationError("Please enter a valid year")

def validate_rating(form, field):
    """Validate rating is between 0 and 10."""
    try:
        rating = float(field.data)
        if rating < 0 or rating > 10:
            raise ValidationError("Rating must be between 0 and 10")
    except ValueError:
        raise ValidationError("Please enter a valid number")
```

### Form Classes
```python
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[
        DataRequired(),
        Length(min=1, max=250, message="Title must be 1-250 characters")
    ])
    year = StringField("Year", validators=[
        DataRequired(),
        validate_year
    ])
    description = StringField("Description", validators=[
        DataRequired(),
        Length(min=10, max=1000, message="Description must be 10-1000 characters")
    ])
    img_url = StringField("Poster Image URL", validators=[
        URL(message="Please enter a valid URL"),
        Optional()
    ])
    submit = SubmitField("Add Movie")
```

## User Interface Components
### Movie Card Component
```html
<div class="movie-card card mb-4">
    <div class="row g-0">
        <div class="col-md-4">
            <img src="{{ movie.img_url or '/static/default-poster.jpg' }}" 
                 class="img-fluid rounded-start" 
                 alt="{{ movie.title }} poster">
        </div>
        <div class="col-md-8">
            <div class="card-body">
                <h5 class="card-title">{{ movie.title }} ({{ movie.year }})</h5>
                
                {% if movie.rating %}
                <div class="rating-badge">
                    <span class="badge bg-primary">Rating: {{ movie.rating }}/10</span>
                    {% if movie.ranking %}
                    <span class="badge bg-success">Rank: #{{ movie.ranking }}</span>
                    {% endif %}
                </div>
                {% endif %}
                
                <p class="card-text">{{ movie.description[:200] }}...</p>
                
                {% if movie.review %}
                <div class="review-section">
                    <h6>Your Review:</h6>
                    <p class="review-text">{{ movie.review }}</p>
                </div>
                {% endif %}
                
                <div class="action-buttons">
                    <a href="{{ url_for('rate_movie', id=movie.id) }}" 
                       class="btn btn-warning btn-sm">Edit Rating</a>
                    <a href="#" class="btn btn-danger btn-sm" 
                       data-bs-toggle="modal" 
                       data-bs-target="#deleteModal{{ movie.id }}">Delete</a>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Responsive Table View
```html
<div class="table-responsive">
    <table class="table table-hover table-striped">
        <thead class="table-dark">
            <tr>
                <th scope="col">Rank</th>
                <th scope="col">Title</th>
                <th scope="col">Year</th>
                <th scope="col">Rating</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for movie in movies %}
            <tr>
                <td>{{ movie.ranking or 'N/A' }}</td>
                <td>
                    <strong>{{ movie.title }}</strong>
                    {% if movie.review %}
                    <br><small class="text-muted">{{ movie.review[:50] }}...</small>
                    {% endif %}
                </td>
                <td>{{ movie.year }}</td>
                <td>
                    {% if movie.rating %}
                    <span class="badge rounded-pill bg-primary">{{ movie.rating }}/10</span>
                    {% else %}
                    <span class="badge rounded-pill bg-secondary">Not Rated</span>
                    {% endif %}
                </td>
                <td>
                    <div class="btn-group btn-group-sm">
                        <a href="{{ url_for('rate_movie', id=movie.id) }}" 
                           class="btn btn-outline-primary">Rate</a>
                        <a href="#" class="btn btn-outline-danger" 
                           data-bs-toggle="modal" 
                           data-bs-target="#deleteModal{{ movie.id }}">Delete</a>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```

## API Integration (Advanced Feature)
### External Movie API
```python
import requests
from typing import Optional, Dict

class MovieAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
    
    def search_movies(self, query: str) -> Optional[Dict]:
        """Search movies using external API."""
        try:
            response = requests.get(
                f"{self.base_url}/search/movie",
                params={
                    "api_key": self.api_key,
                    "query": query,
                    "language": "en-US",
                    "page": 1
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
    
    def get_movie_details(self, movie_id: int) -> Optional[Dict]:
        """Get detailed movie information."""
        try:
            response = requests.get(
                f"{self.base_url}/movie/{movie_id}",
                params={
                    "api_key": self.api_key,
                    "language": "en-US"
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
```

## Performance Optimization
### Database Indexing
```python
class Movie(db.Model):
    # ... existing fields ...
    
    __table_args__ = (
        db.Index('idx_movie_rating', 'rating'),
        db.Index('idx_movie_year', 'year'),
        db.Index('idx_movie_title', 'title'),
        db.Index('idx_movie_ranking', 'ranking'),
    )
```

### Query Optimization
```python
# Efficient query with only needed fields
movies = db.session.query(
    Movie.id,
    Movie.title,
    Movie.year,
    Movie.rating,
    Movie.ranking
).filter(Movie.rating.isnot(None))\
 .order_by(Movie.rating.desc())\
 .limit(20)\
 .all()

# Use joinedload for related data (if adding relationships)
from sqlalchemy.orm import joinedload
movies = Movie.query.options(joinedload(Movie.reviews))\
                    .filter(Movie.rating >= 7.0)\
                    .all()
```

## Testing
### Unit Tests
```python
import unittest
from main import app, db, Movie

class MovieTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        with app.app_context():
            db.create_all()
            # Add test data
            test_movie = Movie(
                title="Test Movie",
                year=2023,
                description="Test description",
                rating=8.5,
                ranking=1,
                review="Great movie!"
            )
            db.session.add(test_movie)
            db.session.commit()
    
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Movie', response.data)
    
    def test_add_movie(self):
        response = self.app.post('/add', data={
            'title': 'New Test Movie',
            'year': '2024',
            'description': 'Another test movie'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
    
    def test_movie_count(self):
        with app.app_context():
            count = Movie.query.count()
            self.assertEqual(count, 1)  # Only our test movie
```

## Deployment Considerations
### Production Configuration
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

app.config.from_object(Config)
```

### Database Migration (Alembic)
```python
# Add database migrations for production
# alembic init migrations
# Configure alembic.ini and migrations/env.py
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head
```

## Project Purpose
This project demonstrates:
- Advanced Flask web application development
- SQLAlchemy ORM with complex database operations
- Comprehensive form handling and validation
- Bootstrap 5 integration for modern UI
- Movie database management system
- Ranking and rating algorithms
- Production-ready application patterns
- API integration concepts
- Performance optimization techniques
- Testing and deployment strategies