Profile/Card Flask Template
==========================

This repository contains a minimal responsive profile/card-style HTML template originally adapted from an HTML5 UP free theme and extended here for use in small Flask demo projects.

Key details
- Purpose: a simple, mobile-friendly profile/card layout to use as a starting point for Flask templates or static sites.
- License: original HTML5 UP assets are provided under the Creative Commons Attribution 3.0 license (see original project for details). Demo images used in the original template are not included.

What this repo contains
- HTML, CSS and JS for a minimal profile/card template
- Placeholder images removed; replace with your own assets
- Simple example Flask app (if present) should serve the template from `templates/`

How to use
1. Replace placeholder images in the `static/` folder with your own images.
2. If using with Flask, put the HTML file into `templates/` and static files into `static/`.
3. Run a minimal Flask app and render the template, e.g.:

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Notes and credits
- Demo images originally come from Unsplash (not included).
- Icons used in the template (if any) originally came from Font Awesome.
- This README is an adapted summary matching the contents of this folder and how to use the template with Flask.
