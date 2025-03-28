from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.orm import relationship
from app.main import db

bcrypt = Bcrypt()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def get_token(self, expire_time=None):
        token = create_access_token(
            identity=self.id,
            expires_delta=expire_time
        )
        return token

    @classmethod
    def authenticate(cls, name, password):
        user = cls.query.filter_by(name=name).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            raise Exception('No user with this password')
        return user


