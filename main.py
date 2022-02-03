import functools
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from style import Content
from tkinter import PhotoImage
# from database_controller import Database
import mysql.connector as mysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
from tkinter import Menu
from datetime import datetime

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"

date_time = datetime.now()
date_time_str = date_time.strftime("%d/%m/%Y %H:%M:%S")


class Window:
    def __init__(self, master):
        super().__init__()

        # Window
        self.master = master

        # TopLevel Frame
        self.reset_password_top = tk.Toplevel
        self.admin_access_top = tk.Toplevel
        self.bug_report_top = tk.Toplevel
        self.change_username_password_top = tk.Toplevel
        self.create_employee_top = tk.Toplevel

        # LabelFrame
        self.content_lf = None
        self.login_register_lf = None
        # Label
        self.admin_access_status_l = ttk.Label

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
        self.employee_role_e = ttk.Entry

        self.forgot_password_email_e = ttk.Entry

        self.admin_access_username_e = ttk.Entry
        self.admin_access_password_e = ttk.Entry

        self.change_username_e = ttk.Entry
        self.change_password_e = ttk.Entry

        # Text
        self.bug_description_e = ttk.Entry

        # String
        self.admin_id_str = str
        self.admin_access_status = None

        # Boolean
        self.admin_access = False
        self.basic_user_access = True

        # Database
        self.db1 = None
        self.mycursor = None

        # Initialize method for login interface
        self.signin_interface()
        # self.main_interface()

        # Initialize class for database
        # Database()

        # Root window configuration
        self.master.title('DormBuilt HMS')
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.resizable(True, True)

        # Initialize class for default styles
        Content.widget_styles(self.master)

    def signin_interface(self):
        # Clean widgets in the master window
        Content.destroy_content(self.master)

        # ================================================ Sign In Interface ===========================================
        top_f = ttk.Frame(self.master, style="Basic.TFrame")
        top_f.pack(side="top", fill="x")

        # ================================================ Logo Interface ==============================================
        logo_f = ttk.Frame(top_f, style="Basic.TFrame")
        logo_f.pack(side="left", padx=20)

        db_logo = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized = db_logo.subsample(2, 2)

        ttk.Label(logo_f, image=self.db_logo_resized).pack(pady=5)

        ttk.Label(logo_f, text='DormBuilt Inc.', style="h1.TLabel").pack(pady=5)

        ttk.Label(top_f, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at velit eu leo \n'
                              'consectetur aliquam. Donec lacus orci, bibendum in sodales et, sollicitudin vel \n '
                              'magna. Nullam elit elit, consectetur commodo erat vitae, auctor porttitor nibh. \n'
                              'In diam nisi, tristique ut mi ac, efficitur auctor rna.',
                  style="h1_body.TLabel").pack(side="left")

        # ================================================ Sign In Form Interface ======================================
        self.login_register_lf = tk.LabelFrame(top_f, bg="#FFFFFF")
        self.login_register_lf.pack(side="right", padx=20, pady=20)

        ttk.Label(self.login_register_lf, text='Sign In', style="h1.TLabel").pack(side="top", pady=10, anchor="nw")

        form_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=5, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel").grid(column=0, row=0, sticky="w")

        self.signin_username_e = ttk.Entry(form_f)
        self.signin_username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel").grid(column=0, row=1, sticky="w")

        self.signin_password_e = ttk.Entry(form_f, show="*")
        self.signin_password_e.grid(column=1, row=1)

        forgot_password_l = ttk.Label(form_f, text="Forgot password?", cursor="hand2", style="link.TLabel")
        forgot_password_l.grid(column=1, row=2, sticky="e")
        forgot_password_l.bind("<Button-1>", self.forgot_password_dialog)

        buttons_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both")

        signin_admin_b = tk.Button(buttons_f, text="Sign in as Administrator", font="OpenSans, 12", fg="#FFFFFF",
                                   bg="#4C8404", relief="flat", command=self.admin_signin_request)
        signin_admin_b.pack(side="top", pady=5, padx=10, fill="x")

        signin_basic_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        signin_basic_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        signin_basic_b = tk.Button(signin_basic_b_lf, text="Sign in as Basic user", font="OpenSans, 12", fg="#4C8404",
                                   bg="#FFFFFF", relief="flat", command=self.basic_user_signin_request)
        signin_basic_b.pack(side="top", fill="x")

        signup_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        signup_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        signup_b = tk.Button(signup_b_lf, text="Sign up", font="OpenSans, 12", fg="#585456",
                             bg="#FFFFFF", relief="flat", command=self.signup_interface)
        signup_b.pack(side="top", fill="x")

        self.signin_username_e.focus()

    def signup_interface(self):
        # Clean widgets in the master window
        Content.destroy_content(self.login_register_lf)

        # ================================================ Login UI ====================================================
        ttk.Label(self.login_register_lf, text='Sign Up', style="h1.TLabel").pack(side="top", pady=10, anchor="nw")

        form_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=10, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel", justify="left").grid(column=0, row=0, sticky="w")

        self.signup_username_e = ttk.Entry(form_f)
        self.signup_username_e.grid(column=1, row=0)
        self.signup_username_e.focus()

        ttk.Label(form_f, text='Password', style="h2.TLabel", justify="left").grid(column=0, row=1, sticky="w")

        self.signup_password_e = ttk.Entry(form_f, show="*")
        self.signup_password_e.grid(column=1, row=1)

        ttk.Label(form_f, text='Email', style="h2.TLabel", justify="left").grid(column=0, row=2, sticky="w")

        self.signup_email_e = ttk.Entry(form_f)
        self.signup_email_e.grid(column=1, row=2)

        buttons_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        signup_b = tk.Button(buttons_f, text="Sign up as Administrator", font="OpenSans, 12", fg="#FFFFFF",
                             bg="#4C8404", relief="flat", command=self.admin_signup_request)
        signup_b.pack(side="top", pady=5, padx=10, fill="x")

        cancel_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        cancel_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        cancel_b = tk.Button(cancel_b_lf, text="Go back", font="OpenSans, 12", fg="#585456",
                             bg="#FFFFFF", relief="flat", command=self.signin_interface)
        cancel_b.pack(fill="x")

    def main_interface(self):
        # Clean widgets in the master window
        Content.destroy_content(self.master)

        # ================================================ Main interface contents =====================================
        # ================================================ Menu Bar Interface ==========================================
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Creating file menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.switch_exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Creating help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Bug report", command=self.bug_report_dialog)
        help_menu.add_separator()
        menu_bar.add_cascade(label="Help", menu=help_menu)

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

        self.admin_access_status = "Off"

        # ================================================ Settings content ============================================
        admin_panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        admin_panel_lf.pack(side="top", fill="x")

        # ================================================ Account Settings ============================================
        account_settings_lf = tk.LabelFrame(admin_panel_lf, bg="#FFFFFF")
        account_settings_lf.pack(side="left", padx=10, pady=10)

        account_settings_label_lf = tk.LabelFrame(account_settings_lf, bg="#FFFFFF", relief="flat")
        account_settings_label_lf.pack(side="top", fill="x")

        ttk.Label(account_settings_label_lf, text='Account settings',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(account_settings_label_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        description_lf = tk.LabelFrame(account_settings_lf, bg="#FFFFFF", relief="flat")
        description_lf.pack(side="top", anchor="nw", pady=10)

        ttk.Label(description_lf, text='Administrative access: ',
                  style="small_info.TLabel").grid(column=0, row=0)

        self.admin_access_status_l = ttk.Label(description_lf, text=self.admin_access_status)
        self.admin_access_status_l.grid(column=1, row=0)

        account_settings_links_lf = tk.LabelFrame(account_settings_lf, bg="#FFFFFF", relief="flat")
        account_settings_links_lf.pack(side="top", anchor="nw", pady=10)

        change_username_password_l = ttk.Label(account_settings_links_lf, text='Change username and password',
                                               style="link.TLabel")
        change_username_password_l.pack(side="top", anchor="w")
        change_username_password_l.bind("<Button-1>", self.change_username_password_dialog)

        # ================================================ Create employee account interface ===========================
        create_account_lf = tk.LabelFrame(admin_panel_lf, bg="#FFFFFF")
        create_account_lf.pack(side="left", padx=10, pady=10, fill="y")

        create_account_label_lf = tk.LabelFrame(create_account_lf, bg="#FFFFFF", relief="flat")
        create_account_label_lf.pack(side="top", fill="x")

        ttk.Label(create_account_label_lf, text='Create employee account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(create_account_label_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        account_settings_links_lf = tk.LabelFrame(create_account_lf, bg="#FFFFFF", relief="flat")
        account_settings_links_lf.pack(side="top", anchor="nw", pady=10)

        create_employee_l = ttk.Label(account_settings_links_lf, text='Create employee account',
                                      style="link.TLabel")
        create_employee_l.pack(side="top", anchor="w")
        create_employee_l.bind("<Button-1>", self.create_employee_dialog)

        # ================================================ Employee info ============================================
        employee_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        employee_info_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(employee_info_lf, text='Employee Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(employee_info_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        # Initialize method for changing content according to admin access
        self.admin_status()

    def notif_content_interface(self):
        self.change_button_color()
        self.notif_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content.destroy_content(self.content_lf)

        # ================================================ Notif content ===============================================

        ttk.Label(self.content_lf, text='Notification', style="h2.TLabel", justify="left").pack(side="top", anchor="nw")

    # ================================================ Dialog Boxes Interface ==========================================
    def admin_access_validation_dialog(self):
        self.admin_access_top = tk.Toplevel(self.master)
        self.admin_access_top.title("Administrator access validation")
        self.admin_access_top.configure(bg="#FFFFFF")
        self.admin_access_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        admin_access_lf = tk.LabelFrame(self.admin_access_top, bg="#FFFFFF")
        admin_access_lf.pack(padx=15, pady=15, fill="both", expand=True)

        account_settings_label_lf = tk.LabelFrame(admin_access_lf, bg="#FFFFFF", relief="flat")
        account_settings_label_lf.pack(side="top", fill="x")

        ttk.Label(account_settings_label_lf, text='Admin access validation',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        forms_lf = tk.LabelFrame(admin_access_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='User Name', style="h2.TLabel").grid(column=0, row=0, sticky="w")

        self.admin_access_username_e = ttk.Entry(forms_lf, width=60)
        self.admin_access_username_e.grid(column=1, row=0, sticky="w", padx=10)
        self.admin_access_username_e.focus()

        ttk.Label(forms_lf, text='Password', style="h2.TLabel").grid(column=0, row=1, sticky="w")

        self.admin_access_password_e = ttk.Entry(forms_lf, width=60)
        self.admin_access_password_e.grid(column=1, row=1, sticky="w", padx=10)

        buttons_lf = tk.LabelFrame(admin_access_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        admin_access_validate_b = tk.Button(buttons_lf, text="Validate", font="OpenSans, 10", fg="#FFFFFF",
                                            bg="#4C8404", relief="flat",
                                            command=self.admin_access_request)
        admin_access_validate_b.pack(side="left")

        ttk.Label(buttons_lf, text="Click here to validate your\n administrative account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.admin_access_top.grab_set()

        self.admin_access_top.mainloop()

    def create_employee_dialog(self, event):
        self.create_employee_top = tk.Toplevel(self.master)
        self.create_employee_top.title("Create employee account")
        self.create_employee_top.configure(bg="#FFFFFF")
        self.create_employee_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        create_employee_lf = tk.LabelFrame(self.create_employee_top, bg="#FFFFFF")
        create_employee_lf.pack(padx=15, pady=15, fill="both", expand=True)

        account_settings_label_lf = tk.LabelFrame(create_employee_lf, bg="#FFFFFF", relief="flat")
        account_settings_label_lf.pack(side="top", fill="x")

        ttk.Label(account_settings_label_lf, text='Create employee account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(account_settings_label_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(create_employee_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Employee Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, sticky="w")

        self.employee_username_e = ttk.Entry(forms_lf, width=60)
        self.employee_username_e.grid(column=1, row=0)
        self.employee_username_e.focus()

        ttk.Label(forms_lf, text='Employee Password', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, sticky="w")

        self.employee_password_e = ttk.Entry(forms_lf, width=60)
        self.employee_password_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Role', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, sticky="w")

        self.employee_role_e = ttk.Entry(forms_lf, width=60)
        self.employee_role_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Manager, Operator', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        buttons_lf = tk.LabelFrame(create_employee_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        create_account_b = tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF",
                                     bg="#4C8404", relief="flat", command=self.create_employee_request)
        create_account_b.pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create an\n employee account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.create_employee_top.grab_set()

        self.create_employee_top.mainloop()

        print(event)

    def change_username_password_dialog(self, event):
        self.change_username_password_top = tk.Toplevel(self.master)
        self.change_username_password_top.title("Change username and password")
        self.change_username_password_top.configure(bg="#FFFFFF")
        self.change_username_password_top.resizable(False, False)

        # ================================================ Widgets for changing username and password ==============
        change_username_password_lf = tk.LabelFrame(self.change_username_password_top, bg="#FFFFFF")
        change_username_password_lf.pack(padx=15, pady=15, fill="both", expand=True)

        account_settings_label_lf = tk.LabelFrame(change_username_password_lf, bg="#FFFFFF", relief="flat")
        account_settings_label_lf.pack(side="top", fill="x")

        ttk.Label(account_settings_label_lf, text='Change username and password',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(account_settings_label_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(change_username_password_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Username', style="h2.TLabel").grid(column=0, row=0, sticky="w")

        self.change_username_e = ttk.Entry(forms_lf, width=60)
        self.change_username_e.grid(column=1, row=0, sticky="w", padx=10)
        self.change_username_e.focus()

        ttk.Label(forms_lf, text='Password', style="h2.TLabel").grid(column=0, row=1, sticky="w")

        self.change_password_e = ttk.Entry(forms_lf, width=60)
        self.change_password_e.grid(column=1, row=1, sticky="w", padx=10)
        self.change_password_e.focus()

        buttons_lf = tk.LabelFrame(change_username_password_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        continue_password_b = tk.Button(buttons_lf, text="Continue", font="OpenSans, 10", fg="#FFFFFF",
                                        bg="#4C8404", relief="flat", command=self.change_username_password_request)
        continue_password_b.pack(side="left")

        ttk.Label(buttons_lf, text="The new username and password will\n be saved on your account",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.change_username_password_top.grab_set()

        self.change_username_password_top.mainloop()

        print(event)

    def forgot_password_dialog(self, event):
        self.reset_password_top = tk.Toplevel(self.master)
        self.reset_password_top.title("Forgot Password")
        self.reset_password_top.configure(bg="#FFFFFF")
        self.reset_password_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        reset_password_lf = tk.LabelFrame(self.reset_password_top, bg="#FFFFFF")
        reset_password_lf.pack(padx=15, pady=15, fill="both", expand=True)

        account_settings_label_lf = tk.LabelFrame(reset_password_lf, bg="#FFFFFF", relief="flat")
        account_settings_label_lf.pack(side="top", fill="x")

        ttk.Label(account_settings_label_lf, text='Forgot password',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        forms_lf = tk.LabelFrame(reset_password_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Email', style="h2.TLabel").grid(column=0, row=0, sticky="w")

        self.forgot_password_email_e = ttk.Entry(forms_lf, width=60)
        self.forgot_password_email_e.grid(column=1, row=0, sticky="w", padx=10)
        self.forgot_password_email_e.focus()

        buttons_lf = tk.LabelFrame(reset_password_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        reset_password_b = tk.Button(buttons_lf, text="Reset password", font="OpenSans, 10", fg="#FFFFFF",
                                     bg="#4C8404", relief="flat", command=self.forgot_password_request)
        reset_password_b.pack(side="left")

        ttk.Label(buttons_lf, text="A new password will be generated and sent to\n"
                                   " the email that are linked to your account.",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.reset_password_top.grab_set()

        self.reset_password_top.mainloop()

        print(event)

    def bug_report_dialog(self):
        self.bug_report_top = tk.Toplevel(self.master)
        self.bug_report_top.title("Bug report")
        self.bug_report_top.configure(bg="#FFFFFF")
        self.bug_report_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        bug_report_lf = tk.LabelFrame(self.bug_report_top, bg="#FFFFFF")
        bug_report_lf.pack(padx=15, pady=15, fill="both", expand=True)

        forms_lf = tk.LabelFrame(bug_report_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Bug description', style="h2.TLabel").pack(side="top", anchor="nw")

        self.bug_description_e = ttk.Entry(forms_lf, width=60)
        self.bug_description_e.pack()
        self.bug_description_e.focus()

        buttons_lf = tk.LabelFrame(bug_report_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        report_bug_b = tk.Button(buttons_lf, text="Report", font="OpenSans, 10", fg="#FFFFFF",
                                 bg="#4C8404", relief="flat", command=self.bug_report)
        report_bug_b.pack(side="left")

        ttk.Label(buttons_lf, text="Your bug report will be sent to our developers.",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.bug_report_top.grab_set()

        self.bug_report_top.mainloop()

    def switch_exit(self):
        exit_yes_no = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
        if exit_yes_no:
            self.master.destroy()
        else:
            pass

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

    def admin_signin_request(self):
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

                self.admin_access = True

                # Instantiate create_widgets method
                self.main_interface()

            self.db1.close()
            self.mycursor.close()

    def admin_signup_request(self):
        if not self.signup_username_e.get():
            self.invalid_input()
        if not self.signup_password_e.get():
            self.invalid_input()
        if not self.signup_email_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO admin (username, password, email, date_created)"
                                      "VALUES (%s,%s,%s,%s)", (self.signup_username_e.get(),
                                                               self.signup_password_e.get(),
                                                               self.signup_email_e.get(), date_time_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                # Initialize method to move back to the login interface
                self.signin_interface()
            except Exception as e:
                self.invalid_input()
                print("Failed to connect")
                print(e)

    def admin_access_request(self):
        if not self.admin_access_username_e.get():
            self.invalid_input()
        if not self.admin_access_password_e.get():
            self.invalid_input()
        else:
            self.database_connect()
            self.mycursor.execute(
                "SELECT * FROM admin where username = '" + self.admin_access_username_e.get() + "' and password = '" +
                self.admin_access_password_e.get() + "' and admin_id = '" + str(1) + "';")
            myresult = self.mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.admin_access = True
                self.admin_access_top.destroy()

            self.db1.close()
            self.mycursor.close()

    def basic_user_signin_request(self):
        if not self.signin_username_e.get():
            self.invalid_input()
        if not self.signin_password_e.get():
            self.invalid_input()
        else:
            self.database_connect()
            self.mycursor.execute(
                "SELECT * FROM basic_user where username = '" + self.signin_username_e.get() + "' and password = '" +
                self.signin_password_e.get() + "';")
            myresult = self.mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.mycursor.execute(
                    "SELECT DISTINCT admin_id FROM basic_user where username = '" + self.signin_username_e.get() + "';")

                # Converts the tuple into integer
                admin_id = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                self.admin_id_str = str(admin_id)
                # print(self.admin_id_str)

                self.admin_access = False
                self.basic_user_access = True

                # Instantiate create_widgets method
                self.main_interface()

            self.db1.close()
            self.mycursor.close()

    def bug_report(self):
        if not self.bug_description_e.get():
            self.invalid_input()
        else:
            self.database_connect()
            self.mycursor.execute(
                "SELECT DISTINCT email FROM admin where admin_id ='" + str(self.admin_id_str) + "';")
            myresult = self.mycursor.fetchone()

            # Convert tuple into string
            admin_email = ''.join(myresult)

            self.db1.close()
            self.mycursor.close()

            email = 'pongodev0914@gmail.com'
            email_password = 'Bin@1110010010'
            send_to_email = 'pongodev0914@gmail.com'
            subject = ('Bug report from ' + admin_email)
            message = self.bug_description_e.get()

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, email_password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()

            tk.messagebox.showinfo("Bug report", "Your bug report has been sent to the developers.")

            self.bug_report_top.destroy()

    def forgot_password_request(self):
        if not self.forgot_password_email_e.get():
            self.invalid_input()
        else:
            otp = randint(10000, 99999)

            self.database_connect()
            self.mycursor.execute("UPDATE admin SET password='" + str(otp) + "' WHERE email='"
                                  + self.forgot_password_email_e.get() + "';")
            print(str(otp), self.forgot_password_email_e.get())

            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            email = 'pongodev0914@gmail.com'
            email_password = 'Bin@1110010010'
            send_to_email = self.forgot_password_email_e.get()
            subject = 'Password reset for Administrative account in Hotel Management System of DormBuilt Inc.'
            message = ("Your new password is\n\n" + str(otp))

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, email_password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()

            tk.messagebox.showinfo("Forgot password", "Please check your email at " +
                                   self.forgot_password_email_e.get() + ".")

            self.reset_password_top.destroy()

    def change_username_password_request(self):
        if not self.change_username_e.get():
            self.invalid_input()
        if not self.change_password_e.get():
            self.invalid_input()
        if not self.admin_access:
            self.admin_access_validation_dialog()
        else:
            self.database_connect()
            self.mycursor.execute("UPDATE admin SET username='" + self.change_username_e.get() + "', password='"
                                  + self.change_password_e.get() + "' WHERE admin_id='"
                                  + str(self.admin_id_str) + "';")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            self.change_username_password_top.destroy()

            self.basic_user_status()

    def create_employee_request(self):
        if not self.employee_username_e.get():
            self.invalid_input()
        if not self.employee_password_e.get():
            self.invalid_input()
        if not self.employee_role_e.get():
            self.invalid_input()
        if not self.admin_access:
            self.admin_access_validation_dialog()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO basic_user (admin_id, username, password, role, date_created)"
                                      "VALUES (%s,%s,%s,%s,%s)", (self.admin_id_str, self.employee_username_e.get(),
                                                                  self.employee_password_e.get(),
                                                                  self.employee_role_e.get(), date_time_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Employee Account is  created")

                self.create_employee_top.destroy()

                self.basic_user_status()
            except Exception as e:
                self.invalid_input()
                print(e)

    # ================================================ Content control =================================================
    def change_button_color(self):
        self.home_b.configure(fg='#7c8084')
        self.settings_b.configure(fg='#7c8084')
        self.notif_b.configure(fg='#7c8084')

    def admin_status(self):
        if self.admin_access:
            self.admin_access_status = "On"
            self.admin_access_status_l.config(text=self.admin_access_status, style="on.TLabel")
        else:
            self.admin_access_status_l.configure(style='off.TLabel')

    def basic_user_status(self):
        if self.basic_user_access:
            self.admin_access = False
        else:
            pass

    # ================================================ Static Methods ==================================================
    @staticmethod
    def invalid_input():
        messagebox.showerror("Error", "Invalid or no input.")

    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='This action is currently under development!')


if __name__ == "__main__":
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
