from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app=Flask(__name__)

db=SQLAlchemy()
app.config['SECRET_KEY']='vivek@123'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
db.init_app(app)


# with app.app_context():
#     db.create_all()
loginManager=LoginManager()
loginManager.init_app(app)

