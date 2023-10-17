from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from config import Config

app = Flask(__name__)
#app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/item'

db = SQLAlchemy(app)
db.init_app(app)

from app import views