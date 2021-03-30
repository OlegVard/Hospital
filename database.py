import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('Hospital.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS timetable(spec text primary key, \
            date text, time text)'''
        )
        self.conn.commit()

    def insert_data(self, spec, date, time):
        self.c.execute(
            '''INSERT INTO timetable(spec, date, time) VALUES (?, ?, ?)''', (spec, date, time)
        )
        self.conn.commit()


class BDAuth:
    def __init__(self):
        self.connect = sqlite3.connect('Users.db')
        self.c = self.connect.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS paslog(login text primary key,
            password text, isdoctor int ) '''
        )
        self.connect.commit()

    def check_pass(self, login, password):
    # добавить проверку на пустоту
        self.c.execute(
            '''SELECT * FROM paslog WHERE login = ?''', (login, ))
        user = self.c.fetchone()
        if password == user[1]:
            if user[2] == 1:
                return 'doc'
            else:
                return 'patient'
