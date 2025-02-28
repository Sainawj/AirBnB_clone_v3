#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', mmethods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
