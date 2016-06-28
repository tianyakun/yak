# __author__ = 'kkk'
# encoding: utf-8

import time

from flask_apscheduler import APScheduler
from .import app
from app import current_market
import dataproxy


def refresh():
    print("refresh starting, start time: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    stocks = dataproxy.get_all()
    if len(stocks) > 0:
        current_market.refresh(stocks)
    else:
        pass
    print("refresh end! end time: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))


def task_init():
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    refresh()

