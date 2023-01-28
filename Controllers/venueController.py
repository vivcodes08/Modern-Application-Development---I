from flask import Blueprint,request
from config import db,app
from models.Venue import Venue
from datetime import datetime
venueBluePrint=Blueprint('venueBluePrint',__name__,url_prefix='/venue')

@venueBluePrint.route('/')
def createVenueForm():
    return "Welcome to the Venue"

@venueBluePrint.route('/createVenue', methods=['POST'])
def createVenue():
    if request.method=='POST':
        print("Form data\n",request.form)
        new_venue=Venue(
            name=request.form.get('name'),
            capacity=request.form.get('capacity'),
            address=request.form.get('address'),
            city=request.form.get('city'),
            image=request.form.get('image'),
            poster=request.form.get('poster'),
            description=request.form.get('description'),
            pincode=request.form.get('pincode'),
            ratings=request.form.get('ratings')
        )

        db.session.add(new_venue)
        db.session.commit()

        return "Venue created successfully"
