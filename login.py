from app import app
import pymysql
from db_config import mysql
from flask import jsonify, request
import uuid
import hashlib
from db_execution import *


#Only extracting integer from string
def extractOnlyInteger(s):
    num = ''.join(x for x in s if x.isdigit())
    return num


#MD5 hashing
def md5Hash(s):
    return hashlib.md5(s.encode()).hexdigest()


#Generate UUID for user
def generateUUID():
    return uuid.uuid4()


# login status (1 = invalid credential, 2 = login successful)
@app.route('/login', methods=['POST'])
def verifyUser():
    try:
        _json = request.json
        _username = _json['username']
        _password = _json['password']
        # validate the received values
        if _username and _password:

            sql = "SELECT tu.*, ta.name FROM tbl_user tu LEFT JOIN tbl_alumni ta ON tu.username = ta.studentId WHERE tu.username=%s"
            data = _username
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            row = cursor.fetchone()

            if row:

                alumniName = row[6]

                # If password validate successful
                if row[2] == _password:
                    return jsonify(loginStatus=2, userID=row[0], activationStatus=row[4], name=alumniName)  # Login Successful
                else:
                    return jsonify(loginStatus=1, userID=0, activationStatus=0)  # Invalid credential
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
                        sql = "INSERT INTO tbl_user (username, password, alumniId, activationStatus, GUID) VALUES (%s, %s, %s, %s, %s)"
                        data = (row1[3], _password, row1[0], 0, generateUUID())
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
                            return jsonify(loginStatus=2, userID=row3[0], activationStatus=row3[4], name=alumniName)
                        else:
                            return jsonify(loginStatus=1, userID=0, activationStatus=0)
                    else:
                        return jsonify(loginStatus=1, userID=0, activationStatus=0)  # Invalid credential

                else:
                    return jsonify(loginStatus=1, userID=0, activationStatus=0)  # Invalid credential
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()




