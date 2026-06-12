# API Endpoints Practice

## Project Overview
A collection of Python scripts that demonstrate working with various public APIs, including ISS location tracking and sunrise/sunset data retrieval. This project focuses on API integration and endpoint consumption.

## Technologies Used
- Python 3.x
- Requests library (HTTP client)
- datetime module (time manipulation)
- dotenv (environment variable management)

## Project Structure
```
Part - Project 33 Endpoints/
├── endpoint_practice.py     # Main API practice script
├── main_ISS_email_test.py   # ISS location with email notifications
├── .env                     # Environment variables (not in repo)
└── README.md               # This file
```

## Features
- International Space Station (ISS) real-time location tracking
- Sunrise/sunset data retrieval for specific coordinates
- API endpoint consumption and response parsing
- Time zone and datetime manipulation
- Geographic coordinate handling

## Available APIs
1. **ISS Location API** (`http://api.open-notify.org/iss-now.json`)
   - Real-time ISS position data
   - Returns latitude and longitude coordinates

2. **Sunrise-Sunset API** (`https://api.sunrise-sunset.org/json`)
   - Sunrise, sunset, and solar noon times
   - Supports formatted and ISO 8601 time formats
   - Geographic coordinate based queries

## How to Run
1. Install required dependencies:
   ```
   pip install requests python-dotenv
   ```
2. Run the scripts:
   ```
   python endpoint_practice.py
   ```
   or
   ```
   python main_ISS_email_test.py
   ```

## Code Examples

### ISS Location Tracking
```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_position = {
    "latitude": data["iss_position"]["latitude"],
    "longitude": data["iss_position"]["longitude"],
}
print(iss_position)
```

### Sunrise-Sunset Data
```python
import requests
from datetime import datetime

response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params={"lat": 36.7201600, "lng": -4.4203400, "formatted": 0},
)
response.raise_for_status()
data = response.json()

solar_noon = data["results"]["solar_noon"].split("T")[1].split(":")[0]
print(f"Solar noon hour: {solar_noon}")
```

## Configuration
- Modify coordinates in the scripts for different locations
- Customize time formatting as needed
- Add error handling for network issues

## API Rate Limits
- ISS API: Generally no rate limits
- Sunrise-Sunset API: Reasonable use expected
- Always check API documentation for current limits

## Error Handling
The scripts include:
- HTTP error status checking
- Network timeout handling
- JSON parsing validation
- Coordinate validation

## Project Purpose
This project demonstrates:
- Consuming RESTful APIs in Python
- Working with JSON responses
- Geographic coordinate systems
- Time and date manipulation
- API integration best practices