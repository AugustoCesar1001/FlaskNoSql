from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost/Flask_Application'
mongo = PyMongo(app)
api = Api(app)



from .models import user, mongodb
from .routes import routes