import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_random_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Software-Engineering-Aglie-Project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False