from controller.event_controller import *
from controller.alumni_controller import *
from controller.login_controller import *
from controller.otp_controller import *
from controller.faq_controller import *
from controller.faq_category_controller import *
from controller.banner_controller import *
from controller.account_controller import *
from controller.image_controller import *
from controller.post_controller import *


@app.route("/")
def home():
    return "You are connected"


if __name__ == '__main__':
    app.run(debug=True)
