from flask import Blueprint,request
from config import db,app
from models.Show import Show
from datetime import datetime
showBluePrint=Blueprint('showBluePrint',__name__,url_prefix='/show')

@showBluePrint.route('/')
def createShowForm(id):
    return "Welcome to create Show Form"

@showBluePrint.route('/createShow', methods=['POST'])
def createShow():
    if request.method=='POST':
        print("Form data\n",request.form)
        new_show=Show(
            name=request.form.get('name'),
            price=request.form.get('price'),
            tags=request.form.get('tags'),
            image=request.form.get('image'),
            poster=request.form.get('poster'),
            description=request.form.get('description'),
            languages=request.form.get('languages'),
            length=datetime.strptime(request.form.get('length'),'%H:%M:%S').time(),
            releaseDate=datetime.strptime(request.form.get('releaseDate'),'%m-%d-%Y').date(),
            ratings=request.form.get('ratings')
        )
        
        db.session.add(new_show)
        db.session.commit()

        return "Show created successfully"
