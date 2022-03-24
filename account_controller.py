from app import app
from flask import jsonify, request
from db_execution import *
from error_handler import *


@app.route("/activate/<int:userId>", methods=['PUT'])
def activateUserAccount(userId):
    try:
        sql = "UPDATE tbl_user set activationStatus=30 where userId=%s"

        if updateRecord(sql, userId) > 0:
            resp = jsonify(message='User account successfully activated')
            resp.status_code = 200
            return resp

        return not_found()

    except Exception as e:
        print(e)
        return internal_server_error(e)
