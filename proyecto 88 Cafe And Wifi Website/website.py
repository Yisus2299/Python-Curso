import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")

_base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(_base_dir, "cafes.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


def get_locations():
    stmt = select(Cafe.location).distinct().order_by(Cafe.location)
    return db.session.execute(stmt).scalars().all()


@app.route("/")
def home():
    loc = request.args.get("loc", "").strip()
    stmt = select(Cafe).order_by(Cafe.name)
    if loc:
        stmt = stmt.where(Cafe.location == loc)
    cafes = db.session.execute(stmt).scalars().all()
    return render_template(
        "index.html",
        cafes=cafes,
        locations=get_locations(),
        selected_loc=loc,
    )


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name", "").strip(),
            map_url=request.form.get("map_url", "").strip(),
            img_url=request.form.get("img_url", "").strip(),
            location=request.form.get("loc", "").strip(),
            seats=request.form.get("seats", "").strip(),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            coffee_price=request.form.get("coffee_price", "").strip() or None,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<int:cafe_id>", methods=["GET", "POST"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return redirect(url_for("home"))

    if request.method == "POST":
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("delete.html", cafe=cafe)


if __name__ == "__main__":
    app.run(debug=True)