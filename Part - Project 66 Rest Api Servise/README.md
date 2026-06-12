# REST API Service for Cafe Management

## Project Overview
A comprehensive RESTful API service built with Flask for managing cafe information. This project implements full CRUD operations with proper HTTP methods, JSON responses, and database integration following REST API best practices.

## Technologies Used
- Python 3.x
- Flask web framework
- SQLAlchemy ORM
- SQLite database
- JSON serialization/deserialization
- HTTP methods (GET, POST, PATCH, DELETE)
- REST API design principles
- Error handling and status codes

## Project Structure
```
Part - Project 66 Rest Api Servise/
├── main.py              # Flask REST API application
├── cafes.db            # SQLite database file
├── requirements.txt    # Python dependencies
├── templates/          # HTML documentation (optional)
└── README.md          # This file
```

## Features
- **Full REST Implementation**: Proper HTTP methods and status codes
- **CRUD Operations**: Create, Read, Update, Delete for cafe resources
- **JSON API**: Clean JSON request/response format
- **Search & Filter**: Query parameters for filtering results
- **Random Endpoint**: Get random cafe from database
- **Error Handling**: Comprehensive error responses
- **Database Integration**: SQLAlchemy with SQLite backend
- **API Documentation**: Well-documented endpoints

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

## Running the API Service
```bash
python main.py
```
The API will be available at: `http://127.0.0.1:5000`

## Database Schema
### Cafe Table Structure
```sql
CREATE TABLE cafes (
    id INTEGER PRIMARY KEY,
    name VARCHAR(250) UNIQUE NOT NULL,
    map_url VARCHAR(500) NOT NULL,
    img_url VARCHAR(500) NOT NULL,
    location VARCHAR(250) NOT NULL,
    seats VARCHAR(250) NOT NULL,
    has_toilet BOOLEAN NOT NULL,
    has_wifi BOOLEAN NOT NULL,
    has_sockets BOOLEAN NOT NULL,
    can_take_calls BOOLEAN NOT NULL,
    coffee_price VARCHAR(250)
);
```

### SQLAlchemy Model
```python
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
```

## API Endpoints

### 1. **GET /** - API Documentation
- **Description**: Returns API documentation and available endpoints
- **Response**: HTML documentation page
- **Status Code**: 200 OK

### 2. **GET /random** - Random Cafe
- **Description**: Returns a random cafe from the database
- **Response**: JSON object with cafe details
- **Status Code**: 200 OK
- **Example Response**:
```json
{
  "cafe": {
    "id": 1,
    "name": "Cafe Ronde",
    "map_url": "https://maps.google.com/?q=Cafe+Ronde",
    "img_url": "https://images.unsplash.com/photo-1501339847302-ac716a8b2931",
    "location": "Paris, France",
    "seats": "30+",
    "has_toilet": true,
    "has_wifi": true,
    "has_sockets": true,
    "can_take_calls": true,
    "coffee_price": "2.50"
  }
}
```

### 3. **GET /all** - All Cafes
- **Description**: Returns all cafes in the database
- **Response**: JSON array of cafe objects
- **Status Code**: 200 OK
- **Query Parameters**:
  - `loc`: Filter by location (optional)

### 4. **GET /search** - Search Cafes
- **Description**: Search cafes by location
- **Parameters**: `loc` (query parameter)
- **Response**: JSON array of matching cafes
- **Status Code**: 200 OK (found), 404 Not Found (no results)
- **Example Request**: `GET /search?loc=London`

### 5. **POST /add** - Add New Cafe
- **Description**: Add a new cafe to the database
- **Request Body**: JSON object with cafe details
- **Response**: JSON success message
- **Status Code**: 201 Created
- **Required Fields**: All cafe attributes except id
- **Example Request**:
```json
{
  "name": "New Cafe",
  "map_url": "https://maps.google.com/?q=New+Cafe",
  "img_url": "https://example.com/image.jpg",
  "location": "New York, USA",
  "seats": "20-30",
  "has_toilet": true,
  "has_wifi": true,
  "has_sockets": false,
  "can_take_calls": true,
  "coffee_price": "3.50"
}
```

### 6. **PATCH /update-price/<int:cafe_id>** - Update Coffee Price
- **Description**: Update coffee price for a specific cafe
- **Request Body**: JSON with `new_price` field
- **Response**: JSON success message
- **Status Code**: 200 OK (updated), 404 Not Found (cafe not found)
- **Example Request**: `PATCH /update-price/1`
```json
{
  "new_price": "3.75"
}
```

### 7. **DELETE /report-closed/<int:cafe_id>** - Report Cafe Closed
- **Description**: Delete a cafe (requires API key for authorization)
- **Parameters**: `api-key` (query parameter for authorization)
- **Response**: JSON success/failure message
- **Status Code**: 200 OK (deleted), 403 Forbidden (invalid API key), 404 Not Found
- **Example Request**: `DELETE /report-closed/1?api-key=TopSecretAPIKey`

## Code Structure
### Main Application (`main.py`)
```python
import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

# Database configuration
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Helper function to convert cafe to dictionary
def cafe_to_dict(cafe):
    return {
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
    }

# Seed database with sample data if empty
def seed_cafes_if_empty():
    if db.session.execute(db.select(Cafe)).first():
        return
    
    db.session.add_all([
        Cafe(
            name="Cafe Ronde",
            map_url="https://maps.google.com/?q=Cafe+Ronde",
            img_url="https://images.unsplash.com/photo-1501339847302-ac716a8b2931",
            location="Paris, France",
            seats="30+",
            has_toilet=True,
            has_wifi=True,
            has_sockets=True,
            can_take_calls=True,
            coffee_price="2.50",
        ),
        # ... more sample cafes
    ])
    db.session.commit()
```

## API Endpoint Implementations
### Random Cafe Endpoint
```python
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    
    if not all_cafes:
        return jsonify(error={"Not Found": "No cafes in database"}), 404
    
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=cafe_to_dict(random_cafe))
```

### Search Endpoint
```python
@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    
    if not location:
        return jsonify(error={"Bad Request": "Location parameter required"}), 400
    
    result = db.session.execute(
        db.select(Cafe).where(Cafe.location.contains(location))
    )
    cafes = result.scalars().all()
    
    if not cafes:
        return jsonify(error={"Not Found": f"No cafes found in {location}"}), 404
    
    return jsonify(cafes=[cafe_to_dict(cafe) for cafe in cafes])
```

### Add Cafe Endpoint
```python
@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.json.get("name"),
            map_url=request.json.get("map_url"),
            img_url=request.json.get("img_url"),
            location=request.json.get("location"),
            seats=request.json.get("seats"),
            has_toilet=bool(request.json.get("has_toilet")),
            has_wifi=bool(request.json.get("has_wifi")),
            has_sockets=bool(request.json.get("has_sockets")),
            can_take_calls=bool(request.json.get("can_take_calls")),
            coffee_price=request.json.get("coffee_price"),
        )
        
        db.session.add(new_cafe)
        db.session.commit()
        
        return jsonify(response={"success": "Successfully added the new cafe"}), 201
    
    except Exception as e:
        return jsonify(error={"Bad Request": str(e)}), 400
```

### Update Price Endpoint
```python
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.json.get("new_price")
    
    if not new_price:
        return jsonify(error={"Bad Request": "New price required"}), 400
    
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": f"No cafe with id {cafe_id}"}), 404
    
    cafe.coffee_price = new_price
    db.session.commit()
    
    return jsonify(response={"success": "Successfully updated the price"})
```

### Delete Cafe Endpoint
```python
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "Invalid API key"}), 403
    
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": f"No cafe with id {cafe_id}"}), 404
    
    db.session.delete(cafe)
    db.session.commit()
    
    return jsonify(response={"success": "Successfully deleted the cafe"})
```

## Error Handling
### Custom Error Responses
```python
@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error={"Not Found": "The requested resource was not found"}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify(error={"Bad Request": "Invalid request parameters"}), 400

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify(error={"Internal Server Error": "Something went wrong"}), 500
```

### Validation Functions
```python
def validate_cafe_data(data):
    """Validate cafe data before processing."""
    required_fields = [
        'name', 'map_url', 'img_url', 'location', 'seats',
        'has_toilet', 'has_wifi', 'has_sockets', 'can_take_calls'
    ]
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Validate URL formats
    url_fields = ['map_url', 'img_url']
    for field in url_fields:
        if field in data and not data[field].startswith(('http://', 'https://')):
            return False, f"Invalid URL format for {field}"
    
    return True, "Validation passed"
```

## API Documentation
### Using Swagger/OpenAPI (Optional Extension)
```python
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Cafe API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

## Testing the API
### Using cURL Commands
```bash
# Get random cafe
curl http://127.0.0.1:5000/random

# Search cafes in London
curl "http://127.0.0.1:5000/search?loc=London"

# Add new cafe
curl -X POST http://127.0.0.1:5000/add \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Cafe", "map_url": "https://maps.google.com/?q=Test", ...}'

# Update coffee price
curl -X PATCH http://127.0.0.1:5000/update-price/1 \
  -H "Content-Type: application/json" \
  -d '{"new_price": "4.00"}'

# Delete cafe (with API key)
curl -X DELETE "http://127.0.0.1:5000/report-closed/1?api-key=TopSecretAPIKey"
```

### Using Python Requests Library
```python
import requests

BASE_URL = "http://127.0.0.1:5000"

# Get random cafe
response = requests.get(f"{BASE_URL}/random")
cafe = response.json()["cafe"]

# Add new cafe
new_cafe = {
    "name": "Python Cafe",
    "map_url": "https://maps.google.com/?q=Python+Cafe",
    # ... other fields
}
response = requests.post(f"{BASE_URL}/add", json=new_cafe)
print(response.status_code, response.json())
```

## Authentication & Authorization
### API Key Implementation
```python
API_KEYS = {
    "admin": "TopSecretAPIKey",
    "user1": "UserSecretKey123",
    "user2": "AnotherSecretKey456"
}

def require_api_key(f):
    """Decorator to require API key for certain endpoints."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('api-key')
        
        if not api_key:
            return jsonify(error={"Unauthorized": "API key required"}), 401
        
        if api_key not in API_KEYS.values():
            return jsonify(error={"Forbidden": "Invalid API key"}), 403
        
        return f(*args, **kwargs)
    return decorated_function

@app.route("/protected-endpoint")
@require_api_key
def protected_endpoint():
    return jsonify(message="Access granted")
```

## Rate Limiting
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/api/search")
@limiter.limit("10 per minute")
def search_endpoint():
    # Limited to 10 requests per minute
    pass
```

## Caching
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/random")
@cache.cached(timeout=60)  # Cache for 60 seconds
def get_random_cafe():
    # Database query
    pass
```

## Database Optimization
### Indexing for Performance
```python
class Cafe(db.Model):
    # ... existing fields ...
    
    __table_args__ = (
        db.Index('idx_cafe_location', 'location'),
        db.Index('idx_cafe_name', 'name'),
        db.Index('idx_cafe_amenities', 'has_wifi', 'has_sockets', 'has_toilet'),
    )
```

### Query Optimization
```python
# Efficient query with only needed fields
def get_cafe_summaries():
    return db.session.query(
        Cafe.id,
        Cafe.name,
        Cafe.location,
        Cafe.coffee_price
    ).filter(
        Cafe.has_wifi == True,
        Cafe.has_sockets == True
    ).order_by(Cafe.name).all()
```

## Deployment Considerations
### Production Configuration
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Security
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    
    # API configuration
    API_KEYS = os.environ.get('API_KEYS', '').split(',')

app.config.from_object(Config)
```

### Docker Configuration
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

## Project Purpose
This project demonstrates:
- RESTful API design principles and best practices
- Full CRUD operations with proper HTTP methods
- JSON API development with Flask
- Database integration with SQLAlchemy
- Error handling and status code management
- API authentication and authorization
- Rate limiting and caching strategies
- Production-ready API deployment patterns
- Comprehensive testing and documentation