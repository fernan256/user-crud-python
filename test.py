# tests.py

import unittest

from flask_testing import TestCase
from sqlalchemy.sql import exists

from app import create_app, db
from app.models import User


class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://dt_admin:dt2017@localhost/user_test_db'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test non-admin user
        user1 = User(email="test_user1@wadas.com", first_name="Diego", last_name="Mayorga", age="31", phone_number="41321211")
        user2 = User(email="test_user2@wadas.com", first_name="Diego", last_name="Mayorga", age="31", phone_number="41321211")

        # save users to database
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of user created
        """
        self.assertEqual(User.query.count(), 2)

    def test_create_user(self):
        """
        Test if a new user is created
        """
        user = User()

        user.email = 'newMail@gamil.com'
        user.first_name = 'Fernando'
        user.last_name = 'Greco'
        user.age = 29
        user.phone_number = 23123
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 3)

    def test_update_user(self):
        """
        Test if an individual user feature is updated
        """
        user = User()
        user.email = 'newMail@gamil.com'
        user.first_name = 'Fernando'
        user.last_name = 'Greco'
        user.age = 29
        user.phone_number = 888888
        db.session.add(user)
        db.session.commit()

        get_user = db.session.query(exists().where(User.phone_number == 888888)).scalar()
        self.assertEqual(get_user, True)

    def test_delete_user(self):
        """
        Test if a user is deleted
        """
        db.session.delete(User.query.get(1))
        db.session.commit()

        self.assertEqual(User.query.count(), 1)


if __name__ == '__main__':
    unittest.main()