# добавить: запиь на прием
# кнопка собрать анамнез и сохранить его
# кнопка выписать рецепт
# сделать сортировку по дате для записи

import tkinter as tk
from tkinter import ttk
from database import DB
from datetime import datetime


class Doctor(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_doc_window()
        self.db = DB()
        f = open("log.txt", 'r')
        self.work_login = f.readline()
        f.close()
        f = open("log.txt", 'w')
        f.write('')
        f.close()
        self.work_login = 'doc1'  # Онли для проверки
        self.date = time_table
        self.week_day = week_day
        self.view_records(self.work_login)

    def init_doc_window(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_open_appointments = tk.Button(toolbar,
                                          text='Записать на прием',
                                          command=lambda: self.open_appointments(),
                                          compound=tk.TOP)
        btn_open_appointments.pack(side=tk.LEFT)
        btn_refresh = tk.Button(toolbar,
                                text='Обновить записи',
                                command=lambda: self.view_records(self.work_login),
                                compound=tk.TOP)
        btn_refresh.pack(side=tk.RIGHT)
        self.tree = ttk.Treeview(columns=('ID', 'Login', 'Time', 'FIO'), heigh=15, show='headings')
        self.tree.column('ID', width=300, anchor=tk.CENTER)
        self.tree.column('Login', width=350, anchor=tk.CENTER)
        self.tree.column('Time', width=200, anchor=tk.CENTER)
        self.tree.column('FIO', width=200, anchor=tk.CENTER)
        self.tree.heading('ID', text='Номер посещения')
        self.tree.heading('Login', text='Логин')
        self.tree.heading('Time', text='Время')
        self.tree.heading('FIO', text='ФИО пациента')
        self.tree.place(x=0, y=30)

    def view_records(self, login):
        pat_list = self.db.get_doc_records(login)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in pat_list]

    def open_appointments(self):
        self.MakeAppointment()

    class MakeAppointment(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_appoint_window()
            self.db = DB()

        def init_appoint_window(self):
            self.title('Запись на прием')
            self.geometry("800x450+200+100")
            self.resizable(False, False)

            date_label = tk.Label(self, text='Дата')
            date_label.place(x=150, y=10)
            date = tk.Entry(self)
            date.place(x=200, y=10)
            doc_label = tk.Label(self, text='Логин доктора')
            doc_label.place(x=100, y=30)
            doc = tk.Entry(self)
            doc.place(x=200, y=30)
            btn_sort = tk.Button(self, text='Вывести записи')
            btn_sort.bind('<Button-1>', lambda event: self.view_appointments(date.get(),
                                                                             doc.get()))
            btn_sort.place(x=400, y=10)
            self.tree = ttk.Treeview(self, columns=('Time', 'Patient'), heigh=15, show='headings')
            self.tree.column('Time', width=200, anchor=tk.CENTER)
            self.tree.column('Patient', width=200, anchor=tk.CENTER)
            self.tree.heading('Time', text='Время')
            self.tree.heading('Patient', text='Пациент')
            self.tree.place(x=50, y=60)

            time_label = tk.Label(self, text='Время')
            pat_label = tk.Label(self, text='Логин пациента')
            time_label.place(x=510, y=50)
            pat_label.place(x=510, y=80)
            btn_add_appoint = tk.Button(self, text='Записать')
            btn_add_appoint.place(x=510, y=105)
            time_entry = tk.Entry(self)
            pat_entry = tk.Entry(self)
            time_entry.place(x=610, y=50)
            pat_entry.place(x=610, y=80)
            btn_add_appoint.bind('<Button-1>', lambda event: self.add_appoint(doc.get(),
                                                                              pat_entry.get(),
                                                                              time_entry.get(),
                                                                              date.get()))

            self.grab_set()
            self.focus_get()

        def view_appointments(self, date, doc):
            rec_list = self.db.get_appointments(date, doc)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in rec_list]

        def add_appoint(self, doc, pat, time, date):
            response = self.db.add_appointment(doc, pat, time, date)
            if response == 0:
                r_label = tk.Label(self, text='Успешно')
                r_label.pack(side=tk.BOTTOM)
                r_label.after(2000, lambda: r_label.pack_forget())
            else:
                r_label = tk.Label(self, text='Ошибка')
                r_label.pack(side=tk.BOTTOM)
                r_label.after(2000, lambda: r_label.pack_forget())


root = tk.Tk()
time_table = datetime.today()
week_day = time_table.weekday()
app = Doctor(root)
app.pack()
root.title("Hospital")
root.geometry("1000x600+300+200")
root.resizable(True, True)
root.mainloop()
