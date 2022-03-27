from app import app
import pymysql
from db_config import mysql
from flask import jsonify, request
import uuid
import hashlib
from db_execution import *
import jwt
import enum
from error_handler import *


# Login status
class loginStatus(enum.Enum):
    Success = 1
    Invalid = 2


# Only extracting integer from string
def extractOnlyInteger(s):
    num = ''.join(x for x in s if x.isdigit())
    return num


# MD5 hashing
def md5Hash(s):
    return hashlib.md5(s.encode()).hexdigest()


# Generate UUID for user
def generateUUID():
    return uuid.uuid4()


def generateToken(guid):
    return jwt.encode({'guid': guid}, app.config['SECRET_KEY'])


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
            row = readOneRecord(sql, data)

            # If account found
            if row:
                # If password validate successful
                if row['password'] == _password:
                    # Generate token if login successful
                    token = generateToken(row['GUID'])

                    return jsonify(loginStatus=loginStatus.Success.value, userID=row['userId'],
                                   activationStatus=row['activationStatus'],
                                   name=row['name'],
                                   token=token, userRole=row['userRoleId'])  # Login Successful

                # Invalid Credentials
                return jsonify({'error': 'Invalid credentials: ' + request.url}), 401

            # No account found, first time login
            else:
                sql = "SELECT * FROM tbl_alumni WHERE studentId=%s"
                data = _username
                row = readOneRecord(sql, data)
                if row:
                    rawPassword = row1['graduatingCampus'] + row1['identificationCard']
                    hashedPassword = md5Hash(rawPassword)

                    # Compare password with user entered password
                    if hashedPassword == _password:
                        sql = "INSERT INTO tbl_user (username, password, alumniId, activationStatus, GUID) VALUES (%s, %s, %s, %s, %s)"
                        data = (row1['studentId'], _password, row1['alumniId'], 0, generateUUID())
                        conn = mysql.connect()
                        cursor = conn.cursor()
                        cursor.execute(sql, data)
                        conn.commit()

                        sql = "SELECT tu.*, ta.name FROM tbl_user tu LEFT JOIN tbl_alumni ta ON tu.username = ta.studentId WHERE tu.username=%s"
                        data = _username
                        row = readOneRecord(sql, data)

                        if row:
                            token = generateToken(row['GUID'])
                            return jsonify(loginStatus=2, userID=row['userId'],
                                           activationStatus=row['activationStatus'], name=row['name'], token=token, userRole=row['userRoleId'])
                        else:
                            return jsonify(loginStatus=1, userID=0, activationStatus=0)
                    else:
                        return jsonify(loginStatus=1, userID=0, activationStatus=0)  # Invalid credential

                else:
                    return jsonify(loginStatus=1, userID=0, activationStatus=0)  # Invalid credential

        return bad_request()
    except Exception as e:
        print(e)
