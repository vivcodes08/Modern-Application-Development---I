from config import app,db
from models import Show,Venue,ShowVenue,User
from Controllers.showController import showBluePrint 
from Controllers.venueController import venueBluePrint
from Controllers.homeController import homeBluePrint
from Controllers.adminController import adminBluePrint
from auth.auth import authBluePrint
# with app.app_context():
#     db.create_all()

app.register_blueprint(showBluePrint)
app.register_blueprint(venueBluePrint)
app.register_blueprint(authBluePrint)
app.register_blueprint(homeBluePrint)
app.register_blueprint(adminBluePrint)
app.run(debug=True)