from flask import redirect,flash,url_for
import re
def signupvalidator(name,email,password):
    print("Inside the sign validatore function ")
    if (len(name) <4):
            return "Username should have more than 4 characters"

    elif (len(password) <8):
            return "Password should have more than 8 characters"
            
    
    elif not re.search(r'[A-Z]', password):
            return "Password should at least contain  1  uppercase characters"
            
    
    elif not re.search(r'[a-z]', password):
            return "Password should at least contain  1  lowercase characters"
    
    elif not re.search("'",email):
           print("inside the comma blocj")
           return "Invalid EmailD !! Only Alphanumeric Email Id's are Allowed"            
    else:
           return ""
     