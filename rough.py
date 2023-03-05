a="name:vivek|email:vivek@gmail.com|role:Admin"

array=a.split("|")
userDetails={}

for i in array:
    (key,value)=i.split(":")
    userDetails[key]=value

print(userDetails)    