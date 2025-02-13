from flask import Blueprint

# Import semua Blueprint dari file route yang ada
from .auth import auth_bp
from .main import main_bp
from .admin import admin_bp

# Fungsi untuk mendaftarkan Blueprint ke aplikasi Flask
def init_routes(app):
    """
    Mendaftarkan semua Blueprint ke aplikasi Flask.

    :param app: Instance Flask aplikasi.
    """
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)