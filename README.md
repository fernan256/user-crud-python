**README**

    This README covers the installation and using of this simple CURD for user management.

**What is this repository for?**
    
    Manage user.
    Version 0.0.1

**Installation**

    Linux installation:

    First: install docker and import the docker container in this repo

    MariaDB -> sudo apt-get update sudo apt-get install postgresql postgresql-contrib sudo apt-get install postgresql-plpython3-9.5 (Para poder ejecutar los queries que tiene python- Si no larga error de que no existe plpython3)

    Install -> python 3.6, flask

**How do I get set up?**

    Install:
        pip install virtualenv
        pip install virtualenvwrapper
        export WORKON_HOME=~/Envs
        source /usr/local/bin/virtualenvwrapper.sh

    Create the virtual environment:
        mkvirtualenv my-venv
        workon my-venv

    Configuration variables:
        export FLASK_CONFIG=development
        export FLASK_APP=run.py
        
    Run the application
        flask run

    Run de my-venv once it's created:
        source ~/Envs/bin/activate

    Database configuration

    Run the db installation to create the user database with the corresponding tables.

    Edit the env file with your user and password.
    
    Summary of set up
    Configuration
    Dependencies
    How to run tests
    Deployment instructions

**Directory structure**

    ├── user-crud-python
       ├── app
       │   ├── __init__.py
       │   ├── templates
       │   ├── models.py
       │   └── views.py
       ├── config.py
       ├── requirements.txt
       └── run.py

**Contribution guidelines**

    Writing tests
    Code review
    Other guidelines

**Who do I talk to?**

    Repo owner or admin
    Other community or team contact