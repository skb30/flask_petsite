# import the db instance from app
from app import db
from datetime import datetime


class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.pub_id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, \
                pub_id): # class constructor
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


# create the model for Object Resource Mapping(ORM)
class Publication(db.Model): # inherit the Model class from alchemey


    __tablename_ = 'publication' # name of the table

    # use ORM to create the SQL
    pub_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) # can't be null

    def __init__(self, name): # class constructor

        self.name = name

    # this built-in creates a string version of the instance which
    # helps in producing a readable format of the output.
    # by using this built-in, you can create an instance
    # of Publication then execute that instance to get the
    # output string. e,g pub=Publication(11,'Oxford Publications')
    def __repr__(self):
        # create 2 place holders, name and id
        return 'Name is {} '.format(self.name)
