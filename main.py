import functools
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from style import Content
from tkinter import PhotoImage
# from database_controller import Database
import mysql.connector as mysql

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"


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

        # Entry
        self.signin_username_e = ttk.Entry
        self.signin_password_e = ttk.Entry

        self.signup_username_e = ttk.Entry
        self.signup_password_e = ttk.Entry
        self.signup_email_e = ttk.Entry

        self.employee_username_e = ttk.Entry
        self.employee_password_e = ttk.Entry

        # Integer
        # self.key = int

        # String
        self.admin_id_str = str

        # Database
        self.db1 = None
        self.mycursor = None

        # Initialize method for login interface
        # self.signin_interface()
        self.main_interface()

        # Initialize class for database
        # Database()

        # Root window configuration
        self.master.title('DormBuilt HMS')
        self.master.resizable(True, True)

        # Initialize class for default styles
        Content.widget_styles(self.master)

    def signin_interface(self):
        self.master.geometry("%dx%d" % (350, 450))

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

        self.signin_username_e = ttk.Entry(form_f)
        self.signin_username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1)

        self.signin_password_e = ttk.Entry(form_f, show="*")
        self.signin_password_e.grid(column=1, row=1)

        buttons_f = ttk.Frame(login_f, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        signin_b = tk.Button(buttons_f, text="Sign in", font="OpenSans, 12", fg="#FFFFFF",
                             bg="#4C8404", relief="flat", command=self.signin_validation)
        signin_b.pack(side="top", pady=5, padx=10, fill="x")

        signup_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        signup_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        signup_b = tk.Button(signup_b_lf, text="Sign up", font="OpenSans, 12", fg="#585456",
                             bg="#FFFFFF", relief="flat", command=self.signup_interface)
        signup_b.pack(side="top", fill="x")

    def signup_interface(self):
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

        ttk.Label(form_f, text='User Name', style="h2.TLabel", justify="left").grid(column=0, row=0, sticky="w")

        self.signup_username_e = ttk.Entry(form_f)
        self.signup_username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1, sticky="w")

        self.signup_username_e = ttk.Entry(form_f, show="*")
        self.signup_username_e.grid(column=1, row=1)

        ttk.Label(form_f, text='Email', style="h2.TLabel", justify="left").grid(column=0, row=2, sticky="w")

        self.signup_username_e = ttk.Entry(form_f)
        self.signup_username_e.grid(column=1, row=2)

        buttons_f = ttk.Frame(register_f, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        cancel_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        cancel_b_lf.pack(side="left", padx=10)

        cancel_b = tk.Button(cancel_b_lf, text="Cancel", font="OpenSans, 12", fg="#585456",
                             bg="#FFFFFF", relief="flat", command=self.signin_interface)
        cancel_b.pack()

        signup_b = tk.Button(buttons_f, text="Continue", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                             relief="flat", command=self.signup_request)
        signup_b.pack(side="right", padx=10)

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
                             relief="flat", command=self.signin_interface)
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
        create_account_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        create_account_lf.pack(side="top", fill="x")

        create_account_form_lf2 = tk.LabelFrame(create_account_lf, bg="#FFFFFF", relief="flat")
        create_account_form_lf2.pack(side="top", fill="x")

        ttk.Label(create_account_form_lf2, text='Create employee account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(create_account_form_lf2, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        create_account_form_lf = tk.LabelFrame(create_account_lf, bg="#FFFFFF", relief="flat")
        create_account_form_lf.pack(side="top", anchor="nw", pady=10)

        ttk.Label(create_account_form_lf, text='Employee Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, sticky="w")

        self.employee_username_e = ttk.Entry(create_account_form_lf)
        self.employee_username_e.grid(column=1, row=0)

        ttk.Label(create_account_form_lf, text='Employee Password', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, sticky="w")

        self.employee_password_e = ttk.Entry(create_account_form_lf)
        self.employee_password_e.grid(column=1, row=1)

        create_account_buttons_lf = tk.LabelFrame(create_account_lf, bg="#FFFFFF", relief="flat")
        create_account_buttons_lf.pack(side="top", anchor="nw")

        create_account_b = tk.Button(create_account_buttons_lf, text="Create account", font="OpenSans, 12",
                                     fg="#FFFFFF", bg="#4C8404", relief="flat", command=self.signup_request)
        create_account_b.pack(side="left", padx=10)

        ttk.Label(create_account_buttons_lf, text='Click here to create an\n employee account!',
                  style="small_info.TLabel").pack(side="left")

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

    # ================================================ Database Control ================================================
    def database_connect(self):
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="hmsdatabase")
            print("Connected to lmsdatabase")
            self.mycursor = self.db1.cursor()
        except Exception as e:
            print("Could not connect to hmsdatabase")
            print(e)

    def signin_validation(self):
        if not self.signin_username_e.get():
            self.invalid_input()
        if not self.signin_password_e.get():
            self.invalid_input()
        else:
            self.database_connect()
            self.mycursor.execute(
                "SELECT * FROM admin where username = '" + self.signin_username_e.get() + "' and password = '" +
                self.signin_password_e.get() + "';")
            myresult = self.mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.mycursor.execute(
                    "SELECT DISTINCT admin_id FROM admin where username = '" + self.signin_username_e.get() + "';")

                # Converts the tuple into integer
                admin_id = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                self.admin_id_str = str(admin_id)
                # print(self.admin_id_str)

                # Instantiate create_widgets method
                self.main_interface()

            self.db1.close()
            self.mycursor.close()

    def signup_request(self):
        if not self.signup_username_e.get():
            self.invalid_input()
        if not self.signup_password_e.get():
            self.invalid_input()
        if not self.signup_email_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO admin (username, password, email) VALUES (%s,%s,%s)",
                                      (self.signup_username_e.get(), self.signup_password_e.get(),
                                       self.signup_email_e.get()))
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                # Initialize method to move back to the login interface
                self.signin_interface()
            except Exception as e:
                self.invalid_input()
                print("Failed to connect")
                print(e)

    # ================================================ Static Methods ==================================================
    @staticmethod
    def invalid_input():
        messagebox.showerror("Error", "Invalid input")

    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='This action is currently under development!')


if __name__ == "__main__":
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
