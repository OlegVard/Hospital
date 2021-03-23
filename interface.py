# this file need to create an interface for my app
import tkinter as tk

class main_window(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):



if __name__ == "__main__":
    root = tk.Tk()
    app = main_window(root)
    app.pack()
    root.title("Hospital")
    root.geometry("700x500+300+200")
    root.resizable(True, True)
    root.mainloop()
