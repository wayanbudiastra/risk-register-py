from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Inisialisasi ekstensi
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    """
    Factory function untuk membuat instance Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inisialisasi ekstensi dengan aplikasi
    from app.models import db
    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Daftarkan Blueprint
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app