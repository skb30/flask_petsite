
# since we don't have access to the flask app at the global level
# we must use the blueprint
from app.pet_site.models import Pet
from app.pet_site import pets
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, flash, request, redirect, url_for
from app.pet_site.forms import CreatePetForm
from datetime import date

@pets.route('/pet_site')
def display_home():
    return render_template('home.html')


@pets.route('/pet_site/delete/<pet_id>', methods=['GET','POST'])
@login_required
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if request.method == 'POST':
        db.session.delete(pet)
        db.session.commit()
        msg = 'pet with id of ' + pet_id + ' deleted successfully'
        flash(msg)
        return redirect(url_for('pets.display_pets'))
    # get request
    return  render_template('delete_pet.html', pet=pet, pet_id=pet.id)

@pets.route('/pet_site/pets/')
def display_pets():

    pets = Pet.query.all()
    today = date.today()

    # calculate the pet's age and store in the pet object attribute
    for pet in pets:
        born = pet.birthdate
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        pet.age = age
    return  render_template('pets.html', pets=pets) # pass pets instance

@pets.route('/pet_site/reg_pet', methods=['GET', 'POST'])
@login_required
def create_pet():

    # create the form
    form = CreatePetForm()

    # form.owner_id = owner_id

    if form.validate_on_submit():
        pet = Pet(owner=form.owner.data,
                name=form.name.data,
                breed=form.breed.data,
                phone=form.phone.data,
                sex=form.sex.data,
                neutered=form.neutered.data,
                vetinfo=form.vetinfo.data,
                feeding=form.feeding.data,
                exercise=form.exercise.data,
                notes=form.notes.data,
                dob=form.dob.data)
        try:
            db.session.add(pet)
            db.session.commit()
        except:
            flash("DB -Error")
            return redirect(url_for('pets.display_home'))
        msg = 'Pet registration data added successfully'
        flash(msg)
        return redirect(url_for('pets.display_home'))
    # get request
    return  render_template('register_pet.html', form=form)
