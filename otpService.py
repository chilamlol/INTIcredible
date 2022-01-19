from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request
from flask_mail import Message
from random import randint
from mail_config import mail
from emailTemplate import *


# sendOTP
@app.route('/OTPservice/send/<string:email>')
def sendOTP(email):
    try:
        otp = randint(000000, 999999)
        msg = Message('OTP', recipients=email.split())
        msg.html = OTPemail(otp)
        mail.send(msg)

        #write to table
        sql = "INSERT INTO tbl_otp (personalEmail, otp, date) Values (%s, %s, CURRENT_DATE())"
        data = (email, otp)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify(message="OTP sent and stored",status="200")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/OTPservice/verify/<string:email>',methods=['POST'])
def verifyOTP(email):
    conn = None
    cursor = None
    try:
        _json = request.json
        _otp = _json['otp']
        _userID = _json['userID']
        if _otp:
            sql = "SELECT otp FROM tbl_otp WHERE personalEmail = %s ORDER BY otpId DESC LIMIT 1"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, email)
            row = cursor.fetchone()
            if row[0] == _otp:
                sql = "UPDATE tbl_user set activationStatus=30 where userID=%s"
                data = _userID
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                return jsonify(otpVerify=1)
        return jsonify(otpVerify=0)
    except Exception as e:
        print(e)



