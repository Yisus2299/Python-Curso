# Image Colour Palette Extractor

A Flask web application that extracts and displays the dominant colors from uploaded images.

## Overview

This project allows users to upload an image and automatically extracts the top 10 dominant colors, displaying them as a color palette. It uses image quantization techniques to identify the most frequent colors in an efficient manner.

## Features

- **Image Upload**: Upload any image file (JPEG, PNG, etc.)
- **Color Extraction**: Identify top 10 dominant colors
- **Hex Code Display**: Show color values in hex format
- **Web Interface**: Simple, user-friendly Flask UI

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Image Processing**: Pillow (PIL)
- **Color Quantization**: PIL's built-in quantization

## Project Structure

```
Part - Project 92 image colour palette/
├── main.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template
└── README.md           # This file
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
   pip install flask pillow
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access in browser**:
   Navigate to `http://localhost:5000`

## How It Works

### 1. RGB to Hex Conversion

```python
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
```

Converts RGB tuple (255, 128, 0) to hex string "#ff8000".

### 2. Color Extraction Algorithm

```python
def extract_top_colors(image_file, top=10):
    # Open and convert image to RGB
    image = Image.open(image_file).convert("RGB")
    
    # Resize for faster processing
    image = image.resize((200, 200), Image.LANCZOS)
    
    # Quantize to reduce to 64 colors
    image = image.quantize(colors=64, method=2)
    
    # Get palette and color counts
    palette = image.getpalette()
    color_counts = image.getcolors(200 * 200)
    
    # Sort by frequency and extract top colors
    results.sort(reverse=True, key=lambda x: x[0])
    top_colors = [rgb_to_hex(rgb) for _, rgb in results[:top]]
    return top_colors
```

### Process Breakdown

| Step | Description |
|------|-------------|
| 1 | Open image and convert to RGB |
| 2 | Resize to 200x200 for performance |
| 3 | Quantize to 64 colors (reduces complexity) |
| 4 | Get color counts from quantized image |
| 5 | Sort by frequency (most common first) |
| 6 | Convert top colors to hex format |

### Why Quantization?

- Reduces processing time significantly
- Groups similar colors together
- Produces more meaningful palette results

### Quantization Method

- `method=2`: Uses Median Cut algorithm (better color distribution)

## Route Handlers

### Home Route (`/`)

```python
@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    filename = None
    if request.method == "POST":
        uploaded = request.files.get("image")
        if uploaded and uploaded.filename:
            colors = extract_top_colors(uploaded, top=10)
            filename = uploaded.filename
    return render_template("index.html", colors=colors, filename=filename)
```

- GET: Show upload form
- POST: Handle file upload, extract colors, display palette

## Web Interface

### Upload Form
- File input for image selection
- Submit button

### Display
- Original filename
- Color palette (10 color boxes)
- Hex codes below each color

## Usage Example

1. Open the application in a browser
2. Click "Choose File" to select an image
3. Click "Upload" or submit the form
4. View the extracted color palette

## Example Output

```
#2D3E50 - Dark blue-gray
#E8E8E8 - Light gray
#4A90A4 - Teal blue
#F5A623 - Orange
#D0021B - Red
#9013FE - Purple
#7ED321 - Green
#FFFFFF - White
#000000 - Black
#BD10E0 - Magenta
```

## Customization

### Change Number of Colors

Modify the `top` parameter:
```python
colors = extract_top_colors(uploaded, top=5)  # Get 5 colors
colors = extract_top_colors(uploaded, top=20) # Get 20 colors
```

### Change Resize Dimensions

Modify the resize values in `extract_top_colors`:
```python
image = image.resize((100, 100), Image.LANCZOS)  # Smaller = faster
image = image.resize((500, 500), Image.LANCZOS)  # Larger = more accurate
```

### Add Color Names

```python
def closest_color_name(hex_code):
    # Implement color name matching
    # Use web colors or predefined dictionary
    pass
```

## Performance Considerations

| Factor | Impact |
|--------|--------|
| Image size | Larger images take longer to process |
| Resize dimensions | Higher = slower but more accurate |
| Color count | More colors = more processing |

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| No file selected | User clicked upload without file | Show error message |
| Unsupported format | Invalid image file | Handle with try/except |

## Flask App Configuration

```python
app = Flask(__name__)
app.run(debug=True)  # Development mode
```

For production, use:
```python
app.run(host='0.0.0.0', port=5000)  # Production mode
```

## Template (templates/index.html)

The HTML template should include:
- Form with file input
- Loop through extracted colors
- Display color swatches with hex codes

```html
{% for color in colors %}
  <div style="background: {{ color }}; width: 50px; height: 50px;"></div>
  <span>{{ color }}</span>
{% endfor %}
```

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)