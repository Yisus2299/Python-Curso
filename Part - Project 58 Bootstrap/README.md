# Bootstrap Framework Introduction

## Project Overview
A hands-on introduction to Bootstrap 5, the popular CSS framework for building responsive, mobile-first websites. This project demonstrates Bootstrap components, grid system, utilities, and responsive design principles.

## Technologies Used
- HTML5
- Bootstrap 5.3
- CSS3 (custom styles)
- JavaScript (Bootstrap components)
- Responsive design principles

## Project Structure
```
Part - Project 58 Bootstrap/
├── index_practice.html     # Main Bootstrap practice file
├── TinDog/                # TinDog project folder
│   ├── css/
│   ├── images/
│   └── index.html
└── README.md              # This file
```

## Features
- Bootstrap 5 CDN integration
- Responsive grid system
- Bootstrap components (cards, buttons, navigation)
- Custom CSS styling
- Mobile-first design approach
- Component customization examples

## Bootstrap Concepts Covered

### 1. **Grid System**
- 12-column responsive grid
- Breakpoints (xs, sm, md, lg, xl, xxl)
- Container, row, column structure
- Responsive column classes

### 2. **Components**
- Cards with images and content
- Buttons with various styles
- Navigation bars
- Typography utilities
- Spacing utilities

### 3. **Utilities**
- Margin and padding classes
- Text alignment and coloring
- Display properties
- Flexbox utilities
- Border and shadow utilities

## Code Examples

### Basic Bootstrap Setup
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap Practice</title>
    <!-- Bootstrap 5 CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        .card-img-top {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card {
            margin-left: auto;
            margin-right: auto;
            width: 18rem;
        }
    </style>
</head>
<body>
    <!-- Bootstrap content goes here -->
    
    <!-- Bootstrap JS Bundle (optional for components) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Bootstrap Card Component
```html
<div class="card">
    <img src="https://picsum.photos/800/400" class="card-img-top" alt="Placeholder Image">
    <div class="card-body">
        <h5 class="card-title">Card Title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>
```

## Bootstrap Grid System

### Basic Grid Example
```html
<div class="container">
    <div class="row">
        <!-- Equal width columns -->
        <div class="col">
            Column 1
        </div>
        <div class="col">
            Column 2
        </div>
        <div class="col">
            Column 3
        </div>
    </div>
    
    <div class="row">
        <!-- Responsive columns -->
        <div class="col-md-8">
            Main content (8 columns on medium+)
        </div>
        <div class="col-md-4">
            Sidebar (4 columns on medium+)
        </div>
    </div>
    
    <div class="row">
        <!-- Stack on mobile, side-by-side on desktop -->
        <div class="col-12 col-md-6 col-lg-4">
            Card 1
        </div>
        <div class="col-12 col-md-6 col-lg-4">
            Card 2
        </div>
        <div class="col-12 col-md-6 col-lg-4">
            Card 3
        </div>
    </div>
</div>
```

## Bootstrap Breakpoints
| Breakpoint | Class Prefix | Dimensions |
|------------|--------------|------------|
| Extra small | None | <576px |
| Small | `sm` | ≥576px |
| Medium | `md` | ≥768px |
| Large | `lg` | ≥992px |
| Extra large | `xl` | ≥1200px |
| Extra extra large | `xxl` | ≥1400px |

## Common Bootstrap Components

### 1. **Navigation Bar**
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">MySite</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### 2. **Buttons**
```html
<!-- Button styles -->
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<!-- Button sizes -->
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary">Normal</button>
<button class="btn btn-primary btn-sm">Small</button>

<!-- Outline buttons -->
<button class="btn btn-outline-primary">Outline Primary</button>
```

### 3. **Forms**
```html
<form>
    <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="email" class="form-control" id="exampleInputEmail1">
        <div class="form-text">We'll never share your email with anyone else.</div>
    </div>
    <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1">
    </div>
    <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## Customizing Bootstrap

### 1. **Custom CSS Overrides**
```css
/* Override Bootstrap styles */
.btn-primary {
    background-color: #ff6b6b;
    border-color: #ff6b6b;
}

.btn-primary:hover {
    background-color: #ff5252;
    border-color: #ff5252;
}

/* Custom utility classes */
.text-gradient {
    background: linear-gradient(45deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

### 2. **CSS Variables** (Bootstrap 5)
```css
:root {
    --bs-primary: #ff6b6b;
    --bs-primary-rgb: 255, 107, 107;
    --bs-secondary: #48dbfb;
    --bs-secondary-rgb: 72, 219, 251;
}
```

## Responsive Design Patterns

### Mobile-First Approach
```html
<!-- Stack on mobile (col-12), 2 columns on tablet (col-md-6), 3 columns on desktop (col-lg-4) -->
<div class="row">
    <div class="col-12 col-md-6 col-lg-4">Content 1</div>
    <div class="col-12 col-md-6 col-lg-4">Content 2</div>
    <div class="col-12 col-md-6 col-lg-4">Content 3</div>
</div>
```

### Hide/Show Based on Screen Size
```html
<!-- Hide on small screens, show on medium+ -->
<div class="d-none d-md-block">
    This content is hidden on mobile.
</div>

<!-- Show only on extra small screens -->
<div class="d-block d-sm-none">
    Mobile-only content.
</div>
```

## Bootstrap Utilities

### Spacing Utilities
```html
<!-- Margin and padding -->
<div class="m-1">Small margin</div>
<div class="m-3">Medium margin</div>
<div class="m-5">Large margin</div>

<div class="p-1">Small padding</div>
<div class="p-3">Medium padding</div>
<div class="p-5">Large padding</div>

<!-- Directional spacing -->
<div class="mt-3">Margin top</div>
<div class="mb-3">Margin bottom</div>
<div class="ms-3">Margin start (left)</div>
<div class="me-3">Margin end (right)</div>

<div class="pt-3">Padding top</div>
<div class="pb-3">Padding bottom</div>
```

### Text Utilities
```html
<!-- Text alignment -->
<p class="text-start">Left aligned</p>
<p class="text-center">Center aligned</p>
<p class="text-end">Right aligned</p>

<!-- Text coloring -->
<p class="text-primary">Primary text</p>
<p class="text-secondary">Secondary text</p>
<p class="text-success">Success text</p>
<p class="text-danger">Danger text</p>
<p class="text-warning">Warning text</p>
<p class="text-info">Info text</p>

<!-- Text transformation -->
<p class="text-lowercase">LOWERCASE TEXT</p>
<p class="text-uppercase">uppercase text</p>
<p class="text-capitalize">capitalized text</p>
```

## Bootstrap JavaScript Components

### Modal Example
```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p>Modal body text goes here.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
        </div>
    </div>
</div>
```

## Best Practices

### 1. **Mobile-First Development**
- Start with mobile layouts
- Use `min-width` media queries
- Test on actual mobile devices

### 2. **Semantic HTML**
```html
<!-- Good -->
<nav class="navbar">
    <ul class="nav">
        <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
    </ul>
</nav>

<!-- Better -->
<nav class="navbar" role="navigation" aria-label="Main navigation">
    <ul class="nav" role="menubar">
        <li class="nav-item" role="none">
            <a href="#" class="nav-link" role="menuitem">Home</a>
        </li>
    </ul>
</nav>
```

### 3. **Accessibility**
- Use proper ARIA attributes
- Ensure color contrast meets WCAG standards
- Test keyboard navigation
- Provide text alternatives for images

### 4. **Performance**
- Use Bootstrap CDN for caching benefits
- Minimize custom CSS overrides
- Remove unused Bootstrap components
- Consider Bootstrap customization build

## Project Purpose
This project demonstrates:
- Bootstrap 5 framework fundamentals
- Responsive grid system implementation
- Component-based design approach
- Mobile-first development principles
- Custom styling and theming techniques
- Practical web development with Bootstrap