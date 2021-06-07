from datetime import datetime
import tkinter as tk
from tkinter import ttk
from database import BDAuth, DB


class Manager(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.initManager()
        self.dataAuth = dbAuth
        self.Hospital_data = Hospital_DB
        self.get_trees_view()

    def initManager(self):
        manager_tool_bar = tk.Frame(bg='#d7d8e0', bd=2)
        manager_tool_bar.pack(side=tk.TOP, fill=tk.X)
        btn_register_pat = tk.Button(manager_tool_bar,
                                     text='Зарегистрировать пацитента',
                                     command=lambda: self.open_pat_register_window(),
                                     compound=tk.TOP)
        btn_register_pat.pack(side=tk.LEFT)
        btn_register_doc = tk.Button(manager_tool_bar,
                                     text='Зарегистрировать врача',
                                     command=lambda: self.open_doc_register_window(),
                                     compound=tk.TOP)
        btn_register_doc.pack(side=tk.LEFT)
        btn_change_password = tk.Button(manager_tool_bar,
                                        text='Сменить пароль',
                                        command=lambda: self.open_change_password_window(),
                                        compound=tk.TOP)
        btn_change_password.pack(side=tk.LEFT)
        btn_del = tk.Button(manager_tool_bar,
                            text='Удалить пользователя',
                            command=lambda: self.open_del_window(),
                            compound=tk.TOP)
        btn_del.pack(side=tk.LEFT)
        btn_make_app = tk.Button(manager_tool_bar,
                                 text='Запись на прием',
                                 command=lambda: self.open_appointment_window(),
                                 compound=tk.TOP)
        btn_make_app.pack(side=tk.LEFT)
        btn_del_app = tk.Button(manager_tool_bar,
                                text='Удалить запись на прием',
                                command=lambda: self.open_delete_appointment_window(),
                                compound=tk.TOP)
        btn_del_app.pack(side=tk.LEFT)
        btn_get_pat_data = tk.Button(text='Показать данные пациента',
                                     command=lambda: self.get_patient_data(
                                         self.pat_tree.set(self.pat_tree.selection()[0], '#1')),
                                     compound=tk.TOP)
        btn_get_pat_data.place(x=10, y=30)
        btn_refresh = tk.Button(manager_tool_bar,
                                text='Обновить данные',
                                command=lambda: self.get_trees_view(),
                                compound=tk.TOP)
        btn_refresh.pack(side=tk.RIGHT)

        self.pat_tree = ttk.Treeview(columns=('Login', 'Name'), heigh=35, show='headings')
        self.pat_tree.column('Login', width=200, anchor=tk.CENTER)
        self.pat_tree.column('Name', width=200, anchor=tk.CENTER)
        self.pat_tree.heading('Login', text='Логин пациента')
        self.pat_tree.heading('Name', text='Имя пациента')
        self.pat_tree.place(x=10, y=70)

        self.doc_tree = ttk.Treeview(columns=('Login', 'Name', 'Spec', 'Room'), heigh=35, show='headings')
        self.doc_tree.column('Login', width=150, anchor=tk.CENTER)
        self.doc_tree.column('Name', width=150, anchor=tk.CENTER)
        self.doc_tree.column('Spec', width=150, anchor=tk.CENTER)
        self.doc_tree.column('Room', width=150, anchor=tk.CENTER)
        self.doc_tree.heading('Login', text='Логин врача')
        self.doc_tree.heading('Name', text='Имя врача')
        self.doc_tree.heading('Spec', text='Специальность')
        self.doc_tree.heading('Room', text='Кабинет')
        self.doc_tree.place(x=450, y=70)

        self.text = tk.Text(width=48,
                            height=40,
                            font="Arial 12",
                            wrap=tk.WORD)
        self.text.place(x=1090, y=70)

    def get_trees_view(self):
        rec_list = self.Hospital_data.get_patients()
        [self.pat_tree.delete(i) for i in self.pat_tree.get_children()]
        [self.pat_tree.insert('', 'end', values=row) for row in rec_list]
        rec_list = self.Hospital_data.get_doctors()
        [self.doc_tree.delete(i) for i in self.doc_tree.get_children()]
        [self.doc_tree.insert('', 'end', values=row) for row in rec_list]

    def get_patient_data(self, login):
        pat_data = self.Hospital_data.get_patient_data(login)
        pat_str = 'Паспорт:' + str(pat_data[0]) + ' Полис:' + str(pat_data[1])
        self.text.delete(1.0, tk.END)
        self.text.insert(1.0, pat_str)

    def open_appointment_window(self):
        self.MakeAppointment()

    def open_doc_register_window(self):
        self.DocRegisterWindow()

    def open_pat_register_window(self):
        self.PatientRegisterWindow()

    def open_change_password_window(self):
        self.ChangePasswordWindow()

    def open_del_window(self):
        self.DelWindow()

    def open_delete_appointment_window(self):
        self.DeleteAppointment()

    class PatientRegisterWindow(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_register_window()
            self.dataAuth = dbAuth
            self.hospital_data = Hospital_DB

        def init_register_window(self):
            self.title('Регистрация пациента')
            self.geometry("500x300+400+300")
            self.resizable(False, False)

            self.label_log = tk.Label(self, text='Логин')
            self.label_log.place(x=100, y=50)
            self.label_pass = tk.Label(self, text='Пароль')
            self.label_pass.place(x=100, y=75)
            self.label_fio = tk.Label(self, text='ФИО')
            self.label_fio.place(x=100, y=100)
            self.label_passport = tk.Label(self, text='Паспорт')
            self.label_passport.place(x=100, y=125)
            self.label_oms = tk.Label(self, text='Номер ОМС')
            self.label_oms.place(x=100, y=150)

            self.entry_log = ttk.Entry(self)
            self.entry_log.place(x=300, y=50)
            self.entry_pass = ttk.Entry(self)
            self.entry_pass.place(x=300, y=75)
            self.entry_fio = ttk.Entry(self)
            self.entry_fio.place(x=300, y=100)
            self.entry_passport = ttk.Entry(self)
            self.entry_passport.place(x=300, y=125)
            self.entry_oms = ttk.Entry(self)
            self.entry_oms.place(x=300, y=150)

            self.btn_reg = tk.Button(self, text='Зарегистрировать')
            self.btn_reg.place(x=100, y=200)
            self.btn_reg.bind('<Button-1>', lambda event: self.register_patient(self.entry_log.get(),
                                                                                self.entry_pass.get(),
                                                                                self.entry_fio.get(),
                                                                                self.entry_passport.get(),
                                                                                self.entry_oms.get()))
            self.bind("<Return>", lambda event: self.register_patient(self.entry_log.get(), self.entry_pass.get(),
                                                                      self.entry_fio.get(), self.entry_passport.get(),
                                                                      self.entry_oms.get()))
            btn_canc = tk.Button(self, text='Закрыть',
                                 command=lambda: self.destroy())
            self.bind("<Escape>", lambda event: self.destroy())
            btn_canc.place(x=300, y=200)

            self.grab_set()
            self.focus_get()

        def register_patient(self, login, password, fio, passport, oms):
            response = self.dataAuth.register(login, password, 'П') + \
                       self.hospital_data.reg_patient(login, fio, passport, oms)
            if response == 0:
                ok_label = tk.Label(self, text="Успешно")
                ok_label.pack(side=tk.BOTTOM)
                ok_label.after(2000, lambda: ok_label.pack_forget())
            else:
                error_label = tk.Label(self, text="Пользователь с таким логином уже есть")
                error_label.pack(side=tk.BOTTOM)
                error_label.after(2000, lambda: error_label.pack_forget())

    class DocRegisterWindow(PatientRegisterWindow):
        def __init__(self):
            super().__init__()
            self.init_doc_register_window()

        def init_doc_register_window(self):
            self.title('Регистрация врача')

            self.label_spec = tk.Label(self, text='Специализация')
            self.label_room = tk.Label(self, text='Кабинет')
            self.label_spec.place(x=100, y=125)
            self.label_room.place(x=100, y=150)
            self.entry_spec = tk.Entry(self)
            self.entry_room = tk.Entry(self)
            self.entry_spec.place(x=300, y=125)
            self.entry_room.place(x=300, y=150)

            self.btn_doc_reg = tk.Button(self, text='Зарагистрировать')
            self.btn_doc_reg.place(x=100, y=200)
            self.btn_doc_reg.bind('<Button-1>', lambda event: self.register_doc(self.entry_log.get(),
                                                                                self.entry_pass.get(),
                                                                                self.entry_spec.get(),
                                                                                self.entry_room.get(),
                                                                                self.entry_fio.get()))
            self.bind("<Return>", lambda event: self.register_doc(self.entry_log.get(),
                                                                  self.entry_pass.get(),
                                                                  self.entry_spec.get(),
                                                                  self.entry_room.get(),
                                                                  self.entry_fio.get()))

            self.entry_passport.destroy()
            self.label_oms.destroy()
            self.label_passport.destroy()
            self.entry_oms.destroy()
            self.btn_reg.destroy()

        def register_doc(self, login, password, spec, room, fio):
            response = self.dataAuth.register(login, password, 'Д') + \
                       self.hospital_data.reg_doc(login, spec, room, fio)
            if response == 0:
                ok_label = tk.Label(self, text="Успешно")
                ok_label.pack(side=tk.BOTTOM)
                ok_label.after(2000, lambda: ok_label.pack_forget())
            else:
                error_label = tk.Label(self, text="Пользователь с таким логином уже есть")
                error_label.pack(side=tk.BOTTOM)
                error_label.after(2000, lambda: error_label.pack_forget())

    class ChangePasswordWindow(PatientRegisterWindow):
        def __init__(self):
            super().__init__()
            self.init_change_password_window()

        def init_change_password_window(self):
            self.title('Смена пароля')

            label_spec = tk.Label(self, text='Новый пароль')
            label_spec.place(x=100, y=100)

            entry_new_pass = ttk.Entry(self)
            entry_new_pass.place(x=300, y=100)

            btn_upd = tk.Button(self, text='Сменить пароль')
            btn_upd.place(x=100, y=200)
            btn_upd.bind('<Button-1>', lambda event: self.change_password(self.entry_log.get(),
                                                                          self.entry_pass.get(),
                                                                          entry_new_pass.get()))
            self.bind("<Return>", lambda event: self.change_password(self.entry_log.get(),
                                                                     self.entry_pass.get(),
                                                                     entry_new_pass.get()))
            self.entry_passport.destroy()
            self.label_oms.destroy()
            self.label_passport.destroy()
            self.label_fio.destroy()
            self.entry_oms.destroy()
            self.entry_fio.destroy()
            self.btn_reg.destroy()

        def change_password(self, login, old_password, new_password):
            response = self.dataAuth.change_password(login, old_password, new_password)
            if response == 0:
                ok_label = tk.Label(self, text="Успешно")
                ok_label.pack(side=tk.BOTTOM)
                ok_label.after(2000, lambda: ok_label.pack_forget())
            else:
                error_label = tk.Label(self, text="Неверно введен логин, старый пароль или новый пароль")
                error_label.pack(side=tk.BOTTOM)
                error_label.after(2000, lambda: error_label.pack_forget())

    class DelWindow(PatientRegisterWindow):
        def __init__(self):
            super().__init__()
            self.init_del_window()

        def init_del_window(self):
            self.title('Удаление пользователя')
            btn_del = tk.Button(self, text='Удалить')
            btn_del.place(x=120, y=200)
            btn_del.bind("<Button-1>", lambda event: self.del_user(self.entry_log.get(),
                                                                   self.entry_pass.get()))
            self.bind("<Return>", lambda event: self.del_user(self.entry_log.get(),
                                                              self.entry_pass.get()))
            self.entry_passport.destroy()
            self.label_oms.destroy()
            self.label_passport.destroy()
            self.label_fio.destroy()
            self.entry_oms.destroy()
            self.entry_fio.destroy()
            self.btn_reg.destroy()

        def del_user(self, login, password):
            response = self.dataAuth.del_user(login, password)
            if response == 0:
                ok_label = tk.Label(self, text="Успешно")
                ok_label.pack(side=tk.BOTTOM)
                ok_label.after(2000, lambda: ok_label.pack_forget())
            else:
                error_label = tk.Label(self, text="Неверно введен логин или пароль")
                error_label.pack(side=tk.BOTTOM)
                error_label.after(2000, lambda: error_label.pack_forget())

    class MakeAppointment(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_appoint_window()
            self.db = Hospital_DB

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

    class DeleteAppointment(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.init_delete_appoint_window()
            self.db = Hospital_DB

        def init_delete_appoint_window(self):
            self.title('Удалить запись на прием')
            self.geometry("600x450+200+100")
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
            btn_sort.bind('<Button-1>', lambda event: self.view_appointments_num(date.get(),
                                                                                 doc.get()))
            btn_sort.place(x=350, y=10)
            self.tree = ttk.Treeview(self, columns=('ID', 'Time', 'Patient'), heigh=15, show='headings')
            self.tree.column('ID', width=150, anchor=tk.CENTER)
            self.tree.column('Time', width=150, anchor=tk.CENTER)
            self.tree.column('Patient', width=150, anchor=tk.CENTER)
            self.tree.heading('ID', text='Номер посещения')
            self.tree.heading('Time', text='Время')
            self.tree.heading('Patient', text='Пациент')
            self.tree.place(x=40, y=60)

            btn_del = tk.Button(self, text='Удалить запись')
            btn_del.place(x=500, y=10)
            btn_del.bind('<Button-1>',
                         lambda event: self.delete_appoint(self.tree.set(self.tree.selection()[0], '#1')))

        def delete_appoint(self, number):
            self.db.del_appointment(number)
            ok_label = tk.Label(self, text="Успешно")
            ok_label.pack(side=tk.BOTTOM)
            ok_label.after(2000, lambda: ok_label.pack_forget())

        def view_appointments_num(self, date, doc):
            rec_list = self.db.get_appointments_num(date, doc)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in rec_list]
            pass


root = tk.Tk()
time_table = datetime.today()
week_day = time_table.weekday()
dbAuth = BDAuth()
Hospital_DB = DB()
app = Manager(root)
app.pack()
root.title("Hospital")
root.geometry("700x500+300+200")
root.resizable(True, True)
root.mainloop()
