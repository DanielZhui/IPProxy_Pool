import os
import sys
from flask import Flask, jsonify, render_template
from tem_filters.timer import format_time
from util import get_find_options

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, base_dir)

app = Flask(__name__)
app.add_template_filter(format_time, 'format_time')


@app.route('/home', methods=['GET'])
def home():
    db = MongoHelper()
    options = get_find_options()
    result = db.find_all(options)
    data = {'proxys': result}
    return render_template('index.html', **data)


@app.route('/api/proxys', methods=['GET'])
def get_proxys():
    db = MongoHelper()
    options = get_find_options()
    result = db.find_all(options)
    return jsonify(result)


if __name__ == '__main__':
    from db_helper.mongo_db import MongoHelper
    app.run()
