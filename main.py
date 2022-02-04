import functools
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from content_controller import Content_control
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
        self.create_room_top = tk.Toplevel

        # LabelFrame
        self.content_lf = None
        self.login_register_lf = None
        self.employee_info_tree_lf = None
        self.employee_info_buttons_lf = None
        self.room_info_tree_lf = None
        self.room_info_buttons_lf = None

        # Label
        self.admin_access_status_l = ttk.Label

        # PhotoImage
        self.db_logo_resized = tkinter.PhotoImage
        self.db_logo_resized_2 = tkinter.PhotoImage

        # Buttons
        self.home_b = tk.Button
        self.settings_b = tk.Button
        self.notif_b = tk.Button

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

        self.room_description_e = ttk.Entry
        self.room_type_e = ttk.Entry

        # Spinbox
        self.room_number_sp = ttk.Spinbox
        self.room_capacity_sp = ttk.Spinbox

        # ComboBox
        self.room_availability_cb = ttk.Combobox

        # Treeview
        self.employee_info_tree = ttk.Treeview
        self.room_info_tree = ttk.Treeview

        # Text
        self.bug_description_e = ttk.Entry

        # String
        self.admin_id_str = str
        self.current_user = None
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

        # Initialize class for default styles
        Content.widget_styles(self.master)

    def signin_interface(self):
        # Clean widgets in the master window
        Content_control.destroy_content(self.master)

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
        Content_control.destroy_content(self.login_register_lf)

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
        Content_control.destroy_content(self.master)

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

        logout_b = tk.Button(top_nav_lf, text="Logout", font=("Times New Roman", 15), fg='#FFFFFF', bg="#BD1E51",
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
        Content_control.destroy_content(self.content_lf)

        # ================================================ Home content ============================================
        home_panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        home_panel_lf.pack(side="top", fill="x")

        # ================================================ Room Settings ============================================
        room_dashboard_lf = tk.LabelFrame(home_panel_lf, bg="#FFFFFF")
        room_dashboard_lf.pack(side="left", padx=10, pady=10)

        room_dashboard_label_lf = tk.LabelFrame(room_dashboard_lf, bg="#FFFFFF", relief="flat")
        room_dashboard_label_lf.pack(side="top", fill="x")

        ttk.Label(room_dashboard_label_lf, text='Room Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(room_dashboard_label_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        room_dashboard_links_lf = tk.LabelFrame(room_dashboard_lf, bg="#FFFFFF", relief="flat")
        room_dashboard_links_lf.pack(side="top", anchor="nw", pady=10)

        create_room_l = ttk.Label(room_dashboard_links_lf, text='Create room', style="link.TLabel")
        create_room_l.pack(side="top", anchor="w")
        create_room_l.bind("<Button-1>", self.create_room_dialog)

        # ================================================ Room info ===============================================
        room_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        room_info_lf.pack(side="top", pady=20, fill="x")

        room_info_title_lf = tk.LabelFrame(room_info_lf, bg="#FFFFFF", relief="flat")
        room_info_title_lf.pack(side="top", fill="x")

        ttk.Label(room_info_title_lf, text='Room Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(room_info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        # ================================================ Room info content ===========================================
        room_info_content_lf = tk.LabelFrame(room_info_lf, bg="#FFFFFF", relief="flat")
        room_info_content_lf.pack(side="top", fill="x")

        self.room_info_tree_lf = tk.LabelFrame(room_info_content_lf, bg="#FFFFFF", relief="flat")
        self.room_info_tree_lf.pack(side="left", fill="both", expand=True)

        room_info_tree_scr = tk.Scrollbar(self.room_info_tree_lf)
        room_info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.room_info_tree = ttk.Treeview(self.room_info_tree_lf, style="default.Treeview",
                                           yscrollcommand=room_info_tree_scr.set)
        self.room_info_tree["columns"] = ("Room ID", "Room Number", "Description", "Type", "Availability", "Capacity")

        # Create columns
        self.room_info_tree.column("#0", width=0, stretch=False)
        self.room_info_tree.column("Room ID", anchor="center", width=80)
        self.room_info_tree.column("Room Number", anchor="center", width=80)
        self.room_info_tree.column("Description", anchor="w", width=120)
        self.room_info_tree.column("Type", anchor="w", width=120)
        self.room_info_tree.column("Availability", anchor="w", width=120)
        self.room_info_tree.column("Capacity", anchor="w", width=120)

        # Create headings
        self.room_info_tree.heading("#0", text="", anchor="w")
        self.room_info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.room_info_tree.heading("Room Number", text="Room Number", anchor="center")
        self.room_info_tree.heading("Description", text="Description", anchor="w")
        self.room_info_tree.heading("Type", text="Type", anchor="w")
        self.room_info_tree.heading("Availability", text="Availability", anchor="w")
        self.room_info_tree.heading("Capacity", text="Capacity", anchor="w")

        self.room_info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.room_info_treeview_request()

        self.room_info_buttons_lf = tk.LabelFrame(room_info_content_lf, bg="#FFFFFF", relief="flat")
        self.room_info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        ttk.Label(self.room_info_buttons_lf, text="! Click on a room to open this section",
                  style="small_info.TLabel").pack(side="top", pady=5, padx=10, anchor="nw")

        # Bind the treeview to database_view_info method
        self.room_info_tree.bind("<ButtonRelease-1>", self.room_info_section)

    def settings_content_interface(self):
        self.change_button_color()
        self.settings_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

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

        ttk.Label(description_lf, text='Current user: ',
                  style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        self.admin_access_status_l = ttk.Label(description_lf, text=self.current_user, style="on.TLabel")
        self.admin_access_status_l.grid(column=1, row=0, sticky="w")

        ttk.Label(description_lf, text='Administrative access: ',
                  style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        self.admin_access_status_l = ttk.Label(description_lf, text=self.admin_access_status)
        self.admin_access_status_l.grid(column=1, row=1, sticky="w")

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

        # ================================================ Employee info ===============================================
        employee_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        employee_info_lf.pack(side="top", pady=20, fill="x")

        employee_info_title_lf = tk.LabelFrame(employee_info_lf, bg="#FFFFFF", relief="flat")
        employee_info_title_lf.pack(side="top", fill="x")

        ttk.Label(employee_info_title_lf, text='Employee Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(employee_info_title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        self.employee_info_tree_lf = tk.LabelFrame(employee_info_lf, bg="#FFFFFF", relief="flat")
        self.employee_info_tree_lf.pack(side="top", fill="both")

        employee_info_tree_scr = tk.Scrollbar(self.employee_info_tree_lf)
        employee_info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.employee_info_tree = ttk.Treeview(self.employee_info_tree_lf, style="default.Treeview",
                                               yscrollcommand=employee_info_tree_scr.set)
        self.employee_info_tree["columns"] = ("ID", "Name", "Role")

        # Create columns
        self.employee_info_tree.column("#0", width=0, stretch=False)
        self.employee_info_tree.column("ID", anchor="center", width=80)
        self.employee_info_tree.column("Name", anchor="w", width=120)
        self.employee_info_tree.column("Role", anchor="w", width=120)

        # Create headings
        self.employee_info_tree.heading("#0", text="", anchor="w")
        self.employee_info_tree.heading("ID", text="ID", anchor="center")
        self.employee_info_tree.heading("Name", text="Name", anchor="w")
        self.employee_info_tree.heading("Role", text="Role", anchor="w")

        self.employee_info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.employee_info_treeview_request()

        self.employee_info_buttons_lf = tk.LabelFrame(self.employee_info_tree_lf, bg="#FFFFFF", relief="flat")
        self.employee_info_buttons_lf.pack(side="top", pady=5, padx=10, anchor="w")

        ttk.Label(self.employee_info_buttons_lf, text="! Click an employee account on the\n list to open this section",
                  style="small_info.TLabel").pack(side="top", pady=5, padx=10, anchor="nw")

        # Bind the treeview to database_view_info method
        self.employee_info_tree.bind("<ButtonRelease-1>", self.employee_info_section)

        # Initialize method for changing content according to admin access
        self.admin_status()

    def notif_content_interface(self):
        self.change_button_color()
        self.notif_b.configure(fg='#395A68')

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Notif content ===============================================

        ttk.Label(self.content_lf, text='Notification', style="h2.TLabel", justify="left").pack(side="top", anchor="nw")

    # ================================================ Dialog Boxes Interface ==========================================
    # System
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

    def switch_exit(self):
        exit_yes_no = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
        if exit_yes_no:
            self.master.destroy()
        else:
            pass

    # Home

    def create_room_dialog(self, event):
        self.create_room_top = tk.Toplevel(self.master)
        self.create_room_top.title("Create employee account")
        self.create_room_top.configure(bg="#FFFFFF")
        self.create_room_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        create_room_lf = tk.LabelFrame(self.create_room_top, bg="#FFFFFF")
        create_room_lf.pack(padx=15, pady=15, fill="both", expand=True)

        create_room_label_lf = tk.LabelFrame(create_room_lf, bg="#FFFFFF", relief="flat")
        create_room_label_lf.pack(side="top", fill="x")

        ttk.Label(create_room_label_lf, text='Create Room',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(create_room_label_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(create_room_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Room number', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, sticky="w")

        self.room_number_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_number_sp.grid(column=1, row=0, sticky="w")
        self.room_number_sp.focus()

        ttk.Label(forms_lf, text='Room description', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, sticky="w")

        self.room_description_e = ttk.Entry(forms_lf, width=60)
        self.room_description_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, sticky="w")

        self.room_type_e = ttk.Entry(forms_lf, width=60)
        self.room_type_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Basic, Suite', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Available', 'Fully Occupied', 'Maintenance')
        self.room_availability_cb.grid(column=1, row=4, sticky="w")

        ttk.Label(forms_lf, text='Room capacity', style="h2.TLabel",
                  justify="left").grid(column=0, row=5, sticky="w")

        self.room_capacity_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_capacity_sp.grid(column=1, row=5, sticky="w")

        buttons_lf = tk.LabelFrame(create_room_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        create_room_b = tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF",
                                  bg="#4C8404", relief="flat", command=self.create_room_request)
        create_room_b.pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create room!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.create_room_top.grab_set()

        self.create_room_top.mainloop()

        print(event)

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

        self.change_password_e = ttk.Entry(forms_lf, show="*", width=60)
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

    # Menu

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

                self.admin_access = True

                # Instantiate methods
                self.admin_get_current_user()
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
                self.basic_user_get_current_user()
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

    def create_room_request(self):
        if not self.room_number_sp.get():
            self.invalid_input()
        if not self.room_availability_cb.get():
            self.invalid_input()
        if not self.room_capacity_sp.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO room (room_number, room_description, room_type, room_availability,"
                                      " room_capacity, admin_id) VALUES (%s,%s,%s,%s,%s,%s)",
                                      (self.room_number_sp.get(), self.room_description_e.get(),
                                       self.room_type_e.get(),
                                       self.room_availability_cb.get(), self.room_capacity_sp.get(), self.admin_id_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Room is  created")

                self.create_room_top.destroy()
                self.home_content_interface()

            except Exception as e:
                self.invalid_input()
                print(e)

    def admin_get_current_user(self):
        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT username FROM admin where admin_id = '" + str(self.admin_id_str) + "';")

        # Converts the tuple into integer
        self.current_user = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

        self.db1.close()
        self.mycursor.close()

    def basic_user_get_current_user(self):
        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT username FROM basic_user where admin_id = '" + str(self.admin_id_str) + "';")

        # Converts the tuple into integer
        self.current_user = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

        self.db1.close()
        self.mycursor.close()

    def employee_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT basic_user.basic_user_id, basic_user.username, basic_user.role "
                              "FROM basic_user where admin_id = ' "
                              + str(self.admin_id_str) + "' ORDER BY basic_user.basic_user_id;")

        employees = self.mycursor.fetchall()

        # Create configure for striped rows
        self.employee_info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.employee_info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in employees:
            if count % 2 == 0:
                self.employee_info_tree.insert(parent="", index="end", iid=count, text="",
                                               values=(record[0], record[1], record[2]), tags=("oddrow",))
            else:
                self.employee_info_tree.insert(parent="", index="end", iid=count, text="",
                                               values=(record[0], record[1], record[2]), tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def room_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT room.room_id, room.room_number, room.room_description, room.room_type, "
                              "room.room_availability, room.room_capacity "
                              "FROM room where admin_id = ' "
                              + str(self.admin_id_str) + "';")

        rooms = self.mycursor.fetchall()

        # Create configure for striped rows
        self.room_info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.room_info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in rooms:
            if count % 2 == 0:
                self.room_info_tree.insert(parent="", index="end", iid=count, text="",
                                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                           tags=("oddrow",))
            else:
                self.room_info_tree.insert(parent="", index="end", iid=count, text="",
                                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                           tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def remove_employee_account_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.employee_info_tree.focus()

            # Grab record values
            values = self.employee_info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM basic_user WHERE basic_user_id = '" + values[0] +
                                  "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            tk.messagebox.showinfo("Removed account successfully")

            self.settings_content_interface()
        except Exception as e:
            self.invalid_input()
            print(e)

    def remove_room_account_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.room_info_tree.focus()

            # Grab record values
            values = self.room_info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM room WHERE room_id = '" + values[0] + "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            tk.messagebox.showinfo("Removed room successfully")

            self.home_content_interface()
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

    def employee_info_section(self, event):
        Content_control.destroy_content(self.employee_info_buttons_lf)

        ttk.Label(self.employee_info_buttons_lf, text='Employee Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        employee_info_label_lf = tk.LabelFrame(self.employee_info_buttons_lf, bg="#FFFFFF", relief="flat")
        employee_info_label_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.employee_info_tree.focus()

        # Grab record values
        values = self.employee_info_tree.item(selected, "values")

        ttk.Label(employee_info_label_lf, text='ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(employee_info_label_lf, text='Name: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(employee_info_label_lf, text='Role: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        # Buttons
        modify_employee_account_b = tk.Button(self.employee_info_buttons_lf, text="Modify", font="OpenSans, 10",
                                              fg="#FFFFFF", bg="#4C8404")
        modify_employee_account_b.pack(side="left", pady=5, padx=10, anchor="w")

        remove_employee_account_b = tk.Button(self.employee_info_buttons_lf, text="Remove", font="OpenSans, 10",
                                              fg="#FFFFFF", bg="#BD1E51", command=self.remove_employee_account_request)
        remove_employee_account_b.pack(side="left", pady=5, padx=10, anchor="w")

        print(event)

    def room_info_section(self, event):
        Content_control.destroy_content(self.room_info_buttons_lf)

        ttk.Label(self.room_info_buttons_lf, text='Room Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        room_info_label_lf = tk.LabelFrame(self.room_info_buttons_lf, bg="#FFFFFF", relief="flat")
        room_info_label_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.room_info_tree.focus()

        # Grab record values
        values = self.room_info_tree.item(selected, "values")

        ttk.Label(room_info_label_lf, text='Room Number: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(room_info_label_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        # Buttons
        room_top_button_lf = tk.LabelFrame(self.room_info_buttons_lf, bg="#FFFFFF", relief="flat")
        room_top_button_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        create_transaction_b_lf = tk.LabelFrame(room_top_button_lf, bd=1, bg="#585456", relief="flat")
        create_transaction_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(create_transaction_b_lf, text="Create transaction", font="OpenSans, 10", fg="#4C8404",
                  bg="#FFFFFF").pack(side="top", fill="x")

        room_bottom_button_lf = tk.LabelFrame(self.room_info_buttons_lf, bg="#FFFFFF", relief="flat")
        room_bottom_button_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(room_bottom_button_lf, text="Modify", font="OpenSans, 10",
                  fg="#FFFFFF", bg="#4C8404").pack(side="left", pady=5, padx=10, anchor="w")

        tk.Button(room_bottom_button_lf, text="Remove", font="OpenSans, 10", fg="#FFFFFF", bg="#BD1E51",
                  command=self.remove_room_account_request).pack(side="left", pady=5, padx=10, anchor="w")

        print(event)

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
