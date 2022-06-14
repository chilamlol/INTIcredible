from app import app
from flask_mail import Mail

mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'noreply.inticredibles@gmail.com'
app.config["MAIL_PASSWORD"] = 'inmkpmrtsbflgozh'
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_DEFAULT_SENDER'] = 'INTIcredibles'
app.config['DEBUG'] = True

mail = Mail(app)
