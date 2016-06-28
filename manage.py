# This file starts the WSGI web application.

from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

# Start a development web server if executed from the command line
if __name__ == "__main__":
    # Manage the command line parameters such as:
    # - python manage.py runserver
    # - python manage.py db

    manager.run()
