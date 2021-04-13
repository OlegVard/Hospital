# косметические правки
import tkinter as tk
from tkinter import ttk
from database import BDAuth
import os


class AuthWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_auth_window()
        self.auth_db = auth_db

    def init_auth_window(self):
        label_log = tk.Label(text='Логин')
        label_log.place(x=150, y=50)
        label_pass = tk.Label(text='Пароль')
        label_pass.place(x=150, y=75)
        self.entry_log = ttk.Entry()
        self.entry_log.place(x=200, y=50)
        self.entry_pass = ttk.Entry(show='*')
        self.entry_pass.place(x=200, y=75)
        self.conf_btn = tk.Button(text='Войти',
                                  command=lambda: self.sing_in(
                                      self.entry_log.get(),
                                      self.entry_pass.get()),
                                  bg='#ffefd5')
        self.conf_btn.place(x=225, y=200)
        root.bind("<Return>", lambda event: self.sing_in(
                            self.entry_log.get(),
                            self.entry_pass.get()))
        root.bind("<Escape>", lambda event: root.destroy())

    def sing_in(self, login, password):
        is_doc = self.auth_db.check_pass(login, password)
        if is_doc == 'doc':
            root.destroy()
            os.system("python Doctor.py")  # подумать над этим
        elif is_doc == 'patient':
            root.destroy()
            os.system("python Patient.py")  # подумать над этим
        elif is_doc == 'manager':
            root.destroy()
            os.system("python Manager.py")
        elif is_doc == 0:
            label_err = tk.Label(root, text='Неверный логин или пароль')
            label_err.pack(side=tk.BOTTOM)
            label_err.after(1000, lambda: label_err.pack_forget())


if __name__ == "__main__":
    root = tk.Tk()
    auth_db = BDAuth()
    app_auth = AuthWindow(root)
    app_auth.pack()
    root.title('Авторизация')
    root.geometry("500x400+400+250")
    root.resizable(False, False)
    root.mainloop()
