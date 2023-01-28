from config import db


class ShowVenue(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    rule=db.Column(db.String(100))
    venueId=db.Column(db.Integer)
    date=db.Column(db.DATE)
    morningSlot=db.Column(db.Integer)
    afternoonSlot=db.Column(db.Integer)
    eveningSlot=db.Column(db.Integer)
    nightSlot=db.Column(db.Integer)