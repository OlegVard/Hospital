import tkinter as tk
from tkinter import ttk
from database import BDAuth


class AuthWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_auth_window()
        self.auth_db = auth_db

    def init_auth_window(self):
        label_log = tk.Label(self, text='Логин')
        label_log.grid(row=0, column=0)
        label_pass = tk.Label(self, text='Пароль')
        label_pass.grid(row=1, column=0)
        self.entry_log = ttk.Entry(self)
        self.entry_log.grid(row=0, column=1)
        self.entry_pass = ttk.Entry(self, show='*')
        self.entry_pass.grid(row=1, column=1)
        self.conf_btn = tk.Button(text='Войти',
                                  command=lambda: self.sing_in(
                                      self.entry_log.get(),
                                      self.entry_pass.get()),
                                  bg='#ffefd5')
        self.conf_btn.place(x=200, y=200)

    def sing_in(self, login, password):
        is_doc = self.auth_db.check_pass(login, password)
        if is_doc == 'doc':
            print('doc')


if __name__ == "__main__":
    root = tk.Tk()
    auth_db = BDAuth()
    root["bg"] = "#FFFAFA"
    app_auth = AuthWindow(root)
    app_auth.pack()
    root.title('Авторизация')
    root.geometry("500x400+400+250")
    root.resizable(False, False)
    root.mainloop()
