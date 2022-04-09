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

        if createRecord(sql, data) > 0:
            resp = jsonify(message="OTP sent and stored")
            resp.status_code = 200
            return resp
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


@app.route('/OTPService/verify/<string:email>', methods=['POST'])
def verifyOTP(email):
    try:
        _json = request.json

        _otp = _json['otp']

        if _otp and request.method == 'POST':
            sql = "SELECT otp FROM tbl_otp WHERE personalEmail = %s ORDER BY otpId DESC LIMIT 1"

            row = readOneRecord(sql, email)

            # Invalid personal email
            if not row:
                return not_found()

            # Default value if not match
            resp = jsonify(otpVerify=0, message="Unsuccessful verification")
            resp.status_code = 400

            # User input OTP match with OTP sent, update status
            if row['otp'] == _otp:
                resp = jsonify(otpVerify=1, message="Successfully verified")
                resp.status_code = 200

            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)
