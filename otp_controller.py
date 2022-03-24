from app import app
from flask import jsonify
from flask import request
from flask_mail import Message
from random import randint
from mail_config import mail
from email_template import *
from error_handler import *
from db_execution import *


def getOTP():
    # Generate random 6 digit OTP
    return randint(000000, 999999)


# sendOTP
@app.route('/OTPService/send/<string:email>')
def sendOTP(email):
    try:
        # generate OTP
        otp = getOTP()

        # Send OTP to email
        msg = Message('OTP', recipients=email.split())
        msg.html = emailOTP(otp)
        mail.send(msg)

        # write to table
        sql = "INSERT INTO tbl_otp (personalEmail, otp, date) Values (%s, %s, CURRENT_DATE())"
        data = (email, otp)

        if createRecord(sql, data):
            resp = jsonify(message="OTP sent and stored")
            resp.status_code = 200
        else:
            resp = jsonify(message="Unable to store")
            resp.status_code = 400
        return resp

    except Exception as e:
        print(e)
        return internal_server_error(e)


@app.route('/OTPService/verify/<string:email>', methods=['POST'])
def verifyOTP(email):
    try:
        _json = request.json

        # return if json body is empty
        if not _json:
            return bad_request()

        # return if json parameter incomplete
        if 'userId' and 'otp' not in _json:
            return unprocessable_entity()

        _otp = _json['otp']

        if _otp and request.method == 'POST':
            sql = "SELECT otp FROM tbl_otp WHERE personalEmail = %s ORDER BY otpId DESC LIMIT 1"

            result = readRecord(sql, email)

            # Invalid personal email
            if not result:
                return not_found()

            # User input OTP match with OTP sent, update status
            if result[0] == _otp:
                resp = jsonify(otpVerify=1, message="Successfully verified")
                resp.status_code = 200
                return resp

        resp = jsonify(otpVerify=0, message="Unsuccessful verification")
        resp.status_code = 400
        return resp

    except Exception as e:
        print(e)
        return internal_server_error(e)
