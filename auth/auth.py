from flask import Blueprint, request,render_template,url_for,make_response,session, redirect
from config import db
from models.User import User
from werkzeug.security import generate_password_hash,check_password_hash

authBluePrint=Blueprint('authBluePrint', __name__)
from flask_login import current_user,login_required
from config import loginManager
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
        
        user_exist=User.find_user(email, 'find')
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
                    response=make_response(render_template('Users/home.html', name=userObj['name']))
                    userdetails=f"name:{userObj['name']}|email:{userObj['email']}|role:{userObj['role']}"
                    print('userDetails', userdetails)
                    response.set_cookie('userDetails', userdetails )
                    session['userDetails']=userObj
                    return response

            else:
                return "Invalid Password"

        else:
            return "Invalid Email"        