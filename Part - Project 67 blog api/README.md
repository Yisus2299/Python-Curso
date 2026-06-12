# Blog API - Flask Blog Application

A full-featured blogging platform built with Flask, featuring database-backed blog posts with rich text editing capabilities.

## Overview

This project is a CRUD-style blog application that allows users to create, read, update, and delete blog posts. It uses Flask-SQLAlchemy for database management and Flask-CKEditor for rich text content editing in blog posts.

## Features

- **Create Blog Posts**: Write new blog entries with title, subtitle, author, image URL, and rich text body
- **View All Posts**: Browse all blog posts on the home page
- **Read Individual Posts**: View full blog posts with complete content
- **Edit Posts**: Modify existing blog posts
- **Delete Posts**: Remove blog posts from the database
- **Rich Text Editing**: CKEditor integration for formatting blog content

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Forms**: Flask-WTF for form handling and validation
- **Rich Text**: CKEditor (via flask-ckeditor)
- **UI Framework**: Bootstrap 5 (via flask-bootstrap5)
- **Date Handling**: Python datetime module

## Project Structure

```
Part - Project 67 blog api/
├── main.py                 # Main Flask application
├── templates/              # HTML templates
│   ├── index.html         # Home page - list all posts
│   ├── post.html          # Single post view
│   ├── make-post.html     # Create/edit post form
│   ├── about.html         # About page
│   └── contact.html       # Contact page
├── static/                # Static assets
├── instance/              # SQLite database location
├── requirements.txt       # Python dependencies
└── requirements_3.13.txt  # Python 3.13 specific dependencies
```

## Database Schema

### BlogPost Table

| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Unique identifier |
| title | String(250) | Blog post title (unique) |
| subtitle | String(250) | Post subtitle |
| date | String(250) | Publication date |
| body | Text | Full blog content (HTML) |
| author | String(250) | Author name |
| img_url | String(250) | Featured image URL |

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
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access in browser**:
   Navigate to `http://localhost:5003`

## How It Works

### Routing

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all blog posts |
| `/post/<id>` | GET | View a specific post |
| `/new-post` | GET/POST | Create a new post |
| `/edit-post/<id>` | GET/POST | Edit an existing post |
| `/delete/<id>` | GET | Delete a post |
| `/about` | GET | About page |
| `/contact` | GET | Contact page |

### Form Handling

The `CreatePostForm` class uses WTForms validators:
- `DataRequired()`: Ensures field is not empty
- `URL()`: Validates image URL format

### Database Operations

- **Read**: `db.session.execute(db.select(BlogPost))`
- **Create**: `db.session.add(new_post)` + `db.session.commit()`
- **Update**: Modify object properties + `db.session.commit()`
- **Delete**: `db.session.delete(post)` + `db.session.commit()`

## Customization

### Adding New Fields

1. Add field to `BlogPost` model class
2. Update `CreatePostForm` in main.py
3. Update template to include new field
4. Run `db.create_all()` again (or use migrations)

### Changing Database

To use a different database (e.g., PostgreSQL), modify the SQLAlchemy URI:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/blog'
```

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)