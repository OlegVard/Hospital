import tkinter as tk
from tkinter import ttk
from database import BDAuth


class Manager(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.initManager()
        self.dataAuth = dbAuth

    def initManager(self):
        manager_tool_bar = tk.Frame(bg='#d7d8e0', bd=2)
        manager_tool_bar.pack(side=tk.TOP, fill=tk.X)
        btn_register = tk.Button(manager_tool_bar,
                                 text='Зарегистрировать',
                                 command=lambda: self.open_register(),
                                 compound=tk.TOP,
                                 bg='#ffefd5')
        btn_register.pack(side=tk.LEFT)

    def register_user(self, login, password, spec):
        self.dataAuth.register(login, password, spec)
        self.ok_lable = tk.Label(self, text="Успешно")
        self.ok_lable.pack(side=tk.BOTTOM)
        self.ok_lable.after(2000, lambda: self.ok_lable.pack_forget())

    def open_register(self):
        self.RegisterWindow()

    class RegisterWindow(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_registrWindow()
            self.view = app

        def init_registrWindow(self):
            self.title('Регистраия пользователя')
            self.geometry("500x300+400+300")
            self.resizable(False, False)

            label_log = tk.Label(self, text='Логин')
            label_log.place(x=100, y=50)
            label_pass = tk.Label(self, text='Пароль')
            label_pass.place(x=100, y=75)
            label_spec = tk.Label(self, text='Тип пользователя')
            label_spec.place(x=100, y=100)

            self.entry_log = ttk.Entry(self)
            self.entry_log.place(x=300, y=50)
            self.entry_pass = ttk.Entry(self)
            self.entry_pass.place(x=300, y=75)
            self.combobox_spec = ttk.Combobox(self, values=[u'М', u'Д', u'П'])
            self.combobox_spec.current(0)
            self.combobox_spec.place(x=300, y=100)

            btn_reg = tk.Button(self, text='Зарегистрировать')
            btn_reg.place(x=100, y=150)
            btn_reg.bind('<Button-1>', lambda event: self.view.register_user(self.entry_log.get(),
                                                                             self.entry_pass.get(),
                                                                             self.combobox_spec.get()))
            btn_canc = tk.Button(self, text='Закрыть',
                                 command=lambda: self.destroy())
            btn_canc.place(x=300, y=150)

            self.grab_set()
            self.focus_get()


root = tk.Tk()
dbAuth = BDAuth()
root["bg"] = "#FFFAFA"
app = Manager(root)
app.pack()
root.title("Hospital")
root.geometry("700x500+300+200")
root.resizable(True, True)
root.mainloop()
