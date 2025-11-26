from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# --- Database config (SQLite file next to app.py) ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "todo.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --- Model ---
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


# ✅ IMPORTANT: run this on import (works on Vercel + locally)
with app.app_context():
    db.create_all()


# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")

        if not title or not desc:
            return redirect(url_for("home"))

        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("home"))

    todos = Todo.query.order_by(Todo.date_created.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.get_or_404(sno)

    if request.method == "POST":
        todo.title = request.form.get("title")
        todo.desc = request.form.get("desc")
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", todo=todo)


@app.route("/delete/<int:sno>", methods=["POST"])
def delete(sno):
    todo = Todo.query.get_or_404(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Local dev only; Vercel will NOT run this
if __name__ == "__main__":
    app.run(debug=True)
