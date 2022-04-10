from quickstart_Flask.models import db
from quickstart_Flask import createApp

def createDB():
    db.create_all(app=createApp)
