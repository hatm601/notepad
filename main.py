from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss

app = Flask(__name__)
app.secret_key = "super-secret-key"
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notepad.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        if not username:
            return render_template("login.html", error="Username required")
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        session["username"] = username
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        content = request.form.get("notepad", "")
        session["notepad"] = content.strip()
        return redirect("/")
    
    note = session.get("notepad", "")
    return render_template("home.html", note=note)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        content = request.form.get("notepad", "")
        session["notepad"] = content.strip()
        return redirect("/")
    note = session.get("notepad", "")
    return render_template("edit.html", note=note)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
