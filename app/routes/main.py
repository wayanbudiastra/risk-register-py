
from flask import Blueprint, url_for, redirect, render_template
from app.routes.auth import auth_bp 

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
     return render_template('auth/login.html')

@main_bp.route('/dashboard')
def dashboard():
    return "Halaman Dashboard"

