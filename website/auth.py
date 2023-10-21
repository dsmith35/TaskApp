from flask import Blueprint, render_template
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register():
    return render_template("login.html", user=current_user)

@auth.route('/login')
def login():
    return render_template("register.html", user=current_user)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"