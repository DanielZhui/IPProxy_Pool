import os
import sys
from flask import Flask, jsonify, render_template
from flask_apscheduler import APScheduler

from tem_filters.timer import format_time
from util import get_find_options

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, base_dir)

app = Flask(__name__)
app.add_template_filter(format_time, 'format_time')


@app.route('/home', methods=['GET'])
def home():
    options = get_find_options()
    result = db.find_all(options)
    data = {'proxys': result}
    return render_template('index.html', **data)


@app.route('/api/proxys', methods=['GET'])
def get_proxys():
    options = get_find_options()
    result = db.find_all(options)
    return jsonify(result)


if __name__ == '__main__':
    from db_helper.mongo_db import MongoHelper
    from conf import Config
    db = MongoHelper()
    app.config.from_object(Config)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0', port=5000)
