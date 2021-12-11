from app import app, db
from flask import render_template, request, flash, redirect, url_for
from forms import RegisterForm
from models import User
from flask_security.core import current_user



@app.route('/')
def login():
    if current_user:
        return redirect('/user_page')
    return redirect(url_for('security.login'))

@app.route('/register')
def register():
    return redirect(url_for('security.register'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


