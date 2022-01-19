from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import request


# add events
@app.route('/alumni/add', methods=['POST'])
def add_alumni():
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _identificationCard = _json['identificationCard']
        _studentId = _json['studentId']
        _personalEmail = _json['personalEmail']
        _studentHandphone = _json['studentHandphone']
        _studentTelephoneNumber = _json['studentTelephoneNumber']
        _graduatingCampus = _json['graduatingCampus']
        _yearOfGraduation = _json['yearOfGraduation']
        _graduatingProgramme = _json['graduatingProgramme']
        _graduatedProgrammeName = _json['graduatedProgrammeName']
        _levelOfStudy = _json['levelOfStudy']
        # validate the received values
        if _name and _identificationCard and _studentId and _personalEmail and _graduatingCampus and _yearOfGraduation and _graduatingProgramme and _graduatedProgrammeName and _levelOfStudy and request.method == 'POST':
            # save edits
            sql = "INSERT INTO tbl_alumni(name, identificationCard, studentId, personalEmail, studentHandphone, studentTelephoneNumber, graduatingCampus, yearOfGraduation, graduatingProgramme, graduatedProgrammeName, levelOfStudy) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_name, _identificationCard, _studentId, _personalEmail, _studentHandphone, _studentTelephoneNumber, _graduatingCampus, _yearOfGraduation, _graduatingProgramme, _graduatedProgrammeName, _levelOfStudy)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Alumni added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


# list all alumni
@app.route('/alumni')
def show_all_alumni():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_alumni")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/alumni/<int:id>')
def show_alumni(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_alumni WHERE alumniId=%s", id)
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
@app.route('/alumni/update/<int:id>', methods=['POST'])
def update_alumni(id):
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _identificationCard = _json['identificationCard']
        _studentId = _json['studentId']
        _personalEmail = _json['personalEmail']
        _studentHandphone = _json['studentHandphone']
        _studentTelephoneNumber = _json['studentTelephoneNumber']
        _graduatingCampus = _json['graduatingCampus']
        _yearOfGraduation = _json['yearOfGraduation']
        _graduatingProgramme = _json['graduatingProgramme']
        _graduatedProgrammeName = _json['graduatedProgrammeName']
        _levelOfStudy = _json['levelOfStudy']
        # validate the received values
        if _name and _identificationCard and _studentId and _personalEmail and _graduatingCampus and _yearOfGraduation and _graduatingProgramme and _graduatedProgrammeName and _levelOfStudy and request.method == 'POST':
            # save edits
            sql = "UPDATE tbl_alumni SET name=%s, identificationCard=%s, studentId=%s, personalEmail=%s, studentHandphone=%s, studentTelephoneNumber=%s, graduatingCampus=%s, yearOfGraduation=%s, graduatingProgramme=%s, graduatedProgrammeName=%s, levelOfStudy=%s WHERE alumniId=%s"
            data = (_name, _identificationCard, _studentId, _personalEmail, _studentHandphone, _studentTelephoneNumber, _graduatingCampus, _yearOfGraduation, _graduatingProgramme, _graduatedProgrammeName, _levelOfStudy,id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify(message='Alumni updated successfully!',status='200')
            resp.status_code = 200
            return resp
        else:
            return not_found()
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