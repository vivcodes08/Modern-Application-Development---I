from config import app,db
from models import Show,Venue,ShowVenue,User
from Controllers.showController import showBluePrint 
# with app.app_context():
#     db.create_all()

app.register_blueprint(showBluePrint)
app.run(debug=True)