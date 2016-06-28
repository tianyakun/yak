# encoding: utf-8
# __author__ = 'kkk'

from app import app

from views import user_blueprint

app.register_blueprint(user_blueprint)
