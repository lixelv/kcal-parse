import mysql.connector

class DB:
    def __init__(self, db_config):
        self.connect = mysql.connector.connect(**db_config)
        self.cursor = self.connect.cursor()

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql.replace('?', '%s'), values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql.replace('?', '%s'), values)
        return self.cursor.fetchall()

    def find_data(self, resp) -> tuple:
        return self.read("SELECT id, name FROM product WHERE LOWER(name) LIKE '%' || %s || '%'", (resp.lower(),))

    def __del__(self):
        self.cursor.close()
        self.connect.close()
