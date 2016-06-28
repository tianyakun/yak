# encoding: utf-8
# __author__ = 'kkk'

from flask import session
from flask_user import current_user
import json

from app import db
from app import current_market

SEPARATOR = ','

def build_portfolio():
    from app.models import UserProfile
    user_profile_id = current_user.user_profile_id
    if user_profile_id is None or UserProfile.query.filter_by(id=user_profile_id).first() is None:
        user_profile = UserProfile()
        db.session.add(user_profile)
        db.session.commit()
        current_user.user_profile_id = user_profile.id
        db.session.commit()
    else:
        pass
    user_profile = UserProfile.query.filter_by(id=current_user.user_profile_id).first()
    session['portfolio'] = user_profile.portfolio


def get_stocks_portfolio(portfolio):
    if portfolio is None or len(portfolio) == 0:
        return
    else:
        stocks_portfolio = []
        for code in portfolio.split(','):
            if current_market.contains(code):
                stocks_portfolio.append(current_market.get(code))
        return stocks_portfolio


def add_portfolio(code):
    portfolio = session['portfolio']
    if portfolio.find(code) == -1:
        portfolio = code + SEPARATOR + portfolio
        from app.models import UserProfile
        user_profile = UserProfile.query.filter_by(id=current_user.user_profile_id).first()
        user_profile.portfolio = portfolio
        db.session.commit()
        session['portfolio'] = user_profile.portfolio
    else:
        pass


def top_portfolio(code):
    portfolio = session['portfolio']
    if portfolio.find(code) == -1 or portfolio.startswith(code):
        pass
    else:
        portfolio = code + SEPARATOR + portfolio.replace(code+SEPARATOR, '').replace(code, '')
    from app.models import UserProfile
    user_profile = UserProfile.query.filter_by(id=current_user.user_profile_id).first()
    user_profile.portfolio = portfolio
    db.session.commit()
    session['portfolio'] = user_profile.portfolio


def delete_portfolio(code):
    portfolio = session['portfolio']
    portfolio = portfolio.replace(code+SEPARATOR, '').replace(code, '')
    from app.models import UserProfile
    user_profile = UserProfile.query.filter_by(id=current_user.user_profile_id).first()
    user_profile.portfolio = portfolio
    db.session.commit()
    session['portfolio'] = user_profile.portfolio
