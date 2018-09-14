from flask import render_template
from app import app, db
from app.models import Va


@app.route('/')
def home():
    va = Va.query.all()
    return render_template('home.html', va=va)
