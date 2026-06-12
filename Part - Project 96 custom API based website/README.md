# Brewery Finder - Custom API Website

A Flask web application that searches for breweries by city using the Open Brewery DB public API.

## Overview

This project is a simple yet functional web application that allows users to search for breweries in any city using the Open Brewery DB API. It demonstrates how to integrate external APIs into a Flask application and display the results in a clean, responsive UI.

## Features

- **API Integration**: Uses Open Brewery DB free public API
- **City Search**: Search breweries by city name
- **Results Display**: Shows brewery name, type, address, and website
- **Error Handling**: Graceful handling of API errors and empty results
- **Single-File Design**: All code contained in one Python file
- **Embedded Template**: HTML template stored as a string in Python

## Tech Stack

- **Backend**: Flask (Python web framework)
- **HTTP Requests**: requests library
- **External API**: Open Brewery DB (https://www.openbrewerydb.org/)
- **Templating**: Jinja2 (embedded in Python file)

## Project Structure

```
Part - Project 96 custom API based website/
├── api_website.py    # Main application (includes template)
└── README.md         # This file
```

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
   pip install flask requests
   ```

4. **Run the application**:
   ```bash
   python api_website.py
   ```

5. **Access in browser**:
   Navigate to `http://localhost:5000`

## How It Works

### API Endpoint

**URL**: `https://api.openbrewerydb.org/v1/breweries`

**Parameters**:
- `by_city`: City name to search
- `per_page`: Number of results (max 50)

### API Request

```python
url = "https://api.openbrewerydb.org/v1/breweries"
params = {"by_city": city, "per_page": 25}
response = requests.get(url, params=params, timeout=10)
breweries = response.json()
```

### API Response Format

```json
[
  {
    "id": 1,
    "name": "Sample Brewery",
    "brewery_type": "micro",
    "street": "123 Main St",
    "city": "Denver",
    "state": "Colorado",
    "postal_code": "80202",
    "website_url": "https://example.com"
  }
]
```

### Embedded HTML Template

```python
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Brewery Finder</title>
  <style>
    /* CSS styles */
  </style>
</head>
<body>
  <!-- HTML content with Jinja2 template variables -->
</body>
</html>
"""
```

The template uses Jinja2 syntax for dynamic content:
- `{{ city }}` - Display search term
- `{{ error }}` - Show error messages
- `{% for b in breweries %}` - Loop through results

### Route Handler

```python
@app.route("/")
def index():
    city = request.args.get("city", "").strip()
    breweries = []
    error = None

    if city:
        try:
            url = "https://api.openbrewerydb.org/v1/breweries"
            params = {"by_city": city, "per_page": 25}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            breweries = response.json()
        except requests.RequestException as exc:
            error = f"Could not fetch breweries: {exc}"

    return render_template_string(TEMPLATE, city=city, breweries=breweries, error=error)
```

## Usage

1. Open the application in a browser
2. Enter a city name in the search box (e.g., "denver", "new york", "san diego")
3. Click "Search" button
4. View the list of breweries found

### Sample Searches

| City | Expected Results |
|------|------------------|
| denver | Multiple breweries in Denver, Colorado |
| new york | Breweries in New York City |
| san diego | San Diego area breweries |
| seattle | Seattle area breweries |

## Template Features

### Search Form

```html
<form method="get">
  <label>
    City:
    <input type="text" name="city" value="{{ city or '' }}" placeholder="e.g. denver">
  </label>
  <button type="submit">Search</button>
</form>
```

### Error Display

```html
{% if error %}
  <p style="color: red;">{{ error }}</p>
{% endif %}
```

### Results Loop

```html
{% for b in breweries %}
  <div class="brewery">
    <h2>{{ b.name }}</h2>
    <div class="meta">{{ b.brewery_type | capitalize }} brewery</div>
    <p>
      {{ b.street or 'Address not available' }}<br>
      {{ b.city }}, {{ b.state }} {{ b.postal_code }}
    </p>
    {% if b.website_url %}
      <p><a href="{{ b.website_url }}" target="_blank">Visit website</a></p>
    {% endif %}
  </div>
{% endfor %}
```

## Customization

### Change API Endpoint

```python
# Use different API
url = "https://api.openbrewerydb.org/v1/breweries/search"
params = {"query": city}
```

### Add More Filters

```python
params = {
    "by_city": city,
    "per_page": 50,
    "by_type": "micro"  # Filter by brewery type
}
```

### Change Number of Results

```python
params = {"by_city": city, "per_page": 50}  # Default: 25, Max: 50
```

### Add Bootstrap Styling

```python
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <!-- Add Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- Use Bootstrap classes -->
</body>
</html>
"""
```

### Save Template to File

For larger projects, move the template to a separate file:

```python
# Instead of render_template_string
return render_template("index.html", city=city, breweries=breweries, error=error)
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| "Could not fetch breweries" | Network issue or API down | Check internet, try again later |
| "No breweries found" | City has no breweries in database | Try a different city |
| Timeout | API took too long | Increase timeout value |

## API Documentation

The Open Brewery DB API provides additional endpoints:

- `GET /v1/breweries` - List all breweries
- `GET /v1/breweries/search?query={term}` - Search by name
- `GET /v1/breweries/{id}` - Get single brewery
- `GET /v1/breweries/autocomplete?by_name={name}` - Autocomplete

### Brewery Types

| Type | Description |
|------|-------------|
| micro | Most craft breweries |
| brewpub | Brewpub/restaurant |
| contract | Contract brewery |
| regional | Regional brewery |
| large | Large industrial brewery |
| planning | In planning |
| bar | Bar/tavern |
| closed | Closed permanently |

## Testing

```bash
# Test API directly
curl "https://api.openbrewerydb.org/v1/breweries?by_city=denver&per_page=5"
```

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)