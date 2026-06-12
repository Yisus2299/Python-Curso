# Web Foundation with CSS

## Project Overview
A comprehensive collection of HTML/CSS files demonstrating foundational web development concepts with a focus on CSS styling, layout, and design principles. This project covers practical CSS implementations for real-world web pages.

## Technologies Used
- HTML5
- CSS3
- Box Model concepts
- Color systems
- Layout techniques
- Responsive design foundations

## Project Structure
```
Part - Project 44 Web Foundation CSS/
├── proyecto44.html        # Main CSS practice project
├── css_colours.html      # Color theory and implementation
├── padding.html          # Box model and spacing
├── README.md             # This file
└── images/               # Image assets (if any)
```

## CSS Concepts Covered

### 1. Box Model Fundamentals
- **Content**: Actual content of the element
- **Padding**: Space between content and border
- **Border**: Edge surrounding padding
- **Margin**: Space outside the border
- **Box-sizing**: Content-box vs border-box

### 2. Color Systems and Theory
- **Color Psychology**: Emotional impact of colors
- **Color Harmony**: Complementary, analogous, triadic schemes
- **Accessibility**: Contrast ratios and color blindness
- **Implementation**: Hexadecimal, RGB, HSL, named colors

### 3. Layout Techniques
- **Display Properties**: block, inline, inline-block, flex
- **Positioning**: static, relative, absolute, fixed, sticky
- **Floats**: Traditional float-based layouts
- **Centering Techniques**: Multiple methods for horizontal/vertical centering

### 4. Typography and Text Styling
- **Font Selection**: Web-safe fonts and Google Fonts
- **Text Properties**: alignment, decoration, transformation
- **Line Height**: Readability and spacing
- **Text Shadows**: Visual effects and depth

## File Descriptions

### `proyecto44.html`
Comprehensive CSS project demonstrating:
- Full webpage styling
- Image styling and positioning
- Color scheme implementation
- Typography system
- Layout structure
```html
<style>
    .osrs {
        border: 5px white solid;
        height: 300px;
        display: block;
        margin: 0 auto;
    }
    body {
        background-color: black;
    }
    .titulo {
        font-size: 50px;
        text-align: center;
        color: white;
    }
</style>
```

### `css_colours.html`
Color theory and implementation:
- Color system comparisons
- Color harmony examples
- Accessibility considerations
- Practical color usage
```html
<style>
    .primary { background-color: #007bff; }
    .secondary { background-color: #6c757d; }
    .success { background-color: #28a745; }
    .danger { background-color: #dc3545; }
    .warning { background-color: #ffc107; }
    .info { background-color: #17a2b8; }
</style>
```

### `padding.html`
Box model and spacing demonstration:
- Padding vs margin differences
- Border styles and implementations
- Box-sizing property usage
- Spacing best practices
```html
<style>
    .box {
        width: 200px;
        height: 100px;
        padding: 20px;
        margin: 15px;
        border: 2px solid #333;
        box-sizing: border-box;
    }
</style>
```

## Code Examples

### Complete Webpage Styling
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Foundation CSS</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Container for centering content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Card component styling */
        .card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 30px;
            margin: 20px 0;
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        /* Typography system */
        h1, h2, h3 {
            color: #2c3e50;
            margin-bottom: 15px;
        }
        
        h1 {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 30px;
        }
        
        p {
            margin-bottom: 15px;
            color: #555;
        }
        
        /* Button styling */
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .btn:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Web Foundation with CSS</h1>
        <div class="card">
            <h2>Modern Web Styling</h2>
            <p>This demonstrates comprehensive CSS styling techniques including typography, layout, and interactive elements.</p>
            <a href="#" class="btn">Learn More</a>
        </div>
    </div>
</body>
</html>
```

## Box Model Visualization
```
┌─────────────────────────────────────┐
│           MARGIN (outside)          │
│  ┌──────────────────────────────┐  │
│  │        BORDER (edge)         │  │
│  │  ┌────────────────────────┐  │  │
│  │  │     PADDING (space)    │  │  │
│  │  │  ┌──────────────────┐  │  │  │
│  │  │  │   CONTENT area   │  │  │  │
│  │  │  └──────────────────┘  │  │  │
│  │  └────────────────────────┘  │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Color System Implementation

### 1. **Primary Color Scheme**
```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --accent-color: #e74c3c;
    --text-color: #2c3e50;
    --background-color: #ecf0f1;
}
```

### 2. **Accessible Contrast**
```css
/* WCAG AA compliant contrast ratios */
.high-contrast {
    color: #000; /* Black text */
    background: #fff; /* White background */
    contrast-ratio: 21:1; /* Excellent */
}

.medium-contrast {
    color: #333; /* Dark gray */
    background: #f8f9fa; /* Light gray */
    contrast-ratio: 7:1; /* Good */
}
```

## Layout Techniques Demonstrated

### 1. **Centering Methods**
```css
/* Method 1: Auto margins */
.center-auto {
    width: 50%;
    margin: 0 auto;
}

/* Method 2: Flexbox */
.flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Method 3: Grid */
.grid-center {
    display: grid;
    place-items: center;
}
```

### 2. **Responsive Foundations**
```css
/* Mobile-first approach */
.container {
    width: 100%;
    padding: 15px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 992px) {
    .container {
        width: 970px;
    }
}
```

## Best Practices Demonstrated
1. **Mobile-First Design**: Starting with mobile layouts
2. **CSS Variables**: Consistent theming with custom properties
3. **Responsive Images**: Proper image sizing and optimization
4. **Accessibility**: Sufficient color contrast and semantic markup
5. **Performance**: Efficient CSS selectors and minimal repaints

## Project Purpose
This project demonstrates:
- Comprehensive CSS styling techniques
- Box model understanding and implementation
- Color theory and accessible color systems
- Layout fundamentals and responsive design
- Typography systems and text styling
- Modern web development foundations