from app import app
from flask_mail import Mail

mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'j18027823@student.newinti.edu.my'
app.config["MAIL_PASSWORD"] = 'gbvzzbplrowmawmv'
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_DEFAULT_SENDER'] = 'Luke Skywalker'
app.config['DEBUG'] = True

mail = Mail(app)
