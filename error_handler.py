from app import app
from flask import request, jsonify


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'message': 'Server couldn\'t process the request, please check your syntax: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(422)
def unprocessable_entity(error=None):
    message = {
        'message': 'JSON parameter incomplete: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 422
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Record not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(500)
def internal_server_error(error):
    message = {
        'message': request.url + ' is currently unable to handle this request.',
        'error': error
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
