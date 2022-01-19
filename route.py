from event_controller import *
from alumni_controller import *
from login import *
from otp_controller import *
from faq_controller import *
from faq_category_controller import *
from banner_controller import *


@app.route("/")
def home():
    return "You are connected"


if __name__ == '__main__':
    app.run(debug=True)
