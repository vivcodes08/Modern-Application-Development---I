from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

db=SQLAlchemy()
app.config['SECRET_KEY']='vivek@123'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
db.init_app(app)
