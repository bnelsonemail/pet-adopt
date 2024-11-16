"""models.py."""

from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()


class Pet(db.Model):
    """Model for pets available for adoption."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """Show details about the pet."""
        return (f"<Pet id={self.id} name={self.name} species={self.species}"
                f"available={self.available}>")


# Function to connect the app with the database
def connect_db(app):
    """Connect this database to a Flask app."""
    db.app = app
    db.init_app(app)
