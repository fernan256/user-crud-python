# app/__init__.py

import os

# third-party imports
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
from flask_migrate import Migrate

# locals imports
config_name = os.getenv('FLASK_CONFIG')

if config_name == 'development':
    from .. config import app_config
elif config_name == 'testing':
    from config import app_config
# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from models import User, UserSchema

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    @app.route('/user', methods=['GET'])
    def list_user():

        all_users = User.query.all()
        print all_users

        if not all_users:
            return jsonify({'message': 'There is no users stored'}), 404
        else:
            result = users_schema.dump(all_users)
            return jsonify(result.data), 200

    @app.route('/user/<int:id>/')
    def get_dev(id):

        if not id:
            return jsonify({'message': 'You need to provide a user id'}), 404
        else:
            user = User.query.get(id)
            if user is None:
                return jsonify({'message': 'There is no user with the provided id'}), 404
            else:
                result = user_schema.dump(user)
                return jsonify(result.data), 200

    @app.route('/user/', methods=['POST'])
    def create_user():

        data = request.json
        if data is None or not data:
            return jsonify({'message': 'You need to provide the corresponding data'}), 404
        else:
            user = User()
            exist = db.session.query(exists().where(User.email == data['email'])).scalar()

            if exist is True:
                return jsonify({'message': 'The user already exist'}), 404
            else:
                user.email = data['email']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.age = data['age']
                user.phone_number = data['phone_number']
                db.session.add(user)
                db.session.commit()
                return jsonify(user_schema.dump(user).data), 201

    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_dev(id):

        if not id:
            return jsonify({'message': 'You need to provide a user id'}), 404
        else:
            db.session.delete(User.query.get(id))
            db.session.commit()
            return jsonify({'result': True}), 200

    @app.route('/user/<int:id>', methods=['PATCH'])
    def update_dev(id):

        if not id:
            return jsonify({'message': 'You need to provide a user id'}), 404
        else:
            data = request.json
            user = User.query.get(id)

            if user is None:
                return jsonify({'message': 'There is no user with the provided id'}), 404

            else:
                user.email = data['email']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.age = data['age']
                user.phone_number = data['phone_number']
                db.session.add(user)
                db.session.commit()
                return jsonify(user_schema.dump(user).data), 200

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({'message': 'Forbidden'}), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({'message': 'Not Found'}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({'message': 'Server Error'}), 500

    return app

