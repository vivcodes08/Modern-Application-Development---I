from config import db


class Venue(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    capacity=db.Column(db.Integer)
    address=db.Column(db.String(1000))
    city=db.Column(db.String(100))
    image=db.Column(db.String(2000))
    poster=db.Column(db.String(2000))
    description=db.Column(db.String(200))
    pincode=db.Column(db.Integer)
    ratings=db.Column(db.String(20))
    