import pymysql as sql

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
FB_APP_ID = 1200420960103822
DATABASE_NAME = 'epytodo'
DATABASE_HOST = 'localhost'
DATABASE_SOCK = '/run/mysqld/mysqld.sock'
DATABASE_USER = 'root'
DATABASE_PASS = 'azerty'

connection = sql.connect(host = DATABASE_HOST,
                        unix_socket = DATABASE_SOCK,
                        user = DATABASE_USER,
                        passwd = DATABASE_PASS,
                        db = DATABASE_NAME
                    )

# try:
## Write in table
#     with connection.cursor() as cursor:
#         sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
#         cursor.execute(sql, ('Salameche', 'IamApokemon'))
#     connection.commit()
#
## Read in table
#     with connection.cursor() as cursor:
#         sql = "SELECT user_id, username FROM user"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
# finally:
#     connection.close()
