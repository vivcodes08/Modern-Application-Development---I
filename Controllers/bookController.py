from flask import Blueprint,redirect,render_template,request
from models.Booking import Booking
from config import db
from datetime import datetime
from models.Show import Show
from models.Venue import Venue
from models.Booking import Booking
from models.User import User
import json

bookBluePrint=Blueprint('bookBluePrint',__name__ ,url_prefix='/book')

def cookietoDict(cString):
      array=cString.split("|")
      userDetails={}
      for i in array:
            (key,value)=i.split(":")
            userDetails[key]=value
      return userDetails   

showTimings={
     "Morning":"9:00 AM - 12:00 PM",
     "Afternoon":"2:00 PM - 5:00 PM ",
     "Night":"7:00 AM - 10:00 PM"

}
@bookBluePrint.route('/' , methods=['GET', 'POST'])
def book():
    if request.method=='POST':
        print("Booking Data\n", request.form)
        datestr=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        datetime_object = datetime.strptime(datestr, "%d/%m/%Y %H:%M:%S")
        quantity=int(request.form.get('quantity'))
        price=int(request.form.get('price'))
        total_amount=quantity*price
        showId=request.form['show_id']
        quantity=request.form['quantity']
        new_booking=Booking(
            show_id=request.form.get('show_id'),
            venue_id=request.form.get('venue_id'),
            user_id=int(request.form.get('user_id')),
            price=price,
            quantity=quantity,
            total_amount=total_amount,
            bookedon=datetime_object
        )
        
        db.session.add(new_booking)
        db.session.commit() 
        Show.updateSeats(showId,quantity)
        return "Booked Successfully"
    

@bookBluePrint.route('/<showId>', methods=['GET'] )
def bookNow(showId):
    showDetails=Show.getShowByShowId(int(showId))[0]
    venueDetails = db.get_or_404(Venue, showDetails['venue'])
    name=request.cookies.get('userDetails');
    userDetails=cookietoDict(name)
    return render_template('Users/book.html', userDetails=userDetails, showDetails=showDetails, venueDetails=venueDetails)  

@bookBluePrint.route('/review', methods=['POST'])
def review():
     bookId=int(request.form.get('id'))
     review=request.form.get('review')
     ratings=int(request.form.get('default-radio'))
     
     Booking.reviewRatingUpdate(bookId, review,ratings)
     return ""


@bookBluePrint.route('/myrequest/<userId>',methods=['GET'])
def myRequest(userId):
     name=request.cookies.get('userDetails');
     userDetails=cookietoDict(name)
     mybookings=Booking.getBookingsByUserId(userId)
     mybookinglist=[]
     userDetails=db.get_or_404(User, userId)
     for x in mybookings:
          ticket={}
          showDetails=Show.getShowByShowId(x.show_id)[0]
          venueDetails = db.get_or_404(Venue, x.venue_id)
          ticket['id']=x.id;
          ticket['showName']=showDetails['name']
          ticket['userName']=userDetails.name
          ticket['venue']=venueDetails.name
          ticket['timings']=showTimings[showDetails['timings']]
          ticket['price']=showDetails['price']
          ticket['quantity']=x.quantity
          ticket['total_amount']=x.total_amount
          ticket['bookedon']=x.bookedon

          mybookinglist.append(ticket)


     print(mybookinglist)      
     return render_template('Users/mybooking.html',tlist=mybookinglist, userDetails=userDetails)