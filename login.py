from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request
from flask_jwt import JWT, jwt_required, current_identity
import hashlib


def extractOnlyInteger(s):
    num = ''.join(x for x in s if x.isdigit())
    return num


def md5Hash(s):
    return hashlib.md5(s.encode()).hexdigest()


# login status (1 = invalid credential, 2 = login successful)
@app.route('/login', methods=['POST'])
def verifyUser():
    try:
        _json = request.json
        _username = _json['username']
        _password = _json['password']
        # validate the received values
        if _username and _password:

            sql = "SELECT * FROM tbl_user WHERE username=%s"
            data = _username
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            row = cursor.fetchone()
            if row:
                # If password validate successful
                if row[2] == _password:
                    return jsonify(loginStatus=2, userId=row[0], activationStatus=row[4])  # Login Successful
                else:
                    return jsonify(loginStatus=1, userId=0, activationStatus=0)  # Invalid credential
            else:
                sql = "SELECT * FROM tbl_alumni WHERE studentId=%s"
                data = _username
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                row1 = cursor.fetchone()
                if row1:
                    rawPassword = row1[7] + row1[2]
                    hashedPassword = md5Hash(rawPassword)
                    if hashedPassword == _password:
                        sql = "INSERT tbl_user (username, password, alumniId, activationStatus) values (%s,%s,%s,%s)"
                        data = (row1[3], _password, row1[0], 0)
                        conn = mysql.connect()
                        cursor = conn.cursor()
                        cursor.execute(sql, data)
                        conn.commit()

                        sql = "SELECT * FROM tbl_user WHERE username=%s"
                        data = _username
                        cursor = conn.cursor()
                        cursor.execute(sql, data)
                        row3 = cursor.fetchone()

                        if row3:
                            return jsonify(loginStatus=2, userId=row3[0], activationStatus=row3[4])
                        else:
                            return jsonify(loginStatus=1, userId=0, activationStatus=0)
                    else:
                        return jsonify(loginStatus=1, userId=0, activationStatus=0)  # Invalid credential

                else:
                    return jsonify(loginStatus=1, userId=0, activationStatus=0)  # Invalid credential
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# reset user password
@app.route('/account/reset-password', methods=['POST'])
def resetPassword():
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
def updateProfile():
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


def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
