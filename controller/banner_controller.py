from app import app
from flask import jsonify, request
from database.db_execution import *
from error_handler import *
from token_verifier import *


# add banner
@app.route('/banner/add', methods=['POST'])
@is_admin
def add_banner():
    try:
        _json = request.json

        _bannerImage = _json['bannerImage']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _sequence = _json['sequence']
        _recordStatus = _json['recordStatus']

        # save edits
        sql = "INSERT INTO tbl_banner(bannerImage, startDate, endDate, sequence, recordStatus) VALUES(%s, %s, %s, %s, %s)"
        data = (_bannerImage, _startDate, _endDate, _sequence, _recordStatus)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Banner added successfully')
            resp.status_code = 201
            return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all banners
@app.route('/banner')
@token_required
def show_all_banner():
    try:
        sql = "SELECT * FROM tbl_banner"
        rows = readAllRecord(sql)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific banner
@app.route('/banner/<int:bannerId>')
@token_required
def show_banner(bannerId):
    try:
        sql = "SELECT * FROM tbl_banner WHERE bannerId=%s"
        row = readOneRecord(sql, bannerId)
        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update Banner
@app.route('/banner/update/<int:bannerId>', methods=['PUT'])
@is_admin
def update_banner(bannerId):
    try:
        _json = request.json

        _bannerImage = _json['bannerImage']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _sequence = _json['sequence']
        _recordStatus = _json['recordStatus']

        # save edits
        sql = "UPDATE tbl_banner SET bannerImage=%s, startDate=%s, endDate=%s, sequence=%s, recordStatus=%s WHERE bannerId=%s"
        data = (_bannerImage, _startDate, _endDate, _sequence, _recordStatus, bannerId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Banner updated successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete Banner
@app.route('/banner/delete/<int:bannerId>', methods=['DELETE'])
@is_admin
def delete_banner(bannerId):
    try:

        sql = "DELETE FROM tbl_banner WHERE bannerId=%s"

        if deleteRecord(sql, bannerId) > 0:
            resp = jsonify(message='Banner deleted successfully')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
