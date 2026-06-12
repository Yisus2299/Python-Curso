# CSS Introduction

## Project Overview
A collection of HTML/CSS files introducing Cascading Style Sheets (CSS) fundamentals. This project demonstrates how to style HTML elements using various CSS techniques including internal styles, selectors, and basic properties.

## Technologies Used
- HTML5
- CSS3
- Internal styling (style tags)
- Basic CSS selectors
- Color and text properties

## Project Structure
```
Part - Project 43 CSS introduction/
├── css_Intoduction.html    # Basic CSS introduction
├── selectores.html        # CSS selectors practice
├── README.md              # This file
└── images/                # Image assets (if any)
```

## CSS Concepts Covered

### 1. CSS Integration Methods
- **Internal CSS**: Styles within `<style>` tags in `<head>`
- **Inline CSS**: Styles directly on elements (not recommended)
- **External CSS**: Separate .css files (concept introduction)

### 2. Basic CSS Selectors
- **Element Selectors**: `h1`, `p`, `div`
- **Class Selectors**: `.classname`
- **ID Selectors**: `#idname`
- **Universal Selector**: `*`

### 3. CSS Properties Demonstrated
- **Color Properties**: `color`, `background-color`
- **Text Properties**: `font-size`, `text-align`, `font-family`
- **Box Model**: `margin`, `padding`, `border`
- **Display Properties**: `display`, `visibility`

### 4. CSS Specificity & Cascade
- Selector specificity hierarchy
- Inheritance principles
- Cascade order importance
- `!important` rule (concept)

## File Descriptions

### `css_Intoduction.html`
Basic CSS introduction file demonstrating:
- Internal CSS styling
- Element selector usage
- Basic color and text properties
- Simple styling examples
```html
<style>
    h1 {
        color: rgba(163, 58, 9, 0.445);
    }
</style>
```

### `selectores.html`
CSS selectors practice file demonstrating:
- Multiple selector types
- Specificity examples
- Nested element styling
- Practical selector usage
```html
<style>
    /* Element selector */
    p { color: blue; }
    
    /* Class selector */
    .highlight { background-color: yellow; }
    
    /* ID selector */
    #main-title { font-size: 2em; }
    
    /* Combined selector */
    div p { margin: 10px; }
</style>
```

## Code Examples

### Basic Internal CSS
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Introduction</title>
    <style>
        /* Element selector */
        h1 {
            color: #333;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        
        /* Class selector */
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
        }
        
        /* ID selector */
        #special-paragraph {
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to CSS</h1>
        <p id="special-paragraph">This paragraph has special styling.</p>
        <p>A regular paragraph with default styling.</p>
    </div>
</body>
</html>
```

### Selector Hierarchy Example
```html
<style>
    /* Universal selector - lowest priority */
    * { margin: 0; padding: 0; }
    
    /* Element selector */
    p { color: black; }
    
    /* Class selector - higher priority */
    .important { color: red; }
    
    /* ID selector - highest priority */
    #main-content { color: blue; }
    
    /* Combined selector */
    div p.important { font-weight: bold; }
</style>
```

## How to Use
1. **Open in Browser**: View styled HTML files
2. **Inspect Elements**: Use browser developer tools (F12)
3. **Modify Styles**: Experiment with different CSS properties
4. **Add New Rules**: Practice writing CSS selectors
5. **Validate CSS**: Use online CSS validators

## Browser Developer Tools
Learn to use:
- **Elements Panel**: View HTML structure
- **Styles Panel**: See applied CSS rules
- **Computed Panel**: View final computed styles
- **Box Model Visualization**: Understand spacing

## Color Systems Demonstrated
1. **Named Colors**: `red`, `blue`, `green`
2. **Hexadecimal**: `#FF0000`, `#00FF00`
3. **RGB**: `rgb(255, 0, 0)`
4. **RGBA**: `rgba(163, 58, 9, 0.445)` (with opacity)
5. **HSL**: `hsl(0, 100%, 50%)`

## Text Styling Properties
- `font-family`: Typeface selection
- `font-size`: Text size (px, em, rem, %)
- `font-weight`: Boldness (normal, bold, 100-900)
- `text-align`: Alignment (left, center, right, justify)
- `line-height`: Line spacing
- `text-decoration`: Underline, overline, line-through

## Best Practices Demonstrated
1. **Internal vs External**: When to use each method
2. **Selector Specificity**: Understanding priority
3. **Color Accessibility**: Sufficient contrast ratios
4. **Font Stacking**: Fallback fonts for compatibility
5. **Units**: Appropriate unit selection (px, em, rem)

## Common Mistakes to Avoid
- Overusing `!important`
- Too specific selectors
- Inline styles (maintainability)
- Non-semantic class names
- Missing vendor prefixes (when needed)

## Project Purpose
This project demonstrates:
- CSS fundamentals and syntax
- Different styling methods
- Selector types and specificity
- Basic property usage
- Browser developer tool usage
- CSS best practices introduction