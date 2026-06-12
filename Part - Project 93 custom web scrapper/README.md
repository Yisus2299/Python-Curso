# Custom Web Scraper

Python web scraping projects that extract data from websites and save it to CSV files for analysis.

## Overview

This project contains two web scraping scripts that extract data from different websites:
1. **News Scraper**: Extracts headlines from Hacker News
2. **Nutrition Scraper**: Extracts nutritional data from a food database

Both scripts use BeautifulSoup for HTML parsing and save results to CSV files.

## Tech Stack

- **Language**: Python
- **HTTP Requests**: requests library
- **HTML Parsing**: BeautifulSoup4
- **Data Storage**: CSV files (built-in csv module)

## Project Structure

```
Part - Project 93 custom web scrapper/
├── scrapping_news.py       # Hacker News scraper
├── scrapping_nutrition.py  # Nutrition data scraper
├── news.csv               # Output from news scraper
├── nutrition.csv          # Output from nutrition scraper
└── README.md              # This file
```

---

# News Scraper

## Overview

Extracts article titles, links, and scores from Hacker News.

## Source

Website: `https://appbrewery.github.io/news.ycombinator.com/`

## Data Extracted

| Field | Description |
|-------|-------------|
| title | Article headline |
| link | URL to the article |
| score | Points/likes on Hacker News |

## How It Works

### 1. Send HTTP Request

```python
import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url, timeout=15)
```

### 2. Parse HTML

```python
soup = BeautifulSoup(response.text, "html.parser")
```

### 3. Find Elements

```python
# Find all article titles (class="storylink")
articles = soup.find_all(name="a", class_="storylink")

# Find all scores (class="score")
scores = soup.find_all(name="span", class_="score")
```

### 4. Extract Data

```python
rows = []
for i, article_tag in enumerate(articles):
    title = article_tag.get_text()
    link = article_tag.get("href")
    score = scores[i].get_text() if i < len(scores) else "0 points"
    rows.append([title, link, score])
```

### 5. Save to CSV

```python
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "link", "score"])
    writer.writerows(rows)
```

## Usage

```bash
python scrapping_news.py
```

## Output (news.csv)

```csv
title,link,score
"How to Build a Startup","https://example.com/article",45 points
"Python Tips and Tricks","https://example.com/python",32 points
...
```

---

# Nutrition Scraper

## Overview

Extracts nutritional information from food items.

## Source

Website: https://github.com/ (or similar nutrition database)

## Data Extracted

Typical fields include:
- Food name
- Calories
- Protein
- Carbohydrates
- Fat
- Serving size

## How It Works

Similar pattern to news scraper:
1. Send HTTP request
2. Parse HTML with BeautifulSoup
3. Find table rows or specific elements
4. Extract text content
5. Write to CSV

## Usage

```bash
python scrapping_nutrition.py
```

## Output (nutrition.csv)

```csv
food,calories,protein,carbs,fat
"Chicken Breast",165,31,0,3.6
"White Rice",130,2.7,28,0.3
...
```

---

# Important Concepts

## Web Scraping Ethics

Before scraping any website:

1. **Check robots.txt**: `https://example.com/robots.txt`
2. **Read Terms of Service**: Some websites prohibit scraping
3. **Be Respectful**: Add delays between requests
4. **Identify Yourself**: Use a proper User-Agent header
5. **Don't Overload Servers**: Limit request rate

## Request Headers

```python
headers = {
    "User-Agent": "MyScraper/1.0 (my@email.com)"
}
response = requests.get(url, headers=headers, timeout=15)
```

## Handling Errors

```python
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()  # Raise exception for 4xx/5xx
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

## Parsing HTML

BeautifulSoup methods:

| Method | Description |
|--------|-------------|
| `find()` | Get first matching element |
| `find_all()` | Get all matching elements |
| `get_text()` | Extract text content |
| `get()` | Get attribute value |

## CSS Selectors vs BeautifulSoup

```python
# BeautifulSoup
soup.find_all("a", class_="storylink")

# Same with CSS selector (using .select)
soup.select("a.storylink")
```

---

# Installation & Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4
   ```

4. **Run scrapers**:
   ```bash
   python scrapping_news.py
   python scrapping_nutrition.py
   ```

---

# Common Issues

## Issue: Empty Results

**Cause**: Website structure changed or JavaScript-rendered content

**Solution**: 
- Inspect website manually
- Check if content loads via JavaScript
- Use Selenium for JavaScript content

## Issue: Rate Limiting

**Cause**: Too many requests too quickly

**Solution**:
```python
import time
time.sleep(1)  # Wait 1 second between requests
```

## Issue: SSL Errors

**Cause**: Certificate verification issues

**Solution**:
```python
response = requests.get(url, verify=False)  # Not recommended for production
```

## Issue: Encoding Problems

**Cause**: Special characters in HTML

**Solution**:
```python
response.encoding = 'utf-8'
```

---

# Alternatives

### For Dynamic Content (JavaScript)

- **Selenium**: Browser automation
- **Playwright**: Modern browser automation
- **Scrapy**: Full-featured scraping framework

### For APIs

Many websites offer APIs - check first!

```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

---

# Legal Considerations

**Only scrape public data you're authorized to access**

- Personal data: Be cautious with privacy laws (GDPR, CCPA)
- Copyrighted content: Don't redistribute scraped content
- Terms of Service: Violating ToS can lead to IP ban
- Commercial use: Get permission before scraping for business

---

# License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)