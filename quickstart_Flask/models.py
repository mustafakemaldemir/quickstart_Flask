from dataclasses import dataclass
from quickstart_Flask import db

@dataclass
class User(db.Model):

    __tablename__ = 'user'

    id = db.Column (db.Integer , primary_key = True)
    username = db.Column (db.String(25))

    def __init__(self , id , username):
        self.id = id
        self.username = username
