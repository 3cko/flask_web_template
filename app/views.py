from flask import render_template, flash, redirect, session, url_for
from app import app, db
from models import User

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template("index.html",
        title = 'index',
        test = 'Hello World',
        )
