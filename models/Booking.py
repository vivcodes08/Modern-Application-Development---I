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
    
    @staticmethod
    def  reviewRatingUpdate(bookId, review, ratings):

        sql=f"Update booking  set review='{review}' , ratings={ratings}  where id={bookId}"
        res=db.engine.execute(sql)
        book=Booking.query.filter_by(id=bookId).first()
        sql2=sql2=f"SELECT  sum(ratings) as sum ,count(*) as count from booking WHERE show_id={book.show_id}"
        res2=db.engine.execute(sql2)
        sum=0
        count=1
        for x in res2:
            sum=x[0]
            count=x[1]

        avg_ratings=sum/count
        stravg=str(avg_ratings)

        sql3=f"Update show set ratings='{stravg}' where id={book.show_id}"  
        res3=db.engine.execute(sql3)  
        return ""