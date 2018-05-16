from datetime import datetime
from app import login_manager
from app import db, bcrypt # app/__init__.py
from flask_login import UserMixin
from app import  login_manager

class User(UserMixin, db.Model): # UserMixin extention allows us to use the db tables

    # create a specail var that defines the table name
    __tablename__  = 'users'

    # define the schema
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40))
    email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)


    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)
    # class methods belong to a class but are not associated with any class instance
    @classmethod
    def create_user(cls, user, email, password): # cls instead of self because it's a class attribute not an instance

        # we get these vars when the user submits the form data
        user = cls(user_name=user,
                   email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8')
                   )
        db.session.add(user)
        db.session.commit()

        return user

# to load the active user session we need this call back function
@login_manager.user_loader
def load_user(id): # custom method
    # loads the user object from the DB
    return  User.query.get(int(id))