# Bootstrap Multi-Page Website

## Project Overview
A complete multi-page website built with Bootstrap 5, demonstrating professional web development practices with multiple pages, custom styling, and responsive design patterns.

## Technologies Used
- HTML5
- Bootstrap 5
- CSS3 (custom styles)
- JavaScript (Bootstrap components)
- Font Awesome icons
- Responsive images
- Multi-page navigation

## Project Structure
```
Part - Project 59 bootstrap pagesite/
├── index.html              # Home page
├── about.html              # About page
├── contact.html            # Contact page
├── post.html               # Blog post page
├── assets/                 # Images and media
├── css/                    # Custom stylesheets
│   └── styles.css
├── js/                     # JavaScript files
│   └── scripts.js
└── README.md               # This file
```

## Features
- Multi-page navigation with active state highlighting
- Responsive Bootstrap grid system
- Custom CSS styling and theming
- Contact form with validation
- Blog post layout with comments
- Image optimization and responsive images
- Footer with social media links
- Mobile-friendly navigation menu

## Pages Overview

### 1. **Home Page (`index.html`)**
- Hero section with call-to-action
- Featured content sections
- Testimonials or client logos
- Newsletter subscription
- Latest blog posts preview

### 2. **About Page (`about.html`)**
- Company/team introduction
- Mission and values
- Team member profiles
- History timeline
- Statistics or achievements

### 3. **Contact Page (`contact.html`)**
- Contact form with validation
- Contact information
- Map integration (concept)
- Office hours
- Social media links

### 4. **Blog Post Page (`post.html`)**
- Article content with typography
- Author information
- Publication date
- Comments section
- Related posts
- Social sharing buttons

## Bootstrap Components Used

### 1. **Navigation Bar**
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="index.html">SiteLogo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="about.html">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="contact.html">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### 2. **Hero Section**
```html
<section class="hero-section bg-primary text-white py-5">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h1 class="display-4 fw-bold">Welcome to Our Website</h1>
                <p class="lead">A professional multi-page website built with Bootstrap 5.</p>
                <a href="about.html" class="btn btn-light btn-lg">Learn More</a>
            </div>
            <div class="col-lg-6">
                <img src="assets/hero-image.jpg" alt="Hero Image" class="img-fluid rounded">
            </div>
        </div>
    </div>
</section>
```

### 3. **Contact Form**
```html
<form class="contact-form" id="contactForm">
    <div class="row">
        <div class="col-md-6 mb-3">
            <label for="name" class="form-label">Full Name</label>
            <input type="text" class="form-control" id="name" required>
        </div>
        <div class="col-md-6 mb-3">
            <label for="email" class="form-label">Email Address</label>
            <input type="email" class="form-control" id="email" required>
        </div>
    </div>
    <div class="mb-3">
        <label for="subject" class="form-label">Subject</label>
        <input type="text" class="form-control" id="subject" required>
    </div>
    <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" rows="5" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Send Message</button>
</form>
```

## Custom Styling Examples

### `css/styles.css`
```css
/* Custom color scheme */
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    --accent-color: #ff6b6b;
    --light-bg: #f8f9fa;
    --dark-text: #212529;
}

/* Custom button styles */
.btn-custom {
    background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
    border: none;
    color: white;
    padding: 12px 30px;
    border-radius: 30px;
    transition: transform 0.3s ease;
}

.btn-custom:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

/* Hero section styling */
.hero-section {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                url('../assets/hero-bg.jpg');
    background-size: cover;
    background-position: center;
    min-height: 80vh;
    display: flex;
    align-items: center;
}

/* Card hover effects */
.card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
}

/* Form styling */
.contact-form .form-control {
    border: 2px solid #dee2e6;
    padding: 12px 15px;
    border-radius: 8px;
}

.contact-form .form-control:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}
```

## Responsive Design Patterns

### Mobile-First Grid
```html
<div class="container">
    <div class="row">
        <!-- Stack on mobile, side-by-side on tablet+ -->
        <div class="col-12 col-md-6 col-lg-4 mb-4">
            <div class="card">
                <!-- Card content -->
            </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4 mb-4">
            <div class="card">
                <!-- Card content -->
            </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4 mb-4">
            <div class="card">
                <!-- Card content -->
            </div>
        </div>
    </div>
</div>
```

### Responsive Images
```html
<!-- Responsive image with different sizes -->
<img src="assets/image-large.jpg" 
     srcset="assets/image-small.jpg 600w,
             assets/image-medium.jpg 1200w,
             assets/image-large.jpg 2000w"
     sizes="(max-width: 768px) 100vw,
            (max-width: 1200px) 50vw,
            33vw"
     alt="Responsive Image"
     class="img-fluid">
```

## JavaScript Enhancements

### `js/scripts.js`
```javascript
// Form validation
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Simple validation
    if (!name || !email || !message) {
        alert('Please fill in all fields');
        return;
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address');
        return;
    }
    
    // Form submission logic
    console.log('Form submitted:', { name, email, message });
    alert('Thank you for your message!');
    this.reset();
});

// Active navigation highlighting
document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});
```

## SEO Best Practices

### 1. **Meta Tags**
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional multi-page website built with Bootstrap 5">
    <meta name="keywords" content="Bootstrap, website, responsive, web development">
    <meta name="author" content="Your Name">
    <title>Bootstrap Website - Home</title>
    
    <!-- Open Graph tags for social media -->
    <meta property="og:title" content="Bootstrap Multi-Page Website">
    <meta property="og:description" content="Professional website built with Bootstrap 5">
    <meta property="og:image" content="assets/og-image.jpg">
    <meta property="og:url" content="https://yourwebsite.com">
</head>
```

### 2. **Semantic HTML**
```html
<header>
    <nav>...</nav>
</header>

<main>
    <section>
        <article>...</article>
    </section>
</main>

<footer>...</footer>
```

## Performance Optimization

### 1. **Image Optimization**
- Use appropriate image formats (WebP, JPEG, PNG)
- Implement lazy loading
- Use responsive images with `srcset`
- Compress images before upload

### 2. **CSS Optimization**
- Minify CSS files for production
- Use CSS variables for theming
- Remove unused Bootstrap components
- Implement critical CSS loading

### 3. **JavaScript Optimization**
- Load scripts asynchronously
- Minify JavaScript files
- Use event delegation
- Implement code splitting if needed

## Accessibility Features

### 1. **ARIA Attributes**
```html
<nav aria-label="Main navigation">
    <ul role="menubar">
        <li role="none">
            <a href="#" role="menuitem">Home</a>
        </li>
    </ul>
</nav>
```

### 2. **Keyboard Navigation**
- Ensure all interactive elements are focusable
- Implement logical tab order
- Provide skip-to-content links
- Test with screen readers

### 3. **Color Contrast**
- Maintain minimum contrast ratio of 4.5:1 for normal text
- Use color contrast checking tools
- Provide alternative text for color-coded information

## Deployment Considerations

### 1. **File Structure**
```
production-site/
├── index.html
├── about.html
├── contact.html
├── post.html
├── assets/
│   ├── images/
│   ├── fonts/
│   └── icons/
├── css/
│   ├── bootstrap.min.css
│   └── styles.min.css
├── js/
│   ├── bootstrap.bundle.min.js
│   └── scripts.min.js
└── favicon.ico
```

### 2. **HTTPS Implementation**
- Use SSL certificate
- Redirect HTTP to HTTPS
- Update internal links to use HTTPS

### 3. **Caching Strategy**
- Implement browser caching
- Use CDN for Bootstrap assets
- Set appropriate cache headers

## Project Purpose
This project demonstrates:
- Professional multi-page website development
- Bootstrap 5 implementation at scale
- Custom styling and theming techniques
- Responsive design principles
- Form validation and user interaction
- SEO and accessibility best practices
- Performance optimization strategies