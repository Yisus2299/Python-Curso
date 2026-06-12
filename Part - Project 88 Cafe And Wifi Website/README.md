# Cafe & WiFi Website

A Flask web application for finding cafes with WiFi, power outlets, and other amenities. Users can browse, add, and delete cafe listings.

## Overview

This project is a directory website that helps people find cafes with WiFi and other amenities. Users can browse cafes by location, view details about each cafe's facilities, add new cafes to the database, and remove listings.

## Features

- **Browse Cafes**: View all cafes or filter by location
- **Location Filter**: Dropdown to filter cafes by city/location
- **Add Cafe**: Form to add new cafes with all amenities
- **Delete Cafe**: Remove cafe listings from the database
- **Cafe Details**: Name, map URL, image, location, seating capacity
- **Amenities**: WiFi, sockets, toilet, calls support

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Templating**: Jinja2 (built into Flask)
- **Styling**: Bootstrap (via templates)

## Project Structure

```
Part - Project 88 Cafe And Wifi Website/
├── website.py              # Main Flask application
├── cafes.db                # SQLite database
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── index.html         # Home page - list cafes
│   ├── add.html           # Add new cafe form
│   └── delete.html        # Delete confirmation
└── static/                # Static assets
```

## Database Schema

### Cafe Table

| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Unique identifier |
| name | String(250) | Cafe name (unique) |
| map_url | String(500) | Google Maps link |
| img_url | String(500) | Cafe image URL |
| location | String(250) | City/location |
| seats | String(250) | Number of seats |
| has_toilet | Boolean | Has bathroom |
| has_wifi | Boolean | Has WiFi |
| has_sockets | Boolean | Has power outlets |
| can_take_calls | Boolean | Good for calls |
| coffee_price | String(250) | Price of coffee |

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
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**:
   ```bash
   python website.py
   ```

5. **Access in browser**:
   Navigate to `http://localhost:5000`

## How It Works

### Main Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | List all cafes (with optional location filter) |
| `/add` | GET/POST | Add a new cafe |
| `/delete/<id>` | GET/POST | Delete a cafe |

### Home Page (`/`)

1. Get optional `loc` query parameter for filtering
2. Query database for cafes (filtered or all)
3. Get unique locations for dropdown
4. Render template with cafes and locations

```python
@app.route("/")
def home():
    loc = request.args.get("loc", "").strip()
    stmt = select(Cafe).order_by(Cafe.name)
    if loc:
        stmt = stmt.where(Cafe.location == loc)
    cafes = db.session.execute(stmt).scalars().all()
    return render_template("index.html", cafes=cafes, ...)
```

### Add Cafe (`/add`)

1. Display form on GET
2. On POST: extract form data, create Cafe object, save to database
3. Redirect to home page

### Delete Cafe (`/delete/<id>`)

1. Get cafe by ID from database
2. Display confirmation on GET
3. On POST: delete from database, redirect to home

## Form Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | text | Yes | Cafe name |
| map_url | url | Yes | Google Maps link |
| img_url | url | Yes | Image URL |
| location | text | Yes | City/location |
| seats | text | Yes | Seating capacity |
| wifi | checkbox | No | Has WiFi |
| sockets | checkbox | No | Has power outlets |
| toilet | checkbox | No | Has bathroom |
| calls | checkbox | No | Good for calls |
| coffee_price | text | No | Price of coffee |

## Template Variables

### index.html
- `cafes`: List of Cafe objects to display
- `locations`: List of unique locations for filter
- `selected_loc`: Currently selected location (if any)

## Adding Sample Data

The database starts empty. To add cafes, use the web interface at `/add`.

Example cafe entry:
- **Name**: "Coffee Central"
- **Map URL**: https://maps.google.com/...
- **Image URL**: https://example.com/coffee.jpg
- **Location**: New York
- **Seats**: 50
- **Amenities**: WiFi ✓, Sockets ✓, Toilet ✓

## Database Management

### Creating the Database
The database is automatically created when you run the app for the first time (SQLAlchemy creates it based on the model).

### Accessing the Database
You can use any SQLite viewer to inspect the database:
```bash
sqlite3 cafes.db
```

## Customization

### Adding New Fields

1. Add field to Cafe model class in website.py
2. Update the HTML form in templates/add.html
3. Update the display in templates/index.html

### Changing Database Location

Modify the SQLAlchemy URI in website.py:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///path/to/your/db.db"
```

### Styling

The templates use Bootstrap for styling. Modify the HTML templates to change colors, layout, or add additional features.

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)