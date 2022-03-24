from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'chilamlol'
app.config['MYSQL_DATABASE_PASSWORD'] = 'intidemo321'
app.config['MYSQL_DATABASE_DB'] = 'chilamlol$alumni'
app.config['MYSQL_DATABASE_HOST'] = 'chilamlol.mysql.pythonanywhere-services.com'

"""
#MySQL configurations for localhost
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'alumni'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
"""


mysql.init_app(app)
#intidemo321