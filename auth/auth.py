from flask import Blueprint, request,render_template,url_for,make_response,session, redirect, flash
from config import db
from models.User import User
from werkzeug.security import generate_password_hash,check_password_hash
from .functions import signupvalidator
authBluePrint=Blueprint('authBluePrint', __name__)
from flask_login import current_user,login_required
from config import loginManager
import re
loginManager.login_view='login'
@loginManager.user_loader
def load_user(user_id):
        try:
            print('Inside User Loader Function')
            return User.query.get(int(user_id))
        except:
            return None

@authBluePrint.route('/auth/<string:email>')
def check_user(email):
    user_exist=User.find_user(email)
    if user_exist:
        return "User Already exist"
    else:
        return "User Do not exists"    



@authBluePrint.route('/register', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('Users/register.html')
    elif(request.method == 'POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        
        if(re.search("'",email) or re.search('"', email) ):
            flash("Invalid EmailD !! Only Alphanumeric Email Id's are Allowed", 'error')
            return redirect(url_for('authBluePrint.signup'))

        user_exist=User.find_user(email, 'find')
        if user_exist:
            flash("Email Id Already Exist",'error')
            return redirect(url_for('authBluePrint.signup'))
        
        err=signupvalidator(name,email,password)
        if(err!=""):
            flash(err,'error')
            return redirect(url_for('authBluePrint.signup'))
        

        
        new_user=User(
            name=name,
            email=email,
            password=generate_password_hash(password,method='sha256'),
            role='User'

        )

        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')


@authBluePrint.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('Users/login.html')
    elif request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        stayLogin=True if request.form.get('stayLogin') else False
        
        if User.find_user(email,'find'):
            user=User.find_user(email,'detail')
            passTest=check_password_hash(user.password, password)
            if passTest:
                    userObj={
                        'id':user[0],
                        'email':user[1],
                        'name':user[3],
                        'role':user[4]
                    }
                    print(userObj)
                    
                    response=make_response(redirect('/home'))
                    userdetails=f"id:{userObj['id']}|name:{userObj['name']}|email:{userObj['email']}|role:{userObj['role']}"
                    response.set_cookie('userDetails', userdetails )
                    print('userDetails', userdetails)
                    
                    session['userDetails']=userObj
                    return response

            else:
                flash("Invalid Password", 'error')
                return redirect(url_for('authBluePrint.login'))

        else:
            flash("Invalid Email Id", 'error')
            return redirect(url_for('authBluePrint.login'))        