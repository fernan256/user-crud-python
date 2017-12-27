**README**

    This README covers the installation and using of this RestFul API. A User CRUD. With this API you'll be abel to 
    create, list all users, show users by id, delete user, update user features individualy.

**What is this repository for?**
    
    Restful API for user CRUD.
    
    Version 1.0.0

**Installation**

    Linux installation:
        install mysql-server, python2.7, mysql-community edition
        

**Database configuration and migration**
    
    Create user and databes that we will use in the instance/config.py:
    
        $ mysql -u root -p
        
        mysql> CREATE USER '<user_name>'@'localhost' IDENTIFIED BY '<password>';
        
        mysql> CREATE DATABASE users_db;
        
        mysql> GRANT ALL PRIVILEGES ON users_db . * TO '<user_name>'@'localhost';
        
    For migrate the models use:
        
        $ flask db init
        
        $ flask db migrate
        
        $ flask db upgrade
    
    For testtin, create the corresponding database:
    
        $ mysql -u root -p
        
        mysql> CREATE DATABASE users_test_db;
        
        mysql> GRANT ALL PRIVILEGES ON users_db . * TO '<user_name>'@'localhost';
    
**Setup URI database config file**

    Create a directory and a file instance/config.py
        
        Inside of that put this:
            # instance/config.py

            import os

            config_name = os.getenv('FLASK_CONFIG')

            if config_name == 'development':
                SQLALCHEMY_DATABASE_URI = 'mysql://<userName>:<pass>@localhost/users_db'
            elif config_name == 'testing':
                SQLALCHEMY_DATABASE_URI = 'mysql://<userName>:<pass>@localhost/user_test_db'
        
**How do I get set up?**
     
     Fisrt install:
        $ pip install virtualenv
        $ pip install virtualenvwrapper
        
        $ export WORKON_HOME=~/Envs
        $ source /usr/local/bin/virtualenvwrapper.sh
        
        $ pip install requirements.txt
     
     Create the virtual environment:
        $ mkvirtualenv my-venv
        $ workon my-venv

        
     Run the application
        $ flask run

     Run de my-venv once it's created:
        $ source ~/Envs/bin/activate
        
**Configuration**

    Configuration variables:
        $ export FLASK_CONFIG=development
        $ export FLASK_APP=run.py
        
    For testing:
        $ export FLASK_CONFIG=testing

**How to run tests**
    
    Run test:
        $ export FLASK_CONFIG=testing
        
        $ python test.py

**Organization / Structure**

    ├── app              # All code related to the running of the app
    │   ├── __init__.py  # All app-wide setup, and endpoints. Called by `run.py`
    │   └── models       # Models
    │
    ├── instance
    │   └── config.py    # Database URI and secret password
    ├── migrations       # Directory with migraton configurations
    ├── config           # Configuration files
    ├── seeds.py         # Used for non-Vagrant local Development
    ├── run.py           # Runs the app!
    └── test.py          # Unit tests

**Who do I talk to?**

    Diego Mayorga
    diego.mayorga86@gmail.com
