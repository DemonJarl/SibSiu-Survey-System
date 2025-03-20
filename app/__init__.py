from flask import Flask
from config import Config
import logging
from logging.handlers import RotatingFileHandler
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)
db = MongoEngine(app)
app.config.from_object(Config)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/survey_system.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    
from app import routes, models, errors