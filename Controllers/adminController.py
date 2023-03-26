from flask import Blueprint,request,jsonify,render_template,make_response,flash,redirect,session,url_for
from config import db
from models.Show import Show
from models.User import User
from models.Venue import Venue
from models.Show import Show
from werkzeug.security import generate_password_hash,check_password_hash
import re
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
        if(userDetails['role'] != 'Admin'):
             return render_template('Admin/404.html')
        venueList=Venue.getAllVenue()

        return render_template('Admin/show.html', userDetails=userDetails,venueList=venueList)
    elif request.method == 'POST':
         return ""


@adminBluePrint.route('/venue', methods=['GET','POST'])
def venue():
    if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        if(userDetails['role'] != 'Admin'):
             return render_template('Admin/404.html')

        return render_template('Admin/venue.html', userDetails=userDetails)    

@adminBluePrint.route('/home')
def home():
    venueList=Venue.getAllVenue();
    print("VenueList")
    print(venueList)
    name=request.cookies.get('userDetails');
    userDetails=cookietoDict(name)
    if(userDetails['role'] != 'Admin'):
             return render_template('Admin/404.html')
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
        if(userDetails['role'] != 'Admin'):
             return render_template('Admin/404.html')
        venue=Venue.getAllVenue(venueId)[0]
        print("Venue In Update Venue\n", venue)
        return render_template('Admin/updateVenue.html',venue=venue, userDetails=userDetails)
     elif (request.method=='POST'):
            res=Venue.updateVenue(venueId,request.form)
            return redirect('/admin/home')
     
showTimings={
     "Morning":"9:00 AM - 12:00 PM",
     "Afternoon":"2:00 PM - 5:00 PM ",
     "Night":"7:00 PM - 10:00 PM"

}


@adminBluePrint.route('/updateShow/<showId>', methods=['GET','POST'])
def updateShow(showId):
      if request.method=='GET':
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        if(userDetails['role'] != 'Admin'):
             return render_template('Admin/404.html')
        show=Show.getShowByShowId(showId)[0]
        print("Show In Update Show\n", show)
        timings=showTimings[show['timings']]
        print("Timings --", timings)

        venueList=Venue.getAllVenue()
        current_venue=Venue.getAllVenue(show['venue'])[0]['name']
        print("current_venue---", current_venue)
        
        return render_template('Admin/updateShow.html',show=show, userDetails=userDetails, venueList=venueList,timings=timings, current_venue=current_venue)
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
        
        if(re.search("'",email) or re.search('"', email) ):
            flash("Invalid EmailD !! Only Alphanumeric Email Id's are Allowed", 'error')
            return redirect(url_for('adminBluePrint.login'))
        
        
        if User.find_user(email,'find'):
            user=User.find_user(email,'detail')
            passTest=check_password_hash(user.password, password)
            if(user.role!='Admin'):
                flash("You don't have Admin Privileges")
                return redirect(url_for('adminBluePrint.login'))
            
            if passTest:
                    userObj={
                        'id':user[0],
                        'email':user[1],
                        'name':user[3],
                        'role':user[4]
                    }
                    print(userObj)
                    
                    response=make_response(redirect('/admin/home'))
                    userdetails=f"id:{userObj['id']}|name:{userObj['name']}|email:{userObj['email']}|role:{userObj['role']}"
                    response.set_cookie('userDetails', userdetails )
                    print('userDetails', userdetails)
                    
                    session['userDetails']=userObj
                    return response

            else:
                flash("Invalid Password", 'error')
                return redirect(url_for('adminBluePrint.login'))

        else:
              flash("Invalid Email Id", 'error')
              return redirect(url_for('adminBluePrint.login'))  
        

