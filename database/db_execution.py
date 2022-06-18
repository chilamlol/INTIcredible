import pymysql
from database.db_config import mysql


def readOneRecord(sql, parameter):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, parameter)
        return cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def readNestedRecord(sql):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def createRecord(sql, data):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rowCount = cursor.rowcount
        conn.commit()
        return rowCount
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def readAllRecord(sql, parameter=None):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, parameter)
        return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def updateRecord(sql, data):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rowCount = cursor.rowcount
        conn.commit()
        return rowCount
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def deleteRecord(sql, parameter):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, parameter)
        rowCount = cursor.rowcount
        conn.commit()
        return rowCount
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
