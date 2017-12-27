# models.py

import os

from flask import Flask
from flask_marshmallow import Marshmallow

config_name = os.getenv('FLASK_CONFIG')

if config_name == 'development':
    from .. app import db
elif config_name == 'testing':
    from app import db

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


class UserSchema(ma.ModelSchema):
    class Meta:
        """
        Fields to expose

        """
        fields = ('id', 'email', 'first_name', 'last_name', 'age', 'phone_number')
