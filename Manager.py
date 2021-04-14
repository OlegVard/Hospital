# !!!!!!вывод врачей(кто работает, а кто нет) или что-то другое
# добавить запись на прием
import tkinter as tk
from tkinter import ttk
from database import BDAuth, DB


class Manager(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.initManager()
        self.dataAuth = dbAuth
        self.Hospital_data = Hospital_DB

    def initManager(self):
        manager_tool_bar = tk.Frame(bg='#d7d8e0', bd=2)
        manager_tool_bar.pack(side=tk.TOP, fill=tk.X)
        btn_register = tk.Button(manager_tool_bar,
                                 text='Зарегистрировать',
                                 command=lambda: self.open_register(),
                                 compound=tk.TOP,
                                 bg='#ffefd5')
        btn_register.pack(side=tk.LEFT)
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

    def register_user(self, login, password, spec):
        response = self.dataAuth.register(login, password, spec)
        if response == 0:
            ok_label = tk.Label(text="Успешно")
            ok_label.pack(side=tk.BOTTOM)
            ok_label.after(2000, lambda: ok_label.pack_forget())
        else:
            error_label = tk.Label(text="Пользователь с таким логином уже есть")
            error_label.pack(side=tk.BOTTOM)
            error_label.after(2000, lambda: error_label.pack_forget())

    def change_password(self, login, old_password, new_password):
        response = self.dataAuth.change_password(login, old_password, new_password)
        if response == 0:
            ok_label = tk.Label(text="Успешно")
            ok_label.pack(side=tk.BOTTOM)
            ok_label.after(2000, lambda: ok_label.pack_forget())
        else:
            error_label = tk.Label(text="Неверно введен логин или старый пароль")
            error_label.pack(side=tk.BOTTOM)
            error_label.after(2000, lambda: error_label.pack_forget())

    def del_user(self, login, password):
        response = self.dataAuth.del_user(login, password)
        if response == 0:
            ok_label = tk.Label(text="Успешно")
            ok_label.pack(side=tk.BOTTOM)
            ok_label.after(2000, lambda: ok_label.pack_forget())
        else:
            error_label = tk.Label(text="Неверно введен логин или пароль")
            error_label.pack(side=tk.BOTTOM)
            error_label.after(2000, lambda: error_label.pack_forget())

    def open_register(self):
        self.RegisterWindow()

    def open_change_password_window(self):
        self.ChangePasswordWindow()

    def open_del_window(self):
        self.DelWindow()

    class RegisterWindow(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_register_window()
            self.view = app

        def init_register_window(self):
            self.title('Регистрация пользователя')
            self.geometry("500x300+400+300")
            self.resizable(False, False)

            label_log = tk.Label(self, text='Логин')
            label_log.place(x=100, y=50)
            label_pass = tk.Label(self, text='Пароль')
            label_pass.place(x=100, y=75)
            self.label_spec = tk.Label(self, text='Тип пользователя')
            self.label_spec.place(x=100, y=100)

            self.entry_log = ttk.Entry(self)
            self.entry_log.place(x=300, y=50)
            self.entry_pass = ttk.Entry(self)
            self.entry_pass.place(x=300, y=75)
            self.combobox_spec = ttk.Combobox(self, values=[u'М', u'Д', u'П'])
            self.combobox_spec.current(0)
            self.combobox_spec.place(x=300, y=100)

            self.btn_reg = tk.Button(self, text='Зарегистрировать')
            self.btn_reg.place(x=100, y=150)
            self.btn_reg.bind('<Button-1>', lambda event: self.view.register_user(self.entry_log.get(),
                                                                                  self.entry_pass.get(),
                                                                                  self.combobox_spec.get()))
            self.bind("<Return>", lambda event: self.view.register_user(self.entry_log.get(),
                                                                        self.entry_pass.get(),
                                                                        self.combobox_spec.get()))
            btn_canc = tk.Button(self, text='Закрыть',
                                 command=lambda: self.destroy())
            self.bind("<Escape>", lambda event: self.destroy())
            btn_canc.place(x=300, y=150)

            self.grab_set()
            self.focus_get()

    class ChangePasswordWindow(RegisterWindow):
        def __init__(self):
            super().__init__()
            self.init_change_password_window()
            self.view = app

        def init_change_password_window(self):
            self.title('Смена пароля')

            label_spec = tk.Label(self, text='Новый пароль')
            label_spec.place(x=100, y=100)

            entry_new_pass = ttk.Entry(self)
            entry_new_pass.place(x=300, y=100)

            btn_upd = tk.Button(self, text='Сменить пароль')
            btn_upd.place(x=100, y=150)
            btn_upd.bind('<Button-1>', lambda event: self.view.change_password(self.entry_log.get(),
                                                                               self.entry_pass.get(),
                                                                               entry_new_pass.get()))
            self.bind("<Return>", lambda event: self.view.change_password(self.entry_log.get(),
                                                                          self.entry_pass.get(),
                                                                          entry_new_pass.get()))

            self.btn_reg.destroy()
            self.label_spec.destroy()
            self.combobox_spec.destroy()

    class DelWindow(RegisterWindow):
        def __init__(self):
            super().__init__()
            self.init_del_window()
            self.view = app

        def init_del_window(self):
            self.title('Удаление пользователя')
            btn_del = tk.Button(self, text='Удалить')
            btn_del.place(x=120, y=150)
            btn_del.bind("<Button-1>", lambda event: self.view.del_user(self.entry_log.get(),
                                                                        self.entry_pass.get()))
            self.bind("<Return>", lambda event: self.view.del_user(self.entry_log.get(),
                                                                   self.entry_pass.get()))
            self.btn_reg.destroy()
            self.label_spec.destroy()
            self.combobox_spec.destroy()


root = tk.Tk()
dbAuth = BDAuth()
Hospital_DB = DB()
app = Manager(root)
app.pack()
root.title("Hospital")
root.geometry("700x500+300+200")
root.resizable(True, True)
root.mainloop()
