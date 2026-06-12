# Music List Scraping Project

## Project Overview
A Python web scraping project that extracts music chart data from Billboard's Hot 100 list. This project demonstrates practical web scraping techniques for extracting structured data from music ranking websites.

## Technologies Used
- Python 3.x
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP client)
- File I/O operations
- Data cleaning and formatting

## Project Structure
```
Part - Project 46 music list scrapping/
├── musiclist.py          # Main music scraping script
├── musiclist.txt        # Output file with music list
└── README.md            # This file
```

## Features
- Billboard Hot 100 chart scraping
- HTML parsing with CSS class selectors
- Data extraction and text cleaning
- File output in readable format
- Error handling and graceful degradation
- Date-specific chart scraping

## Prerequisites
1. Python 3.x installed
2. Required Python libraries:
   ```
   pip install beautifulsoup4 requests
   ```

## How to Run
```
python musiclist.py
```

## Target Website
The script scrapes data from:
```
https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/
```

**Note**: This uses a practice version of Billboard charts specifically designed for web scraping education.

## Code Explanation

### Main Scraping Logic
```python
from bs4 import BeautifulSoup
import requests

# Target URL (practice Billboard chart)
url = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

# Find all music title elements using CSS class selector
all_music_list = soup.find_all(name="h3", class_="chart-entry__title")

# Extract text from each music element
music_titles = [music.get_text() for music in all_music_list]

# Write to file
with open("musiclist.txt", "w", encoding="utf-8") as file:
    for title in music_titles:
        file.write(f"{title}\n")
        print(title)
```

## HTML Structure Targeted
The script targets this specific HTML structure:
```html
<h3 class="chart-entry__title">Song Title 1 - Artist Name</h3>
<h3 class="chart-entry__title">Song Title 2 - Artist Name</h3>
<!-- ... more song entries ... -->
<h3 class="chart-entry__title">Song Title 100 - Artist Name</h3>
```

## Output Format
The script creates `musiclist.txt` with content like:
```
Song Title 1 - Artist Name
Song Title 2 - Artist Name
Song Title 3 - Artist Name
...
Song Title 100 - Artist Name
```

## Data Processing

### 1. **Text Extraction**
```python
# Basic text extraction
raw_text = music.get_text()

# Alternative: Get specific attribute
# song_id = music.get('data-song-id')
```

### 2. **Data Cleaning** (Extended Example)
```python
def clean_song_data(raw_text):
    """Clean and parse song data from raw HTML text"""
    # Remove extra whitespace
    cleaned = raw_text.strip()
    
    # Split song and artist (assuming format: "Song - Artist")
    if " - " in cleaned:
        song, artist = cleaned.split(" - ", 1)
    else:
        song, artist = cleaned, "Unknown Artist"
    
    return {
        'song': song.strip(),
        'artist': artist.strip()
    }

# Process all songs
for music in all_music_list:
    song_data = clean_song_data(music.get_text())
    print(f"Song: {song_data['song']}, Artist: {song_data['artist']}")
```

## Advanced Features

### 1. **Date-Specific Scraping**
```python
import datetime

# Get specific date's chart
def get_chart_for_date(date_str):
    """Construct URL for specific date's chart"""
    base_url = "https://appbrewery.github.io/bakeboard-hot-100/"
    return f"{base_url}{date_str}/"

# Example: Get last week's chart
last_week = datetime.date.today() - datetime.timedelta(days=7)
chart_url = get_chart_for_date(last_week.strftime("%Y-%m-%d"))
```

### 2. **Multiple Data Points**
```python
# Extract additional information if available
def extract_detailed_info(soup):
    """Extract multiple data points from chart"""
    songs = []
    
    # Find all chart entries
    entries = soup.find_all("div", class_="chart-entry")
    
    for entry in entries:
        song_info = {
            'title': entry.find("h3", class_="chart-entry__title").get_text(),
            'rank': entry.find("span", class_="chart-entry__rank").get_text(),
            'artist': entry.find("span", class_="chart-entry__artist").get_text(),
            'last_week': entry.find("span", class_="chart-entry__last-week").get_text(),
            'peak': entry.find("span", class_="chart-entry__peak").get_text(),
            'weeks': entry.find("span", class_="chart-entry__weeks").get_text()
        }
        songs.append(song_info)
    
    return songs
```

## Error Handling
```python
import requests
from requests.exceptions import RequestException

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()  # Raise exception for 4xx/5xx responses
    
    # Check content type
    if 'text/html' not in response.headers.get('Content-Type', ''):
        print("Warning: Response is not HTML")
    
except RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Export Options

### 1. **Text File (Current)**
```python
with open("musiclist.txt", "w", encoding="utf-8") as file:
    for title in music_titles:
        file.write(f"{title}\n")
```

### 2. **CSV File**
```python
import csv

with open("musiclist.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rank", "Song", "Artist"])
    for i, title in enumerate(music_titles, 1):
        writer.writerow([i, title])
```

### 3. **JSON File**
```python
import json

music_data = [
    {"rank": i, "title": title}
    for i, title in enumerate(music_titles, 1)
]

with open("musiclist.json", "w", encoding="utf-8") as jsonfile:
    json.dump(music_data, jsonfile, indent=2, ensure_ascii=False)
```

## Best Practices Demonstrated

### 1. **Respectful Scraping**
- Reasonable request frequency
- Proper error handling
- Timeout implementation
- User-Agent identification

### 2. **Data Quality**
- UTF-8 encoding for international characters
- Text cleaning and normalization
- Consistent output formatting
- Error recovery mechanisms

### 3. **Code Maintainability**
- Clear variable naming
- Modular function design
- Comprehensive comments
- Graceful degradation

## Real Billboard Scraping Considerations

For actual Billboard.com scraping:
1. **Check robots.txt**: `https://www.billboard.com/robots.txt`
2. **Review Terms of Service**: Commercial use restrictions
3. **Consider Official API**: Billboard may offer official data access
4. **Rate Limiting**: Implement delays between requests
5. **Legal Compliance**: Ensure data usage complies with copyright laws

## Project Purpose
This project demonstrates:
- Practical web scraping applications
- Music chart data extraction
- HTML parsing with CSS selectors
- Data cleaning and formatting
- File output in multiple formats
- Error handling and robustness
- Ethical web scraping considerations