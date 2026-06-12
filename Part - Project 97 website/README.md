# E-Commerce Store Website

A complete Flask-based e-commerce application with shopping cart, user authentication, and Stripe payment integration.

## Overview

This project is a fully functional e-commerce store featuring product browsing, shopping cart management, user registration/login, and checkout via Stripe payment gateway. It uses SQLite for data storage and Flask-Login for authentication.

## Features

- **Product Catalog**: Display products with images, prices, and descriptions
- **Shopping Cart**: Add/remove items, view cart total
- **User Authentication**: Register, login, logout functionality
- **Password Security**: PBKDF2-SHA256 password hashing
- **Stripe Checkout**: Secure payment integration
- **Session Management**: Persistent cart across pages
- **Flash Messages**: User feedback for actions
- **Protected Routes**: Checkout requires authentication

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite (native Python)
- **Authentication**: Flask-Login
- **Security**: Werkzeug password hashing
- **Payments**: Stripe API
- **Templating**: Jinja2 (built into Flask)

## Project Structure

```
Part - Project 97 website/
├── website.py              # Main Flask application
├── store.db               # SQLite database
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html        # Home page (product listing)
│   ├── cart.html         # Shopping cart
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   ├── success.html      # Payment success page
│   └── cancel.html       # Payment cancelled page
├── static/               # Static assets
│   └── images/          # Product images
├── .vscode/             # VS Code configuration
└── __pycache__/         # Python cache
```

## Database Schema

### Users Table

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER (PK) | Unique identifier |
| email | TEXT (UNIQUE) | User email |
| password | TEXT | Hashed password |

## Products

The store includes 3 sample products:

| Product | Price | Description |
|---------|-------|-------------|
| Coffee Mug | $18.00 | A strong mug for your strongest coffee |
| Soft Hoodie | $42.00 | A cozy hoodie for work or weekend wear |
| Notebook | $12.00 | A beautiful notebook for ideas and tasks |

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
   pip install flask flask-login stripe
   ```

4. **Configure Environment Variables** (optional):
   ```bash
   export SECRET_KEY="your-secret-key"
   export STRIPE_SECRET_KEY="sk_test_..."
   export STRIPE_PUBLISHABLE_KEY="pk_test_..."
   ```

5. **Run the application**:
   ```bash
   python website.py
   ```

6. **Access in browser**:
   Navigate to `http://localhost:5000`

## How It Works

### Application Setup

```python
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "please-change-this-secret")
```

### Database Initialization

```python
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)"
    )
    conn.commit()
    conn.close()
```

### User Model

```python
class User(UserMixin):
    def __init__(self, id_, email, password_hash):
        self.id = id_
        self.email = email
        self.password_hash = password_hash
```

### Shopping Cart

Cart is stored in Flask session:

```python
cart = session.get("cart", {})
cart[product_id] = cart.get(product_id, 0) + 1
session["cart"] = cart
```

### Routes Overview

| Route | Method | Description | Access |
|-------|--------|-------------|--------|
| `/` | GET | Product listing | Public |
| `/add-to-cart/<id>` | GET | Add product to cart | Public |
| `/cart` | GET | View cart | Public |
| `/remove-from-cart/<id>` | GET | Remove from cart | Public |
| `/checkout` | POST | Process payment | Requires login |
| `/register` | GET/POST | Create account | Public |
| `/login` | GET/POST | User login | Public |
| `/logout` | GET | User logout | Requires login |
| `/success` | GET | Payment success | Public |
| `/cancel` | GET | Payment cancelled | Public |

### Stripe Integration

```python
checkout_session = stripe.checkout.Session.create(
    payment_method_types=["card"],
    line_items=line_items,
    mode="payment",
    success_url=url_for("success", _external=True),
    cancel_url=url_for("cancel", _external=True),
    customer_email=current_user.email,
)
return redirect(checkout_session.url, code=303)
```

### Context Processor

```python
@app.context_processor
def inject_cart():
    cart = session.get("cart", {})
    count = sum(cart.values())
    return {"cart_count": count, "stripe_publishable_key": STRIPE_PUBLISHABLE_KEY}
```

Makes cart count available in all templates.

### Password Security

```python
from werkzeug.security import generate_password_hash, check_password_hash

# Hashing
password_hash = generate_password_hash(password)

# Verification
check_password_hash(stored_hash, password)
```

## Customization

### Adding New Products

Edit the `PRODUCTS` list in `website.py`:

```python
PRODUCTS = [
    {
        "id": "new-product",
        "name": "New Product",
        "price_cents": 2500,
        "price_display": "$25.00",
        "description": "Product description",
        "image": "images/new-product.jpg",
    },
]
```

### Adding Database Fields

1. Modify the CREATE TABLE SQL
2. Update registration to collect additional data
3. Update templates to display new fields

### Changing to Production Database

```python
# PostgreSQL example
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/store'
```

### Stripe Production Keys

Set environment variables:
```bash
export STRIPE_SECRET_KEY="sk_live_..."
export STRIPE_PUBLISHABLE_KEY="pk_live_..."
```

## Template Variables

### Global Variables (available in all templates)

- `cart_count`: Number of items in cart
- `stripe_publishable_key`: Stripe public key
- `current_user`: Logged-in user object

### Product Listing

- `products`: List of product dictionaries

### Cart Page

- `items`: List of cart items with details
- `total`: Total price in cents
- `total_display`: Formatted total (e.g., "$50.00")

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| "Product not found" | Invalid product ID | Check product ID in URL |
| "Your cart is empty" | Cart is empty | Add items before checkout |
| "Stripe checkout failed" | Invalid API key | Configure Stripe keys |
| "Email already registered" | User exists | Use different email |

## Security Considerations

1. **Never commit secret keys** to version control
2. Use environment variables for sensitive data
3. In production, use HTTPS
4. Implement rate limiting for login attempts
5. Add CSRF protection for forms
6. Validate all user inputs

## Testing Stripe

Use Stripe's test mode:
- Test card: 4242 4242 4242 4242
- Any future date for expiry
- Any 3 digits for CVC

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)