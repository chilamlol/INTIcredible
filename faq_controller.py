from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *
import json
from token_verifier import *


# add FAQ
@app.route('/faq/add', methods=['POST'])
@is_admin
def add_faq():
    try:
        _json = request.json

        _question = _json['question']
        _answer = _json['answer']
        _recordStatus = _json['recordStatus']
        _faqCatId = _json['faqCatId']

        # save edits
        sql = "INSERT INTO tbl_faq(question, answer, recordStatus, faqCatId) VALUES(%s, %s, %s, %s)"

        data = (_question, _answer, _recordStatus, _faqCatId)

        if createRecord(sql, data) > 0:
            resp = jsonify('FAQ added successfully!')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all FAQ
@app.route('/faq')
@token_required
def show_all_faq():
    try:
        sql = "SELECT * FROM tbl_faq"
        rows = readAllRecord(sql)
        print(rows)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all FAQ nested
@app.route('/faq/nested')
@token_required
def show_all_faq_nested():
    try:

        # Requires MySQL 5.7 and above
        sql = " SELECT JSON_ARRAYAGG(JSON_OBJECT('faqCatId', tfc.faqCatId, 'name', tfc.name, 'recordStatus',tfc.recordStatus, 'faq', tf.faqList))" \
              " FROM " \
              " tbl_faq_category tfc" \
              " LEFT JOIN (" \
              " SELECT faqCatId," \
              " JSON_ARRAYAGG(JSON_OBJECT('faqId', faqId, 'question', question, 'answer', answer, 'recordStatus', recordStatus)) faqList " \
              " FROM tbl_faq" \
              " GROUP BY faqCatId" \
              " ) tf ON tf.faqCatId = tfc.faqCatId WHERE tf.faqList IS NOT NULL"

        """
        # Doesn't require MySQL version
        sql = ''' SELECT CONCAT('[', GROUP_CONCAT(CONCAT('{','"faqCatId":"', tfc.faqCatId, '", "name":"',tfc.name,'", "recordStatus":"', tfc.recordStatus, '", "faq":[', IFNULL((SELECT GROUP_CONCAT(CONCAT('{"faqId":"', tf.faqId, '", "question":"', tf.question, '", "answer":"', tf.answer,'"}') SEPARATOR ', ') FROM tbl_faq tf WHERE tf.faqCatId = tfc.faqCatId),''),']','}') SEPARATOR ', '), ']') FROM tbl_faq_category tfc'''
        """

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        # Convert list to string to remove unwanted characters
        res = str(row)[2:-3].replace("\\", "")

        # Convert back to JSON
        resp = jsonify(json.loads(res))
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific FAQ
@app.route('/faq/<int:faqId>')
@token_required
def show_faq(faqId):
    try:

        sql = "SELECT * FROM tbl_faq WHERE faqId=%s"

        row = readOneRecord(sql, faqId)

        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Update FAQ
@app.route('/faq/update/<int:faqId>', methods=['PUT'])
@is_admin
def update_faq(faqId):
    try:
        _json = request.json

        _question = _json['question']
        _answer = _json['answer']
        _recordStatus = _json['recordStatus']
        _faqCatId = _json['faqCatId']

        # save edited
        sql = "UPDATE tbl_faq SET question=%s, answer=%s, recordStatus=%s, faqCatId=%s WHERE faqId=%s"

        data = (_question, _answer, _recordStatus, _faqCatId, faqId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='FAQ updated successfully')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete FAQ
@app.route('/faq/delete/<int:faqId>', methods=['DELETE'])
@is_admin
def delete_faq(faqId):
    try:
        sql = "DELETE FROM tbl_faq WHERE faqId=%s"
        if deleteRecord(sql, faqId) > 0:
            resp = jsonify(message='FAQ deleted successfully')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
