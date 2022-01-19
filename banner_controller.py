from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request


# add banner
@app.route('/banner/add', methods=['POST'])
def add_banner():
    conn = None
    cursor = None
    try:
        _json = request.json
        _bannerImage = _json['bannerImage']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _sequence = _json['sequence']
        _recordStatus = _json['recordStatus']
        # validate the received values
        if _bannerImage and _startDate and _endDate and _sequence and _recordStatus and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_banner(bannerImage, startDate, endDate, sequence, recordStatus) VALUES(%s, %s, %s, %s, %s)"
            data = (_bannerImage, _startDate, _endDate, _sequence, _recordStatus)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Banner added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


# list all banners
@app.route('/banner')
def show_all_banner():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_banner")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


# list specific banner
@app.route('/event/<int:bannerId>')
def show_banner(bannerId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_banner WHERE bannerId=%s", bannerId)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Update Banner
@app.route('/banner/update/<int:bannerId>', methods=['POST'])
def update_banner(bannerId):
    conn = None
    cursor = None
    try:
        _json = request.json
        _bannerImage = _json['bannerImage']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _sequence = _json['sequence']
        _recordStatus = _json['recordStatus']
        # validate the received values
        if _bannerImage and _startDate and _endDate and _sequence and _recordStatus and request.method == 'POST':
            # save edits
            sql = "UPDATE tbl_banner SET bannerImage=%s, startDate=%s, endDate=%s, sequence=%s, recordStatus=%s WHERE bannerId=%s"
            data = (_bannerImage, _startDate, _endDate, _sequence, _recordStatus, bannerId)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Banner updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Delete Banner
@app.route('/banner/delete/<int:bannerId>')
def delete_banner(bannerId):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_banner WHERE bannerId=%s", bannerId)
        conn.commit()
        resp = jsonify('Banner deleted successfully!')
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
