from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
import json
from token_verifier import *


# create like
@app.route('/like/add', methods=['POST'])
# @token_required
def add_like():
    try:
        _json = request.json

        _userId = _json['userId']
        _postId = _json['postId']

        # save edits
        sql = " INSERT INTO tbl_like(userId, postId,status) VALUES(%s, %s,%s)"

        data = (_userId, _postId,1)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Like added successfully')
            resp.status_code = 201
            return resp
        else:
            resp = jsonsify(message='User already liked')
            resp.status_code = 400
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete like
@app.route('/like/unlike/<int:postId>/<int:userId>', methods=['DELETE'])
# @token_required
def delete_like(postId, userId):
    try:
        sql = "UPDATE tbl_like SET status = 0 WHERE postId = %s, userId = %s"

        data = (postId, userId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Like successfully deleted')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)
