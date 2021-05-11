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
        self.work_login = 'doc1'    # Онли для проверки
        self.date = time_table
        self.week_day = week_day
        self.view_records(self.work_login)

    def init_doc_window(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_open_dialog = tk.Button(toolbar,
                                    text='Записать на прием',
                                    command=lambda: self.open_dialog(),
                                    compound=tk.TOP,
                                    bg='#ffefd5')
        btn_open_dialog.pack(side=tk.LEFT)
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
        [self.tree.insert('', 'end', values=row) for row in pat_list]

    def open_dialog(self):
        self.Child()

    class Child(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_child()
            self.view = app

        def init_child(self):
            self.title('Запись на прием')
            self.geometry("500x300+400+300")
            self.resizable(False, False)

            label_des = tk.Label(self, text='Время')
            label_des.place(x=100, y=50)
            label_doc = tk.Label(self, text='Дата')
            label_doc.place(x=100, y=100)
            label_comb = tk.Label(self, text='Специальность')
            label_comb.place(x=100, y=75)

            self.entry_time = ttk.Entry(self)
            self.entry_time.place(x=300, y=50)
            self.entry_date = ttk.Entry(self)
            self.entry_date.place(x=300, y=100)
            self.combobox = ttk.Combobox(self, values=[u'0', u'1'])
            self.combobox.current(0)
            self.combobox.place(x=300, y=75)

            btn_conf = tk.Button(self, text='Записать')
            btn_conf.place(x=100, y=150)
            #btn_conf.bind('<Button-1>', lambda event: pass)

            btn_canc = tk.Button(self, text='Закрыть',
                                 command=lambda: self.destroy())
            btn_canc.place(x=300, y=150)
            root.bind("<Escape>", lambda event: self.destroy())

            self.grab_set()
            self.focus_get()


root = tk.Tk()
time_table = datetime.today()
week_day = time_table.weekday()
app = Doctor(root)
app.pack()
root.title("Hospital")
root.geometry("1000x600+300+200")
root.resizable(True, True)
root.mainloop()
