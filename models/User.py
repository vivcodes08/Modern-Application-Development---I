from config import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100), nullable=False)
    name=db.Column(db.String(100))
    role=db.Column(db.String(20))


    @staticmethod
    def find_user(email, flag):
       res=db.engine.execute(f"Select * from User where email='{email}'")
       result=res.fetchall()
       print(result)
       found=len(result)
       print(found)

       if flag=='find':
          if found>0:
               return [True, result]
          else:
                return False    
       elif flag=='detail':
           if found>0:
               return result[0]
       else:
               return "Please Provide a revalant Flag"    
             
    
