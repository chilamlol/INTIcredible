from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *
from datetime import datetime
import json


def convertStringToDateTime(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


# add events
@app.route('/event/add', methods=['POST'])
def add_event():
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
        if _name and _description and _image and _registerLink \
                and _startDate and _endDate and _status and request.method == 'POST':

            # save edits
            sql = "INSERT INTO tbl_event(name, description, image, registerLink, startDate, endDate, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"

            # Convert string to Date time
            startDate = str(convertStringToDateTime(_startDate))
            endDate = str(convertStringToDateTime(_endDate))

            data = (_name, _description, _image, _registerLink, startDate, endDate, _status)

            if createRecord(sql, data) > 0:
                resp = jsonify(message='Event added successfully!')
                resp.status_code = 201
                return resp

        return bad_request()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# list all events
@app.route('/event')
def show_all_event():
    try:
        sql = "SELECT * FROM tbl_event"
        rows = readAllRecord(sql)

        result = []

        for row in rows:
            row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
            row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")
            result.append(row)

        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# list specific event
@app.route('/event/<int:eventId>')
def show_event(eventId):
    try:
        sql = "SELECT * FROM tbl_event WHERE eventId=%s"

        row = readOneRecord(sql, eventId)

        if not row:
            return not_found()

        # Convert date time format for output
        row['startDate'] = row['startDate'].strftime("%Y-%m-%d %H:%M:%S")  # 2022-03-25 17:14:20
        row['endDate'] = row['endDate'].strftime("%Y-%m-%d %H:%M:%S")

        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return internal_server_error(e)


# Update event
@app.route('/event/update/<int:eventId>', methods=['PUT'])
def update_event(eventId):
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
        if _name and _description and _image and _registerLink \
                and _startDate and _endDate and _status and request.method == 'PUT':

            # save edits
            sql = "UPDATE tbl_event SET name=%s, description=%s, image=%s, registerLink=%s, startDate=%s, endDate=%s, status=%s WHERE eventId=%s"

            data = (_name, _description, _image, _registerLink, _startDate, _endDate, _status, eventId)

            if updateRecord(sql, data) > 0:
                resp = jsonify(message='Event updated successfully')
                resp.status_code = 200
                return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)


# Delete Event
@app.route('/event/delete/<int:eventId>', methods=['DELETE'])
def delete_event(eventId):
    try:
        sql = "DELETE FROM tbl_event WHERE eventId=%s"

        if deleteRecord(sql, eventId) > 0:
            resp = jsonify(message='Event deleted successfully')
            resp.status_code = 200
            return resp

        return not_found
    except Exception as e:
        print(e)
        return internal_server_error(e)
