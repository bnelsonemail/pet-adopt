"""app / __init__.py."""

import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from config.config import DevelopmentConfig, ProductionConfig
from app.routes import register_routes
from app.extensions import db


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)

    # Load configuration
    if os.getenv('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)

    # Register routes
    with app.app_context():
        db.create_all()
        register_routes(app)

    return app
