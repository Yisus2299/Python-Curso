# Stock Market Monitoring System

## Project Overview
A comprehensive stock market monitoring application that tracks stock prices using Alpha Vantage API and retrieves related news using NewsAPI. The system alerts users when stocks show significant price movements.

## Technologies Used
- Python 3.x
- Alpha Vantage API (stock market data)
- NewsAPI (financial news)
- Requests library
- JSON data caching
- os module (file operations)

## Project Structure
```
Part - Project 36 API Stock/
├── main.py              # Main stock monitoring application
├── stock_TSLA_daily.json # Cached stock data (generated)
├── news_TSLA.json       # Cached news data (generated)
└── README.md           # This file
```

## Features
- Real-time stock price monitoring (Tesla Inc by default)
- 5% price change detection triggers news alerts
- Financial news aggregation from multiple sources
- JSON caching to respect API rate limits
- Configurable stock symbols and thresholds
- Comprehensive error handling

## Prerequisites
### API Keys Required
1. **Alpha Vantage API Key**
   - Sign up at: https://www.alphavantage.co/support/#api-key
   - Free tier: 5 API requests per minute, 500 per day

2. **NewsAPI Key**
   - Sign up at: https://newsapi.org/register
   - Free tier: 100 requests per day

### API Configuration
Update the API keys in the script:
```python
STOCK_API_KEY = "8F7350UC5TV86YFK"  # Alpha Vantage key
NEWS_API_KEY = "4152daf86f024426acf342a93c83657f"  # NewsAPI key
```

## Installation
1. Install required dependencies:
   ```
   pip install requests
   ```

2. Configure API keys as shown above

## How to Run
```
python main.py
```

## Configuration Options
### Stock Selection
```python
STOCK_NAME = "TSLA"           # Stock symbol
COMPANY_NAME = "Tesla Inc"    # Full company name
```

### Alert Threshold
```python
# Price change percentage that triggers news alerts
PRICE_CHANGE_THRESHOLD = 5  # Percentage (5% by default)
```

### Cache Settings
- Stock data cached in `stock_{STOCK_NAME}_daily.json`
- News data cached in `news_{STOCK_NAME}.json`
- Cache reduces API calls and respects rate limits

## How It Works
1. **Stock Price Monitoring**
   - Retrieves daily stock prices from Alpha Vantage
   - Calculates percentage change between trading days
   - Triggers alert when change exceeds threshold

2. **News Aggregation**
   - When alert triggered, fetches relevant news
   - Searches for company-related articles
   - Returns top 3 most relevant news pieces

3. **Caching System**
   - Stores API responses locally
   - Reduces API rate limit consumption
   - Improves application performance

## API Rate Limits
### Alpha Vantage
- Free tier: 5 requests per minute, 500 per day
- Premium tiers available for higher limits
- Consider time-series data (daily, weekly, monthly)

### NewsAPI
- Free tier: 100 requests per day
- Rate limits per IP address
- Commercial plans available

## Error Handling
- API rate limit detection and handling
- Network timeout management
- Invalid stock symbol validation
- JSON parsing error recovery
- Cache file corruption handling

## Output Example
```
📈 STOCK ALERT: TSLA (Tesla Inc)
📊 Price Change: +5.8% (Yesterday: $250.12 → Today: $264.67)

📰 RELATED NEWS:
1. Tesla Announces New Battery Technology
   Source: Bloomberg - 2 hours ago
   Summary: Tesla unveils revolutionary battery tech...

2. Elon Musk Discusses Future Plans
   Source: CNBC - 5 hours ago
   Summary: CEO Elon Musk outlines expansion plans...

3. Tesla Q4 Earnings Exceed Expectations
   Source: Financial Times - 1 day ago
   Summary: Tesla reports better-than-expected Q4 results...
```

## Project Purpose
This project demonstrates:
- Financial API integration
- Rate limit management strategies
- Data caching techniques
- Multi-API system design
- Financial data analysis
- News aggregation systems