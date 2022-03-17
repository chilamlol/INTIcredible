from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request


# add FAQ
@app.route('/faq/add', methods=['POST'])
def add_faq():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question = _json['question']
        _answer = _json['answer']
        _recordStatus = _json['recordStatus']
        _faqCatId = _json['faqCatId']
        # validate the received values
        if _question and _answer and _recordStatus and _faqCatId and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_faq(question, answer, recordStatus, faqCatId) VALUES(%s, %s, %s, %s)"
            data = (_question, _answer, _recordStatus, _faqCatId)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('FAQ added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


# list all FAQ
@app.route('/faq')
def show_all_faq():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_faq")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


# list specific FAQ
@app.route('/faq/<int:faqId>')
def show_faq(faqId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_faq WHERE faqId=%s", faqId)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Update FAQ
@app.route('/faq/update/<int:faqId>', methods=['POST'])
def update_faq(faqId):
    conn = None
    cursor = None
    try:
        _json = request.json
        _question = _json['question']
        _answer = _json['answer']
        _recordStatus = _json['recordStatus']
        _faqCatId = _json['faqCatId']
        # validate the received values
        if _question and _answer and _recordStatus and _faqCatId and request.method == 'POST':
            # save edited
            sql = "UPDATE tbl_faq SET question=%s, answer=%s, recordStatus=%s, faqCatId=%s WHERE faqId=%s"
            data = (_question, _answer, _recordStatus, _faqCatId, faqId)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('FAQ updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Delete FAQ
@app.route('/faq/delete/<int:faqId>')
def delete_faq(faqId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_faq WHERE faqId=%s", faqId)
        conn.commit()
        resp = jsonify('FAQ deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
