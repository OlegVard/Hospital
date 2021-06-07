import tkinter as tk
from tkinter import ttk
from database import DB


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
        btn_help = tk.Button(toolbar,
                             text='Оказать прием',
                             command=lambda: self.open_help(self.tree.set(
                                 self.tree.selection()[0], '#2'), self.work_login),
                             compound=tk.TOP)
        btn_help.pack(side=tk.LEFT)
        tree_label = tk.Label(text='Посещения')
        tree_label.place(x=30, y=30)
        text_label = tk.Label(text='Заметки')
        text_label.place(x=1050, y=30)
        notes_text = tk.Text(width=50,
                             height=40,
                             font="Arial 12",
                             wrap=tk.WORD)
        notes_text.place(x=1050, y=50)
        self.tree = ttk.Treeview(columns=('ID', 'Login', 'Time', 'FIO'), heigh=35, show='headings')
        self.tree.column('ID', width=250, anchor=tk.CENTER)
        self.tree.column('Login', width=250, anchor=tk.CENTER)
        self.tree.column('Time', width=250, anchor=tk.CENTER)
        self.tree.column('FIO', width=250, anchor=tk.CENTER)
        self.tree.heading('ID', text='Номер посещения')
        self.tree.heading('Login', text='Логин')
        self.tree.heading('Time', text='Время')
        self.tree.heading('FIO', text='ФИО пациента')
        self.tree.place(x=30, y=50)

    def view_records(self, login):
        pat_list = self.db.get_doc_records(login)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in pat_list]

    def open_appointments(self):
        self.MakeAppointment()

    def open_help(self, pat_login, doc_login):
        self.Help(pat_login, doc_login)

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
            self.app_tree = ttk.Treeview(self, columns=('Time', 'Patient'), heigh=15, show='headings')
            self.app_tree.column('Time', width=200, anchor=tk.CENTER)
            self.app_tree.column('Patient', width=200, anchor=tk.CENTER)
            self.app_tree.heading('Time', text='Время')
            self.app_tree.heading('Patient', text='Пациент')
            self.app_tree.place(x=50, y=60)

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
            [self.app_tree.delete(i) for i in self.app_tree.get_children()]
            [self.app_tree.insert('', 'end', values=row) for row in rec_list]

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

    class Help(tk.Toplevel):
        def __init__(self, pat_login, doc_login):
            super().__init__(root)
            self.hospital_data = DB()
            self.init_help_window(pat_login, doc_login)

        def init_help_window(self, pat_login, doc_login):
            self.title('Запись на прием')
            self.geometry("1000x700+200+100")
            self.resizable(False, False)

            anamnesis_label = tk.Label(self, text='Анамнез')
            anamnesis_label.place(x=10, y=10)
            anamnesis_text = tk.Text(self,
                                     width=50,
                                     height=35,
                                     font="Arial 12",
                                     wrap=tk.WORD)
            anamnesis_text.place(x=10, y=30)
            diagnosis_label = tk.Label(self, text='Диагноз')
            diagnosis_label.place(x=510, y=10)
            diagnosis_text = tk.Text(self,
                                     width=50,
                                     height=15,
                                     font="Arial 12",
                                     wrap=tk.WORD)
            diagnosis_text.place(x=510, y=30)
            treatment_label = tk.Label(self, text='Лечение')
            treatment_label.place(x=510, y=310)
            treatment_text = tk.Text(self,
                                     width=50,
                                     height=15,
                                     font="Arial 12",
                                     wrap=tk.WORD)
            treatment_text.place(x=510, y=330)
            button_conf = tk.Button(self, text='Внести данные')
            button_conf.bind('<Button-1>', lambda event: self.insert_help_data(doc_login,
                                                                               pat_login,
                                                                               anamnesis_text.get(1.0, tk.END),
                                                                               diagnosis_text.get(1.0, tk.END),
                                                                               treatment_text.get(1.0, tk.END)))
            button_conf.place(x=510, y=650)

        def insert_help_data(self, doc_login, pat_login, anamnesis, diagnosis, treatment):
            response = self.hospital_data.insert_help_data(doc_login, pat_login, anamnesis, diagnosis, treatment)
            if response == 0:
                ok_label = tk.Label(self, text="Успешно")
                ok_label.pack(side=tk.BOTTOM)
                ok_label.after(2000, lambda: ok_label.pack_forget())


root = tk.Tk()
app = Doctor(root)
app.pack()
root.title("Hospital")
root.geometry("1000x600+300+200")
root.resizable(True, True)
root.mainloop()
