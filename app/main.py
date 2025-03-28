from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from dotenv import load_dotenv

import os

load_dotenv()

bcrypt = Bcrypt()
jwt = JWTManager()

db = SQLAlchemy()
login_manager = LoginManager()

# Create the Flask app instance and configure it with SQLAlchemy and JWT extensions


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from handlers.routes import register_routes
    register_routes(app, db)

    login_manager.login_view = "login"
    migrate = Migrate(app, db, render_as_batch=True)

    return app


# Start the application
app = create_app()


@login_manager.user_loader
def load_user(user_id):
    from app.models.User import User
    return User.query.get(int(user_id))
