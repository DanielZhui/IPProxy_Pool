import os
import sys
from flask import Flask, jsonify

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, base_dir)

app = Flask(__name__)


@app.route('/api/proxys', methods=['GET'])
def get_proxys():
    db = MongoHelper()
    result = db.find_all()
    return jsonify(result)


if __name__ == '__main__':
    from db_helper.mongo_db import MongoHelper
    app.run()
