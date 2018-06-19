# flask_wtf is the module and FlaskForm is the class
from flask_wtf import FlaskForm
# import form fields
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# check to see if the email is already in the DB

def check_email(form, field):
    # build the query and call the DB
    email = User.query.filter_by(email=field.data).first()

    if email:
        raise ValidationError('Email Already Exists')

# inherits FlaskForm
class RegistrationForm(FlaskForm):
    name = StringField('Name ', validators=[DataRequired(),Length(3,40, message='between 3 to 40 characters')])
    email = StringField("E-mail", validators=[DataRequired(), Email(), check_email])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm',validators=[DataRequired()])

    submit =SubmitField('Register')

# inherits FlaskForm
class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')

    submit =SubmitField('LogIn')
