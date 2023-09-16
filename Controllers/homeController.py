from flask import Blueprint,request,jsonify,render_template, redirect
from config import db
from models.Show import Show
homeBluePrint=Blueprint('homeBluePrint',__name__)

@homeBluePrint.route('/search' ,methods=[ 'POST'])
def search():
    if request.method == 'POST':
        category=request.form["category"]
        name=request.form["searchtext"]
        print(request.form)
        res=Show.getShowByName(name,category)
        print("Home Result\n", res)
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)

        return render_template('Users/dashboard.html',showList=res, userDetails=userDetails);

def cookietoDict(cString):
      array=cString.split("|")
      userDetails={}
      for i in array:
            (key,value)=i.split(":")
            userDetails[key]=value
      return userDetails      


@homeBluePrint.route('/home')
def home():
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        print("UserDetails Cookies")
        print(userDetails)
        return render_template('Users/home.html', userDetails=userDetails)


      


@homeBluePrint.route('/dashboard')
def dashboard():
        showList= Show.getShowByName(name="", category="Show")
        print("ShowList\n", showList)
        name=request.cookies.get('userDetails');
        userDetails=cookietoDict(name)
        return render_template('Users/dashboard.html',showList=showList, userDetails=userDetails)

@homeBluePrint.route('/logout')
def logout():
      return redirect('/')



@homeBluePrint.route('/')
def base():
      return render_template('firstpage.html')