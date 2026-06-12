# Coffee & WiFi Project

## Project Overview
A Flask web application for discovering and rating cafes with good coffee, WiFi, and power outlets. This platform allows users to browse, add, and rate cafes based on their amenities.

## Technologies Used
- Python 3.x
- Flask web framework
- Flask-Bootstrap5 (frontend styling)
- Flask-WTF (form handling)
- CSV data storage
- HTML/CSS with Bootstrap
- WTForms validation

## Project Structure
```
Part - Project 62 Coffee & wifi project/
├── main.py              # Flask application
├── cafe-data.csv        # Cafe database (CSV format)
├── requirements.txt     # Python dependencies
├── static/              # Static files (CSS, images)
├── templates/           # HTML templates
│   ├── index.html      # Home page
│   ├── add.html        # Add cafe form
│   └── cafes.html      # Cafe listings
└── README.md           # This file
```

## Features
- **Cafe Discovery**: Browse cafes with ratings for coffee, WiFi, and power outlets
- **Add New Cafes**: Form-based submission for new cafe entries
- **Rating System**: Emoji-based ratings (☕ for coffee, 💪 for WiFi, 🔌 for power)
- **Location Information**: Google Maps URLs for each cafe
- **Operating Hours**: Display opening and closing times
- **Responsive Design**: Mobile-friendly Bootstrap interface
- **Form Validation**: Server-side validation with WTForms

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

## Dependencies
Key packages required:
 - `flask`: Web framework
 - `flask-bootstrap5`: Bootstrap integration
 - `flask-wtf`: Form handling
 - `wtforms`: Form validation
 - `python-dotenv`: Environment variable management

## Cafe Rating System
### Coffee Rating (☕)
- 0: No coffee available
- 1-5: Number of coffee cups indicates quality

### WiFi Strength (💪)
- 0: No WiFi
- 1-5: Number of muscle emojis indicates signal strength

### Power Availability (🔌)
- 0: No power outlets
- 1-5: Number of plug emojis indicates outlet availability

## Database Schema (CSV)
The `cafe-data.csv` file contains:
- `Cafe Name`: Name of the cafe
- `Location`: Google Maps URL
- `Open`: Opening time (e.g., "8AM")
- `Close`: Closing time (e.g., "5:30PM")
- `Coffee`: Coffee rating (0-5)
- `Wifi`: WiFi rating (0-5)
- `Power`: Power outlet rating (0-5)

## Form Structure
The add cafe form includes:
1. **Cafe Name** (required): Text field
2. **Google Maps URL** (required): Valid URL field
3. **Opening Time** (required): Time format (e.g., "8AM")
4. **Closing Time** (required): Time format (e.g., "5:30PM")
5. **Coffee Rating** (required): Dropdown (0-5 with ☕ emojis)
6. **WiFi Rating** (required): Dropdown (0-5 with 💪 emojis)
7. **Power Rating** (required): Dropdown (0-5 with 🔌 emojis)

## Application Routes
- `/`: Home page with introduction
- `/add`: Add new cafe form (GET/POST)
- `/cafes`: Display all cafes in table format

## Code Structure
### Main Application (`main.py`)
```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Google Maps URL', validators=[DataRequired(), URL()])
    # ... additional form fields

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Save to CSV
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        cafes = list(csv_data)
    return render_template('cafes.html', cafes=cafes)
```

## CSV Data Handling
The application uses CSV for data persistence:
- **Reading**: `csv.reader()` for loading cafe data
- **Writing**: `csv.writer()` for adding new cafes
- **Structure**: Comma-delimited with UTF-8 encoding

## Form Validation
### Client-Side (HTML5)
```html
<input type="text" required>
<input type="url" required>
```

### Server-Side (WTForms)
```python
validators=[DataRequired(), URL()]
```

## Bootstrap Components Used
- **Navigation**: Bootstrap navbar for site navigation
- **Forms**: Bootstrap form styling and layout
- **Tables**: Responsive tables for cafe listings
- **Cards**: Content cards for displaying information
- **Buttons**: Styled form submission buttons

## Security Features
1. **CSRF Protection**: Flask-WTF provides Cross-Site Request Forgery protection
2. **Input Validation**: Both client and server-side validation
3. **Secret Key**: Application secret key for session security
4. **URL Validation**: Ensures Google Maps links are valid URLs

## Customization Options
### Change Rating Emojis
Modify the `rating_choices()` function in `main.py`:
```python
def rating_choices(emoji_char):
    return [(str(i), '✘' if i == 0 else emoji_char * i) for i in range(6)]
```

### Add New Cafe Attributes
1. Add new fields to `CafeForm` class
2. Update form template (`add.html`)
3. Modify CSV writing logic
4. Update table display in `cafes.html`

### Change Data Storage
To switch from CSV to database:
1. Implement SQLAlchemy models
2. Replace CSV read/write with database operations
3. Update form handling to use database sessions

## Error Handling
The application includes:
- Form validation errors displayed to users
- File I/O error handling for CSV operations
- 404 error page for invalid routes
- Input sanitization for user submissions

## Testing the Application
### Manual Testing
1. Start the Flask development server
2. Visit each route to ensure proper rendering
3. Test form submission with valid/invalid data
4. Verify CSV file updates after form submission
5. Check responsive design on different screen sizes

### Automated Testing (Example)
```python
import unittest
from main import app

class CafeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_cafes_page(self):
        response = self.app.get('/cafes')
        self.assertEqual(response.status_code, 200)
```

## Deployment Considerations
### Production Deployment
1. **Use Production Server**: Replace Flask development server with Gunicorn or uWSGI
2. **Environment Variables**: Store secret keys in environment variables
3. **Database Migration**: Consider moving from CSV to SQL database
4. **HTTPS**: Implement SSL/TLS for secure connections
5. **Caching**: Add caching for better performance

### Cloud Deployment Options
- **Heroku**: Simple Flask deployment with PostgreSQL
- **PythonAnywhere**: Python-focused hosting platform
- **AWS Elastic Beanstalk**: Scalable AWS deployment
- **DigitalOcean App Platform**: Managed app hosting

## Project Purpose
This project demonstrates:
- Full-stack web development with Flask
- Form handling and validation with WTForms
- CSV-based data persistence
- Bootstrap 5 integration for responsive design
- Practical web application patterns
- User input validation and security
- Data visualization with tables and ratings