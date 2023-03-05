from flask import Blueprint,request, render_template
from config import db,app
from models.Show import Show
from datetime import datetime
showBluePrint=Blueprint('showBluePrint',__name__,url_prefix='/show')
from models.User import User
from flask_login import current_user,login_required

def cookietoDict(cString):
      array=cString.split("|")
      userDetails={}
      for i in array:
            (key,value)=i.split(":")
            userDetails[key]=value
      return userDetails   


@showBluePrint.route('/')
def createShowForm():
    print(current_user.name)
    return current_user;

@showBluePrint.route('/createShow', methods=['POST'])
def createShow():
    if request.method=='POST':
        print("Form data\n",request.form)
        new_show=Show(
            name=request.form.get('name') ,
            price=request.form.get('price'),
            tags=request.form.get('tags'),
            image=request.form.get('image'),
            venue=request.form.get('venue') ,
            description=request.form.get('description') or "",
            languages=request.form.get('language')or " ",
            length=datetime.strptime(request.form.get('length'),'%H:%M').time(),
            # releaseDate=datetime.strptime(request.form.get('releaseDate'),'%m-%d-%Y').date() 
            ratings=request.form.get('ratings')
        )
        
        db.session.add(new_show)
        db.session.commit()

        return "Show created successfully"



@showBluePrint.route('/editShow/<venueId>', methods=['GET'])
def getShowByVenueId(venueId):
    venueId=int(venueId)
    showList=Show.getShowByVenueId(venueId);
    name=request.cookies.get('userDetails');
    userDetails=cookietoDict(name)

    return render_template('Admin/editshow.html', userDetails=userDetails, showList=showList)
