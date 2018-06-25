# import the db instance from app
from app import db
from datetime import datetime


class Pet(db.Model):

    __tablename__ = 'petprofile'

    age = 0
    # Relationship
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Data
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)
    neutered = db.Column(db.String(3), nullable=False)
    sex = db.Column(db.String(10))
    exercise = db.Column(db.Text)
    feeding = db.Column(db.Text)
    notes = db.Column(db.Text)
    vetinfo = db.Column(db.Text)
    phone = db.Column(db.String(20))
    image = db.Column(db.String(100), unique=True),
    birthdate = db.Column(db.DateTime)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, owner,
                 phone,
                 name,
                 breed,
                 sex,
                 neutered,
                 vetinfo,
                 feeding,
                 exercise,
                 notes,
                 birthdate): # class constructor
        self.owner = owner
        self.phone = phone
        self.name = name
        self.breed = breed
        self.sex = sex
        self.neutered = neutered
        self.vetinfo = vetinfo
        self.feeding = feeding
        self.exercise = exercise
        self.notes = notes
        self.birthdate = birthdate
        self.rating = 0.0

    def __repr__(self):
        return '{} by {}'.format(self.name, self.register_date)

