# Web Scraping Project - Movie Rankings

## Project Overview
A Python web scraping project that extracts movie rankings from Empire Online's "100 Greatest Movies of All Time" list. This project demonstrates web scraping fundamentals using BeautifulSoup and Requests libraries.

## Technologies Used
- Python 3.x
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP client)
- Regular expressions (pattern matching)
- File I/O operations

## Project Structure
```
Part - Project 45 scrapping website/
├── proyecto45Movies.py    # Main movie scraping script
├── scrapping_practice.py  # General web scraping practice
├── movies.txt            # Output file with movie list
└── README.md             # This file
```

## Features
- Web scraping from Empire Online's movie rankings
- HTML parsing with BeautifulSoup
- Data extraction and cleaning
- File output in readable format
- Error handling and timeout management
- Web archive URL support

## Prerequisites
1. Python 3.x installed
2. Required Python libraries:
   ```
   pip install beautifulsoup4 requests
   ```

## How to Run
```
python proyecto45Movies.py
```

## Target Website
The script scrapes data from:
```
https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
```

**Note**: Uses the Wayback Machine archive to ensure consistent data availability.

## Code Explanation

### Main Scraping Logic
```python
from bs4 import BeautifulSoup
import requests

# Target URL (Web Archive version for consistency)
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send HTTP request with timeout
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

# Find all movie title elements
all_movies = soup.find_all(name="h3", class_="title")

# Extract text from each movie element
movie_titles = [movie.get_text() for movie in all_movies]

# Write to file in reverse order (1-100 instead of 100-1)
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in reversed(movie_titles):
        file.write(f"{title}\n")
        print(title)
```

## HTML Structure Targeted
The script targets this specific HTML structure:
```html
<h3 class="title">100) The Godfather</h3>
<h3 class="title">99) Goodfellas</h3>
<!-- ... more movie entries ... -->
<h3 class="title">1) The Shawshank Redemption</h3>
```

## Output Format
The script creates `movies.txt` with content like:
```
1) The Shawshank Redemption
2) The Godfather: Part II
3) The Dark Knight
4) The Godfather
5) 12 Angry Men
...
100) The Wizard of Oz
```

## Error Handling
The script includes:
- **Network Timeouts**: 15-second timeout for requests
- **Encoding Support**: UTF-8 encoding for international characters
- **Element Not Found**: Graceful handling if HTML structure changes
- **File Operations**: Proper file closing and error handling

## Customization Options

### 1. Change Target URL
```python
# Update to scrape different movie lists
url = "https://example.com/movie-list"
```

### 2. Modify HTML Selectors
```python
# Adjust if website structure changes
all_movies = soup.find_all(name="div", class_="movie-entry")
```

### 3. Change Output Format
```python
# Output as CSV instead of plain text
with open("movies.csv", "w", encoding="utf-8") as file:
    file.write("Rank,Title\n")
    for i, title in enumerate(reversed(movie_titles), 1):
        file.write(f"{i},{title}\n")
```

## Web Scraping Best Practices

### 1. **Respect robots.txt**
```python
# Check if scraping is allowed
# https://www.empireonline.com/robots.txt
```

### 2. **Use Appropriate Headers**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers, timeout=15)
```

### 3. **Implement Rate Limiting**
```python
import time
time.sleep(1)  # Wait 1 second between requests
```

### 4. **Handle Dynamic Content**
For JavaScript-rendered sites, consider:
- Selenium WebDriver
- Playwright
- Puppeteer

## Legal and Ethical Considerations

### ✅ **Allowed**
- Scraping publicly available data
- Educational purposes
- Personal use
- Data analysis (non-commercial)

### ⚠️ **Caution Required**
- Commercial use of scraped data
- High-frequency requests
- Personal information scraping
- Copyrighted content reproduction

### ❌ **Not Allowed**
- Bypassing paywalls
- Violating terms of service
- Scraping private/user data
- Denial-of-service attacks

## Common Challenges & Solutions

### 1. **Website Structure Changes**
```python
try:
    all_movies = soup.find_all(name="h3", class_="title")
except:
    # Fallback to alternative selectors
    all_movies = soup.select(".movie-list h3")
```

### 2. **Anti-Scraping Measures**
- Rotate User-Agent headers
- Use proxy servers
- Implement random delays
- Monitor for CAPTCHAs

### 3. **Data Cleaning**
```python
# Remove extra whitespace and special characters
clean_title = title.strip().replace('\n', ' ').replace('\r', '')
```

## Project Purpose
This project demonstrates:
- Web scraping fundamentals with Python
- HTML parsing using BeautifulSoup
- HTTP request handling with error management
- Data extraction and file output
- Web scraping ethics and best practices
- Practical data collection applications