from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *


# add merchant
@app.route('/merchant/add', methods=['POST'])
# @is_admin
def add_merchant():
    try:
        _json = request.json

        _name = _json['name']
        _logo = _json['logo']

        # save edits
        sql = "INSERT INTO tbl_merchant(name, logo, createdDate, modifiedDate, status) VALUES(%s, %s, NOW(), NOW(), 1)"
        data = (_name, _logo)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Merchant added successfully')
            resp.status_code = 201
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all merchant
@app.route('/merchant')
# @is_admin
def show_all_merchant():
    try:
        sql = "SELECT * FROM tbl_merchant WHERE status = 1"
        rows = readAllRecord(sql)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific merchant
@app.route('/merchant/<int:merchantId>')
# @is_admin
def show_merchant(merchantId):
    try:
        sql = "SELECT * FROM tbl_merchant WHERE merchantId=%s AND status = 1"
        row = readOneRecord(sql, merchantId)
        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update Merchant
@app.route('/merchant/update/<int:merchantId>', methods=['PUT'])
# @is_admin
def update_merchant(merchantId):
    try:
        _json = request.json

        _name = _json['name']
        _logo = _json['logo']

        # save edits
        sql = "UPDATE tbl_merchant SET name=%s, logo=%s, modifiedDate=NOW() WHERE merchantId=%s"
        data = (_name, _logo, merchantId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Merchant updated successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete merchant
# Update status to 0 (false)
@app.route('/merchant/delete/<int:merchantId>', methods=['PUT'])
# @is_admin
def delete_merchant(merchantId):
    try:

        sql = "UPDATE tbl_merchant SET status = 0 WHERE merchantId = %s"

        if deleteRecord(sql, merchantId) > 0:
            resp = jsonify(message='Merchant deleted successfully')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
