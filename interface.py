# this file needs to create an interface for my app
import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        btn_open_dialog = tk.Button(toolbar,
                                    text='Записаться на прием',
                                    command=lambda: self.open_dialog(),
                                    compound=tk.TOP,
                                    bg='#ffefd5')
        btn_open_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        self.Child()

    class Child(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_child()

        def init_child(self):
            self.title('Запись на прием')
            self.geometry("500x300+400+300")
            self.resizable(False, False)
            self.grab_set()
            self.focus_get()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.title("Hospital")
    root.geometry("700x500+300+200")
    root.resizable(True, True)
    root.mainloop()
