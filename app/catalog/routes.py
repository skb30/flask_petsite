
# since we don't have access to the flask app at the global level
# we must use the blueprint
from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm


@main.route('/')
def display_books():

    books = Book.query.all()
    return  render_template('home.html', books=books) # pass books instance

@main.route('/display/publisher/<pub_id>') # anything between <> is passed as an arg
def display_publisher(pub_id):

  # do the db query using the pub_id passed from the browser.
    # get the pub id that was passed from home.html
    publisher = Publication.query.filter_by(pub_id=pub_id).first()
    # get all books with that id
    publisher_books = Book.query.filter_by(pub_id=publisher.pub_id).all()

    # pass publisher and publisher books to the html
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        msg = 'book with id of ' + book_id + ' deleted successfully'
        flash(msg)
        return redirect(url_for('main.display_books'))
    # get request
    return  render_template('delete_book.html', book=book, book_id=book.id)

@main.route('/edit/book/<book_id>', methods=['GET','POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    # post request
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        msg = 'book edited successfully'
        flash(msg)
        return redirect(url_for('main.display_books'))
    # get request
    return  render_template('edit_book.html', form=form)