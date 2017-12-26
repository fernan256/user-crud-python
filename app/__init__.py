# app/__init__.py

# third-party imports
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# locals imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# ma = Marshmallow(config)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    from models import User, UserSchema

    user_schema = UserSchema()

    @app.route('/user', methods=['GET'])
    def list_user():

        users = User.query.all()
        result = user_schema.dump(users)
        print result
        return jsonify(user_schema.dump(users).data)

    @app.route('/user/show/<int:id>/')
    def get_dev(id):

        user = User.query.get(id)
        result = user_schema.dump(user)
        return jsonify(result.data)

    @app.route('/user/create/', methods=['POST'])
    def create_user():

        data = request.json
        user = User()
        exist = db.session.query(exists().where(User.email == data['email'])).scalar()

        if exist is True:
            return jsonify({'message': 'pet is already stored'}), 404
        # if not request.json or not 'name' in request.json:
        #    abort(400)
        else:
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.age = data['age']
            user.phone_number = data['phone_number']
            db.session.add(user)
            db.session.commit()
        return jsonify(user_schema.dump(user).data), 200

    @app.route('/user/delete/<int:id>', methods=['DELETE'])
    def delete_dev(id):
        db.session.delete(User.query.get(id))
        db.session.commit()
        return jsonify({'result': True})

    @app.route('/user/update/<int:id>', methods=['PATCH'])
    def update_dev(id):

        data = request.json
        user = User.query.get(id)

        if user is None:
            return jsonify({'message': 'pet is already stored'}), 404

        else:
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.age = data['age']
            user.phone_number = data['phone_number']
            db.session.add(user)
            db.session.commit()
        return jsonify(user_schema.dump(user).data), 200

    return app

