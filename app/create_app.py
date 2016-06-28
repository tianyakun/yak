# encoding: utf-8
# __author__ = 'kkk'

from flask_mail import Mail
from flask_user import UserManager, SQLAlchemyAdapter
from flask_wtf.csrf import CsrfProtect

from config import load_config
from . import app, db
from .models import User, UserProfile
from .task import task_init

@app.before_first_request
def initialize_app_on_first_request():
    """
    do something on first HTTP request
    """
    print("do something on first HTTP request.")


def create_app(extra_config_settings={}):
    """
    Initialize Flask applicaton
    """
    # Initialize app config settings
    app.config.from_object(load_config())
    # Read extra config settings from function parameter 'extra_config_settings'
    app.config.update(extra_config_settings)  # Overwrite with 'extra_config_settings' parameter

    # Setup Flask-Mail
    mail = Mail(app)

    # Setup WTForms CsrfProtect
    CsrfProtect(app)

    # Setup Flask-User to handle users account related forms
    # from app.core.models import User, MyRegisterForm
    # from app.core.views import user_profile_page

    # Create all database tables
    db.create_all()

    db_adapter = SQLAlchemyAdapter(db, User, UserProfileClass=UserProfile)  # Setup the SQLAlchemy DB Adapter

    user_manager = UserManager(db_adapter, app,  # Init Flask-User and bind to app
                               # register_form=MyRegisterForm,  # using a custom register form with UserProfile fields
                               # user_profile_view_function=user_profile_page,
    )

    # Setup task
    # task_init()

    return app
