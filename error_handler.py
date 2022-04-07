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


@app.errorhandler(401)
def unauthorized(error=None):
    message = {
        'error': 'Token is invalid: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp


@app.errorhandler(403)
def forbidden(error=None):
    message = {
        'error': 'Invalid credentials: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 403
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'error': 'Record not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'error': 'Something went wrong. Please try again later: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
