import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from style import Content
from tkinter import PhotoImage


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('DormBuilt HMS')
        self.resizable(False, False)
        # self.geometry('300x450')

        # Initialize class for default styles
        Content.widget_styles(self.master)

        # ================================================ Login UI ====================================================
        self.login_f = tk.LabelFrame(self, bg="#FFFFFF")
        self.login_f.pack()

        welcome_f = ttk.Frame(self.login_f, style="Basic.TFrame")
        welcome_f.pack(side="top", ipady=20, fill="both")

        db_logo = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized = db_logo.subsample(2, 2)

        ttk.Label(welcome_f, image=self.db_logo_resized).pack(pady=5)

        ttk.Label(welcome_f, text='DormBuilt Inc.', style="h1.TLabel", justify="center").pack(pady=5)

        form_f = ttk.Frame(self.login_f, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=10, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel", justify="left").grid(column=0, row=0)

        self.username_e = ttk.Entry(form_f)
        self.username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1)

        self.password_e = ttk.Entry(form_f, show="*")
        self.password_e.grid(column=1, row=1)

        buttons_f = ttk.Frame(self.login_f, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        self.register_b = tk.Button(buttons_f, text="Register", font="OpenSans, 12", fg="#4C8404", bg="#D4DEC9",
                                    relief="flat", command=self.button_clicked)
        self.register_b.pack(side="left", padx=10)

        self.login_b = tk.Button(buttons_f, text="Login", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                                 relief="flat", command=self.button_clicked)
        self.login_b.pack(side="right", padx=10)

    def main_interface(self):
        pass


    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='Hello, Tkinter!')


if __name__ == "__main__":
    win = Window()
    win.mainloop()
