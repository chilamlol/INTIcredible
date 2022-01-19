from eventController import *
from alumniController import *
from login import *
from otpService import *

@app.route("/")
def home():
    return "You are connected"


if __name__ == '__main__':
    app.run(debug=True)
