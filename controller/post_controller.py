from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


# create post
@app.route('/post/add', methods=['POST'])  # @is_admin
def add_post():
    try:
        _json = request.json

        _text = _json['text']
        _file = _json['file']
        _image = _json['image']
        _approval = _json['approval']
        _status = _json['status']
        _userId = _json['userId']

        # save edits
        sql = " INSERT INTO tbl_post(text, file, image, approval, " \
              " createdDate, modifiedDate, status, userId) VALUES(%s, %s, %s, %s, NOW(), NOW(), %s, %s)"

        data = (_text, _file, _image, _approval, _status, _userId)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Post added successfully')
            resp.status_code = 201
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all post
@app.route('/post')  # @token_required
def show_all_post():
    try:
        sql = "SELECT * FROM tbl_post"
        rows = readAllRecord(sql)

        result = []

        # Convert date time format for output
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


# list specific post
@app.route('/post/<int:postId>')  # @token_required
def show_post(postId):
    try:
        sql = "SELECT * FROM tbl_post WHERE postId=%s"

        row = readOneRecord(sql, postId)

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


# Update post
@app.route('/post/update/<int:postId>', methods=['PUT'])  # @token_required
def update_post(postId):
    try:
        _json = request.json

        _text = _json['text']
        _file = _json['file']
        _image = _json['image']
        _approval = _json['approval']
        _status = _json['status']
        _userId = _json['userId']

        # save edits
        sql = " UPDATE tbl_post SET text=%s, file=%s, image=%s, approval=%s, " \
              " modifiedDate=NOW(), status=%s, userId=%s WHERE postId=%s"

        data = (_text, _file, _image, _approval, _status, _userId, postId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Post updated successfully!')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete post (update status to false)
# This API doesn't requires admin privilege as user can delete their post.
@app.route('/post/delete/<int:postId>', methods=['PUT'])  # @token_required
def delete_post(postId):
    try:
        sql = "UPDATE tbl_post SET modifiedDate = NOW(), status = 'false' WHERE postId=%s"

        if updateRecord(sql, postId) > 0:
            resp = jsonify(message='Post successfully inactivated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)
