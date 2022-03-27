import jwt
from db_execution import *
from flask import request, jsonify
from functools import wraps


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'user-token' in request.headers:
            token = request.headers['user-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing' + request.url}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])

            # verify token
            sql = "SELECT * FROM tbl_user WHERE userId = %s"
            row = readOneRecord(sql, data)

        except Exception as e:
            return jsonify({
                'message': 'Token is invalid ' + request.url
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated
