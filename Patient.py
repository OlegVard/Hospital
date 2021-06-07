import tkinter as tk
from tkinter import ttk
from database import DB


class PatientWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = DB()
        f = open("log.txt", 'r')
        self.work_login = f.readline()
        f.close()
        f = open("log.txt", 'w')
        f.write('')
        f.close()
        self.tree_past = None
        self.tree_fut = None
        self.text = None
        self.init_patient_window()
        self.view_past_records(self.work_login)
        self.view_fut_records(self.work_login)

    def init_patient_window(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_view_treatment = tk.Button(toolbar,
                                       text='Открыть рекомендации по лечению',
                                       compound=tk.TOP,
                                       command=lambda: self.open_treatment())
        btn_view_treatment.pack(side=tk.RIGHT)

        self.tree_past = ttk.Treeview(columns=('ID', 'Date', 'Diagnosis', 'FIO'), heigh=14, show='headings')
        self.tree_past.column('ID', width=200, anchor=tk.CENTER)
        self.tree_past.column('Date', width=200, anchor=tk.CENTER)
        self.tree_past.column('Diagnosis', width=200, anchor=tk.CENTER)
        self.tree_past.column('FIO', width=200, anchor=tk.CENTER)
        self.tree_past.heading('ID', text='Номер посещения')
        self.tree_past.heading('Date', text='Дата посещения')
        self.tree_past.heading('Diagnosis', text='Диагноз')
        self.tree_past.heading('FIO', text='ФИО Врача')
        self.tree_past.place(x=0, y=55)

        past_label = tk.Label(text='Предыдущие посещения')
        past_label.place(x=0, y=30)

        self.tree_fut = ttk.Treeview(columns=('ID', 'Date', 'Time', 'FIO', 'Room'), heigh=14, show='headings')
        self.tree_fut.column('ID', width=100, anchor=tk.CENTER)
        self.tree_fut.column('Date', width=150, anchor=tk.CENTER)
        self.tree_fut.column('Time', width=150, anchor=tk.CENTER)
        self.tree_fut.column('FIO', width=200, anchor=tk.CENTER)
        self.tree_fut.column('Room', width=200, anchor=tk.CENTER)
        self.tree_fut.heading('ID', text='Номер посещения')
        self.tree_fut.heading('Date', text='Дата посещения')
        self.tree_fut.heading('Time', text='Время посещения')
        self.tree_fut.heading('FIO', text='ФИО Врача')
        self.tree_fut.heading('Room', text='Кабинет')
        self.tree_fut.place(x=0, y=390)
        fut_label = tk.Label(text='Будущие посещения')
        fut_label.place(x=0, y=365)

        text_label = tk.Label(text='Рекомендации по лечению')
        text_label.place(x=853, y=30)
        self.text = tk.Text(width=61,
                            height=30,
                            font="Arial 14",
                            wrap=tk.WORD)
        self.text.place(x=853, y=55)

    def open_treatment(self):
        treatment = self.db.get_treatment(self.tree_past.set(self.tree_past.selection()[0], '#1'))
        self.text.delete(1.0, tk.END)
        self.text.insert(1.0, treatment[0])

    def view_past_records(self, login):
        rec_list = self.db.get_past_records(login)
        [self.tree_past.insert('', 'end', values=row) for row in rec_list]

    def view_fut_records(self, login):
        rec_list = self.db.get_fut_records(login)
        [self.tree_fut.insert('', 'end', values=row) for row in rec_list]


root = tk.Tk()
app = PatientWindow(root)
app.pack()
root.title("Hospital")
root.geometry("1000x600+300+200")
root.resizable(True, True)
root.mainloop()
