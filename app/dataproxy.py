# encoding: utf-8
# __author__ = 'kkk'

import tushare as ts
import pandas as pd
import json
from datetime import datetime
from datetime import timedelta

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_all():
    try:
        df = pd.DataFrame(ts.get_today_all())
        j_datas = json.loads(df.to_json(orient='records'))
        stocks = []
        from models import Stock
        for j_data in j_datas:
            stocks.append(Stock(j_data))
        return stocks
    except IOError:
        pass


def get_realtime_detail(code):
    try:
        df = ts.get_realtime_quotes(code)
        field_dict = json.loads(df.to_json(orient='records'))[0]
    except IOError:
        pass
    from models import StockDetail
    return StockDetail(field_dict)


def get_trading_records(code):
    try:
        df = ts.get_today_ticks(code)
        j_datas = json.loads(df.to_json(orient='records'))
        trading_records = []
        from models import TradingRecord
        for j_data in j_datas:
            trading_records.append(TradingRecord(code, j_data))
        return trading_records
    except IOError:
        pass


def get_stock_basics():
    try:
        df = ts.get_stock_basics()
        df.reset_index(level=0, inplace=True)
        return json.loads(df.to_json(orient='records'))
    except IOError:
        pass


def get_hist_data(code, ktype='D', start=datetime.today()-timedelta(days=3*365.25), end=datetime.today()):
    try:
        df = ts.get_hist_data(code, ktype=ktype, start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"), retry_count=3, pause=3)
        df.reset_index(level=0, inplace=True)
        df['code'] = code
        df['ktype'] = ktype
        return json.loads(df.to_json(orient='records'))
    except Exception:
        pass



