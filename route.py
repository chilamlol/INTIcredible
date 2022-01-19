from event_controller import *
from alumni_controller import *
from login import *
from otp_controller import *


@app.route("/")
def home():
    return "You are connected"


if __name__ == '__main__':
    app.run(debug=True)
