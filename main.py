import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('DormBuilt HMS')
        # self.geometry('300x50')

        self.login_f = tk.Frame(self, bg="#ffffff")
        self.login_f.pack(padx=30, pady=30, ipadx=10, ipady=10)

        ttk.Label(self.login_f, text='WELCOME').pack()

        self.username_e = ttk.Entry(self.login_f)
        self.username_e.pack()

        ttk.Label(self.login_f, text='User Name').pack()

        self.password_e = ttk.Entry(self.login_f, show="*")
        self.password_e.pack()

        ttk.Label(self.login_f, text='Password').pack()










        """
        self.top_nav_frame = ttk.Frame(self)
        self.top_nav_frame.pack()

        ttk.Label(self.top_nav_frame, text='top nav').pack()

        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack()

        ttk.Label(self.top_nav_frame, text='top nav').pack()

        # button
        self.button = ttk.Button(self, text='Click Me', command=self.button_clicked)
        self.button.pack()
        """


    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='Hello, Tkinter!')


if __name__ == "__main__":
    win = Window()
    win.mainloop()
