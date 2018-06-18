import os

debug = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:hje000sb@localhost/catalog_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False