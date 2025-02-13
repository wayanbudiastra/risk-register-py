from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Inisialisasi database dan bcrypt untuk hashing password
db = SQLAlchemy()
bcrypt = Bcrypt()

# Import model agar bisa diakses di seluruh aplikasi
from app.models.user import User

