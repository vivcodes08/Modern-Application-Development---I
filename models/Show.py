from config import db


class Show(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Integer)
    tags=db.Column(db.String(1000))
    image=db.Column(db.String(2000))
    poster=db.Column(db.String(2000))
    description=db.Column(db.String(200))
    languages=db.Column(db.String(200))
    length=db.Column(db.TIME)
    releaseDate=db.Column(db.DATE)
    ratings=db.Column(db.String(20))

    @staticmethod
    def showExists(id):
        show=db.get_or_404(Show,id)
        isExist=isinstance(show,Show)
        return isExist;

    @staticmethod
    def getShowByName(name):
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
                'poster':i[5],
                'description':i[6],
                'language':i[7],
                'length':i[8],
                'releaseDate':i[9],
                'ratings':i[10]
            }
            shows.append(dict)

        return shows    


            


       

