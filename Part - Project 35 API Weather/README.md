# Weather API with SMS Notifications

## Project Overview
A comprehensive weather monitoring application that retrieves forecast data from OpenWeather API and sends SMS notifications via Twilio. Features multi-language support and formatted weather alerts.

## Technologies Used
- Python 3.x
- OpenWeather API (weather data)
- Twilio API (SMS notifications)
- Babel (internationalization)
- datetime module
- locale module (localization)
- Requests library

## Project Structure
```
Part - Project 35 API Weather/
├── wheater.py           # Main weather application
├── image.png           # Weather icon/related image
└── README.md           # This file
```

## Features
- Real-time weather data retrieval from OpenWeather API
- SMS weather alerts via Twilio
- Multi-language support (Spanish/English)
- Formatted date and time localization
- Configurable weather thresholds and alerts
- Error handling and graceful degradation

## Prerequisites
### API Keys Required
1. **OpenWeather API Key**
   - Sign up at: https://openweathermap.org/api
   - Free tier available

2. **Twilio Account**
   - Sign up at: https://www.twilio.com
   - Verify phone number for WhatsApp sandbox

### Environment Variables
Set the following environment variables:
```bash
# PowerShell (Windows)
$env:OPENWEATHER_API_KEY="your_openweather_api_key"
$env:TWILIO_ACCOUNT_SID="your_twilio_account_sid"
$env:TWILIO_AUTH_TOKEN="your_twilio_auth_token"

# Linux/Mac
export OPENWEATHER_API_KEY="your_openweather_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_account_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
```

## Installation
1. Install required dependencies:
   ```
   pip install requests twilio babel python-dotenv
   ```

2. Configure environment variables as shown above

## How to Run
```
python wheater.py
```

## Configuration Options
### City/Location
Modify the `CITY_QUERY` variable in the script:
```python
CITY_QUERY = "San Juan de los Morros, Guarico, VE"  # Default
```

### Operating Modes
The script supports two modes:
- **Mode A**: Single weather alert at specific time
- **Mode B**: Daily summary with multiple forecast points

### SMS Configuration
```python
SMS_FROM = "+12183187447"  # Your Twilio sandbox number
SMS_TO = "+584122446504"   # Your verified phone number
```

## Weather Data Retrieved
- Current temperature (Celsius/Fahrenheit)
- Weather conditions (sunny, rainy, cloudy, etc.)
- Humidity percentage
- Wind speed and direction
- Sunrise and sunset times
- UV index
- Precipitation probability

## Internationalization
The application includes Spanish localization:
- Formatted dates in Spanish
- Localized time display
- Multi-language weather descriptions

## Error Handling
- API key validation
- Network timeout handling
- Invalid location handling
- SMS delivery confirmation
- Graceful degradation when services unavailable

## SMS Format Example
```
🌤️ Weather Alert - San Juan de los Morros
📅 Friday, June 12, 2026
⏰ 14:30 local time

🌡️ Temperature: 28°C (82°F)
☁️ Conditions: Partly cloudy
💧 Humidity: 65%
💨 Wind: 15 km/h NE
🌅 Sunrise: 06:15 AM
🌇 Sunset: 06:45 PM

Stay prepared! 😊
```

## Project Purpose
This project demonstrates:
- Integration of multiple external APIs
- SMS notification systems
- Internationalization and localization
- Weather data processing
- Professional error handling
- Scheduled task automation