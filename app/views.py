# encoding: utf-8
# __author__ = 'kkk'

from flask import redirect, render_template, flash, session, url_for
from flask_user import current_user

from . import app
from .forms import StockSearchForm
from app import dataproxy, current_market
from .utils import *
from app.users.portfolio import build_portfolio
from app import mongo
from MACD import Get_MACD
import json
from datetime import datetime


# app_blueprint = Blueprint('app', __name__, url_prefix='/')


@app.errorhandler(404)
def not_found(e):
    return render_template('/404.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StockSearchForm(request.form)
    page, per_page, offset = get_page_items()
    stocks = current_market.sub(offset, offset+per_page)
    pagination = get_pagination(page=page,
                                per_page=per_page,
                                total=current_market.size(),
                                record_name='stocks',
                                format_total=True,
                                format_number=True,
                                )
    if current_user.is_authenticated:
        build_portfolio()
        from users.portfolio import get_stocks_portfolio
        stocks_portfolio = get_stocks_portfolio(session['portfolio'])
        return render_template('/index.html', stocks=stocks, stocks_portfolio=stocks_portfolio, form=form, page=page, per_page=per_page, pagination=pagination,)
    else:
        return render_template('/index.html', stocks=stocks, form=form, page=page, per_page=per_page, pagination=pagination,)


@app.route('/detail/<code>', methods=['GET'])
def detail(code):
    stock_detail = dataproxy.get_realtime_detail(code)
    stock = current_market.get(code)
    from models import StockBasic
    stock_basic = StockBasic(mongo.stock_basic.find_one({"code":code}))
    trading_records = dataproxy.get_trading_records(code)
    if trading_records is not None and len(trading_records) > 30:
        trading_records = trading_records[0:30]
    mkcode = get_mkcode(stock_detail.code)
    return render_template('detail.html', stockdetail=stock_detail, stock=stock, stockbasic=stock_basic, tradingrecords=trading_records, mkcode=mkcode)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = StockSearchForm(request.form)
    code = form.stocklookup.data.encode("utf-8")
    if current_market.contains(code):
        stock = current_market.get(code)
        return render_template('index.html', search_stock=stock, form=form)
    else:
        flash("nothing find!")
        return redirect(url_for('index'))


# @app.route('/basics', methods=['GET', 'POST'])
# def basics():
#     j_datas = dataproxy.get_stock_basics()
#     mongo.stock_basic.insert(j_datas)
#     return redirect(url_for('index'))


# @app.route('/basic/<code>', methods=['GET', 'POST'])
# def basic(code):
#     j_basic = mongo.stock_basic.find_one({"code":code})
#     if j_basic is not None:
#         from models import StockBasic
#         stock_basic = StockBasic(j_basic)
#         return stock_basic.__str__()
#     else:
#         return redirect(url_for('index'))


# @app.route('/history', methods=['GET', 'POST'])
# def history():
#     j_stock_basics = mongo.stock_basic.find()
#     for j_stock_basic in j_stock_basics:
#         try:
#             from models import StockBasic
#             stock_basic = StockBasic(j_stock_basic)
#             code = stock_basic.code.encode("utf-8")
#             j_hist_tata = mongo.hist_data.find({"code":code})
#             if j_hist_tata.count() <= 0:
#                 print(code + " " + str())
#                 try:
#                     start_date = datetime.strptime(str(stock_basic.timeToMarket), '%Y%m%d')
#                     if (start_date - datetime.today()).days > 365.25*3:
#                         raise Exception
#                     j_data = dataproxy.get_hist_data(code, ktype='D', start=start_date)
#                     if j_data is not None:
#                         mongo.hist_data.insert(j_data)
#                 except Exception:
#                     j_data = dataproxy.get_hist_data(code, ktype='D')
#                     if j_data is not None:
#                         mongo.hist_data.insert(j_data)
#         except Exception:
#             pass
#     return redirect(url_for('index'))



@app.route('/macd', methods=['GET', 'POST'])
def macd():
    Get_MACD('002256')
    return redirect(url_for('index'))



