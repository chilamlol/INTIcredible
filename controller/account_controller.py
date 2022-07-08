from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *
from controller.login_controller import generateUUID


# Initial activate user account
@app.route("/activate/<int:userId>", methods=['PUT'])
def activate_user_account(userId):
    try:
        sql = "UPDATE tbl_user set activationStatus=30 where userId=%s"

        if updateRecord(sql, userId) > 0:
            resp = jsonify(message='User account successfully activated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)

# List admins
@app.route("/account/admin")
#@is_super_admin
def show_admins():
    try:
        sql = "SELECT * FROM tbl_user WHERE userRoleId = 3"
        rows = readAllRecord(sql)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)

# Create Admin
@app.route("/account/admin/add", methods=['POST'])
#@is_super_admin
def add_admin():
    try:
        _json = request.json

        _username = _json['username']
        _password = _json['password']

        sql = " INSERT INTO tbl_user(username, password, activationStatus, GUID, " \
              " userRoleId) VALUES (%s, %s, 30, %s, 3) "
        data = (_username, _password, generateUUID())

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Admin added successfully')
            resp.status_code = 201
            return resp

        # unsuccessful to add admin
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# help Admin reset password
@app.route("/account/admin/reset-password/<string:username>", methods=['PUT'])
@is_super_admin
def change_admin_password(username):
    try:
        _json = request.json

        _password = _json['password']

        sql = " UPDATE tbl_user SET password = %s WHERE username = %s AND userRoleId IN (2, 3)"
        data = (_password, username)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Admin password updated successfully')
            resp.status_code = 200
            return resp

        # unsuccessful to add admin
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# reset user password
@app.route('/account/reset-password/<int:userId>', methods=['PUT'])
def reset_user_password(userId):
    try:
        _json = request.json

        _password = _json['password']

        if _password and request.method == 'PUT':

            # Check if password no changes
            sql = " SELECT * FROM tbl_user WHERE password = %s AND  userId = %s "
            data = (_password, userId)

            row = readOneRecord(sql, data)

            # if return row, then password is the same
            if row:
                resp = jsonify(message = 'Password remain unchange')
                resp.status_code = 202
                return resp

            # Update data
            sql = " UPDATE tbl_user SET password=%s, activationStatus= CASE WHEN activationStatus = 0 THEN 10 ELSE activationStatus END WHERE userId=%s "

            # if update successful return code 200
            if updateRecord(sql, data) > 0:
                resp = jsonify(message='Password reset successfully')
                resp.status_code = 200
                return resp

            # else return user not found
            return not_found()

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# update profile
@app.route('/account/update-profile/<int:userId>', methods=['PUT'])
def update_user_profile(userId):
    try:
        _json = request.json
        _email = _json['email']
        _handphone = _json['handphone']
        _telephone = _json['telephone']
        _profilePicture = _json['profilePicture']
        if _email and _handphone and _telephone and request.method == 'PUT':

            sql = "UPDATE tbl_alumni ta JOIN tbl_user tu ON ta.alumniId = tu.alumniId " \
                  "SET ta.personalEmail=%s, ta.studentHandphone=%s, ta.studentTelephoneNumber=%s, tu.profilePicture=%s, " \
                  "tu.activationStatus = CASE WHEN tu.activationStatus = 10 THEN 20 ELSE tu.activationStatus END WHERE tu.userId=%s "
            data = (_email, _handphone, _telephone,_profilePicture, userId)

            if updateRecord(sql, data) > 0:
                resp = jsonify(message='User profile successfully updated')
                resp.status_code = 200
                return resp

            return not_found()

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# get user info by username or userId
@app.route("/account/info/<string:userIdOrUsername>")
def get_user_info_by_username_or_userId(userIdOrUsername):
    try:
        sql = " SELECT tu.*, ta.personalEmail, ta.studentHandphone, ta.studentTelephoneNumber " \
              " FROM tbl_user tu JOIN tbl_alumni ta ON tu.username = ta.studentId WHERE tu.username=%s OR tu.userId=%s"
        data = (userIdOrUsername, userIdOrUsername)

        row = readOneRecord(sql, data)

        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)

