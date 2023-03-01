from flask import Blueprint,request,jsonify
from config import db
from models.Show import Show
homeBluePrint=Blueprint('homeBluePrint',__name__)

@homeBluePrint.route('/search' ,methods=[ 'POST'])
def search():
    if request.method == 'POST':
        name=request.form["searchtext"]
        res=Show.getShowByName(name)
        print("Home Result\n", res)

        return res;