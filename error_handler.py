from app import app
from flask import request, jsonify


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'error': 'Missing Required Parameters: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'error': 'Record not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'error': 'The server encountered an internal error or misconfiguration and was unable to complete your process: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
