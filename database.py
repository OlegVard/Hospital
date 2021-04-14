import sqlite3


class DB:  # база данных больницы
    def __init__(self):
        self.conn = sqlite3.connect('Hospital.db')
        self.c = self.conn.cursor()

    def get_records(self, login):
        self.c.execute(
            '''SELECT ID, Patient, Time, FIO 
                        FROM records INNER JOIN patients
                        ON records.Patient = patients.Patient_login
                        WHERE Doctor=?''',
            (login,)
        )
        pat_list = self.c.fetchall()
        return pat_list

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
        try:
            self.c.execute(
                '''SELECT * FROM paslog WHERE login = ?''', (login,))
            user = self.c.fetchone()
            if password == user[1]:
                if user[2] == "Д":
                    return 'doc'
                elif user[2] == "П":
                    return 'patient'
                else:
                    return "manager"
            else:
                return 0
        except TypeError:
            return 0

    def register(self, login, password, spec):
        try:
            self.c.execute(
                '''INSERT INTO paslog(login, password, isdoctor) VALUES (?, ?, ?)''', (login, password, spec)
            )
            self.connect.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1

    def change_password(self, login, old_password, new_password):
        try:
            self.c.execute(
                '''SELECT * FROM paslog WHERE login = ?''', (login,)
            )
            user = self.c.fetchone()
            if user[1] == old_password:
                self.c.execute(
                    '''UPDATE paslog SET password=? WHERE login=?''',
                    (new_password, login)
                )
            self.connect.commit()
            return 0
        except TypeError:
            return -1

    def del_user(self, login, password):
        try:
            self.c.execute(
                '''SELECT * FROM paslog WHERE login=?''', (login,)
            )
            user = self.c.fetchone()
            if user[1] == password:
                self.c.execute(
                    '''DELETE FROM paslog WHERE login=?''', (login,)
                )
                self.connect.commit()
                return 0
            else:
                return -1
        except TypeError:
            return -1
