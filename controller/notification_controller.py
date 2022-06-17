from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


# create notification
@app.route('/notification/add', methods=['POST'])
# @is_admin
def add_notification():
    try:
        _json = request.json

        _title = _json['title']
        _description = _json['description']
        _image = _json['image']
        _push = _json['push']

        # save edits
        sql = " INSERT INTO tbl_notification(title, description, image, push, " \
              " createdDate, modifiedDate, status) VALUES (%s, %s, %s, %s, NOW(), NOW(), 1) "

        data = (_title, _description, _image, _push)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Notification added successfully')
            resp.status_code = 201
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all active notification
# pushed or not pushed notification depends on input
@app.route('/notification/<string:isPushed>')
# @token_required
def show_all_notification(isPushed):
    try:
        sql = " SELECT * FROM tbl_notification WHERE status = 1 "

        # if isPushed = 1, display only active and pushed notification
        if isPushed == "pushed":
            sql += " AND push = 1 "
        elif isPushed == "notPushed":
            sql += " AND push = 0 "

        rows = readAllRecord(sql)

        result = []

        # Convert date time format for output
        # yyyy-MM-dd HH:MM:SS
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


# list specific active notification
@app.route('/notification/<int:notificationId>')
# @is_admin
def show_notification(notificationId):
    try:
        sql = "SELECT * FROM tbl_notification WHERE notificationId=%s AND status = 1"

        row = readOneRecord(sql, notificationId)

        if not row:
            return not_found()

        # Convert date time format for output
        row['createdDate'] = row['createdDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
        row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update notification
@app.route('/notification/update/<int:notificationId>', methods=['PUT'])
# @is_admin
def update_notification(notificationId):
    try:
        _json = request.json

        _title = _json['title']
        _description = _json['description']
        _image = _json['image']
        _push = _json['push']

        # save edits
        sql = " UPDATE tbl_notification SET title=%s, description=%s, " \
              " image=%s, push=%s WHERE notificationId=%s"

        data = (_title, _description, _image, _push, notificationId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Notification updated successfully')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Push notification
@app.route('/notification/push/<int:notificationId>', methods=['PUT'])
# @is_admin
def push_notification(notificationId):
    try:

        # save edits
        sql = " UPDATE tbl_notification SET push = 1, " \
              " modifiedDate=NOW() WHERE notificationId=%s"

        if updateRecord(sql, notificationId) > 0:
            resp = jsonify(message='Notification successfully pushed')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete notification (update status to false)
@app.route('/notification/delete/<int:notificationId>', methods=['PUT'])
# @is_admin
def delete_notification(notificationId):
    try:
        sql = "UPDATE tbl_notification SET modifiedDate = NOW(), status = 0 WHERE notificationId=%s"

        if updateRecord(sql, notificationId) > 0:
            resp = jsonify(message='Notification successfully inactivated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)
