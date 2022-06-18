from app import app
import jwt
from database.db_execution import *
from flask import request, jsonify
from functools import wraps
from error_handler import *


# decorator for verifying the JWT for alumni
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'user-token' in request.headers:
            token = request.headers['user-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing: ' + request.url}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, options={"verify_signature": False})

            # verify token
            sql = "SELECT * FROM tbl_user WHERE GUID = %s"
            row = readOneRecord(sql, data['guid'])

        except Exception as e:
            return unauthorized()
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)

    return decorated


# decorator for verifying the JWT for admin
def is_admin(f):
    @wraps(f)
    def decoded(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'user-token' in request.headers:
            token = request.headers['user-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing' + request.url}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, options={"verify_signature": False})

            # verify token
            sql = "SELECT * FROM tbl_user WHERE GUID = %s AND userRoleId IN (2, 3)"
            row = readOneRecord(sql, data['guid'])

            if not row:
                return unauthorized()

        except Exception as e:
            return unauthorized()
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)

    return decoded


# decorator for verifying the JWT for super admin
def is_super_admin(f):
    @wraps(f)
    def decoded(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'user-token' in request.headers:
            token = request.headers['user-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing' + request.url}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, options={"verify_signature": False})

            # verify token
            sql = "SELECT * FROM tbl_user WHERE GUID = %s AND userRoleId = 2"
            row = readOneRecord(sql, data['guid'])

            if not row:
                return unauthorized()

        except Exception as e:
            return unauthorized()
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)

    return decoded
