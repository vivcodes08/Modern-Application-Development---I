from flask import Blueprint, request
from config import db
from models.User import User
from werkzeug.security import generate_password_hash,check_password_hash

authBluePrint=Blueprint('authBluePrint', __name__)

@authBluePrint.route('/auth/<string:email>')
def check_user(email):
    user_exist=User.find_user(email)
    if user_exist:
        return "User Already exist"
    else:
        return "User Do not exists"    



@authBluePrint.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return "Welcome to the Sign Up Page"
    elif(request.method == 'POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        
        user_exist=User.find_user(email)
        if user_exist:
            return "Email Id Already Exists"
        new_user=User(
            name=name,
            email=email,
            password=generate_password_hash(password,method='sha256'),
            role='User'

        )

        db.session.add(new_user)
        db.session.commit()
        return "User created Successfully"


@authBluePrint.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return "Welcome to the MovieApp"
    elif request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        stayLogin=True if request.form.get('stayLogin') else False
        
        if User.find_user(email,'find'):
            user=User.find_user(email,'detail')
            passTest=check_password_hash(user.password, password)
            if passTest:
                return "Successfully Logined"

            else:
                return "Invalid Password"

        else:
            return "Invalid Email"        