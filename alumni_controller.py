from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *
from token_verifier import *


# add alumni
@app.route('/alumni/add', methods=['POST'])
@is_admin
def add_alumni():
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

        # save edits
        sql = "INSERT INTO tbl_alumni(name, identificationCard, studentId, personalEmail, " \
              "studentHandphone, studentTelephoneNumber, graduatingCampus, yearOfGraduation, " \
              "graduatingProgramme, graduatedProgrammeName, levelOfStudy) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data = (_name, _identificationCard, _studentId, _personalEmail, _studentHandphone, _studentTelephoneNumber,
                _graduatingCampus, _yearOfGraduation, _graduatingProgramme, _graduatedProgrammeName, _levelOfStudy)

        if createRecord(sql, data) > 0:
            resp = jsonify(message='Alumni added successfully')
            resp.status_code = 201
            return resp

        # Return error if missing parameter
        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all alumni
@app.route('/alumni')
@token_required
def show_all_alumni():
    try:
        sql = "SELECT * FROM tbl_alumni"
        rows = readAllRecord(sql)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific alumni
@app.route('/alumni/<int:alumniId>')
@token_required
def show_alumni(alumniId):
    try:
        sql = "SELECT * FROM tbl_alumni WHERE alumniId=%s"

        row = readOneRecord(sql, alumniId)

        if not row:
            return not_found()

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update alumni
@app.route('/alumni/update/<int:alumniId>', methods=['PUT'])
@is_admin
def update_alumni(alumniId):
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

        # save edits
        sql = "UPDATE tbl_alumni SET name=%s, identificationCard=%s, studentId=%s, personalEmail=%s, " \
              "studentHandphone=%s, studentTelephoneNumber=%s, graduatingCampus=%s, yearOfGraduation=%s, " \
              "graduatingProgramme=%s, graduatedProgrammeName=%s, levelOfStudy=%s WHERE alumniId=%s"

        data = (_name, _identificationCard, _studentId, _personalEmail, _studentHandphone,
                _studentTelephoneNumber, _graduatingCampus, _yearOfGraduation,
                _graduatingProgramme, _graduatedProgrammeName, _levelOfStudy, alumniId)

        if updateRecord(sql, data) > 0:
            resp = jsonify(message='Alumni updated successfully!')
            resp.status_code = 200
            return resp

        # Return error if missing parameter
        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete Alumni
@app.route('/alumni/delete/<int:alumniId>', methods=['DELETE'])
@is_admin
def delete_alumni(alumniId):
    try:
        sql = "DELETE FROM tbl_alumni WHERE alumniId=%s"

        if deleteRecord(sql, alumniId) > 0:
            resp = jsonify(message='Alumni successfully deleted')
            resp.status_code = 200
            return resp

        return not_found()
    except Exception as e:
        print(e)
        return internal_server_error(e)
