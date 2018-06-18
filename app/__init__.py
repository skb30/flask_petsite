# app/__init__.py


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# init 3rd party packages
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager() # provides session mgmt for Flask.  Handles common user auth tasks.
# let the flask login mgr know what function we are using to log the user in
login_manager.login_view = 'authentication.do_the_login'
# security - protect sensitive data
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

# application factory
def create_app(config_type):

    app = Flask(__name__)

    # build the path to the selected config file
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    # load the configuration into our app
    app.config.from_pyfile(configuration)

    # intialize bootstrap by passing the flask app to bootstrap
    bootstrap.init_app(app)
    # setup login
    login_manager.init_app(app) #initialize lg mgr
    bcrypt.init_app(app) # init secuirty SSL

    # link db to our app
    db.init_app(app) # bind database to flask

    # tell Flask we're using a blueprint. note: main is defined in catalog/__init__.py package
    # from app.catalog import main
    # app.register_blueprint(main) # register the blueprint
    # register the auth blueprint
    from app.auth import authentication
    app.register_blueprint(authentication)

    # register the pets blueprint
    from app.pet_site import pets
    app.register_blueprint(pets)

    return app

# don't be confused with all the __init__.py files. we create blueprints inside the
# subpackages (auth and catalog) and register blueprints with the top level
# root package which is the app folder
#