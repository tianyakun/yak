# encoding: utf-8
# __author__ = 'kkk'

from flask import redirect, render_template, url_for, Blueprint
from flask_user import login_required, current_user
from app import *
from portfolio import *

user_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static', url_prefix='/user')

# The User page is accessible to authenticated users (users that have logged in)
@user_blueprint.route('/')
@login_required  # Limits access to authenticated users
def profile():
    # Process GET or invalid POST
    return render_template('profile.html')

@user_blueprint.route('/add_p/<code>', methods=['GET'])
@login_required  # Limits access to authenticated users
def add_p(code):
    # Process GET or invalid POST
    add_portfolio(code)
    return redirect(url_for('index'))


@user_blueprint.route('/top_p/<code>', methods=['GET'])
@login_required  # Limits access to authenticated users
def top_p(code):
    # Process GET or invalid POST
    top_portfolio(code)
    return redirect(url_for('index'))


@user_blueprint.route('/delete_p/<code>', methods=['GET'])
@login_required  # Limits access to authenticated users
def delete_p(code):
    # Process GET or invalid POST
    delete_portfolio(code)
    return redirect(url_for('index'))


