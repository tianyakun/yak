# __author__ = 'kkk'
# encoding: utf-8

import os


class Config(object):
    """Base config class."""

    #####################################################
    #               Root path of project                #
    #####################################################
    ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    #################################################
    #               Flask app config                #
    #################################################
    APP_NAME = "yakshare"
    DEBUG = False
    TESTING = False
    secret_key = "YakShare"
    SESSION_TYPE = "null"
    # PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    # SESSION_COOKIE_NAME = 'yak_session'

    # Site domain
    # SITE_TITLE = "yak"
    # SITE_DOMAIN = "http://localhost:5000"

    # Flask-DebugToolbar
    # DEBUG_TB_INTERCEPT_REDIRECTS = True

    # Sentry config
    # SENTRY_DSN = ''

    # Host string, used by fabric
    # HOST_STRING = "root@12.34.56.78"

    ######################################################
    #       flask-sqlalchemy settings                    #
    ######################################################
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(ROOT_PATH, 'app.sqlite') #根目录下的app.sqlite
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    ##################################################################
    #       MONGO                                                    #
    ##################################################################
    MONGO_URI = 'mongodb://localhost:27017/'
    MONGO_DBNAME = 'yak'
    MONGO_USERNAME = None
    MONGO_PASSWORD = None

    ####################################################################
    #               Flask-Mail settings                                #
    ####################################################################
    MAIL_USERNAME = '1024954390@qq.com'
    MAIL_PASSWORD = 'kmvvnctiiyexbfbh'
    MAIL_DEFAULT_SENDER = '1024954390@qq.com'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True

    #################################################
    #               Flask-User settings             #
    #################################################
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = True  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_REGISTRATION = True  # Allow new users to register
    USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = True  # Register and Login with username
    # USER_AFTER_LOGIN_ENDPOINT = 'index'
    # USER_AFTER_LOGOUT_ENDPOINT = 'index'


    #############################################################
    #               Flask-APScheduler settings                  #
    #               task.py                                     #
    #############################################################
    func_path = 'app.task:refresh'
    JOBS = [
        {
            'id': 'refresh1',
            'func': func_path,
            'trigger': {
                'type': 'cron',
                'day_of_week' : '0-4',
                'hour' : '9-10',
                'minute' : '*',
                'second' : 0
            }

        },
        {
            'id': 'refresh2',
            'func': func_path,
            'trigger': {
                'type': 'cron',
                'day_of_week' : '0-4',
                'hour' : '11',
                'minute' : '0-30',
                'second' : 0
            }

        },
        {
            'id': 'refresh3',
            'func': func_path,
            'trigger': {
                'type': 'cron',
                'day_of_week' : '0-4',
                'hour' : '13-14',
                'minute' : '*',
                'second' : 0
            }

        },
    ]

    SCHEDULER_VIEWS_ENABLED = True