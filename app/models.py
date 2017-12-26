# models.py

from flask import Flask
from app import db
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)


class User(db.Model):
    """
    Create user table

    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    age = db.Column(db.Integer, index=True)
    phone_number = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User: {}>'.format(self.first_name)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
