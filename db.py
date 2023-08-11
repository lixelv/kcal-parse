import sqlite3

class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def add_second_name(self, values: list | tuple | set) -> None:
        self.do('INSERT INTO second_name (name, url, first_name_id) VALUES (?, ?, ?)', tuple(values))

    def add_data(self, values: list | tuple | set) -> None:
        self.do(f'INSERT INTO data (product, kcal, protein, fat, carbonates, url, second_name_id) VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(values))
