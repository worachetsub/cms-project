"""
The flask application package.
"""
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger

## Set the logging level
app.logger.setLevel(logging.DEBUG)

# ## Create a file handler that logs messages to a file
# handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
# handler.setLevel(logging.INFO)  # Set the level for the handler

# ## Create a logging format
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)

# ## Add the handler to the app's logger
# app.logger.addHandler(handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
