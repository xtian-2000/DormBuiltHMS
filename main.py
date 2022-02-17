import functools
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

# import time

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"

date_time = datetime.now()
date_time_str = date_time.strftime("%d/%m/%Y %H:%M:%S")

hms_version = "DORv1.14"


class Window:
    def __init__(self, master):
        super().__init__()

        # Window
        self.master = master

        # TopLevel Frame
        self.dialog_box_top = tk.Toplevel

        # LabelFrame
        self.content_lf = None
        self.login_register_lf = None
        self.info_content_lf = None
        self.info_tree_lf = None
        self.info_buttons_lf = None

        # Label
        self.admin_access_status_l = ttk.Label

        self.room_cost_l = ttk.Label

        # PhotoImage
        db_logo_im = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized = db_logo_im.subsample(2, 2)
        self.db_logo_resized_2 = db_logo_im.subsample(6, 6)

        hms_logo_im = PhotoImage(file=r"pongodev_hms_small_logo.png")
        self.hms_logo_im_resized = hms_logo_im.subsample(8, 8)

        signin_im = PhotoImage(file=r"signin_l.png")
        self.signin_im_resized = signin_im.subsample(1, 1)

        signup_im = PhotoImage(file=r"signup_l.png")
        self.signup_im_resized = signup_im.subsample(1, 1)

        logout_im = PhotoImage(file=r"exit_b.png")
        self.logout_im_resized = logout_im.subsample(1, 1)

        remove_im = PhotoImage(file=r"remove_b.png")
        self.remove_im_resized = remove_im.subsample(1, 1)

        copy_im = PhotoImage(file=r"copy_b.png")
        self.copy_im_resized = copy_im.subsample(1, 1)

        edit_im = PhotoImage(file=r"modify_b.png")
        self.edit_im_resized = edit_im.subsample(1, 1)

        create_im = PhotoImage(file=r"create_b.png")
        self.create_im_resized = create_im.subsample(1, 1)

        empty_im = PhotoImage(file=r"empty_l.png")
        self.empty_im_resized = empty_im.subsample(1, 1)

        add_basic_im = PhotoImage(file=r"add_basic_b.png")
        self.add_basic_im_resized = add_basic_im.subsample(1, 1)

        home_active_im = PhotoImage(file=r"home_active_b.png")
        self.home_active_im_resized = home_active_im.subsample(1, 1)

        home_inactive_im = PhotoImage(file=r"home_inactive_b.png")
        self.home_inactive_im_resized = home_inactive_im.subsample(1, 1)

        tenant_active_im = PhotoImage(file=r"tenant_active_b.png")
        self.tenant_active_im_resized = tenant_active_im.subsample(1, 1)

        tenant_inactive_im = PhotoImage(file=r"tenant_inactive_b.png")
        self.tenant_inactive_im_resized = tenant_inactive_im.subsample(1, 1)

        payment_active_im = PhotoImage(file=r"payment_active_b.png")
        self.payment_active_im_resized = payment_active_im.subsample(1, 1)

        payment_inactive_im = PhotoImage(file=r"payment_inactive_b.png")
        self.payment_inactive_im_resized = payment_inactive_im.subsample(1, 1)

        discount_active_im = PhotoImage(file=r"discount_active_b.png")
        self.discount_active_im_resized = discount_active_im.subsample(1, 1)

        discount_inactive_im = PhotoImage(file=r"discount_inactive_b.png")
        self.discount_inactive_im_resized = discount_inactive_im.subsample(1, 1)

        account_active_im = PhotoImage(file=r"account_active_b.png")
        self.account_active_im_resized = account_active_im.subsample(1, 1)

        account_inactive_im = PhotoImage(file=r"account_inactive_b.png")
        self.account_inactive_im_resized = account_inactive_im.subsample(1, 1)

        notif_active_im = PhotoImage(file=r"notif_active_b.png")
        self.notif_active_im_resized = notif_active_im.subsample(1, 1)

        notif_inactive_im = PhotoImage(file=r"notif_inactive_b.png")
        self.notif_inactive_im_resized = notif_inactive_im.subsample(1, 1)

        # Buttons
        self.home_b = tk.Button
        self.tenants_b = tk.Button
        self.payments_b = tk.Button
        self.discounts_b = tk.Button
        self.accounts_b = tk.Button
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

        self.tenant_name_e = ttk.Entry

        self.bug_description_e = ttk.Entry

        self.discount_code_e = ttk.Entry

        # Spinbox
        self.room_number_sp = ttk.Spinbox
        self.room_capacity_sp = ttk.Spinbox
        self.room_price_sp = ttk.Spinbox
        self.tenant_id_sp = ttk.Spinbox
        self.payment_amount_sp = ttk.Spinbox

        self.discount_amount_sp = ttk.Spinbox

        # ComboBox
        self.room_availability_cb = ttk.Combobox

        self.tenant_status_cb = ttk.Combobox

        self.discount_status_cb = ttk.Combobox

        # Treeview
        self.info_tree = ttk.Treeview

        # String
        self.admin_id_str = str
        self.basic_user_id_str = str
        self.current_user = None
        self.admin_access_status = None

        # Int
        self.room_id = int

        self.tenant_id = int

        self.discount_id = int

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
        logo_f.pack(side="left", padx=20, fill="both", expand=True)

        tk.Label(logo_f, image=self.db_logo_resized, bg="#FFFFFF").pack(side="top", pady=5, anchor="center")

        ttk.Label(logo_f, text='DormBuilt Inc.', style="h1.TLabel").pack(side="top", pady=5, anchor="center")

        ttk.Label(logo_f, text='Dormbuilt is a company that recognizes housing needs of the community within\n '
                               'the institution and dedicates its expertise to better serve them.',
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        tk.Label(logo_f, bg="#FFFFFF").pack(side="top", pady=20, anchor="center")

        tk.Label(logo_f, image=self.hms_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", padx=10, pady=5, anchor="center")

        ttk.Label(logo_f, text="Hotel Management System comes with a slew of capabilities, from a user-friendly \n"
                               "interface to extensive data management controls,as well as extra data visualization\n"
                               "options. Extend your business with a centralized system that takes care of the hassle\n"
                               "of data processing.",
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        # ================================================ Sign In Form Interface ======================================
        self.login_register_lf = tk.LabelFrame(top_f, bg="#FFFFFF")
        self.login_register_lf.pack(side="right", padx=40, pady=20, anchor="n")

        tk.Label(self.login_register_lf, image=self.signin_im_resized, bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(self.login_register_lf, text='Sign In', style="h1.TLabel").pack(side="top", pady=10, anchor="center")

        form_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=5, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.signin_username_e = ttk.Entry(form_f)
        self.signin_username_e.grid(column=1, row=0)

        ttk.Label(form_f, text='Password', style="h2.TLabel").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.signin_password_e = ttk.Entry(form_f, show="*")
        self.signin_password_e.grid(column=1, row=1)

        forgot_password_l = ttk.Label(form_f, text="Forgot password?", cursor="hand2", style="link.TLabel")
        forgot_password_l.grid(column=1, row=2, sticky="e")
        forgot_password_l.bind("<Button-1>", self.forgot_password_dialog)

        buttons_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both")

        tk.Button(buttons_f, text="Sign in as Administrator", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                  relief="flat", command=self.admin_signin_request).pack(side="top", pady=5, padx=10, fill="x")

        tk.Button(buttons_f, text="Sign in as Basic user", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", command=self.basic_user_signin_request).pack(side="top", pady=5, padx=10, fill="x")

        signup_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        signup_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        tk.Button(signup_b_lf, text="Sign up", font="OpenSans, 12", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.signup_interface).pack(side="top", fill="x")

        self.signin_username_e.focus()

        # ================================================ Filler Interface ===========================================
        middle_f = ttk.Frame(self.master, style="Basic.TFrame")
        middle_f.pack(side="top", fill="both", expand=True)

        # ================================================ Footer Interface ===========================================
        footer_f = ttk.Frame(self.master, style="Basic.TFrame")
        footer_f.pack(side="bottom", fill="x")

        ttk.Label(footer_f, text='Copyright © 2022 PONGODEV', style="small_info.TLabel").pack(pady=20)

    def signup_interface(self):
        # Clean widgets in the master window
        Content_control.destroy_content(self.login_register_lf)

        # ================================================ Login UI ====================================================
        tk.Label(self.login_register_lf, image=self.signup_im_resized, bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(self.login_register_lf, text='Sign Up', style="h1.TLabel").pack(side="top", pady=10, anchor="center")

        form_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        form_f.pack(side="top", ipadx=10, ipady=10, fill="both")

        ttk.Label(form_f, text='User Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.signup_username_e = ttk.Entry(form_f)
        self.signup_username_e.grid(column=1, row=0)
        self.signup_username_e.focus()

        ttk.Label(form_f, text='Password', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.signup_password_e = ttk.Entry(form_f, show="*")
        self.signup_password_e.grid(column=1, row=1)

        ttk.Label(form_f, text='Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.signup_email_e = ttk.Entry(form_f)
        self.signup_email_e.grid(column=1, row=2)

        buttons_f = ttk.Frame(self.login_register_lf, style="Basic.TFrame")
        buttons_f.pack(side="top", fill="both", ipady=20)

        tk.Button(buttons_f, text="Sign up as Administrator", font="OpenSans, 12", fg="#FFFFFF", bg="#4C8404",
                  relief="flat", command=self.admin_signup_request).pack(side="top", pady=5, padx=10, fill="x")

        cancel_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        cancel_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        tk.Button(cancel_b_lf, text="Go back", font="OpenSans, 12", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.signin_interface).pack(fill="x")

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

        ttk.Label(top_nav_lf, image=self.db_logo_resized_2).pack(side="left", pady=5)

        ttk.Label(top_nav_lf, text='DormBuilt Inc. | Hotel Management System ',
                  style="h2.TLabel", justify="left").pack(side="left")

        tk.Button(top_nav_lf, text="Logout", font=("Times New Roman", 15), fg='#FFFFFF', bg="#BD1E51", relief="flat",
                  image=self.logout_im_resized, compound="left",
                  command=self.signin_interface).pack(side="right", padx=20)

        # ================================================ Left-Nav widgets ============================================
        left_nav_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        left_nav_lf.pack(side="left", fill="both")

        self.home_b = tk.Button(left_nav_lf, text=" Home", font=("OpenSans", 15), fg='#395A68',
                                bg="#FFFFFF", relief="flat", image=self.home_active_im_resized, compound="left",
                                command=self.home_content_interface)
        self.home_b.pack(side="top", anchor="w")

        self.tenants_b = tk.Button(left_nav_lf, text=" Tenants", font=("OpenSans", 15), fg='#7c8084',
                                   bg="#FFFFFF", relief="flat", image=self.tenant_inactive_im_resized, compound="left",
                                   command=self.tenant_content_interface)
        self.tenants_b.pack(side="top", anchor="w")

        self.payments_b = tk.Button(left_nav_lf, text=" Payments", font=("OpenSans", 15), fg='#7c8084',
                                    bg="#FFFFFF", relief="flat", image=self.payment_inactive_im_resized,
                                    compound="left", command=self.payment_content_interface)
        self.payments_b.pack(side="top", anchor="w")

        self.discounts_b = tk.Button(left_nav_lf, text=" Discounts", font=("OpenSans", 15), fg='#7c8084',
                                     bg="#FFFFFF", relief="flat", image=self.discount_inactive_im_resized,
                                     compound="left", command=self.discount_content_interface)
        self.discounts_b.pack(side="top", anchor="w")

        self.accounts_b = tk.Button(left_nav_lf, text=" Accounts", font=("OpenSans", 15), fg='#7c8084',
                                    bg="#FFFFFF", relief="flat", image=self.account_inactive_im_resized,
                                    compound="left", command=self.account_settings_content_interface)
        self.accounts_b.pack(side="top", anchor="w")

        self.notif_b = tk.Button(left_nav_lf, text=" Notifications", font=("OpenSans", 15), fg='#7c8084',
                                 bg="#FFFFFF", relief="flat", image=self.notif_inactive_im_resized,
                                 compound="left", command=self.notif_content_interface)
        self.notif_b.pack(side="top", anchor="w")

        ttk.Label(left_nav_lf, text=hms_version, style="small_info.TLabel").pack(side="bottom", pady=20)

        # ================================================ Left-Nav widgets ============================================
        self.content_lf = tk.LabelFrame(self.master, bg="#FFFFFF")
        self.content_lf.pack(side="left", fill="both", expand=True)

        # Initialize home_content_interface method
        self.home_content_interface()

    def home_content_interface(self):
        self.change_button_color()
        self.home_b.configure(fg='#395A68', image=self.home_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Home content ============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Room Settings ============================================
        room_dashboard_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
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

        set_room_price_to_type_l = ttk.Label(room_dashboard_links_lf, text='Set room price according to room type',
                                             style="link.TLabel")
        set_room_price_to_type_l.pack(side="top", anchor="w")
        set_room_price_to_type_l.bind("<Button-1>", self.set_room_price_to_type_dialog)

        # ================================================ Room info ===============================================
        room_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        room_info_lf.pack(side="top", pady=20, fill="x")

        room_info_title_lf = tk.LabelFrame(room_info_lf, bg="#FFFFFF", relief="flat")
        room_info_title_lf.pack(side="top", fill="x")

        ttk.Label(room_info_title_lf, text='Room Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(room_info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(room_info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_room_information_module).pack(fill="x")

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(room_info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_room_information_module).pack(side="top", fill="x")

    def tenant_content_interface(self):
        self.change_button_color()
        self.tenants_b.configure(fg='#395A68', image=self.tenant_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Home content ============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Room Settings ============================================
        tenant_dashboard_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
        tenant_dashboard_lf.pack(side="left", padx=10, pady=10)

        tenant_dashboard_label_lf = tk.LabelFrame(tenant_dashboard_lf, bg="#FFFFFF", relief="flat")
        tenant_dashboard_label_lf.pack(side="top", fill="x")

        ttk.Label(tenant_dashboard_label_lf, text='Tenants Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(tenant_dashboard_label_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        tenant_dashboard_links_lf = tk.LabelFrame(tenant_dashboard_lf, bg="#FFFFFF", relief="flat")
        tenant_dashboard_links_lf.pack(side="top", anchor="nw", pady=10)

        create_tenant_l = ttk.Label(tenant_dashboard_links_lf, text='Create a tenant account', style="link.TLabel")
        create_tenant_l.pack(side="top", anchor="w")
        create_tenant_l.bind("<Button-1>", self.create_tenant_account_dialog)

        # ================================================ Tenant info ===============================================
        tenant_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        tenant_info_lf.pack(side="top", pady=20, fill="x")

        tenant_info_title_lf = tk.LabelFrame(tenant_info_lf, bg="#FFFFFF", relief="flat")
        tenant_info_title_lf.pack(side="top", fill="x")

        ttk.Label(tenant_info_title_lf, text='Tenant Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(tenant_info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(tenant_info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_tenant_information_module).pack(fill="x")

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(tenant_info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_tenant_information_module).pack(side="top", fill="x")

    def payment_content_interface(self):
        self.change_button_color()
        self.payments_b.configure(fg='#395A68', image=self.payment_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Home content ============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Room Settings ============================================
        payment_dashboard_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
        payment_dashboard_lf.pack(side="left", padx=10, pady=10)

        payment_dashboard_label_lf = tk.LabelFrame(payment_dashboard_lf, bg="#FFFFFF", relief="flat")
        payment_dashboard_label_lf.pack(side="top", fill="x")

        ttk.Label(payment_dashboard_label_lf, text='Payments Settings',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(payment_dashboard_label_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        # ================================================ Tenant info ===============================================
        payment_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        payment_info_lf.pack(side="top", pady=20, fill="x")

        payment_info_title_lf = tk.LabelFrame(payment_info_lf, bg="#FFFFFF", relief="flat")
        payment_info_title_lf.pack(side="top", fill="x")

        ttk.Label(payment_info_title_lf, text='Payment Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(payment_info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(payment_info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat").pack(fill="x")

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(payment_info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_tenant_information_module).pack(side="top", fill="x")

    def discount_content_interface(self):
        self.change_button_color()
        self.discounts_b.configure(fg='#395A68', image=self.discount_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Home content ============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Discount Dashboard ==========================================
        discount_dashboard_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
        discount_dashboard_lf.pack(side="left", padx=10, pady=10)

        discount_dashboard_label_lf = tk.LabelFrame(discount_dashboard_lf, bg="#FFFFFF", relief="flat")
        discount_dashboard_label_lf.pack(side="top", fill="x")

        ttk.Label(discount_dashboard_label_lf, text='Discount Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(discount_dashboard_label_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        discount_dashboard_links_lf = tk.LabelFrame(discount_dashboard_lf, bg="#FFFFFF", relief="flat")
        discount_dashboard_links_lf.pack(side="top", anchor="nw", pady=10)

        create_discount_l = ttk.Label(discount_dashboard_links_lf, text='Create discount code', style="link.TLabel")
        create_discount_l.pack(side="top", anchor="w")
        create_discount_l.bind("<Button-1>", self.create_discount_dialog)

        # ================================================ Tenant info ===============================================
        discount_info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        discount_info_lf.pack(side="top", pady=20, fill="x")

        discount_info_title_lf = tk.LabelFrame(discount_info_lf, bg="#FFFFFF", relief="flat")
        discount_info_title_lf.pack(side="top", fill="x")

        ttk.Label(discount_info_title_lf, text='Discount Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(discount_info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(discount_info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_discount_information_module).pack(fill="x")

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(discount_info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_discount_information_module).pack(side="top", fill="x")

    def account_settings_content_interface(self):
        self.change_button_color()
        self.accounts_b.configure(fg='#395A68', image=self.account_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        self.admin_access_status = "Off"

        # ================================================ Settings content ============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Account Settings ============================================
        account_settings_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
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
        create_account_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
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

        self.info_tree_lf = tk.LabelFrame(employee_info_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="top", fill="both")

        tk.Button(self.info_tree_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#4C8404", relief="flat", command=self.show_employee_information_module).pack(side="top", fill="x")

        # Initialize method for changing content according to admin access
        self.admin_status()

    def notif_content_interface(self):
        self.change_button_color()
        self.notif_b.configure(fg='#395A68', image=self.notif_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Notif content ===============================================
        panel_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        panel_lf.pack(side="top", fill="x")

        # ================================================ Notif Dashboard =============================================
        notif_dashboard_lf = tk.LabelFrame(panel_lf, bg="#FFFFFF")
        notif_dashboard_lf.pack(side="left", padx=10, pady=10)

        notif_dashboard_title_lf = tk.LabelFrame(notif_dashboard_lf, bg="#FFFFFF", relief="flat")
        notif_dashboard_title_lf.pack(side="top", fill="x")

        ttk.Label(notif_dashboard_title_lf, text='Notification Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(notif_dashboard_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

    # ================================================ Modularized Interface ===========================================

    # Home
    def show_room_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview",
                                      yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Room ID", "Room Number", "Description", "Type", "Availability", "Capacity",
                                     "Price", "Current Occupants")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Room ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Room Number", anchor="center", width=80)
        self.info_tree.column("Description", anchor="w", width=120)
        self.info_tree.column("Type", anchor="w", width=120)
        self.info_tree.column("Availability", anchor="w", width=120)
        self.info_tree.column("Capacity", anchor="w", width=120)
        self.info_tree.column("Price", anchor="center", width=80)
        self.info_tree.column("Current Occupants", anchor="center", width=80)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.info_tree.heading("Room Number", text="Room Number", anchor="center")
        self.info_tree.heading("Description", text="Description", anchor="w")
        self.info_tree.heading("Type", text="Type", anchor="w")
        self.info_tree.heading("Availability", text="Availability", anchor="w")
        self.info_tree.heading("Capacity", text="Capacity", anchor="w")
        self.info_tree.heading("Price", text="Price", anchor="center")
        self.info_tree.heading("Current Occupants", text="Current Occupants", anchor="center")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.room_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on a room to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.room_info_section)

    # Tenant
    def show_tenant_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Tenant ID", "Tenant Name", "Status", "Balance", "Date created")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Tenant ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Tenant Name", anchor="w", width=120)
        self.info_tree.column("Status", anchor="center", width=120)
        self.info_tree.column("Balance", anchor="w", width=60)
        self.info_tree.column("Date created", anchor="center", width=0, stretch=False)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Tenant ID", text="Tenant ID", anchor="center")
        self.info_tree.heading("Tenant Name", text="Tenant Name", anchor="w")
        self.info_tree.heading("Status", text="Status", anchor="center")
        self.info_tree.heading("Balance", text="Balance", anchor="w")
        self.info_tree.heading("Date created", text="Date created", anchor="center")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.tenant_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on an account to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.tenant_info_section)

    # Discount
    def show_discount_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview",
                                      yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Discount ID", "Discount Code", "Discount Amount", "Discount Status",
                                     "Date created")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Discount ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Discount Code", anchor="w", width=80)
        self.info_tree.column("Discount Amount", anchor="center", width=80)
        self.info_tree.column("Discount Status", anchor="center", width=80)
        self.info_tree.column("Date created", width=0, stretch=False)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Discount ID", text="Discount ID", anchor="center")
        self.info_tree.heading("Discount Code", text="Discount Code", anchor="w")
        self.info_tree.heading("Discount Amount", text="Discount Amount (%)", anchor="center")
        self.info_tree.heading("Discount Status", text="Discount Status", anchor="center")
        self.info_tree.heading("Date created", text="Date created", anchor="w")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.discount_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on a discount to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.discount_info_section)

    # Accounts
    def show_employee_information_module(self):
        Content_control.destroy_content(self.info_tree_lf)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview",
                                      yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("ID", "Name", "Role")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("ID", anchor="center", width=80)
        self.info_tree.column("Name", anchor="w", width=120)
        self.info_tree.column("Role", anchor="w", width=120)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("ID", text="ID", anchor="center")
        self.info_tree.heading("Name", text="Name", anchor="w")
        self.info_tree.heading("Role", text="Role", anchor="w")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.employee_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_tree_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="top", pady=5, padx=10, anchor="w")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on an account to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")
        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.employee_info_section)

    # ================================================ Dialog Boxes Interface ==========================================

    # Sign in
    def forgot_password_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Forgot Password")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Forgot password',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Email', style="h2.TLabel").grid(column=0, row=0, sticky="w")

        self.forgot_password_email_e = ttk.Entry(forms_lf, width=60)
        self.forgot_password_email_e.grid(column=1, row=0, sticky="w", padx=10)
        self.forgot_password_email_e.focus()

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Reset password", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.forgot_password_request).pack(side="left")

        ttk.Label(buttons_lf, text="A new password will be generated and sent to\n"
                                   " the email that are linked to your account.",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    # Home
    def create_room_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create room")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create Room',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Room number', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.room_number_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_number_sp.grid(column=1, row=0, sticky="w")
        self.room_number_sp.focus()

        ttk.Label(forms_lf, text='Room description', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_description_e = ttk.Entry(forms_lf, width=60)
        self.room_description_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, padx=2.5, pady=2.5, row=2, sticky="w")

        self.room_type_e = ttk.Entry(forms_lf, width=60)
        self.room_type_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Basic, Suite', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Available', 'Fully Occupied', 'Maintenance')
        self.room_availability_cb.grid(column=1, row=4, sticky="w")

        ttk.Label(forms_lf, text='Room capacity', style="h2.TLabel",
                  justify="left").grid(column=0, row=5, padx=2.5, pady=2.5, sticky="w")

        self.room_capacity_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_capacity_sp.grid(column=1, row=5, sticky="w")

        ttk.Label(forms_lf, text='Room price', style="h2.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, pady=2.5, sticky="w")

        self.room_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.room_price_sp.grid(column=1, row=6, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=7, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", image=self.add_basic_im_resized, compound="left",
                  command=self.create_room_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create room!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def modify_room_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Modify room")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Modify room information',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Room number', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.room_number_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_number_sp.grid(column=1, row=0, sticky="w")
        self.room_number_sp.focus()

        ttk.Label(forms_lf, text='Room description', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_description_e = ttk.Entry(forms_lf, width=60)
        self.room_description_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.room_type_e = ttk.Entry(forms_lf, width=60)
        self.room_type_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Basic, Suite', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Available', 'Fully Occupied', 'Maintenance')
        self.room_availability_cb.grid(column=1, row=4, sticky="w")

        ttk.Label(forms_lf, text='Room capacity', style="h2.TLabel",
                  justify="left").grid(column=0, row=5, padx=2.5, pady=2.5, sticky="w")

        self.room_capacity_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_capacity_sp.grid(column=1, row=5, sticky="w")

        ttk.Label(forms_lf, text='Room price', style="h2.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, pady=2.5, sticky="w")

        self.room_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.room_price_sp.grid(column=1, row=6, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=7, sticky="w")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # Insert values to entry widgets
        self.room_number_sp.insert(0, values[1])
        self.room_description_e.insert(0, values[2])
        self.room_type_e.insert(0, values[3])
        self.room_availability_cb.insert(0, values[4])
        self.room_capacity_sp.insert(0, values[5])
        self.room_price_sp.insert(0, values[6])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.modify_room_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to modify room information!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def copy_and_create_room_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Copy info and create new room")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Copy info and create new room',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Room number', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.room_number_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_number_sp.grid(column=1, row=0, sticky="w")
        self.room_number_sp.focus()

        ttk.Label(forms_lf, text='Room description', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_description_e = ttk.Entry(forms_lf, width=60)
        self.room_description_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.room_type_e = ttk.Entry(forms_lf, width=60)
        self.room_type_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Basic, Suite', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Available', 'Fully Occupied', 'Maintenance')
        self.room_availability_cb.grid(column=1, row=4, sticky="w")

        ttk.Label(forms_lf, text='Room capacity', style="h2.TLabel",
                  justify="left").grid(column=0, row=5, padx=2.5, pady=2.5, sticky="w")

        self.room_capacity_sp = ttk.Spinbox(forms_lf, from_=0, to=30, wrap=True)
        self.room_capacity_sp.grid(column=1, row=5, sticky="w")

        ttk.Label(forms_lf, text='Room price', style="h2.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, pady=2.5, sticky="w")

        self.room_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.room_price_sp.grid(column=1, row=6, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=7, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.room_id = values[0]

        # Insert values to entry widgets
        self.room_description_e.insert(0, values[2])
        self.room_type_e.insert(0, values[3])
        self.room_availability_cb.insert(0, values[4])
        self.room_capacity_sp.insert(0, values[5])
        self.room_price_sp.insert(0, values[6])

        # Disable widgets
        self.room_description_e.config(state="disabled")
        self.room_type_e.config(state="disabled")
        self.room_availability_cb.config(state="disabled")
        self.room_capacity_sp.config(state="disabled")
        self.room_price_sp.config(state="disabled")

        tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404",
                  relief="flat", command=self.create_room_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create new room \nfrom derived information!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def set_room_price_to_type_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Set room prices")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Set room price',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", pady=10, fill="both", expand=True)

        ttk.Label(forms_lf, text='Room price', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.room_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.room_price_sp.grid(column=1, row=0, padx=2.5, pady=2.5, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=2, row=0, sticky="w")

        ttk.Label(forms_lf, text='Room Type', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_type_e = ttk.Entry(forms_lf, width=40)
        self.room_type_e.grid(column=1, row=1, columnspan=2)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Set price", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.set_room_price_to_type_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to set the room price \naccording to room type!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def create_transaction_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create transaction")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create transaction',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms1_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms1_lf.pack(side="top", fill="both", pady=15, expand=True)

        ttk.Label(forms1_lf, text='Payment Information',
                  style="on.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(forms1_lf, text='Room cost', style="small_info.TLabel",
                  justify="left").grid(column=0, row=1, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=values[6], style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=1, sticky="w")

        ttk.Label(forms1_lf, text='Discount Code', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, sticky="w")

        self.discount_code_e = ttk.Entry(forms1_lf, width=30)
        self.discount_code_e.grid(column=1, row=2)

        apply_b_lf = tk.LabelFrame(forms1_lf, bd=1, bg="#585456", relief="flat")
        apply_b_lf.grid(column=2, row=2, padx=10)

        tk.Button(apply_b_lf, text="Apply", font="OpenSans, 10", fg="#4C8404", bg="#FFFFFF",
                  relief="flat", command=self.apply_discount_request).pack(fill="x")

        forms2_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms2_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms2_lf, text='Tenant ID', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_id_sp = ttk.Spinbox(forms2_lf, from_=0, to=99999, wrap=True)
        self.tenant_id_sp.grid(column=1, row=0, sticky="w")
        self.tenant_id_sp.focus()

        ttk.Label(forms2_lf, text='Payment Amount', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.payment_amount_sp = ttk.Spinbox(forms2_lf, from_=0, to=99999, wrap=True)
        self.payment_amount_sp.grid(column=1, row=1, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.create_transaction_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create transaction!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # Tenant
    def create_tenant_account_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create tenant account")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create tenant account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Tenant Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_name_e = ttk.Entry(forms_lf, width=60)
        self.tenant_name_e.grid(column=1, row=0)
        self.tenant_name_e.focus()

        ttk.Label(forms_lf, text='Tenant Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.tenant_status_cb = ttk.Combobox(forms_lf)
        self.tenant_status_cb['values'] = ('Active', 'Inactive')
        self.tenant_status_cb.current(1)
        self.tenant_status_cb.grid(column=1, row=1, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Create account", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.create_tenant_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create a tenant account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()
        print(event)

    def modify_tenant_account_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Modify tenant account")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Modify tenant account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Tenant Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_name_e = ttk.Entry(forms_lf, width=60)
        self.tenant_name_e.grid(column=1, row=0)
        self.tenant_name_e.focus()

        ttk.Label(forms_lf, text='Tenant Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.tenant_status_cb = ttk.Combobox(forms_lf)
        self.tenant_status_cb['values'] = ('Active', 'Inactive')
        self.tenant_status_cb.current(1)
        self.tenant_status_cb.grid(column=1, row=1, sticky="w")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # Insert values to entry widgets
        self.tenant_name_e.insert(0, values[1])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.modify_tenant_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to modify tenant account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # Discount
    def create_discount_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create discount")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create discount',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Discount Code', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.discount_code_e = ttk.Entry(forms_lf, width=30)
        self.discount_code_e.grid(column=1, row=0)
        self.discount_code_e.focus()

        ttk.Label(forms_lf, text="Ex: BASIC10, SUITE10",
                  style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(forms_lf, text='Discount Amount', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.discount_amount_sp = ttk.Spinbox(forms_lf, from_=0, to=100, wrap=True)
        self.discount_amount_sp.grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text="in percentage",
                  style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Discount Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.discount_status_cb = ttk.Combobox(forms_lf)
        self.discount_status_cb['values'] = ('Active', 'Inactive')
        self.discount_status_cb.current(0)
        self.discount_status_cb.grid(column=1, row=4, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.create_discount_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create discount!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()
        print(event)

    def modify_discount_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Modify discount")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Modify discount',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Discount Code', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.discount_code_e = ttk.Entry(forms_lf, width=30)
        self.discount_code_e.grid(column=1, row=0)
        self.discount_code_e.focus()

        ttk.Label(forms_lf, text="Ex: BASIC10, SUITE10",
                  style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(forms_lf, text='Discount Amount', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.discount_amount_sp = ttk.Spinbox(forms_lf, from_=0, to=100, wrap=True)
        self.discount_amount_sp.grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text="in percentage",
                  style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Discount Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.discount_status_cb = ttk.Combobox(forms_lf)
        self.discount_status_cb['values'] = ('Active', 'Inactive')
        self.discount_status_cb.grid(column=1, row=4, sticky="w")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # Insert values to entry widgets
        self.discount_code_e.insert(0, values[1])
        self.discount_amount_sp.insert(0, values[2])
        self.discount_status_cb.insert(0, values[3])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.modify_discount_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to modify discount!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # Accounts
    def change_username_password_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Change username and password")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for changing username and password ==============
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Change username and password',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Username', style="h2.TLabel").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.change_username_e = ttk.Entry(forms_lf, width=60)
        self.change_username_e.grid(column=1, row=0, sticky="w", padx=10)
        self.change_username_e.focus()

        ttk.Label(forms_lf, text='Password', style="h2.TLabel").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.change_password_e = ttk.Entry(forms_lf, show="*", width=60)
        self.change_password_e.grid(column=1, row=1, sticky="w", padx=10)
        self.change_password_e.focus()

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Continue", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.change_username_password_request).pack(side="left")

        ttk.Label(buttons_lf, text="The new username and password will\n be saved on your account",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def create_employee_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create employee account")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create employee account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Employee Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.employee_username_e = ttk.Entry(forms_lf, width=60)
        self.employee_username_e.grid(column=1, row=0)
        self.employee_username_e.focus()

        ttk.Label(forms_lf, text='Employee Password', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.employee_password_e = ttk.Entry(forms_lf, width=60)
        self.employee_password_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text='Role', style="h2.TLabel",
                  justify="left").grid(column=0, row=2, padx=2.5, pady=2.5, sticky="w")

        self.employee_role_e = ttk.Entry(forms_lf, width=60)
        self.employee_role_e.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Manager, Operator', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.create_employee_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create an\n employee account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    # Menu
    def bug_report_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Bug report")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Report a bug',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Bug description', style="h2.TLabel").pack(side="top", padx=2.5, pady=2.5, anchor="nw")

        self.bug_description_e = ttk.Entry(forms_lf, width=60)
        self.bug_description_e.pack()
        self.bug_description_e.focus()

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Report", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.bug_report).pack(side="left")

        ttk.Label(buttons_lf, text="Your bug report will be sent to our developers.",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def switch_exit(self):
        exit_yes_no = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
        if exit_yes_no:
            self.master.destroy()
        else:
            pass

    # System
    def admin_access_validation_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Administrator access validation")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==============================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Admin access validation',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='User Name', style="h2.TLabel").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.admin_access_username_e = ttk.Entry(forms_lf, width=60)
        self.admin_access_username_e.grid(column=1, row=0, sticky="w", padx=10)
        self.admin_access_username_e.focus()

        ttk.Label(forms_lf, text='Password', style="h2.TLabel").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.admin_access_password_e = ttk.Entry(forms_lf, width=60)
        self.admin_access_password_e.grid(column=1, row=1, sticky="w", padx=10)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Validate", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  command=self.admin_access_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to validate your\n administrative account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # ================================================ Database Control ================================================

    # Sign In
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
                tk.messagebox.showerror("Error", "Invalid User Name And Password")
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

    def admin_get_current_user(self):
        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT username FROM admin where admin_id = '" + str(self.admin_id_str) + "';")

        # Converts the tuple into integer
        self.current_user = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

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
                tk.messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.mycursor.execute(
                    "SELECT DISTINCT admin_id FROM basic_user where username = '" + self.signin_username_e.get() + "';")

                # Converts the tuple into integer
                admin_id = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                self.admin_id_str = str(admin_id)

                self.admin_access = False
                self.basic_user_access = True

                # Instantiate create_widgets method
                self.basic_user_get_id_request()
                self.basic_user_get_current_user()
                self.main_interface()

            self.db1.close()
            self.mycursor.close()

    def basic_user_get_id_request(self):
        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT basic_user_id FROM basic_user where username = '" + self.signin_username_e.get() + "';")

        # Converts the tuple into integer
        basic_user_id = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
        self.basic_user_id_str = str(basic_user_id)

        print(self.basic_user_id_str)

        self.db1.close()
        self.mycursor.close()

    def basic_user_get_current_user(self):
        self.database_connect()
        """
        self.mycursor.execute(
            "SELECT DISTINCT username FROM basic_user where admin_id = '" + str(self.admin_id_str) + "';")
            """
        self.mycursor.execute(
            "SELECT DISTINCT username FROM basic_user where basic_user_id = '" + str(self.basic_user_id_str) + "';")

        # Converts the tuple into integer
        self.current_user = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

        self.db1.close()
        self.mycursor.close()

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

            self.dialog_box_top.destroy()

    # Sign Up

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

    # Home
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
                                      " room_capacity, admin_id, room_price) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                      (self.room_number_sp.get(), self.room_description_e.get(),
                                       self.room_type_e.get(),
                                       self.room_availability_cb.get(), self.room_capacity_sp.get(), self.admin_id_str,
                                       self.room_price_sp.get()))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Room is  created")

                self.dialog_box_top.destroy()
                self.show_room_information_module()

            except Exception as e:
                self.invalid_input()
                print(e)

    def modify_room_request(self):
        if not self.room_number_sp.get():
            self.invalid_input()
        if not self.room_availability_cb.get():
            self.invalid_input()
        if not self.room_capacity_sp.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("UPDATE room SET room_number = '"
                                      + self.room_number_sp.get() + "', room_description = '"
                                      + self.room_description_e.get() + "', room_type = '"
                                      + self.room_type_e.get() + "', room_availability = '"
                                      + self.room_availability_cb.get() + "', room_capacity = '"
                                      + self.room_capacity_sp.get() + "', room_price = '"
                                      + self.room_price_sp.get() + "' WHERE room_id = '"
                                      + self.room_id + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Room information is modified")

                self.dialog_box_top.destroy()
                self.show_room_information_module()

            except Exception as e:
                self.invalid_input()
                print(e)

    def room_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT room.room_id, room.room_number, room.room_description, room.room_type, "
                              "room.room_availability, room.room_capacity, room.room_price, room.current_occupants "
                              "FROM room where admin_id = ' "
                              + str(self.admin_id_str) + "';")

        rooms = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in rooms:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def set_room_price_to_type_request(self):
        if not self.room_price_sp.get():
            self.invalid_input()
        if not self.room_type_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE room SET room_price='" + self.room_price_sp.get() + "' WHERE admin_id='" +
                                      str(self.admin_id_str) + "' and room_type='" + self.room_type_e.get() + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Removed room successfully")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def apply_discount_request(self):
        if not self.discount_code_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute(
                    "SELECT * FROM discount where discount_code = '" + self.discount_code_e.get() +
                    "' and admin_id = '" + str(self.admin_id_str) + "';")
                myresult = self.mycursor.fetchone()
                if myresult is None:
                    tk.messagebox.showerror("Error", "Invalid Discount Code")
                else:
                    self.mycursor.execute(
                        "SELECT DISTINCT discount_amount FROM discount where discount_code = '"
                        + self.discount_code_e.get() + "' and admin_id = '" + str(self.admin_id_str) + "';")

                    # Converts the tuple into integer
                    discount_amount = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                    discounted_price = (int(self.room_cost_l.cget("text")) - (int(self.room_cost_l.cget("text")) *
                                                                              discount_amount / 100))
                    print(discounted_price)
                    self.room_cost_l.config(text=discounted_price)

                self.db1.close()
                self.mycursor.close()
            except Exception as e:
                self.invalid_request()
                print(e)

    def create_transaction_request(self):
        if not self.tenant_id_sp.get():
            self.invalid_input()
        if not self.payment_amount_sp.get():
            self.invalid_input()
        else:
            try:
                # remaining_balance = (int(self.room_cost_l.cget("text")) - int(self.payment_amount_sp.get()))

                self.database_connect()
                self.mycursor.execute("INSERT INTO payment (payment_amount, room_id, tenant_id, admin_id, "
                                      "basic_user_id, date_created, discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), str(self.room_id),
                                       self.tenant_id_sp.get(),
                                       str(self.admin_id_str), str(self.basic_user_id_str), str(date_time_str),
                                       self.discount_code_e.get()))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                # self.room_add_occupant()

                messagebox.showinfo("Success", "Transaction is  created")

                self.dialog_box_top.destroy()
                self.show_room_information_module()

            except Exception as e:
                self.invalid_request()
                print(e)

    def room_add_occupant(self):
        remaining_balance = (int(self.room_cost_l.cget("text")) - int(self.payment_amount_sp.get()))

        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT current_occupants FROM room where room_id = '"
            + self.room_id + "';")

        # Converts the tuple into integer
        current_occupants_int = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
        current_occupants = current_occupants_int + 1

        self.mycursor.execute("UPDATE room SET current_occupants = '" + current_occupants + "';")

        self.db1.commit()
        self.db1.close()
        self.mycursor.close()
        print(remaining_balance)

    def remove_room_account_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM room WHERE room_id = '" + values[0] + "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Removed room successfully")

            self.home_content_interface()
        except Exception as e:
            self.invalid_input()
            print(e)

    # Tenant
    def create_tenant_request(self):
        if not self.tenant_name_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO tenant (tenant_name, tenant_status, date_created, admin_id) "
                                      "VALUES (%s,%s,%s,%s)",
                                      (self.tenant_name_e.get(), self.tenant_status_cb.get(), date_time_str,
                                       self.admin_id_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Tenant's account is created")

                self.dialog_box_top.destroy()
                self.tenant_content_interface()

            except Exception as e:
                self.invalid_input()
                print(e)

    def modify_tenant_request(self):
        if not self.tenant_name_e.get():
            self.invalid_input()
        if not self.tenant_status_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("UPDATE tenant SET tenant_name = '"
                                      + self.tenant_name_e.get() + "', tenant_status = '"
                                      + self.tenant_status_cb.get() + "'  WHERE tenant_id = '"
                                      + self.tenant_id + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Tenant information is modified successfully")

                self.dialog_box_top.destroy()
                self.show_tenant_information_module()

            except Exception as e:
                self.invalid_input()
                print(e)

    def remove_tenant_account_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM tenant WHERE tenant_id = '" + values[0] + "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Removed tenant account successfully")

            self.tenant_content_interface()
        except Exception as e:
            messagebox.showinfo("Error", "Unsuccessful in removing account")
            print(e)

    def tenant_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT tenant.tenant_id, tenant.tenant_name, tenant.tenant_status, "
                              "tenant.tenant_balance, tenant.date_created FROM tenant where admin_id = ' "
                              + str(self.admin_id_str) + "';")

        tenants = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in tenants:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    # Discount
    def create_discount_request(self):
        if not self.discount_code_e.get():
            self.invalid_input()
        if not self.discount_amount_sp.get():
            self.invalid_input()
        if not self.discount_status_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO discount (discount_code, discount_amount, admin_id,"
                                      " basic_user_id, date_created, discount_status) VALUES (%s,%s,%s,%s,%s,%s)",
                                      (self.discount_code_e.get(), self.discount_amount_sp.get(),
                                       str(self.admin_id_str), str(self.basic_user_id_str), date_time_str,
                                       self.discount_status_cb.get()))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Discount code is  created")

                self.dialog_box_top.destroy()
                self.show_discount_information_module()

            except Exception as e:
                self.invalid_request()
                print(e)

    def modify_discount_request(self):
        if not self.discount_code_e.get():
            self.invalid_input()
        if not self.discount_amount_sp.get():
            self.invalid_input()
        if not self.discount_status_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("UPDATE discount SET discount_code = '"
                                      + self.discount_code_e.get() + "', discount_amount = '"
                                      + self.discount_amount_sp.get() + "', discount_status = '"
                                      + self.discount_status_cb.get() + "'  WHERE discount_id = '"
                                      + self.discount_id + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Discount information is modified successfully")

                self.dialog_box_top.destroy()
                self.show_discount_information_module()

            except Exception as e:
                self.invalid_request()
                print(e)

    def discount_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT discount.discount_id, discount.discount_code, discount.discount_amount, "
                              "discount.discount_status, discount.date_created FROM discount where admin_id = ' "
                              + str(self.admin_id_str) + "';")

        discount = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in discount:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def remove_discount_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM discount WHERE discount_id = '" + values[0] + "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Removed discount successfully")

            self.discount_content_interface()
        except Exception as e:
            self.invalid_input()
            print(e)

    # Accounts

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

            self.dialog_box_top.destroy()

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

                self.dialog_box_top.destroy()

                self.basic_user_status()
            except Exception as e:
                self.invalid_input()
                print(e)

    def employee_info_treeview_request(self):
        self.database_connect()
        self.mycursor.execute("SELECT basic_user.basic_user_id, basic_user.username, basic_user.role "
                              "FROM basic_user where admin_id = ' "
                              + str(self.admin_id_str) + "' ORDER BY basic_user.basic_user_id;")

        employees = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in employees:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2]), tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2]), tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def remove_employee_account_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM basic_user WHERE basic_user_id = '" + values[0] +
                                  "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            tk.messagebox.showinfo("Removed account successfully")

            self.account_settings_content_interface()
        except Exception as e:
            self.invalid_input()
            print(e)

    # Menu
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

            self.dialog_box_top.destroy()

    # System
    def database_connect(self):
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="hmsdatabase")
            print("Connected to lmsdatabase")
            self.mycursor = self.db1.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Could not connect to database. \n Please check your internet connection")
            print("Could not connect to hmsdatabase")
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
                self.admin_access_password_e.get() + "' and admin_id = '" + str(self.admin_id_str) + "';")
            myresult = self.mycursor.fetchone()
            if myresult is None:
                messagebox.showerror("Error", "Invalid User Name And Password")
            else:
                self.admin_access = True
                self.dialog_box_top.destroy()

            self.db1.close()
            self.mycursor.close()

    # ================================================ Content control =================================================
    def change_button_color(self):
        self.home_b.configure(fg='#7c8084', image=self.home_inactive_im_resized)
        self.tenants_b.configure(fg='#7c8084', image=self.tenant_inactive_im_resized)
        self.payments_b.configure(fg='#7c8084', image=self.payment_inactive_im_resized)
        self.discounts_b.configure(fg='#7c8084', image=self.discount_inactive_im_resized)
        self.accounts_b.configure(fg='#7c8084', image=self.account_inactive_im_resized)
        self.notif_b.configure(fg='#7c8084', image=self.notif_inactive_im_resized)

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

    def room_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Room Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        room_info_label_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        room_info_label_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.room_id = values[0]

        ttk.Label(room_info_label_lf, text='Room ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(room_info_label_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Number: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(room_info_label_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Capacity: ',
                  style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(room_info_label_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Price: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(room_info_label_lf, text=values[6], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Type: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(room_info_label_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(room_info_label_lf, text='Current Occupants: ',
                  style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(room_info_label_lf, text=values[7], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Availability: ',
                  style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(room_info_label_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Description: ',
                  style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(room_info_label_lf, text=values[2],
                  style="small_info.TLabel").grid(column=1, row=7, columnspan=2, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Create transaction", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.create_im_resized, compound="left", justify="left",
                  command=self.create_transaction_dialog).pack(side="top", pady=5, fill="x")

        copy_create_b_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        copy_create_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(copy_create_b_lf, text=" Copy and create new", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.copy_im_resized, compound="left", justify="left",
                  command=self.copy_and_create_room_dialog).pack(side="top", fill="x")

        modify_b_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        modify_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(modify_b_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left", justify="left",
                  command=self.modify_room_dialog).pack(side="top", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51", relief="flat",
                  image=self.remove_im_resized, compound="left", justify="left",
                  command=self.remove_room_account_request).pack(side="top", pady=5, fill="x")

        print(event)

    def employee_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Employee Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        employee_info_label_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        employee_info_label_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        ttk.Label(employee_info_label_lf, text='ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(employee_info_label_lf, text='Name: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(employee_info_label_lf, text='Role: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(employee_info_label_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        # Buttons
        tk.Button(self.info_buttons_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left",
                  justify="left").pack(side="left", pady=5, padx=10, anchor="w")

        tk.Button(self.info_buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51", relief="flat",
                  image=self.remove_im_resized, compound="left",
                  command=self.remove_employee_account_request).pack(side="left", pady=5, padx=10, anchor="w")

        print(event)

    def tenant_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Tenant Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.tenant_id = values[0]

        ttk.Label(info_lf, text='Tenant ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Tenant Name: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Tenant Status: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Tenant Balance: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        modify_b_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        modify_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(modify_b_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left", justify="left",
                  command=self.modify_tenant_account_dialog).pack(side="top", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51", relief="flat",
                  image=self.remove_im_resized, compound="left",
                  command=self.remove_tenant_account_request).pack(side="top", pady=5, fill="x")

        print(event)

    def discount_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Discount Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.discount_id = values[0]

        ttk.Label(info_lf, text='Discount ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Discount Code: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Discount Amount: ',
                  style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Discount Status: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        modify_b_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        modify_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(modify_b_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left", justify="left",
                  command=self.modify_discount_dialog).pack(side="top", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_discount_request).pack(side="top", pady=5, fill="x")

        print(event)

    # ================================================ Static Methods ==================================================
    @staticmethod
    def invalid_input():
        messagebox.showerror("Error", "Invalid or no input.")

    @staticmethod
    def invalid_request():
        messagebox.showerror("Error", "Database request unsuccessful! \n Please your internet connection.")

    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='This action is currently under development!')


if __name__ == "__main__":
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
