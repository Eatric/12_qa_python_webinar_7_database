import psycopg2

from settings import Settings


class Database:
    def __init__(self):
        try:
            self.database = psycopg2.connect(dbname=Settings.DB_NAME, user=Settings.DB_USER, password=Settings.DB_PASS,
                                             host=Settings.DB_HOST)
        except:
            print("Can`t connect to database")

    def get_user(self, user_email):
        users = None
        with self.database.cursor() as cursor:
            cursor.execute("SELECT * FROM \"user\" WHERE email=%s", (user_email,))
            users = cursor.fetchall()

        return users
