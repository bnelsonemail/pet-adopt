"""Config.py."""

import os
import logging
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env
# Explicitly locate the .env file
dotenv_path = find_dotenv()
if not dotenv_path:
    print("DEBUG: .env file not found!")
else:
    print(f"DEBUG: .env file found at {dotenv_path}")

# Load the .env file
load_dotenv(dotenv_path)

# Debugging
print("DEBUG: Loading .env file...")
print("DEBUG: SQLALCHEMY_DATABASE_URI from .env =",
      os.environ.get("SQLALCHEMY_DATABASE_URI"))


class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    FLASK_ENV = 'development'
    USE_RELOADER = True
    SQLALCHEMY_ECHO = True
    # Use the database URI from the .env file
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    FLASK_ENV = 'production'
    SQLALCHEMY_ECHO = False
    # Use the database URI from the .env file
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Debugging
    print("DEBUG: SQLALCHEMY_DATABASE_URI =", SQLALCHEMY_DATABASE_URI)

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("SQLALCHEMY_DATABASE_URI is not set for "
                         "ProductionConfig.")


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_ECHO = False
    # Use the test database URI from the .env file
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')


# Initialize the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -'
                              '%(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)
