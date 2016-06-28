# encoding: utf-8
# __author__ = 'kkk'

from flask import request
from flask.ext.paginate import Pagination

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_page_items():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    offset = (page - 1) * per_page
    return page, per_page, offset


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(css_framework='bootstrap3',
                      link_size='sm',
                      show_single_page=False,
                      **kwargs
                      )

def get_mkcode(code):
    if code.startswith('6'):
        return 'sh' + code
    else:
        return 'sz' + code
