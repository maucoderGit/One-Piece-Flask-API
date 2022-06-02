from os import urandom

SECRET_KEY = urandom(50)

PROPAGATE_ECEPTIONS = True

# Database Configuration

SQLALCHEMY_DATABASE_URI = 'sqlite:///crews.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False