from app import app, db, mail
from flask import render_template, request, flash, redirect, url_for
from forms import RegisterForm
from models import User
from flask_security.core import current_user




@app.route('/')
def login():
    if current_user:
        return redirect('/user_page')
    return redirect(url_for('security.login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('security.login'))
    return redirect(url_for('security.register'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


