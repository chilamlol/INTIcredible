from app import app
from flask import jsonify, request, render_template
from error_handler import *
from token_verifier import *
import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image/upload', methods=['POST'])
#@token_required
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return bad_request()

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return bad_request()

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/home/chilamlol/INTIcredible/static/', filename))

            resp = jsonify(message="Image uploaded")
            resp.status_code=201
            return resp

        return internal_server_error()