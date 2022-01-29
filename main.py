import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from style import Content
from tkinter import PhotoImage
import mysql.connector as mysql


class Window:
    def __init__(self, master):
        super().__init__()

        # Window
        self.master = master

        # LabelFrame
        self.content_lf = None

        # PhotoImage
        self.db_logo_resized = tkinter.PhotoImage
        self.db_logo_resized_2 = tkinter.PhotoImage

        # Buttons
        self.home_b = tk.Button
        self.settings_b = tkinter.Button
        self.notif_b = tkinter.Button

        # Initialize method for login interface
        self.login_interface()
        # self.main_interface()

    def login_interface(self):
        # Root window configuration
        self.master.title('DormBuilt HMS')
        self.master.resizable(True, True)
        self.master.geometry("%dx%d" % (350, 450))

        # Initialize class for default styles
        Content.widget_styles(self.master)

        # Clean widgets in the master window
        Content.destroy_content(self.master)

        # ================================================ Login UI ====================================================
        login_f = tk.LabelFrame(self.master, bg="#FFFFFF")
        login_f.pack(anchor="center")

        logo_f = ttk.Frame(login_f, style="Basic.TFrame")
        logo_f.pack(side="top", ipady=20, fill="both")

        db_logo = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized = db_logo.subsample(2, 2)

        ttk.Label(logo_f, image=self.db_logo_resized).pack(pady=5)

        ttk.Label(logo_f, text='DormBuilt Inc.', style="h1.TLabel", justify="center").pack(pady=5)

        form_f = ttk.Frame(login_f, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=10, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel", justify="left").grid(column=0, row=0)

        username_e = ttk.Entry(form_f)
        username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1)

        password_e = ttk.Entry(form_f, show="*")
        password_e.grid(column=1, row=1)

        buttons_f = ttk.Frame(login_f, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        admin_signin_b = tk.Button(buttons_f, text="Sign in as an Administrator", font="OpenSans, 12", fg="#FFFFFF",
                                   bg="#4C8404", relief="flat", command=self.main_interface)
        admin_signin_b.pack(side="top", pady=5, padx=10, fill="x")

        user_signin_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        user_signin_lf.pack(side="top", pady=5, padx=10, fill="x")

        user_signin_b = tk.Button(user_signin_lf, text="Sign in as a User", font="OpenSans, 12", fg="#585456",
                                  bg="#FFFFFF", relief="flat", command=self.main_interface)
        user_signin_b.pack(side="top", fill="x")

        register_b = tk.Button(buttons_f, text="Register", font="OpenSans, 12", fg="#4C8404", bg="#D4DEC9",
                               relief="flat", command=self.register_interface)
        register_b.pack(side="top", pady=5, padx=10, fill="x")

    def register_interface(self):
        # Clean widgets in the master window
        Content.destroy_content(self.master)

        # ================================================ Login UI ====================================================
        register_f = tk.LabelFrame(self.master, bg="#FFFFFF")
        register_f.pack(anchor="center")

        logo_f = ttk.Frame(register_f, style="Basic.TFrame")
        logo_f.pack(side="top", ipady=20, fill="both")

        ttk.Label(logo_f, image=self.db_logo_resized).pack(pady=5)

        ttk.Label(logo_f, text='DormBuilt Inc.', style="h1.TLabel", justify="center").pack(pady=5)

        form_f = ttk.Frame(register_f, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=10, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel", justify="left").grid(column=0, row=0)

        username_e = ttk.Entry(form_f)
        username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1)

        password_e = ttk.Entry(form_f, show="*")
        password_e.grid(column=1, row=1)

        ttk.Label(form_f, text='Email', style="h2.TLabel", justify="left").grid(column=0, row=2)

        email_e = ttk.Entry(form_f)
        email_e.grid(column=1, row=2)

        buttons_f = ttk.Frame(register_f, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        cancel_b = tk.Button(buttons_f, text="Cancel", font="OpenSans, 12", fg="#4C8404", bg="#D4DEC9",
                             relief="flat", command=self.login_interface)
        cancel_b.pack(side="left", padx=10)

        register_b = tk.Button(buttons_f, text="Register", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                               relief="flat", command=self.button_clicked)
        register_b.pack(side="right", padx=10)

    def main_interface(self):
        # Root window configuration
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.resizable(True, True)
        self.master.geometry("%dx%d" % (width, height))

        # Clean widgets in the master window
        Content.destroy_content(self.master)

        # ================================================ Main interface contents =====================================

        # ================================================ Top-Nav Interface ===========================================
        top_nav_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        top_nav_lf.pack(side="top", fill="x")

        db_logo = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized_2 = db_logo.subsample(6, 6)

        ttk.Label(top_nav_lf, image=self.db_logo_resized_2).pack(side="left", pady=5)

        ttk.Label(top_nav_lf, text='DormBuilt Inc. | Hotel Management System ',
                  style="h2.TLabel", justify="left").pack(side="left")

        logout_b = tk.Button(top_nav_lf, text="Logout", font=("Times New Roman", 15), fg='#BD1E51', bg="#FFFFFF",
                             relief="flat", command=self.login_interface)
        logout_b.pack(side="right")

        # ================================================ Left-Nav widgets ============================================
        left_nav_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        left_nav_lf.pack(side="left", fill="both")

        self.home_b = tk.Button(left_nav_lf, text="Home", font=("Times New Roman", 15), fg='#395A68',
                                bg="#FFFFFF", relief="flat", command=self.home_content_interface)
        self.home_b.pack(side="top", anchor="w")

        self.settings_b = tk.Button(left_nav_lf, text="Settings", font=("Times New Roman", 15), fg='#7c8084',
                                    bg="#FFFFFF", relief="flat", command=self.settings_content_interface)
        self.settings_b.pack(side="top", anchor="w")

        self.notif_b = tk.Button(left_nav_lf, text="Notifications", font=("Times New Roman", 15), fg='#7c8084',
                                 bg="#FFFFFF", relief="flat", command=self.notif_content_interface)
        self.notif_b.pack(side="top", anchor="w")

        # ================================================ Left-Nav widgets ============================================
        self.content_lf = tk.LabelFrame(self.master, bg="#FFFFFF")
        self.content_lf.pack(side="left", fill="both", expand=True)

        # Initialize home_content_interface method
        self.home_content_interface()

    def home_content_interface(self):
        self.change_button_color()
        self.home_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content.destroy_content(self.content_lf)

        # ================================================ Home content ================================================

        ttk.Label(self.content_lf, text='Home', style="h2.TLabel", justify="left").pack(side="top", anchor="nw")

        # Profile view database container
        room_availability_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        room_availability_lf.pack(side="top", pady=10, fill="both")

        ttk.Label(room_availability_lf, text='Room Availability', style="h2.TLabel",
                  justify="left").pack(side="left", anchor="nw")

        add_room = tk.Button(room_availability_lf, text="+ Add room", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                             relief="flat", command=self.button_clicked)
        add_room.pack(side="left", padx=10, anchor="nw")

        """
        remove_room = tk.Button(room_availability_lf, text="Remove room", font="OpenSans, 12", fg="#585456",
                                bg="#FFFFFF", command=self.button_clicked)
        remove_room.pack(side="left", padx=10, anchor="nw")"""

    def settings_content_interface(self):
        self.change_button_color()
        self.settings_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content.destroy_content(self.content_lf)

        # ================================================ Settings content ============================================

        ttk.Label(self.content_lf, text='Settings', style="h2.TLabel", justify="left").pack(side="top", anchor="nw")

    def notif_content_interface(self):
        self.change_button_color()
        self.notif_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content.destroy_content(self.content_lf)

        # ================================================ Notif content ===============================================

        ttk.Label(self.content_lf, text='Notification', style="h2.TLabel", justify="left").pack(side="top", anchor="nw")

    def change_button_color(self):
        self.home_b.configure(fg='#7c8084')
        self.settings_b.configure(fg='#7c8084')
        self.notif_b.configure(fg='#7c8084')

    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='This action is currently under development!')


if __name__ == "__main__":
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
