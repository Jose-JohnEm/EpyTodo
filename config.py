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

# input_username = "Kino"
# input_pass = "passwd"

try:
# Write in table
    # with connection.cursor() as cursor:
    #     sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
    #     cursor.execute(sql, ('Kino', 'passwd'))
    # connection.commit()

# Read in table
    # with connection.cursor() as cursor:
    #     sql = "SELECT user_id FROM user WHERE username =%s and password =%s"
    #     cursor.execute(sql, (input_username, input_pass))
    #     result = cursor.fetchall()
    #     print(result)
    #     user_id = result
# Read task for user
    # with connection.cursor() as cursor:
    #     sql = "SELECT * FROM task INNER JOIN user_has_task WHERE user_has_task.fk_user_id = %s and task.task_id = user_has_task.fk_task_id"
    #     cursor.execute(sql, (user_id))
    #     result = cursor.fetchall()
    #     print(result)
# finally:
#     connection.close()
