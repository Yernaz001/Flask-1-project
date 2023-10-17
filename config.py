import os

class Config:
    SECRET_KEY = os.environ.get('YOUR_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://postgres:123@localhost:5432/item')
    SQLALCHEMY_TRACK_MODIFICATIONS = False