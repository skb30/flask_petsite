from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc

# if __name__ == '__main__':

# use our app factory to create the app
flask_app = create_app('prod')


# tell flask to use the current app. remember with this scalable arch
# we can run several differnt instances of this app
with flask_app.app_context():
    db.create_all()


    # if user doesn't exist in db, then create it.
    if not User.query.filter_by(user_name='harry').first():
        # class method defined in models.py
        User.create_user(user='harry',
                         email='harry@potters.com',
                        password='secret')

    flask_app.run()