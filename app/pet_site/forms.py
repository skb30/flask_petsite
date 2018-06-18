from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, RadioField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.fields.html5 import DateField, DateTimeField
from app.auth.models import User



class CreatePetForm(FlaskForm):
    #owner_id = IntegerField('Owner ID', validators=[DataRequired()])
    owner = StringField('Owner Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Pet Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    sex = RadioField('Sex', choices=[('male', 'Male'), ('female', 'Female')])
    neutered = RadioField('Neutered', choices=[('yes', 'Neutered/Spade (Yes)'),
                                               ('no', 'Neutered/Spade (No)' )],
                                                default='yes', validators=[DataRequired()])
    # rating = FloatField('Rating', validators=[DataRequired()])
    vetinfo  = StringField('Vet Contact Information', validators=[DataRequired()])
    feeding  = StringField('Feeding Instructions', validators=[DataRequired()])
    exercise  = StringField('Exercise Instructions', validators=[DataRequired()])
    notes  = StringField('Other information I should know', validators=[DataRequired()])
    dob  = DateField('Pets Date Of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    # dropOff  = DateTimeField('Drop Off Date and Time', format='%H:%M:%S', validators=[DataRequired()])
    # pickUp  = DateTimeField('Pickup Date and Time', format='%H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Register Your Pet')

class SimpleForm(FlaskForm):
    example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])

class EditPetForm(FlaskForm):
    owner = StringField('Owner Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Pet Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit      = SubmitField('Update')