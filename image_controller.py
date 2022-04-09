from app import app
from flask import jsonify, request
from error_handler import *
from token_verifier import *


@app.route('/image/<string:imagePath>')
#@token_required
def getImageWithFilePath(imagePath):
    return render_template("image.html", image=imagePath)
