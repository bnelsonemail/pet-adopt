"""run.py."""

from app import create_app

# Create the Flask application using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the Flask app
    app.run()
