from flask import Blueprint,request
from config import db
from models.ShowVenue import ShowVenue
from datetime import datetime

svBluePrint=Blueprint('svBluePrint',__name__)

@svBluePrint.route('/')
def getShowVenueForm():
    return "this is showVenue Form"
    