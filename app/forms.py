# encoding: utf-8
# __author__ = 'kkk'

from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, BooleanField, PasswordField, RadioField, validators
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class StockSearchForm(Form):
    stocklookup = TextField('stocklookup', [validators.Length(min=1, max=18)])
