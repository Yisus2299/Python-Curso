# Kanye West Quotes App

A desktop application that fetches and displays random Kanye West quotes using the Kanye.rest API.

## Overview

This project is a simple Tkinter-based desktop application that fetches random motivational (and sometimes controversial) quotes from Kanye West via a public API and displays them in a graphical interface. Each time you click the button, a new quote is fetched from the API.

## Features

- **API Integration**: Fetches real-time quotes from Kanye.rest API
- **Graphical User Interface**: Clean Tkinter-based UI
- **Image Integration**: Displays custom Kanye West image
- **Error Handling**: Handles API request errors gracefully
- **Background Image**: Shows custom background in the UI

## Tech Stack

- **Language**: Python
- **GUI Framework**: Tkinter (Python standard library)
- **HTTP Requests**: requests library
- **API**: https://api.kanye.rest (free, no authentication required)

## Project Structure

```
Kanye-quotes-start/
├── main_kanye.py       # Main application file
├── kanye.png          # Kanye button image
├── background.png     # Background image
└── README.md          # This file
```

## Installation & Setup

1. **Ensure Python is installed**:
   ```bash
   python --version
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests
   ```

3. **Run the application**:
   ```bash
   python main_kanye.py
   ```

## How It Works

### API Request

```python
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    return quote
```

The application makes a GET request to the free Kanye.rest API, which returns a JSON response with a quote.

### API Response Format

```json
{
  "quote": "I am the greatest artist of all time."
}
```

### GUI Setup

```python
window = Tk()
window.title("Kanye Says...")
window.config(padx=70, pady=30)
```

### Canvas Configuration

```python
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=str(BASE_DIR / "background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, 
    text="Kanye Quote Goes HERE", 
    width=250, 
    font=("Arial", 20, "bold"), 
    fill="black"
)
canvas.grid(row=0, column=0)
```

### Button Configuration

```python
kanye_img = PhotoImage(file=str(BASE_DIR / "kanye.png"))
kanye_button = Button(
    image=kanye_img, 
    highlightthickness=0, 
    command=get_quote
)
kanye_button.grid(row=1, column=0)
```

## Code Explanation

### Main Components

| Component | Description |
|-----------|-------------|
| `get_quote()` | Fetches quote from API and updates canvas text |
| `Canvas` | Displays background image and quote text |
| `Button` | Kanye image button that triggers API call |
| `PhotoImage` | Loads PNG images for background and button |

### Flow

1. User clicks the Kanye button
2. `get_quote()` is called
3. HTTP GET request sent to `https://api.kanye.rest`
4. Response parsed as JSON
5. Quote text updated on canvas

### Path Resolution

```python
BASE_DIR = Path(__file__).resolve().parent
```

Uses `pathlib` to resolve the correct path to image files regardless of where the script is run from.

## Customization

### Change API Endpoint

```python
# Use a different quote API
response = requests.get("https://api.quotable.io/random")
data = response.json()
quote = data["content"]
```

### Change Window Size

```python
window.config(padx=70, pady=30)  # Padding around elements
canvas = Canvas(width=300, height=414)  # Canvas dimensions
```

### Change Quote Font

```python
quote_text = canvas.create_text(
    150, 207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Helvetica", 18, "bold"),  # Change font family, size, style
    fill="black"
)
```

### Add More Functionality

```python
def get_quote():
    try:
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()
        data = response.json()
        quote = data["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException:
        canvas.itemconfig(quote_text, text="Error fetching quote")
```

## Troubleshooting

### Issue: Images not loading

**Solution**: Ensure `kanye.png` and `background.png` are in the same directory as `main_kanye.py`.

### Issue: API request fails

**Solution**: 
- Check internet connection
- The free API may have rate limits
- Add try/except for error handling

### Issue: "PhotoImage" not defined

**Solution**:
```python
from tkinter import PhotoImage
```

## Example Output

When you click the Kanye button, the quote text will change to something like:

> "I am the greatest artist of all time."

Or:

> "I love you so much."

## API Information

**Endpoint**: `https://api.kanye.rest`

**Method**: GET

**Response Format**:
```json
{
  "quote": "Your quote here"
}
```

**Rate Limits**: The free API has rate limits. For production use, consider caching quotes or using a different API.

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)