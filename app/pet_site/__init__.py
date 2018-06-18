
# app/pet_site/__init__.py

from flask import Blueprint

pets = Blueprint('pets', __name__, template_folder='templates')

from app.pet_site import routes
