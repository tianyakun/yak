# encoding: utf-8
# __author__ = 'kkk'

from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    test = mongo.db.test.find_one_or_404({'name': "yak"})
    return str(test)


if __name__ == '__main__':
    app.run(debug=True)
