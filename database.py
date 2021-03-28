import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('Hospital.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS timetable(CartNum integer primary key, date text, time text)'''
        )
        self.conn.commit()
