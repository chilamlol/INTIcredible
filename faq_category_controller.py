from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *


# add FAQ category
@app.route('/faq/category/add', methods=['POST'])
def add_faq_category():
    try:
        _json = request.json

        # return error if json body is empty
        if not _json:
            return bad_request()

        # return error if json parameter incomplete
        if 'name' and 'recordStatus' not in _json:
            return unprocessable_entity()

        _name = _json['name']
        _recordStatus = _json['recordStatus']

        # validate the received values
        if _name and _recordStatus and request.method == 'POST':

            # save edits
            sql = "INSERT INTO tbl_faq_category(name, recordStatus) VALUES(%s, %s)"

            data = (_name, _recordStatus)

            if createRecord(sql, data) > 0:
                resp = jsonify(message='FAQ category added successfully')
                resp.status_code = 200
                return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all FAQ category
@app.route('/faq/category')
def show_all_faq_category():
    try:
        sql = "SELECT * FROM tbl_faq_category"
        rows = readAllRecord(sql)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific FAQ category
@app.route('/faq/category/<int:faqCatId>')
def show_faq_category(faqCatId):
    try:
        sql = "SELECT * FROM tbl_faq_category WHERE faqCatId=%s"

        row = readOneRecord(sql, fqpCatId)

        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update FAQ category
@app.route('/faq/category/update/<int:faqCatId>', methods=['PUT'])
def update_faq_category(faqCatId):
    try:
        _json = request.json

        # return error if json body is empty
        if not _json:
            return bad_request()

        # return error if json parameter incomplete
        if 'name' and 'recordStatus' not in _json:
            return unprocessable_entity()

        _name = _json['name']
        _recordStatus = _json['recordStatus']

        # validate the received values
        if _name and _recordStatus and request.method == 'PUT':

            # save edits
            sql = "UPDATE tbl_faq_category SET name=%s, recordStatus=%s WHERE faqCatId=%s"

            data = (_name, _recordStatus, faqCatId)

            if updateRecord(sql, data) > 0:
                resp = jsonify(message='FAQ category updated successfully')
                resp.status_code = 200
                return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete FAQ category
@app.route('/faq/category/delete/<int:faqCatId>', methods=['DELETE'])
def delete_faq_category(faqCatId):
    try:
        sql = "DELETE FROM tbl_faq_category WHERE faqCatId=%s"

        if deleteRecord(sql, faqCatId) > 0:
            resp = jsonify(message='FAQ category deleted successfully')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
