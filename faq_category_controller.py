from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request


# add FAQ category
@app.route('/faq/category/add', methods=['POST'])
def add_faq_category():
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _recordStatus = _json['recordStation']
        # validate the received values
        if _name and _recordStatus and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_faq_category(name, recordStatus) VALUES(%s, %s)"
            data = (_name, _recordStatus)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('FAQ category added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


# list all FAQ category
@app.route('/faq/category')
def show_all_faq_category():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_faq_category")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


# list specific FAQ category
@app.route('/faq/category/<int:faqCatId>')
def show_faq_category(faqCatId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_faq_category WHERE faqCatId=%s", faqCatId)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Update FAQ category
@app.route('/faq/category/update/<int:faqCatId>', methods=['POST'])
def update_faq_category(faqCatId):
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _recordStatus = _json['recordStatus']
        # validate the received values
        if _name and _recordStatus and request.method == 'POST':
            # save edits
            sql = "UPDATE tbl_faq_category SET name=%s, recordStatus=%s WHERE faqCatId=%s"
            data = (_name, _recordStatus, faqCatId)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('FAQ category updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Delete FAQ category
@app.route('/faq/category/delete/<int:faqCatId>')
def delete_faq_category(faqCatId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_faq_category WHERE faqCatId=%s", faqCatId)
        conn.commit()
        resp = jsonify('FAQ category deleted successfully!')
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