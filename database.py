import psycopg2

from config import setting

DB_NAME = setting.get_param('DB_NAME')
DB_USER = setting.get_param('DB_USER')
DB_PASW = setting.get_param('DB_PASW')
DB_HOST = setting.get_param('DB_HOST')
DB_PORT = setting.get_param('DB_PORT')
#DB_CONN = setting('connections')


def connection ():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASW, host=DB_HOST,port=DB_PORT)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return conn

def selectdate (proceedure , inputedData ):
    try:
        cursor = connection().cursor()
        #cursor.execute("select %s('%s');" % (proceedure,inputedData))
        cursor.callproc(proceedure,inputedData)
        return cursor.fetchone()
    except Exception as e:
        print("DataBase [Error]: ",e )
        return 1,e

