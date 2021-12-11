from flask import Blueprint, render_template


confirm_email = Blueprint('confirm_email', __name__, template_folder='templates')

@confirm_email.route('/')
def index():
    return "<center>Comfirm Email</center>"