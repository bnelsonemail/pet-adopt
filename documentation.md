# Adopt: Pet Adoption Web Application

## **Scope of the Project**
The "Adopt" web application allows users to manage pets available for adoption. This application includes the following features:

1. **Homepage Listing Pets**:
   - Lists pets with their names and photos (if available).
   - Displays "Available" in bold for pets open for adoption.

2. **Add Pet**:
   - A form for adding new pets, with validations for input fields.

3. **Edit Pet Information**:
   - A page to view a pet's details and edit fields such as photo URL, notes, and availability.

4. **Validation**:
   - Form fields include validations for species, photo URL, and age.

5. **Responsive Routing**:
   - Supports dynamic routes for editing individual pet records.

6. **Clean Code and Documentation**:
   - Consistent naming conventions, docstrings, comments, and a `requirements.txt` file for dependencies.

---

## **File Structure**

adopt/
├── config/
│   ├── __init__.py       # Makes the config folder a module
│   ├── config.py         # Configuration settings
├── app/
│   ├── __init__.py       # Application factory and initialization (the one I provided)
│   ├── model.py          # SQLAlchemy models
│   ├── forms.py          # WTForms classes
│   ├── routes.py         # Routes for the app
│   ├── templates/        # HTML templates
│   └── static/           # Static assets (e.g., images, CSS)
|   |   └── img/
|   |       └── default-pet.jpg  # Placeholder image for pets without photos
|   ├── templates/            # HTML templates
|   |   │ 
|   |   ├── homepage.html # Homepage template showing pets 
|   |   │ 
|   |   ├── add_pet.html # Form for adding a pet 
|   |   │ 
|   |   ├── edit_pet.html # Form for editing a pet 
|
├── requirements.txt      # Python dependencies
└── README.md # Project description and setup instructions
└── .env                  # Environment variables (ignored by Git)
└── run.py                # Entry point to run the app
