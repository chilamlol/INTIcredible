from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


# create comment
@app.route('/comment/add', methods=['POST'])
# @token_required
def add_comment():
    try:
        _json = request.json

        _text = _json['text']
        _status = _json['status']
        _userId = _json['userId']
        _postId = _json['postId']

        # save edits
        sql = " INSERT INTO tbl_comment(text, status, createdDate, modifiedDate, " \
              " userId, postId) VALUES (%s, %s, NOW(), NOW(), %s, %s) "

        data = (_text, _status, _userId, postId)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Comment added successfully')
            resp.status_code = 201
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all post
@app.route('/comment')
# @token_required
def show_all_comment():
    try:
        sql = "SELECT * FROM tbl_comment"
        rows = readAllRecord(sql)

        result = []

        # Convert date time format for output
        # yyyy-MM-dd HH:MM:SS
        for row in rows:
            row['createdDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific comment
@app.route('/comment/<int:commentId>')
# @token_required
def show_comment(commentId):
    try:
        sql = "SELECT * FROM tbl_comment WHERE commentId=%s"

        row = readOneRecord(sql, commentId)

        if not row:
            return not_found()

        # Convert date time format for output
        row['createdDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
        row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update comment
@app.route('/comment/update/<int:commentId>', methods=['PUT'])
# @token_required
def update_comment(commentId):
    try:
        _json = request.json

        _text = _json['text']
        _status = _json['status']
        _userId = _json['userId']
        _postId = _json['postId']

        # save edits
        sql = " UPDATE tbl_comment SET text=%s, modifiedDate=NOW(), " \
              " status=%s, userId=%s, postId=%s WHERE commentId=%s"

        data = (_text, _status, _userId, _postId, commentId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Comment updated successfully!')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete comment (update status to false)
# This API doesn't requires admin privilege as user can delete their comment.
@app.route('/comment/delete/<int:commentId>', methods=['PUT'])
# @token_required
def delete_comment(commentId):
    try:
        sql = "UPDATE tbl_comment SET modifiedDate = NOW(), status = 'false' WHERE commentId=%s"

        if updateRecord(sql, commentId) > 0:
            resp = jsonify(message='Comment successfully inactivated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)