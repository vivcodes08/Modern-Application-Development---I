from config import db


class Show(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Integer)
    tags=db.Column(db.String(1000))
    image=db.Column(db.String(2000))
    venue=db.Column(db.Integer)
    capacity=db.Column(db.Integer)
    languages=db.Column(db.String(200))
    length=db.Column(db.TIME)
    timings=db.Column(db.String(100))
    ratings=db.Column(db.String(20))

    @staticmethod
    def showExists(id):
        show=db.get_or_404(Show,id)
        isExist=isinstance(show,Show)
        return isExist;

    @staticmethod
    def getShowByName(name=""):
        res=db.engine.execute(f"Select * from Show where name like '%{name}%'")
        result=res.fetchall()
        shows=[]
        for i in result:
            dict={
                'id':i[0],
                'name':i[1],
                'price':i[2],
                'tags':i[3],
                'image':i[4],
                'venue':i[5],
                'description':i[6],
                'language':i[7],
                'length':i[8],
                'releaseDate':i[9],
                'ratings':i[10]
            }
            shows.append(dict)

        return shows

    @staticmethod
    def getShowByVenueId(venueId):
        res=db.engine.execute(f"Select * from Show where venue ={venueId}")
        result=res.fetchall()
        shows=[]
        for i in result:
            dict={
                'id':i[0],
                'name':i[1],
                'price':i[2],
                'tags':i[3],
                'image':i[4],
                'venue':i[5],
                'capacity':i[6],
                'language':i[7],
                'length':i[8],
                'timings':i[9],
                'ratings':i[10]
            }
            shows.append(dict)

        return shows

    @staticmethod
    def getShowByShowId(showId):
        res=db.engine.execute(f"Select * from Show where id ={showId}")
        result=res.fetchall()
        shows=[]
        for i in result:
            dict={
                'id':i[0],
                'name':i[1],
                'price':i[2],
                'tags':i[3],
                'image':i[4],
                'venue':i[5],
                'capacity':i[6],
                'language':i[7],
                'length':i[8],
                'timings':i[9],
                'ratings':i[10]
            }
            shows.append(dict)

        return shows   
   

    @staticmethod
    def deleteShow(showId,venueId):
        sql=f"delete from show where id={showId} and venue={venueId}"
        print("SQL Delete Query\n",sql)
        res=db.engine.execute(sql)
        print(res)
        return res;      

    @staticmethod
    def updateShow(id, newShow):
         name=newShow['name'].replace("'", "''")
         language=newShow['language'].replace("'","''")
         image=newShow['image'].replace("'","''")
         tags=newShow['tags'].replace("'","''")
         sql=f"Update show set name='{name}' ,ratings='{newShow['ratings']}' ,languages='{language}' ,price={newShow['price']}, image='{image}',  tags='{tags}' where id={id}"   
         res=db.engine.execute(sql)
         return 0;   
            


       

