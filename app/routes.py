"""app / routes.py."""

from flask import render_template, redirect
from app.model import db, Pet
from app.forms import AddPetForm, EditPetForm


def register_routes(app):
    """Register application routes."""

    @app.route('/')
    def show_homepage():
        """Show list of pets."""
        pets = Pet.query.all()
        return render_template('homepage.html', pets=pets)

    @app.route('/add', methods=["GET", "POST"])
    def add_pet():
        """Add a new pet."""
        form = AddPetForm()
        if form.validate_on_submit():
            pet = Pet(
                name=form.name.data,
                species=form.species.data,
                photo_url=form.photo_url.data or None,
                age=form.age.data or None,
                notes=form.notes.data or None,
            )
            db.session.add(pet)
            db.session.commit()
            return redirect('/')
        return render_template('add_pet.html', form=form)

    @app.route('/<int:pet_id>', methods=["GET", "POST"])
    def show_edit_pet(pet_id):
        """Show pet details and edit form."""
        pet = Pet.query.get_or_404(pet_id)
        form = EditPetForm(obj=pet)

        if form.validate_on_submit():
            pet.photo_url = form.photo_url.data
            pet.notes = form.notes.data
            pet.available = form.available.data
            db.session.commit()
            return redirect('/')
        return render_template('edit_pet.html', pet=pet, form=form)
