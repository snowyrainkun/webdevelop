import os

import requests
from flask import Flask, session, render_template, jsonify, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# api
res = requests.get("https://www.goodreads.com/book/review_counts.json",
                   params={"key": "KEY", "isbns": "9781632168146"})
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# flask login
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    return render_template("layout.html")
