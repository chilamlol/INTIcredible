from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *


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


# reset user password
@app.route('/account/reset-password', methods=['POST'])
def reset_password():
    try:
        _json = request.json
        _userId = _json['userId']
        _password = _json['password']
        if _userId and _password and request.method == 'POST':

            sql = "SELECT * FROM tbl_user WHERE userId=%s"
            data = _userId
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            row = cursor.fetchone()
            if row:
                if row[4] == 0:
                    sql = "UPDATE tbl_user set password=%s, activationStatus=10 where userId=%s"
                    data = (_password, _userId)
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.execute(sql, data)
                    conn.commit()
                    resp = jsonify(message="Password Update Successfully!", status="200")
                    resp.status_code = 200
                    return resp
                else:
                    sql = "UPDATE tbl_user set password=%s where userId=%s"
                    data = (_password, _userId)
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.execute(sql, data)
                    conn.commit()
                    resp = jsonify(message="Password Reset Successfully!", status="200")
                    resp.status_code = 200
                    return resp
            else:
                resp = jsonify(message="Unable to find user!", status="201")
                resp.status_code = 201
                return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# update profile
@app.route('/account/update-profile', methods=['POST'])
def update_profile():
    try:
        _json = request.json
        _userId = _json['userId']
        _email = _json['email']
        _handphone = _json['handphone']
        _telephone = _json['telephone']
        if _userId and _email and _handphone and _telephone and request.method == 'POST':

            sql = "SELECT * FROM tbl_user WHERE userId=%s"
            data = _userId
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            row = cursor.fetchone()

            if row:
                sql = "UPDATE tbl_alumni set personalEmail=%s, studentHandphone=%s, studentTelephoneNumber=%s where alumniId=%s"
                data = (_email, _handphone, _telephone, row[3])
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()

                sql = "UPDATE tbl_user set activationStatus=20 where userId=%s"
                data = _userId
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()

                resp = jsonify(message="Update Successful!", status="200")
                resp.status_code = 200
                return resp
            else:
                resp = jsonify(message="Unable to find user!", status="201")
                resp.status_code = 201
                return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/account/info/<string:username>")
def get_account_info(username):
    try:
        sql = "SELECT tu.userId, ta.personalEmail FROM tbl_user tu JOIN tbl_alumni ta ON tu.username = ta.studentId WHERE tu.username=%s"

        row = readOneRecord(sql, username)

        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)

