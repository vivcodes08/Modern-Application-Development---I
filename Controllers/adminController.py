from flask import Blueprint,request,jsonify,render_template,make_response,redirect,session
from config import db
from models.Show import Show
from models.User import User
from models.Venue import Venue
from models.Show import Show
from werkzeug.security import generate_password_hash,check_password_hash
adminBluePrint=Blueprint('adminBluePrint',__name__ ,url_prefix='/admin')

def cookietoDict(cString):
      array=cString.split("|")
      userDetails={}
      for i in array:
            (key,value)=i.split(":")
            userDetails[key]=value
      return userDetails   

@adminBluePrint.route('/show', methods=['GET','POST'])
def show():
    if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        venueList=Venue.getAllVenue()

        return render_template('Admin/show.html', userDetails=userDetails,venueList=venueList)
    elif request.method == 'POST':
         return ""


@adminBluePrint.route('/venue', methods=['GET','POST'])
def venue():
    if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)

        return render_template('Admin/venue.html', userDetails=userDetails)    

@adminBluePrint.route('/home')
def home():
    venueList=Venue.getAllVenue();
    print("VenueList")
    print(venueList)
    name=request.cookies.get('userDetails');
    userDetails=cookietoDict(name)
    return render_template('Admin/home.html',  userDetails=userDetails, venueList=venueList)

@adminBluePrint.route('/deleteShow/<showId>/<venueId>' ,methods=['GET'])
def deleteShow(showId,venueId):
        res=Show.deleteShow(showId,venueId)
        return redirect(f'/show/editShow/{venueId}')

@adminBluePrint.route('/deleteVenue/<venueId>', methods=['GET'])
def deleteVenue(venueId):
    res=Venue.deleteVenueById(venueId)
    return redirect('/admin/home')

@adminBluePrint.route('/updateVenue/<venueId>', methods=['GET', 'POST'])
def updateVenue(venueId):
     if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        venue=Venue.getAllVenue(venueId)[0]
        print("Venue In Update Venue\n", venue)
        return render_template('Admin/updateVenue.html',venue=venue, userDetails=userDetails)
     elif (request.method=='POST'):
            res=Venue.updateVenue(venueId,request.form)
            return redirect('/admin/home')
     

@adminBluePrint.route('/updateShow/<showId>', methods=['GET','POST'])
def updateShow(showId):
      if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        show=Show.getShowByShowId(showId)[0]
        print("Show In Update Show\n", show)
        venueList=Venue.getAllVenue()
        return render_template('Admin/updateShow.html',show=show, userDetails=userDetails, venueList=venueList)
      elif(request.method == 'POST'):
           res=Show.updateShow(showId,request.form)
           return redirect('/admin/home')

@adminBluePrint.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method=='GET':
            return render_template('Admin/login.html')
    elif request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        stayLogin=True if request.form.get('stayLogin') else False
        
        if User.find_user(email,'find'):
            user=User.find_user(email,'detail')
            passTest=check_password_hash(user.password, password)
            if(user.role!='Admin'): return "Your are not Admin"
            if passTest:
                    userObj={
                        'id':user[0],
                        'email':user[1],
                        'name':user[3],
                        'role':user[4]
                    }
                    print(userObj)
                    
                    response=make_response(redirect('/admin/home'))
                    userdetails=f"name:{userObj['name']}|email:{userObj['email']}|role:{userObj['role']}"
                    response.set_cookie('userDetails', userdetails )
                    print('userDetails', userdetails)
                    
                    session['userDetails']=userObj
                    return response

            else:
                return "Invalid Password"

        else:
            return "Invalid Email"    
        

