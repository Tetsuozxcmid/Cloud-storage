from app.main import db
from app.models import User

class Object(db.Model):
    __tablename__ = 'objects'
    id = db.Column(db.Integer,primary_key=True)
    
    filename = db.Column(db.String)
    data = db.Column(db.LargeBinary, nullable=False)
    user_name = db.Column(db.String, db.ForeignKey('users.name'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<User - {self.filename}'
    
    def get_id(self):
        return self.id