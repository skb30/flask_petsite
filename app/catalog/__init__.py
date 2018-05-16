
# app/catalog/__init__.py

from flask import Blueprint
# let's blueprint know where the html files are
main = Blueprint('main', __name__, template_folder='templates')

# instead of writing our routes code here, we import it. This keeps it segregated.
# also, we import it at the bottom to avoid a circular references
from app.catalog import routes