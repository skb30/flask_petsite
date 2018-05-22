from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User
from app.auth.forms import LoginForm


@at.route('/register', methods = ['POST', 'GET'])
def register_user():


    if current_user.is_authenticated:
        flash('you are already logged-in')
        return redirect(url_for('main.display_books'))
    # first time  get request these values are set to none
    name = None
    email = None

    # create an instance of the RegisterForm. This function will get
    # passed to the decorator method route
    form = RegistrationForm()

    # if we get a post request (form has been submitted) then extract
    # the data from the form
    # if request.method == 'POST':
    #     name = form.name.data
    #     email = form.email.data

    # flask form method will validate the data with an implied post request
    # if POST and valid
    if form.validate_on_submit():
        # capture the data a save in db
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )

        flash("Registration successful")
        # remember this is the post path so redirect to login page
        return redirect(url_for('authentication.do_the_login')) # blueprint url
    # else GET, return to reg form
    return render_template('registration.html', form=form)


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@at.route('/login', methods=['GET', 'POST'])
def do_the_login():

    if current_user.is_authenticated:
        flash('you are already logged-in')
        return redirect(url_for('main.display_books'))

    # if its a get request then display the login form
    form = LoginForm() # form will be passed to render_template

    # implied POST reqeust
    if form.validate_on_submit():
        # get email from the db using what was entered in the email field of the form
        user = User.query.filter_by(email=form.email.data).first()
        # check email and password
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentals, Please try again')
            return redirect(url_for('authentication.do_the_login'))

        # flask login mgr method for updating session object
        login_user(user, form.stay_loggedin.data) # check-box on the form 'stay logged in'
        return redirect(url_for('main.display_books'))

    return  render_template('login.html', form=form)

@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))