import sqlite3
from datetime import datetime


class DB:  # база данных больницы
    def __init__(self):
        self.conn = sqlite3.connect('Hospital.db')
        self.c = self.conn.cursor()

    def get_doc_records(self, login):
        date = datetime.date(datetime.today())
        s_date = str(date.day) + '.' + str(date.month) + '.' + str(date.year)[-2:]
        self.c.execute(
            '''SELECT ID, Patient, Time, FIO 
                        FROM records INNER JOIN patients
                        ON records.Patient = patients.Patient_login
                        WHERE Doctor=? AND Date =?''', (login, s_date)
        )
        pat_list = self.c.fetchall()
        return pat_list

    def get_past_records(self, login):
        self.c.execute(
            '''SELECT id_app, Date, diagnosis, FIO 
             FROM appointments INNER JOIN doctors
             ON appointments.Doctor = doctors.Doc_login
             WHERE Patient=?''', (login,)
        )
        app_list = self.c.fetchall()
        return app_list

    def get_fut_records(self, login):
        self.c.execute(
            '''SELECT ID, Date, Time, FIO, room 
             FROM records INNER JOIN doctors
             ON records.Doctor = doctors.Doc_login
             WHERE Patient=?''', (login,)
        )
        app_list = self.c.fetchall()
        return app_list

    def get_treatment(self, app_id):
        self.c.execute(
            '''SELECT treatment 
            FROM appointments
            WHERE id_app = ?''', (app_id,)
        )
        treatment = self.c.fetchone()
        return treatment

    def get_appointments(self, date, doc):
        self.c.execute(
            '''SELECT Time, Patient
            FROM records 
            WHERE Date=? AND Doctor=?''',
            (date, doc)
        )
        appointments = self.c.fetchall()
        return appointments

    def add_appointment(self, doc, pat, time, date):
        try:
            self.c.execute(
                '''INSERT INTO records(Doctor, Patient, Time, Date) 
                VALUES (?, ?, ?, ?)''',
                (doc, pat, time, date)
            )
            self.conn.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1

    def del_appointment(self, number):
        self.c.execute(
            '''DELETE FROM records WHERE ID=?''', (number,)
        )
        self.conn.commit()

    def get_appointments_num(self, date, doc):
        self.c.execute(
            '''SELECT ID, Time, Patient
            FROM records 
            WHERE Date=? AND Doctor=?''',
            (date, doc)
        )
        appointments = self.c.fetchall()
        return appointments

    def reg_patient(self, login, fio, passport, oms):
        try:
            self.c.execute(
                '''INSERT INTO patients(Patient_login, FIO, Passport, OMS)
                VALUES (?, ?, ?, ?)''', (login, fio, passport, oms)
            )
            self.conn.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1

    def reg_doc(self, login, spec, room, fio):
        try:
            self.c.execute(
                '''INSERT INTO doctors(Doc_login, Specialization, Room, FIO)
                VALUES (?, ?, ?, ?)''', (login, spec, room, fio)
            )
            self.conn.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1

    def get_patients(self):
        self.c.execute(
            '''SELECT Patient_login, FIO 
            FROM patients'''
        )
        return self.c.fetchall()

    def get_doctors(self):
        self.c.execute(
            '''SELECT Doc_login, Specialization, FIO, room
            FROM doctors'''
        )
        return self.c.fetchall()

    def get_patient_data(self, login):
        self.c.execute(
            '''SELECT Passport, OMS 
            FROM patients 
            WHERE Patient_login=?''',
            (login, )
        )
        return self.c.fetchone()

    def insert_help_data(self, doc_login, pat_login, anamnesis, diagnosis, treatment):
        date = datetime.date(datetime.today())
        s_date = str(date.day) + '.' + str(date.month) + '.' + str(date.year)[-2:]
        try:
            self.c.execute(
                '''INSERT INTO appointments(Doctor, Patient, Date, anamnesis, diagnosis, treatment) 
                VALUES (?, ?, ?, ?, ?, ?)''',
                (doc_login, pat_login, s_date, anamnesis, diagnosis, treatment)
            )
            self.conn.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1


class BDAuth:   # база данных авторизации
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
                '''INSERT INTO paslog(login, password, isdoctor) 
                VALUES (?, ?, ?)''', (login, password, spec)
            )
            self.connect.commit()
            return 0
        except sqlite3.IntegrityError:
            return -1

    def change_password(self, login, old_password, new_password):
        try:
            self.c.execute(
                '''SELECT Login, Password  FROM paslog WHERE login = ?''', (login,)
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
