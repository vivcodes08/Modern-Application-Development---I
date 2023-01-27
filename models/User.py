from config import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100), nullable=False)
    name=db.Column(db.String(100))
    role=db.Column(db.String(20))