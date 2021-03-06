from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
import json
from token_verifier import *


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

# list all post for admin
@app.route('/post')
@token_required
def show_all_posts():
    try:
        sql = " SELECT tp.*, ta.name AS 'alumniName' " \
              " FROM (tbl_post tp " \
              " LEFT JOIN tbl_user tu " \
              " ON tp.userId = tu.userId" \
              " LEFT JOIN tbl_alumni ta" \
              " ON tu.alumniId = ta.alumniId) " \
              " WHERE tp.status = 1 " \
              " ORDER BY tp.createdDate DESC "

        rows = readAllRecord(sql)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['createdDate'] = row['createdDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)

# create post
@app.route('/post/add', methods=['POST'])
# @token_required
def add_post():
    try:
        _json = request.json

        _text = _json['text']
        _file = _json['file']
        _image = _json['image']
        _userId = _json['userId']

        # save edits
        sql = " INSERT INTO tbl_post(text, file, image, approval, " \
              " createdDate, modifiedDate, status, userId) VALUES(%s, %s, %s, 0, NOW(), NOW(), 1, %s)"

        data = (_text, _file, _image, _userId)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Post added successfully')
            resp.status_code = 201
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all post active and approved
@app.route('/post/<string:approval>')
# @token_required
def show_all_post(approval):
    try:
        sql = " SELECT * FROM tbl_post WHERE status = 1 "

        # Approval have 3 condition, if input anything else return all
        if approval == "rejected":
            sql += " AND approval = 2 "
        elif approval == "pending":
            sql += " AND approval = 0 "
        elif approval == "approved":
            sql += " AND approval = 1 "

        # 1st come 1st serve approval
        sql += " ORDER BY createdDate asc"

        rows = readAllRecord(sql)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['createdDate'] = row['createdDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)

"""
# list specific active and approved post
@app.route('/post/<int:postId>')
# @token_required
def show_post(postId):
    try:
        sql = "SELECT * FROM tbl_post WHERE postId=%s AND status = 1"

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
"""


# list pending or rejected post by user
@app.route('/post/<string:approval>/<int:userId>')
# @token_required
def show_post_by_user(approval, userId):
    try:
        sql = " SELECT * FROM tbl_post WHERE userId=%s AND status = 1 "

        # Approval have 3 condition, if input anything else return all
        if approval == "rejected":
            sql += " AND approval = 2 "
        elif approval == "pending":
            sql += " AND approval = 0 "
        elif approval == "approved":
            sql += " AND approval = 1 "

        sql += " ORDER BY createdDate DESC "

        rows = readAllRecord(sql, userId)

        if not rows:
            return not_found()

        result = []

        # Convert date time format for output
        for row in rows:
            row['createdDate'] = row['createdDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list post and their comment
@app.route('/post/nested/<int:userId>')
# @token_required
def show_all_post_nested(userId):
    try:
        # Requires MySQL 5.7 and above
        sql = " SELECT JSON_ARRAYAGG(JSON_OBJECT('postId', tp.postId, 'text', tp.text, 'file', tp.file, " \
              " 'image', tp.image, 'approval', tp.approval, 'createdDate', DATE_FORMAT(tp.createdDate, '%%Y-%%m-%%d %%T'), " \
              " 'modifiedDate', DATE_FORMAT(tp.modifiedDate, '%%Y-%%m-%%d %%T'), " \
              " 'status', tp.status, 'userId', tp.userId, 'likeCount', IFNULL(likeCount,0), 'comment', tc.commentList, " \
              " 'userProfile', tu.profilePicture, 'userName', ta.name, " \
              " 'userLike', EXISTS(SELECT 1 FROM tbl_like tl WHERE tl.postId = tp.postId and status=1 and userId=%s))) " \
              " FROM " \
              " tbl_post tp Join tbl_user tu on tp.userId = tu.userId join tbl_alumni ta on tu.alumniId = ta.alumniId " \
              " LEFT JOIN ( " \
              " SELECT postId, " \
              " JSON_ARRAYAGG(JSON_OBJECT('commentId', tc.commentId, 'text', tc.text, 'createdDate', DATE_FORMAT(tc.createdDate, '%%Y-%%m-%%d %%T'), " \
              " 'modifiedDate', DATE_FORMAT(tc.modifiedDate, '%%Y-%%m-%%d %%T'), 'status', tc.status, 'userId', " \
              " tc.userId,'userProfile', tu.profilePicture,'userName',ta.name)) commentList " \
              " FROM tbl_comment tc Join tbl_user tu on tc.userId = tu.userId join tbl_alumni ta on tu.alumniId = ta.alumniId " \
              " GROUP BY postId " \
              " ) tc ON tp.postId = tc.postId " \
              " LEFT JOIN ( " \
              " SELECT postId, count(userId) AS 'likeCount' " \
              " FROM tbl_like where status=1" \
              " GROUP BY postId " \
              " ) tl ON tp.postId = tl.postId " \
              " WHERE tp.status = 1 AND tp.approval = 1 " \
              " ORDER BY tp.createdDate DESC "

        row = readNestedRecord(sql, userId)

        if row is None:
            return not_found()

        # Convert list to string to remove unwanted characters
        res = str(row)[2:-3].replace("\\", "")

        # Convert back to JSON
        resp = jsonify(json.loads(res))
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update post
@app.route('/post/update/<int:postId>', methods=['PUT'])
# @token_required
def update_post(postId):
    try:
        _json = request.json

        _text = _json['text']
        _file = _json['file']
        _image = _json['image']

        # save edits
        sql = " UPDATE tbl_post SET text=%s, file=%s, image=%s, " \
              " modifiedDate=NOW() WHERE postId=%s"

        data = (_text, _file, _image, postId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Post updated successfully')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Approve post
@app.route('/post/<string:approval>/<int:postId>', methods=['PUT'])
# @is_admin
def approve_post(approval, postId):
    try:
        _json = request.json

        if approval == "approve":
            _approval = 1
        elif approval == "reject":
            _approval = 2
        else:
            # unknown input
            return bad_request()

        # save edits
        sql = " UPDATE tbl_post SET approval=%s, " \
              " modifiedDate=NOW() WHERE postId=%s"

        data = (_approval, postId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Post approval successfully updated')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete post (update status to false)
# This API doesn't requires admin privilege as user can delete their post.
@app.route('/post/delete/<int:postId>', methods=['PUT'])
# @token_required
def delete_post(postId):
    try:
        sql = "UPDATE tbl_post SET modifiedDate = NOW(), status = 0 WHERE postId=%s"

        if updateRecord(sql, postId) > 0:
            resp = jsonify(message='Post successfully inactivated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)
