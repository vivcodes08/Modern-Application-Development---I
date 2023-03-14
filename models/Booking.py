from config import db


class Booking(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    show_id=db.Column(db.Integer)
    venue_id=db.Column(db.Integer)
    user_id=db.Column(db.Integer)
    price=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    total_amount=db.Column(db.Integer)
    review=db.Column(db.String(200))
    ratings=db.Column(db.Integer)
    bookedon=db.Column(db.TIMESTAMP, default=False)

    @staticmethod
    def getBookingsByUserId(userId):
        res=Booking.query.filter_by(user_id=userId).all()
        return res