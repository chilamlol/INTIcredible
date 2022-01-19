from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request

# add events
@app.route('/event/add', methods=['POST'])
def add_event():
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _description = _json['description']
        _image = _json['image']
        _registerLink = _json['registerLink']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _status = _json['status']
        # validate the received values
        if _name and _description and _image and _registerLink and _startDate and _endDate and _status and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_event(name, description, image, registerLink, startDate, endDate, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            data = (_name, _description, _image, _registerLink, _startDate, _endDate, _status)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Event added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


# list all events
@app.route('/event')
def show_all_event():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_event")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/event/<int:id>')
def show_event(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_event WHERE eventId=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Update event
@app.route('/event/update/<int:id>', methods=['POST'])
def update_event(id):
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _description = _json['description']
        _image = _json['image']
        _registerLink = _json['registerLink']
        _startDate = _json['startDate']
        _endDate = _json['endDate']
        _status = _json['status']
        # validate the received values
        if _name and _description and _image and _registerLink and _startDate and _endDate and _status and request.method == 'POST':
            # save edits
            sql = "UPDATE tbl_event SET name=%s, description=%s, image=%s, registerLink=%s, startDate=%s, endDate=%s, status=%s WHERE eventId=%s"
            data = (_name, _description, _image, _registerLink, _startDate, _endDate, _status, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Event updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Delete Event
@app.route('/event/delete/<int:id>')
def delete_event(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_event WHERE eventId=%s", id)
        conn.commit()
        resp = jsonify('Event deleted successfully!')
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