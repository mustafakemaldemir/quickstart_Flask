from re import A
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp():

    app = Flask(__name__)

    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/db_name'

    db.init_app(app)

    return app