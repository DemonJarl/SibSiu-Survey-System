import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MOGODB_SETTINGS = {
    'db': 'survey_system',
    'host': 'mongodb://localhost/survey_system_db'
    }