import os
import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "store.db")

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "please-change-this-secret")

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

PRODUCTS = [
    {
        "id": "coffee-mug",
        "name": "Coffee Mug",
        "price_cents": 1800,
        "price_display": "$18.00",
        "description": "A strong mug for your strongest coffee.",
        "image": "images/coffee-mug.jpg",
    },
    {
        "id": "soft-hoodie",
        "name": "Soft Hoodie",
        "price_cents": 4200,
        "price_display": "$42.00",
        "description": "A cozy hoodie for work or weekend wear.",
        "image": "images/soft-hoodie.jpg",
    },
    {
        "id": "notebook",
        "name": "Notebook",
        "price_cents": 1200,
        "price_display": "$12.00",
        "description": "A beautiful notebook for ideas and tasks.",
        "image": "images/notebook.jpg",
    },
]

class User(UserMixin):
    def __init__(self, id_, email, password_hash):
        self.id = id_
        self.email = email
        self.password_hash = password_hash


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, password FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(row[0], row[1], row[2])
    return None


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)"
    )
    conn.commit()
    conn.close()


# Initialize the database when the app module loads.
# Flask 3 no longer supports before_first_request.
init_db()


@app.context_processor
def inject_cart():
    cart = session.get("cart", {})
    count = sum(cart.values())
    return {"cart_count": count, "stripe_publishable_key": STRIPE_PUBLISHABLE_KEY}


@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)


@app.route("/add-to-cart/<product_id>")
def add_to_cart(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        flash("Product not found.", "warning")
        return redirect(url_for("index"))

    cart = session.get("cart", {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session["cart"] = cart
    flash(f"Added {product['name']} to cart.", "success")
    return redirect(url_for("index"))


@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            item_total = product["price_cents"] * quantity
            total += item_total
            items.append({
                "id": product_id,
                "name": product["name"],
                "image": product["image"],
                "price_cents": product["price_cents"],
                "price_display": product["price_display"],
                "quantity": quantity,
                "item_total": item_total,
                "item_total_display": f"${item_total // 100}.{item_total % 100:02d}",
            })
    return render_template(
        "cart.html",
        items=items,
        total=total,
        total_display=f"${total // 100}.{total % 100:02d}",
    )


@app.route("/remove-from-cart/<product_id>")
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    if product_id in cart:
        cart.pop(product_id)
        session["cart"] = cart
        flash("Item removed from cart.", "success")
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["POST"])
@login_required
def checkout():
    if not stripe.api_key:
        flash("Stripe secret key is not configured. Set STRIPE_SECRET_KEY in your environment.", "danger")
        return redirect(url_for("cart"))

    cart = session.get("cart", {})
    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("cart"))

    line_items = []
    for product_id, quantity in cart.items():
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": product["name"], "description": product["description"]},
                        "unit_amount": product["price_cents"],
                    },
                    "quantity": quantity,
                }
            )

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=url_for("success", _external=True),
            cancel_url=url_for("cancel", _external=True),
            customer_email=current_user.email,
        )
        return redirect(checkout_session.url, code=303)
    except Exception as exc:
        flash(f"Stripe checkout failed: {exc}", "danger")
        return redirect(url_for("cart"))


@app.route("/success")
def success():
    session.pop("cart", None)
    return render_template("success.html")


@app.route("/cancel")
def cancel():
    return render_template("cancel.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not email or not password:
            flash("Please provide an email and password.", "warning")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "warning")
            return render_template("register.html")

        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password_hash),
            )
            conn.commit()
            flash("Account created. Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("That email is already registered.", "warning")
        finally:
            conn.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, email, password FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()

        if row and check_password_hash(row[2], password):
            user = User(row[0], row[1], row[2])
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("index"))

        flash("Email or password is incorrect.", "danger")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
