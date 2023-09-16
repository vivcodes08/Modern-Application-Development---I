from config import db


class Venue(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    capacity=db.Column(db.Integer)
    address=db.Column(db.String(1000))
    city=db.Column(db.String(100))
    image=db.Column(db.String(2000))
    poster=db.Column(db.String(2000))
    description=db.Column(db.String(200))
    pincode=db.Column(db.Integer)
    ratings=db.Column(db.String(20))

    @staticmethod
    def getAllVenue(Id=0):
        print("ID in getAllVenue is " , Id)
        sql=""
        if (Id!=0):
                sql=f"select * from venue where id={Id}"
        else:
             sql="select * from venue"        

        res=db.engine.execute(sql)
        result=res.fetchall()
        venues=[]
        for i in result:
            dict={
                'id':i[0],
                'name':i[1],
                'capacity':i[2],
                'address':i[3],
                'city':i[4],
                'image':i[5],
                'poster':i[6],
                'description':i[7],
                'pincode':i[8],
                'ratings':i[9]
            }
            venues.append(dict)
        return venues
    
    @staticmethod
    def deleteVenueById(venueId):
        sql=f"delete from venue where id={venueId}"
        sql2=f"delete from show where venue={venueId}"

        print("Delete venue Query \n", sql)
        print("Delete Show By VenueId\n", sql2)

        res1=db.engine.execute(sql2)
        res=db.engine.execute(sql)
        

        return 0;

    @staticmethod
    def updateVenue(id, newVenue):
         name=newVenue['name'].replace("'", "''")
         address=newVenue['address'].replace("'","''")
         image=newVenue['image'].replace("'","''")
         city=newVenue['city'].replace("'","''")
         sql=f"Update venue set name='{name}' , address='{address}' ,capacity={newVenue['capacity']}, image='{image}', pincode={newVenue['pincode']} , city='{city}' where id={id}"   
         res=db.engine.execute(sql)
         return 0;   
    @staticmethod
    def getCapacityByVenueId(venueId):
         
         sql=f"select capacity from venue where id={venueId}"
         res=db.engine.execute(sql)
         capacity=[]
         for i in res:
            dict={
                   "capacity":i[0]
              }
            capacity.append(dict) 
         print(capacity)
         return capacity[0]['capacity']

