# __author__ = 'kkk'
# encoding: utf-8

import collections

current_code_dict = collections.OrderedDict()
current_name_dict = collections.OrderedDict()


def refresh(stock_list):
    current_code_dict.clear()
    current_name_dict.clear()
    for stock in stock_list:
        current_code_dict[str(stock.code.encode("utf-8"))] = stock
        current_name_dict[str(stock.name.encode("utf-8"))] = stock


def size():
    return len(current_code_dict)


def contains(key):
    return key in current_code_dict or key in current_name_dict


def get(key):
    stock = current_code_dict.get(key)
    if stock is None:
        stock = current_name_dict.get(key)
    return stock


def sub(start, end):
    if end >= size():
        end = size() -1

    if start >=0 and start < end:
        return current_code_dict.values()[start : end]
    else:
        pass