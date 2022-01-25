from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = '\x12\xc9\xf7<?s5\xed\x17\xd4M\xa8\xdc3\x01\xe8\xfa\x8e\x10]\x07YA\x8b'

CORS(app)