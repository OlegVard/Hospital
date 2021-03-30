# this file needs to create an interface for my app
import tkinter as tk
from tkinter import ttk
from database import DB


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_open_dialog = tk.Button(toolbar,
                                    text='Записаться на прием',
                                    command=lambda: self.open_dialog(),
                                    compound=tk.TOP,
                                    bg='#ffefd5')
        btn_open_dialog.pack(side=tk.LEFT)

    def records(self, spec, date, time):
        self.db.insert_data(spec, date, time)

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

            btn_conf = tk.Button(self, text='Записаться')
            btn_conf.place(x=100, y=150)
            btn_conf.bind('<Button-1>', lambda event: self.view.records(self.combobox.get(),
                                                                        self.entry_date.get(),
                                                                        self.entry_time.get()))

            btn_canc = tk.Button(self, text='Закрыть',
                                 command=lambda: self.destroy())
            btn_canc.place(x=300, y=150)

            self.grab_set()
            self.focus_get()


root = tk.Tk()
db = DB()
root["bg"] = "#FFFAFA"
app = MainWindow(root)
app.pack()
root.title("Hospital")
root.geometry("700x500+300+200")
root.resizable(True, True)
root.mainloop()
