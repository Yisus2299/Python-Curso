import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# create Database and a new table
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


app = Flask(__name__)
_base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    _base_dir, "books-collection.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) # database created with a table

with app.app_context():  # Create A New Record
    db.create_all()
    if db.session.query(Book).first() is None:
        db.session.add(
            Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        )
        db.session.commit()


def _parse_rating(raw: str) -> float:
    try:
        return float((raw or "0").strip())
    except ValueError:
        return 0.0


@app.route("/")
def home():
    books = Book.query.order_by(Book.id).all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form.get("title", "").strip(),
            author=request.form.get("author", "").strip(),
            rating=_parse_rating(request.form.get("rating", "")),
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book = db.session.get(Book, book_id)
    if book is None:
        return redirect(url_for("home"))

    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("delete.html", book=book, book_id=book_id)


@app.route("/update/<int:book_id>", methods=["GET", "POST"])
def update(book_id):
    book = db.session.get(Book, book_id)
    if book is None:
        return redirect(url_for("home"))

    if request.method == "POST":
        book.title = request.form.get("title", "").strip()
        book.author = request.form.get("author", "").strip()
        book.rating = _parse_rating(request.form.get("rating", ""))
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", book=book, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)