# INTIcredibles

This is the backend API for all the service in INTIcredible app and admin web portal. The API are built using Python with Flask frame work.

**Prerequisite**

* Python 3.7
* Flask
  * Flask-MySQL
  * Flask-Mail
* PyMySQL
* Hashlib
* MySQL 5.7 and above
* PyJWT

API key is using JWT hashed GUID.

<br />

## Run the system on local
**Install library**
```
pip install -r /path/to/requirements.txt
```
### Console
```
python route.py
```

## Run the system with Docker
* Default host = localhost
* Default port = 5000

<br />

**How to build Docker image?**
```
docker image build -t yourimagename
```

\
**How to run in Docker?**
```
docker run --restart=always -d -p 5000:5000 yourimagename
```
