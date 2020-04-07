import pymysql as sql

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
FB_APP_ID = 1200420960103822
DATABASE_NAME = 'epytodo'
DATABASE_HOST = 'localhost'
DATABASE_SOCK = '/run/mysqld/mysqld.sock'
DATABASE_USER = 'root'
DATABASE_PASS = 'azerty'

connect = sql.connect(host = DATABASE_HOST,
                        unix_socket = DATABASE_SOCK,
                        user = DATABASE_USER,
                        passwd = DATABASE_PASS,
                        db = DATABASE_NAME
                        )