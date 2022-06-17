from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *
from datetime import timedelta, date


# add voucher
@app.route('/voucher/add', methods=['POST'])
# @token_required
def add_voucher():
    try:
        _json = request.json

        _merchantId = _json['merchantId']
        _code = _json['code']
        _title = _json['title']
        _description = _json['description']
        _image = _json['image']
        _expiryType = _json['expiryType']
        _expiryDate = _json['expiryDate']
        _expiryDay = _json['expiryDay']
        _voucherClaimableAmount = _json['voucherClaimableAmount']
        _voucherLimit = _json['voucherLimit']
        _startDate = _json['startDate']
        _endDate = _json['endDate']

        # save edits
        sql = " INSERT INTO tbl_voucher(merchantId, code, title, description, image, " \
              " expiryType, expiryDate, expiryDay, voucherClaimableAmount, voucherLimit, " \
              " startDate, endDate, createdDate, modifiedDate, status) VALUES (%s, %s, %s, " \
              " %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW(), 1)"
        data = (_merchantId, _code, _title, _description, _image, _expiryType, _expiryDate,
                _expiryDate, _voucherClaimableAmount, _voucherLimit, _startDate, _endDate)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Voucher added successfully')
            resp.status_code = 201
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all claimable voucher for the user
@app.route('/voucher/<int:userId>')
# @token_required
def show_all_voucher_for_user(userId):
    try:
        sql = " SELECT tv.*, tm.name AS 'merchantName', tm.logo AS 'merchantLogo' " \
              " FROM (tbl_voucher tv " \
              " LEFT JOIN tbl_user_voucher tuv " \
              " ON tv.voucherId = tuv.voucherId" \
              " LEFT JOIN tbl_merchant tm" \
              " ON tm.merchantId = tv.merchantId) " \
              " WHERE tv.status = 1 " \
              " AND tm.status = 1 " \
              " GROUP BY tv.voucherId " \
              " HAVING COUNT(tuv.userId = %s) < tv.voucherClaimableAmount " \
              " AND COUNT(tuv.voucherId) < tv.voucherLimit;"

        rows = readAllRecord(sql, userId)

        if not rows:
            resp = jsonify(message="No claimable voucher for user")
            resp.status_code = 400
            return resp

        result = []

        # Convert date time format for output
        for row in rows:
            row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")
            row['createdDate'] = row['createdDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['modifiedDate'] = row['modifiedDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# retrieve user voucher
@app.route('/voucher/<string:voucherStatus>/<int:userId>')
# @token_required
def list_user_claimed_voucher(voucherStatus, userId):
    try:
        sql = " SELECT tv.title, tv.description, tv.image, " \
              " tm.name, tm.logo, tuv.* " \
              " FROM tbl_user_voucher tuv " \
              " LEFT JOIN tbl_voucher tv " \
              " ON tuv.voucherId = tv.voucherId " \
              " LEFT JOIN tbl_merchant tm " \
              " ON tv.merchantId = tm.merchantId " \
              " WHERE tuv.userId = %s " \

        if voucherStatus == "active":
            sql += " AND tuv.redeemable = 1 " \
                   " AND NOW() < tuv.expiryDate "
        elif voucherStatus == "expired":
            sql += " AND NOW() > tuv.expiryDate "
        elif voucherStatus == "redeemed":
            sql += " AND tuv.redeemable = 0 "

        rows = readAllRecord(sql, userId)

        if not rows:
            not_found()

        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# valid voucher
@app.route('/voucher/valid/<int:voucherId>')
#@token_required
def valid_voucher_claim(voucherId):
    try:
        _json = request.json

        sql = " SELECT tv.voucherLimit " \
              " FROM (tbl_voucher tv " \
              " INNER JOIN tbl_user_voucher tuv " \
              " ON tv.voucherId = tuv.voucherId) " \
              " GROUP BY tv.voucherId " \
              " HAVING COUNT(tuv.voucherId = %s) < tv.voucherLimit "

        row = readOneRecord(sql, voucherId)

        if not row:
            resp = jsonify(message='Voucher has been fully claim')
            resp.status_code = 400
            return resp

        resp = jsonify(message='Voucher is claimable')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# claim voucher
@app.route('/voucher/claim', methods=['POST'])
# @token_required
def claim_voucher():
    try:
        _json = request.json

        _userId = _json['userId']
        _voucherId = _json['voucherId']

        # Get expiry date
        sql = " SELECT tv.expiryType, tv.code, tv.voucherLimit, " \
              " COUNT(tuv.voucherId) AS 'currentVoucherCount', " \
              " CASE WHEN tv.expiryType = 1 THEN tv.expiryDate " \
              " ELSE tv.expiryDay " \
              " END AS 'expiry' " \
              " FROM tbl_voucher tv " \
              " JOIN tbl_user_voucher tuv " \
              " ON tv.voucherId = tuv.voucherId " \
              " WHERE tv.voucherId = %s " \
              " GROUP BY tv.voucherId "
        row = readOneRecord(sql, _voucherId)

        if not row:
            not_found()

        # if expiryType = 1, then use expiryDate
        # else have to get today + expiryDays
        if int(row['expiryType']) == 1:
            expiryDate = row['expiry']
        else:
            expiryDate = date.today() + timedelta(days=int(row['expiry']))

        # Obtain barcode
        # get integer length
        length = len(str(row['voucherLimit']))

        # format the number
        temp = format(row['currentVoucherCount'], '0' + str(length) + 'd')
        barcode = row["code"] + str(temp)

        # save edits
        sql = " INSERT INTO tbl_user_voucher(userId, voucherId, redeemable, barcode," \
              " expiryDate, createdDate) VALUES(%s, %s, 1, %s, %s, NOW()) "

        data = (_userId, _voucherId, barcode, expiryDate)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Voucher successfully claimed')
            resp.status_code = 200
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Redeem Voucher
@app.route('/voucher/redeem/<int:userVoucherId>', methods=['PUT'])
# @token_required
def redeem_voucher(userVoucherId):
    try:
        # save edits
        sql = " UPDATE tbl_user_voucher SET redeemable = 0, modifiedDate = NOW() WHERE userVoucherId = %s"

        if updateRecord(sql, userVoucherId) > 0:
            resp = jsonify(message='Voucher redeem successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update Voucher
@app.route('/voucher/update/<int:voucherId>', methods=['PUT'])
# @is_admin
def update_voucher(voucherId):
    try:
        _json = request.json

        _merchantId = _json['merchantId']
        _code = _json['code']
        _title = _json['title']
        _description = _json['description']
        _image = _json['image']
        _expiryType = _json['expiryType']
        _expiryDate = _json['expiryDate']
        _expiryDay = _json['expiryDay']
        _voucherClaimableAmount = _json['voucherClaimableAmount']
        _voucherLimit = _json['voucherLimit']
        _startDate = _json['startDate']
        _endDate = _json['endDate']

        # save edits
        sql = " UPDATE tbl_voucher SET merchantId = %s, code = %s, title = %s, description = %s, " \
              " image = %s, expiryType = %s, expiryDate = %s, expiryDay = %s, voucherClaimableAmount = %s, " \
              " voucherLimit = %s, startDate = %s, endDate = %s, modifiedDate = NOW() WHERE voucherId = %s"
        data = (_merchantId, _code, _title, _description, _image, _expiryType, _expiryDate,
                _expiryDate, _voucherClaimableAmount, _voucherLimit, _startDate, _endDate, voucherId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Voucher updated successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete voucher
# Update status to 0 (false)
@app.route('/voucher/delete/<int:voucherId>', methods=['PUT'])
# @is_admin
def delete_voucher(voucherId):
    try:

        sql = "UPDATE tbl_voucher SET status = 0 WHERE voucherId = %s"

        if deleteRecord(sql, voucherId) > 0:
            resp = jsonify(message='voucher successfully deleted')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
