# encoding: utf-8
# __author__ = 'kkk'

from flask_user import UserMixin
from __init__ import db

import sys

reload(sys)
sys.setdefaultencoding('utf8')


# Define the User data model. Make sure to add flask.ext.users UserMixin !!!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_profile_id = db.Column(db.Integer(), db.ForeignKey('user_profile.id', ondelete='CASCADE'))

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    is_active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # Relationships
    user_profile = db.relationship('UserProfile', uselist=False, foreign_keys=[user_profile_id])

    def __repr__(self):
        return '<id: {}, user_profile_id: {}, username: {}, is_active: {}, email: {}' \
            .format(self.id, self.user_profile_id, self.username, self.is_active, self.email)


# Define the UserProfile data model.
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # User information
    portfolio = db.Column(db.String(500), nullable=False, default='')

    def __repr__(self):
        return '<id: {}, portfolio: {}' \
            .format(self.id, self.portfolio)


class Stock():
    def __init__(self, code, name, trade, changepercent, open, high, low, settlement, volume, turnoverratio, pb, mktcap, per):
        self.code = code #代码
        self.name = name #名称
        self.trade = trade #现价
        self.changepercent = changepercent #涨跌幅
        self.open = open #开盘价
        self.high = high #最高价
        self.low = low #最低价
        self.settlement = settlement #昨日收盘价
        self.volume = volume #成交量
        self.turnoverratio = turnoverratio #换手率
        self.pb = pb
        self.mktcap = mktcap #市值
        self.per = per

    def __init__(self, field_dict):
        self.code = field_dict['code'] #代码
        self.name = field_dict['name'] #名称
        self.trade = field_dict['trade'] #现价
        self.changepercent = field_dict['changepercent'] #涨跌幅
        self.open = field_dict['open'] #开盘价
        self.high = field_dict['high'] #最高价
        self.low = field_dict['low'] #最低价
        self.settlement = field_dict['settlement'] #昨日收盘价
        self.volume = field_dict['volume'] #成交量
        self.turnoverratio = field_dict['turnoverratio'] #换手率
        self.pb = field_dict['pb'] #换手率
        self.mktcap = field_dict['mktcap'] #换手率
        self.per = field_dict['per'] #换手率

    def __str__(self):
        return '<code: {}, name: {}, trade: {}, changepercent: {}, open: {}, high: {}, low: {}, settlement: {}, volume: {}, turnoverratio: {}, pb: {}, mktcap: {}, per: {}>' \
            .format(self.code, self.name, self.trade, self.changepercent, self.open, self.high, self.low, self.settlement, self.volume, self.turnoverratio, self.pb, self.mktcap, self.per)


class StockDetail():
    def __init__(self, code, name, open, pre_close, price, high, low, bid, ask, volume, amount, b1_v, b1_p, b2_v, b2_p, b3_v, b3_p, b4_v, b4_p, b5_v, b5_p, a1_v, a1_p, a2_v, a2_p, a3_v, a3_p, a4_v, a4_p, a5_v, a5_p, date,time):
        self.code = code #代码
        self.name = name #名称
        self.open = open #今日开盘价
        self.pre_close = pre_close #昨日收盘价
        self.price = price #当前价格
        self.high = high #今日最高价
        self.low = low #今日最低价
        self.bid = bid #即“买一”报价
        self.ask = ask #即“卖一”报价
        self.volume = volume #成交量 maybe you need do volume/100
        self.amount = amount #成交金额（元 CNY）
        self.b1_v = b1_v #委买一（笔数 bid volume）
        self.b1_p = b1_p #委买一（价格 bid price）
        self.b2_v = b2_v #“买二”
        self.b2_p = b2_p #“买二”
        self.b3_v = b3_v #“买三”
        self.b3_p = b3_p #“买三”
        self.b4_v = b4_v #“买四”
        self.b4_p = b4_p #“买四”
        self.b5_v = b5_v #“买五”
        self.b5_p = b5_p #“买五”
        self.a1_v = a1_v #委卖一（笔数 ask volume）
        self.a1_p = a1_p #委卖一（价格 ask price）
        self.a2_v = a2_v #“卖二”
        self.a2_p = a2_p #“卖二”
        self.a3_v = a3_v #“卖三”
        self.a3_p = a3_p #“卖三”
        self.a4_v = a4_v #“卖四”
        self.a4_p = a4_p #“卖四”
        self.a5_v = a5_v #“卖五”
        self.a5_p = a5_p #“卖五”
        self.date = date #日期
        self.time = time #时间
        self.change = float(price) - float(pre_close)

    def __init__(self, field_dict):
        self.code = field_dict['code'] #代码
        self.name = field_dict['name'] #名称
        self.open = field_dict['open'] #今日开盘价
        self.pre_close = field_dict['pre_close'] #昨日收盘价
        self.price = field_dict['price'] #当前价格
        self.high = field_dict['high'] #今日最高价
        self.low = field_dict['low'] #今日最低价
        self.bid = field_dict['bid'] #即“买一”报价
        self.ask = field_dict['ask'] #即“卖一”报价
        self.volume = field_dict['volume'] #成交量 maybe you need do volume/1
        self.amount = field_dict['amount'] #成交金额（元 CNY）
        self.b1_v = field_dict['b1_v'] #委买一（笔数 bid volume）
        self.b1_p = field_dict['b1_p'] #委买一（价格 bid price）
        self.b2_v = field_dict['b2_v'] #“买二”
        self.b2_p = field_dict['b2_p'] #“买二”
        self.b3_v = field_dict['b3_v'] #“买三”
        self.b3_p = field_dict['b3_p'] #“买三”
        self.b4_v = field_dict['b4_v'] #“买四”
        self.b4_p = field_dict['b4_p'] #“买四”
        self.b5_v = field_dict['b5_v'] #“买五”
        self.b5_p = field_dict['b5_p'] #“买五”
        self.a1_v = field_dict['a1_v'] #委卖一（笔数 ask volume）
        self.a1_p = field_dict['a1_p'] #委卖一（价格 ask price）
        self.a2_v = field_dict['a2_v'] #“卖二”
        self.a2_p = field_dict['a2_p'] #“卖二”
        self.a3_v = field_dict['a3_v'] #“卖三”
        self.a3_p = field_dict['a3_p'] #“卖三”
        self.a4_v = field_dict['a4_v'] #“卖四”
        self.a4_p = field_dict['a4_p'] #“卖四”
        self.a5_v = field_dict['a5_v'] #“卖五”
        self.a5_p = field_dict['a5_p'] #“卖五”
        self.date = field_dict['date'] #日期
        self.time = field_dict['time'] #时间
        self.change = float(self.price) - float(self.pre_close)

    def __str__(self):
        return '<code: {}, name: {}, open: {}, pre_close: {}, price: {}, high: {}, low: {}, bid: {}, ask: {}, volume: {}, amount: {}, b1_v: {}, b1_p: {}, b2_v: {}, b2_p: {}, b3_v: {}, b3_p: {}, b4_v: {}, b4_p: {}, b5_v: {}, b5_p: {}, a1_v: {}, a1_p: {}, a2_v: {}, a2_p: {}, a3_v: {}, a3_p: {}, a4_v: {}, a4_p: {}, a5_v: {}, a5_p: {}, date: {}, time: {}>'\
            .format(self.code, self.name, self.open, self.pre_close, self.price, self.high, self.low, self.bid, self.ask, self.volume, self.amount, self.b1_v, self.b1_p, self.b2_v, self.b2_p, self.b3_v, self.b3_p, self.b4_v, self.b4_p, self.b5_v, self.b5_p, self.a1_v, self.a1_p, self.a2_v, self.a2_p, self.a3_v, self.a3_p, self.a4_v, self.a4_p, self.a5_v, self.a5_p, self.date, self.time)


class TradingRecord:
    def __init__(self, code, time, price, pchange, change, volume, amount, type):
        self.code=code #代码
        self.time=time #时间
        self.price=price #当前价格
        self.pchange=pchange #涨跌幅
        self.change=change #价格变动
        self.volume=volume #成交手
        self.amount=amount #成交金额(元)
        self.type=type #买卖类型【买盘、卖盘、中性盘】

    def __init__(self, code, field_dict):
        self.code=code #代码
        self.time=field_dict['time'] #时间
        self.price=field_dict['price'] #当前价格
        self.pchange=field_dict['pchange'] #涨跌幅
        self.change=field_dict['change'] #价格变动
        self.volume=field_dict['volume'] #成交手
        self.amount=field_dict['amount'] #成交金额(元)
        self.type=field_dict['type'] #买卖类型【买盘、卖盘、中性盘】

    def __str__(self):
        return '<code: {}, time: {}, price: {}, pchange: {}, change: {}, volume: {}, amount: {}, type: {}>' \
            .format(self.code, self.time, self.price, self.pchange, self.change, self.volume, self.amount, self.type)


class StockBasic:
    """
    上市公司基本情况,
    属性包括:所属行业, 地区, 市盈率, 流通股本, 总股本(万), 总资产(万), 流动资产, 固定资产, 公积金, 每股公积金, 每股收益, 每股净资, 市净率, 上市日期
    """
    def __init__(self):
        self.code = code	#代码
        self.name = name	#名称
        self.industry = industry	#所属行业
        self.area = area	#地区
        self.pe = pe	#市盈率
        self.outstanding = outstanding	#流通股本
        self.totals = totals	#总股本(万)
        self.totalAssets = totalAssets	#总资产(万)
        self.liquidAssets = liquidAssets	#流动资产
        self.fixedAssets = fixedAssets	#固定资产
        self.reserved = reserved	#公积金
        self.reservedPerShare = reservedPerShare	#每股公积金
        self.esp = esp	#每股收益
        self.bvps = bvps	#每股净资
        self.pb = pb	#市净率
        self.timeToMarket = timeToMarket	#上市日期

    def __init__(self, field_dict):
        self.code = field_dict['code']	#代码
        self.name = field_dict['name']	#名称
        self.industry = field_dict['industry']	#所属行业
        self.area = field_dict['area']	#地区
        self.pe = field_dict['pe']	#市盈率
        self.outstanding = field_dict['outstanding']	#流通股本
        self.totals = field_dict['totals']	#总股本(万)
        self.totalAssets = field_dict['totalAssets']	#总资产(万)
        self.liquidAssets = field_dict['liquidAssets']	#流动资产
        self.fixedAssets = field_dict['fixedAssets']	#固定资产
        self.reserved = field_dict['reserved']	#公积金
        self.reservedPerShare = field_dict['reservedPerShare']	#每股公积金
        self.esp = field_dict['esp']	#每股收益
        self.bvps = field_dict['bvps']	#每股净资
        self.pb = field_dict['pb']	#市净率
        self.timeToMarket = field_dict['timeToMarket']	#上市日期

    def __str__(self):
        return '<code: {}, name: {}, industry: {}, area: {}, pe: {}, outstanding: {}, totals: {}, totalAssets: {}, liquidAssets: {}, fixedAssets: {}, reserved: {}, reservedPerShare: {}, esp: {}, bvps: {}, pb: {}, timeToMarket: {}>' \
            .format(self.code, self.name, self.industry, self.area, self.pe, self.outstanding, self.totals, self.totalAssets, self.liquidAssets, self.fixedAssets, self.reserved, self.reservedPerShare, self.esp, self.bvps, self.pb, self.timeToMarket)
