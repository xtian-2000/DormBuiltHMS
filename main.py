import functools
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from content_controller import Content_control
from style import Content
from tkinter import PhotoImage
# from database_controller import Database
import mysql.connector as mysql
from random import randint
from tkinter import Menu
from datetime import datetime
from fpdf import FPDF
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
import webbrowser

# Import needed for compilation
import babel.numbers

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"

date = datetime.now()
date_str = date.strftime('%x')

print(date_str)
time = datetime.now()
time_str = time.strftime('%X')

# Create variable for first day of the month
fday_month = datetime.today().replace(day=1)
fday_month_str = fday_month.strftime('%x')

hms_version = "DORv1.55"


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
        self.footer_lf = None

        # Label
        self.admin_access_status_l = ttk.Label
        self.room_cost_l = ttk.Label
        self.amount_to_be_paid_l = ttk.Label
        self.discount_l = ttk.Label
        self.payment_description_l = ttk.Label
        self.application_fee_l = ttk.Label
        self.amenities_cost_l = ttk.Label

        # PhotoImage
        db_logo_im = PhotoImage(file=r"Dormbuilt_logo.png")
        self.db_logo_resized = db_logo_im.subsample(2, 2)
        self.db_logo_resized_2 = db_logo_im.subsample(6, 6)

        hms_logo_im = PhotoImage(file=r"pongodev_hms_small_logo.png")
        self.hms_logo_im_resized = hms_logo_im.subsample(8, 8)

        download_im = PhotoImage(file=r"download_b.png")
        self.download_im_resized = download_im.subsample(1, 1)

        create_tenant_basic_im = PhotoImage(file=r"create_tenant_basic_b.png")
        self.create_tenant_basic_im_resized = create_tenant_basic_im.subsample(1, 1)

        exclamation_im = PhotoImage(file=r"exclamation_mark.png")
        self.exclamation_im_resized = exclamation_im.subsample(1, 1)

        receipt_im = PhotoImage(file=r"receipt_b.png")
        self.receipt_im_resized = receipt_im.subsample(1, 1)

        single_bed_im = PhotoImage(file=r"single_bed_l.png")
        self.single_bed_im_resized = single_bed_im.subsample(1, 1)

        double_bed_im = PhotoImage(file=r"double_bed_l.png")
        self.double_bed_im_resized = double_bed_im.subsample(1, 1)

        available_im = PhotoImage(file=r"available_im.png")
        self.available_im_resized = available_im.subsample(1, 1)

        reserved_im = PhotoImage(file=r"reserved_l.png")
        self.reserved_im_resized = reserved_im.subsample(1, 1)

        full_im = PhotoImage(file=r"full_im.png")
        self.full_im_resized = full_im.subsample(1, 1)

        maintenance_im = PhotoImage(file=r"maintenance_im.png")
        self.maintenance_im_resized = maintenance_im.subsample(1, 1)

        modify_basic_im = PhotoImage(file=r"modify_basic_b.png")
        self.modify_basic_im_resized = modify_basic_im.subsample(1, 1)

        modify_admin_im = PhotoImage(file=r"modify_admin_b.png")
        self.modify_admin_im_resized = modify_admin_im.subsample(1, 1)

        report_im = PhotoImage(file=r"report_b.png")
        self.report_im_resized = report_im.subsample(1, 1)

        minimalist_logo_im = PhotoImage(file=r"minimalist_l.png")
        self.minimalist_logo_im_resized = minimalist_logo_im.subsample(1, 1)

        cloud_logo_im = PhotoImage(file=r"cloud_database_l.png")
        self.cloud_logo_im_resized = cloud_logo_im.subsample(1, 1)

        intuitive_logo_im = PhotoImage(file=r"intuitive_interface_l.png")
        self.intuitive_logo_im_resized = intuitive_logo_im.subsample(1, 1)

        web_logo_im = PhotoImage(file=r"online_reservation_module_l.png")
        self.web_logo_im_resized = web_logo_im.subsample(1, 1)

        blue_line_im = PhotoImage(file=r"blue_line_l.png")
        self.blue_line_im_resized = blue_line_im.subsample(1, 1)

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

        assessment_im = PhotoImage(file=r"create_assessment_b.png")
        self.assessment_im_resized = assessment_im.subsample(1, 1)

        empty_im = PhotoImage(file=r"empty_l.png")
        self.empty_im_resized = empty_im.subsample(1, 1)

        add_basic_im = PhotoImage(file=r"add_basic_b.png")
        self.add_basic_im_resized = add_basic_im.subsample(1, 1)

        add_admin_im = PhotoImage(file=r"add_admin_b.png")
        self.add_admin_im_resized = add_admin_im.subsample(1, 1)

        home_active_im = PhotoImage(file=r"home_active_b.png")
        self.home_active_im_resized = home_active_im.subsample(1, 1)

        home_inactive_im = PhotoImage(file=r"home_inactive_b.png")
        self.home_inactive_im_resized = home_inactive_im.subsample(1, 1)

        dashboard_active_im = PhotoImage(file=r"analytics_dashboard_active_b.png")
        self.dashboard_active_im_resized = dashboard_active_im.subsample(1, 1)

        dashboard_inactive_im = PhotoImage(file=r"analytics_dashboard_inactive_b.png")
        self.dashboard_inactive_im_resized = dashboard_inactive_im.subsample(1, 1)

        tenant_active_im = PhotoImage(file=r"tenant_active_b.png")
        self.tenant_active_im_resized = tenant_active_im.subsample(1, 1)

        tenant_inactive_im = PhotoImage(file=r"tenant_inactive_b.png")
        self.tenant_inactive_im_resized = tenant_inactive_im.subsample(1, 1)

        booking_active_im = PhotoImage(file=r"booking_active_b.png")
        self.booking_active_im_resized = booking_active_im.subsample(1, 1)

        booking_inactive_im = PhotoImage(file=r"booking_inactive_b.png")
        self.booking_inactive_im_resized = booking_inactive_im.subsample(1, 1)

        payment_active_im = PhotoImage(file=r"payment_active_b.png")
        self.payment_active_im_resized = payment_active_im.subsample(1, 1)

        payment_inactive_im = PhotoImage(file=r"payment_inactive_b.png")
        self.payment_inactive_im_resized = payment_inactive_im.subsample(1, 1)

        assessment_active_im = PhotoImage(file=r"assessment_active_b.png")
        self.assessment_active_im_resized = assessment_active_im.subsample(1, 1)

        assessment_inactive_im = PhotoImage(file=r"assessment_inactive_b.png")
        self.assessment_inactive_im_resized = assessment_inactive_im.subsample(1, 1)

        discount_active_im = PhotoImage(file=r"discount_active_b.png")
        self.discount_active_im_resized = discount_active_im.subsample(1, 1)

        discount_inactive_im = PhotoImage(file=r"discount_inactive_b.png")
        self.discount_inactive_im_resized = discount_inactive_im.subsample(1, 1)

        account_active_im = PhotoImage(file=r"account_active_b.png")
        self.account_active_im_resized = account_active_im.subsample(1, 1)

        account_inactive_im = PhotoImage(file=r"account_inactive_b.png")
        self.account_inactive_im_resized = account_inactive_im.subsample(1, 1)

        action_history_active_im = PhotoImage(file=r"action_history_active_b.png")
        self.action_history_active_im_resized = action_history_active_im.subsample(1, 1)

        action_history_inactive_im = PhotoImage(file=r"action_history_inactive_b.png")
        self.action_history_inactive_im_resized = action_history_inactive_im.subsample(1, 1)

        notif_active_im = PhotoImage(file=r"notif_active_b.png")
        self.notif_active_im_resized = notif_active_im.subsample(1, 1)

        notif_inactive_im = PhotoImage(file=r"notif_inactive_b.png")
        self.notif_inactive_im_resized = notif_inactive_im.subsample(1, 1)

        # DateEntry
        self.dashboard_filter_from = DateEntry
        self.dashboard_filter_to = DateEntry

        # Buttons
        self.home_b = tk.Button
        self.dashboard_b = tk.Button
        self.tenants_b = tk.Button
        self.assessment_b = tk.Button
        self.payments_b = tk.Button
        self.booking_b = tk.Button
        self.discounts_b = tk.Button
        self.accounts_b = tk.Button
        self.action_history_b = tk.Button
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

        self.tenant_name_e = ttk.Entry
        self.tenant_email_e = ttk.Entry

        self.bug_description_e = ttk.Entry

        self.discount_code_e = ttk.Entry
        self.search_e = ttk.Entry

        # Spinbox
        self.room_number_sp = ttk.Spinbox
        self.room_capacity_sp = ttk.Spinbox
        self.room_price_sp = ttk.Spinbox
        self.tenant_id_sp = ttk.Spinbox
        self.payment_amount_sp = ttk.Spinbox
        self.discount_amount_sp = ttk.Spinbox
        self.amenity_price_sp = ttk.Spinbox
        self.tenant_id_filter_sp = ttk.Spinbox

        # ComboBox
        self.room_availability_cb = ttk.Combobox
        self.tenant_status_cb = ttk.Combobox
        self.discount_status_cb = ttk.Combobox
        self.payment_description_cb = ttk.Combobox
        self.order_by_cb = ttk.Combobox
        self.room_type_cb = ttk.Combobox
        self.new_room_type_cb = ttk.Combobox

        # Treeview
        self.info_tree = ttk.Treeview

        # File Dialog
        self.save_file_dialog = None

        # String
        self.admin_id_str = str
        self.basic_user_id_str = str
        self.current_user = None
        self.action_description = str

        # Int
        self.room_id = int
        self.tenant_id = int
        self.discount_id = int
        self.employee_id = int
        self.booking_id = int

        self.discount_reduction = None

        # Boolean
        self.admin_access_bool = False
        self.basic_user_access_bool = False
        self.discount_applied_bool = False

        # Database
        self.db1 = None
        self.mycursor = None

        # Initialize method for login interface
        self.signin_interface()

        # Initialize class for database
        # Database()

        # Root window configuration
        self.master.title('DormBuilt HMS')
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (width, height))
        self.master.iconbitmap(r"pongodev_logo.ico")

        # Initialize class for default styles
        Content.widget_styles(self.master)

    def signin_interface(self):
        # Clean widgets in the master window
        Content_control.destroy_content(self.master)

        # ================================================ Sign In Interface ===========================================
        top_f = ttk.Frame(self.master, style="Basic.TFrame")
        top_f.pack(side="top", fill="x")

        # ================================================ Logo Interface ==============================================
        hms_logo_lf = tk.LabelFrame(top_f, bg="#FFFFFF")
        hms_logo_lf.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        tk.Label(hms_logo_lf, image=self.hms_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", padx=10, pady=5, anchor="center")

        ttk.Label(hms_logo_lf, text="Hotel Management System comes with a slew of \n"
                                    "capabilities, from a user-friendly interface \n"
                                    "to extensive data management controls,as well \n"
                                    "as extra data visualization options. Extend your\n"
                                    "business with a centralized system that takes care\n"
                                    "of the hassle of data processing.",
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        db_logo_lf = tk.LabelFrame(top_f, bg="#FFFFFF", relief="flat")
        db_logo_lf.pack(side="left", padx=20, pady=20, fill="both", expand=True)

        ttk.Label(db_logo_lf, text='Developed for:', style="h1_body.TLabel").pack(side="top", pady=10, anchor="w")

        tk.Label(db_logo_lf, image=self.db_logo_resized, bg="#FFFFFF").pack(side="top", anchor="w")

        ttk.Label(db_logo_lf, text='DormBuilt Inc.', style="h1.TLabel").pack(side="top", pady=5, anchor="w")

        ttk.Label(db_logo_lf, text='Dormbuilt is a company that recognizes housing \n'
                                   'needs of the community within the institution and\n'
                                   'dedicates its expertise to better serve them.',
                  style="h2.TLabel").pack(side="top", pady=5, anchor="w")

        tk.Label(db_logo_lf, image=self.blue_line_im_resized, bg="#FFFFFF").pack(side="top", pady=5, anchor="w")

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

        tk.Button(buttons_f, text="Sign in as Basic User", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", command=self.basic_user_signin_request).pack(side="top", pady=5, padx=10, fill="x")

        signup_b_lf = tk.LabelFrame(buttons_f, bd=1, bg="#585456", relief="flat")
        signup_b_lf.pack(side="top", pady=5, padx=10, fill="x")

        tk.Button(signup_b_lf, text="Sign up", font="OpenSans, 12", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.signup_interface).pack(side="top", fill="x")

        self.signin_username_e.focus()

        # ================================================ Filler Interface ===========================================
        middle_f = ttk.Frame(self.master, style="Basic.TFrame")
        middle_f.pack(side="top", fill="both", expand=True)

        # Minimalist feature
        minimalist_logo_lf = tk.LabelFrame(middle_f, bg="#FFFFFF", relief="flat")
        minimalist_logo_lf.pack(side="left", ipady=10, padx=20, pady=60, anchor="n", fill="x", expand=True)

        tk.Label(minimalist_logo_lf, image=self.minimalist_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(minimalist_logo_lf, text='Minimalist Design',
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        ttk.Label(minimalist_logo_lf, text="The interface of Dormbuilt's Hotel Management \n"
                                           "System's is aimed towards a minimalist design \n"
                                           "for a clean and concise look.",
                  style="h2.TLabel").pack(side="top", pady=5, anchor="center")

        # Cloud Database feature
        cloud_logo_lf = tk.LabelFrame(middle_f, bg="#FFFFFF", relief="flat")
        cloud_logo_lf.pack(side="left", ipady=10, padx=20, pady=60, anchor="n", fill="x", expand=True)

        tk.Label(cloud_logo_lf, image=self.cloud_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(cloud_logo_lf, text='Cloud Database',
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        ttk.Label(cloud_logo_lf, text="The Dormbuilt's Hotel Management System  \n"
                                      "uses the service of cloud database in storing\n"
                                      "information.",
                  style="h2.TLabel").pack(side="top", pady=5, anchor="center")

        # Intuitive interface feature
        intuitive_logo_lf = tk.LabelFrame(middle_f, bg="#FFFFFF", relief="flat")
        intuitive_logo_lf.pack(side="left", ipady=10, padx=20, pady=60, anchor="n", fill="x", expand=True)

        tk.Label(intuitive_logo_lf, image=self.intuitive_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(intuitive_logo_lf, text='Intuitive Interface',
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        ttk.Label(intuitive_logo_lf, text="The interface of Dormbuilt's Hotel Management \n"
                                          "System is designed for ease of operation and \n"
                                          "intuitive interface structure. ",
                  style="h2.TLabel").pack(side="top", pady=5, anchor="center")

        # Website feature
        web_logo_lf = tk.LabelFrame(middle_f, bg="#FFFFFF", relief="flat")
        web_logo_lf.pack(side="left", ipady=10, padx=20, pady=60, anchor="n", fill="x", expand=True)

        tk.Label(web_logo_lf, image=self.web_logo_im_resized,
                 bg="#FFFFFF").pack(side="top", anchor="center")

        ttk.Label(web_logo_lf, text='Online Reservation Module',
                  style="h1_body.TLabel").pack(side="top", pady=5, anchor="center")

        ttk.Label(web_logo_lf, text="The Dormbuilt's Hotel Management System is paired \n"
                                    "with an online reservation module that enables the \n"
                                    "hotel to expand its operations online.",
                  style="h2.TLabel").pack(side="top", pady=5, anchor="center")

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
        help_menu.add_command(label="User Manual", command=self.generate_user_manual)
        help_menu.add_command(label="FAQs", command=self.generate_faqs)
        help_menu.add_command(label="Developer's Information", command=self.developer_information)
        help_menu.add_separator()
        help_menu.add_command(label="User Ratings", command=self.user_ratings)
        help_menu.add_command(label="Bug report", command=self.bug_report_dialog)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # ================================================ Top-Nav Interface ===========================================
        top_nav_lf = tk.LabelFrame(self.master, bg="#FFFFFF", relief="flat")
        top_nav_lf.pack(side="top", fill="x")

        tk.Label(top_nav_lf, image=self.db_logo_resized_2, bg="#FFFFFF").pack(side="left", pady=5)

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

        self.dashboard_b = tk.Button(left_nav_lf, text=" Dashboard", font=("OpenSans", 15), fg='#7c8084',
                                     bg="#FFFFFF", relief="flat", image=self.dashboard_inactive_im_resized,
                                     compound="left", command=self.dashboard_content_interface)
        self.dashboard_b.pack(side="top", anchor="w")

        self.tenants_b = tk.Button(left_nav_lf, text=" Tenants", font=("OpenSans", 15), fg='#7c8084',
                                   bg="#FFFFFF", relief="flat", image=self.tenant_inactive_im_resized, compound="left",
                                   command=self.tenant_content_interface)
        self.tenants_b.pack(side="top", anchor="w")

        self.assessment_b = tk.Button(left_nav_lf, text=" Assessments", font=("OpenSans", 15), fg='#7c8084',
                                      bg="#FFFFFF", relief="flat", image=self.assessment_inactive_im_resized,
                                      compound="left", command=self.assessment_content_interface)
        self.assessment_b.pack(side="top", anchor="w")

        self.payments_b = tk.Button(left_nav_lf, text=" Payments", font=("OpenSans", 15), fg='#7c8084',
                                    bg="#FFFFFF", relief="flat", image=self.payment_inactive_im_resized,
                                    compound="left", command=self.payment_content_interface)
        self.payments_b.pack(side="top", anchor="w")

        self.booking_b = tk.Button(left_nav_lf, text=" Booking", font=("OpenSans", 15), fg='#7c8084',
                                   bg="#FFFFFF", relief="flat", image=self.booking_inactive_im_resized,
                                   compound="left", command=self.booking_content_interface)
        self.booking_b.pack(side="top", anchor="w")

        self.discounts_b = tk.Button(left_nav_lf, text=" Discounts", font=("OpenSans", 15), fg='#7c8084',
                                     bg="#FFFFFF", relief="flat", image=self.discount_inactive_im_resized,
                                     compound="left", command=self.discount_content_interface)
        self.discounts_b.pack(side="top", anchor="w")

        self.accounts_b = tk.Button(left_nav_lf, text=" Accounts", font=("OpenSans", 15), fg='#7c8084',
                                    bg="#FFFFFF", relief="flat", image=self.account_inactive_im_resized,
                                    compound="left", command=self.account_settings_content_interface)
        self.accounts_b.pack(side="top", anchor="w")

        self.action_history_b = tk.Button(left_nav_lf, text=" Action History", font=("OpenSans", 15), fg='#7c8084',
                                          bg="#FFFFFF", relief="flat", image=self.action_history_inactive_im_resized,
                                          compound="left", command=self.action_history_interface)
        self.action_history_b.pack(side="top", anchor="w")

        self.notif_b = tk.Button(left_nav_lf, text=" Notifications", font=("OpenSans", 15), fg='#7c8084',
                                 bg="#FFFFFF", relief="flat", image=self.notif_inactive_im_resized,
                                 compound="left", command=self.notif_content_interface)
        self.notif_b.pack(side="top", anchor="w")

        ttk.Label(left_nav_lf, text=hms_version, style="small_info.TLabel").pack(side="bottom", pady=20)

        # ================================================ Left-Nav widgets ============================================
        self.content_lf = tk.LabelFrame(self.master)
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
        create_room_l.grid(column=0, row=0, sticky="w")
        create_room_l.bind("<Button-1>", self.create_room_dialog)

        set_room_price_to_type_l = ttk.Label(room_dashboard_links_lf, text='Set room price according to room type',
                                             style="link.TLabel")
        set_room_price_to_type_l.grid(column=0, row=1, sticky="w")
        set_room_price_to_type_l.bind("<Button-1>", self.set_room_price_to_type_dialog)

        set_amenities_price_to_type_l = ttk.Label(room_dashboard_links_lf, text='Set amenities price according to '
                                                                                'room type', style="link.TLabel")
        set_amenities_price_to_type_l.grid(column=0, row=2, sticky="w")
        set_amenities_price_to_type_l.bind("<Button-1>", self.set_room_amenities_to_type_dialog)

        set_room_capacity_to_type_l = ttk.Label(room_dashboard_links_lf,
                                                text='Set room capacity according to room type', style="link.TLabel")
        set_room_capacity_to_type_l.grid(column=1, row=0, sticky="w")
        set_room_capacity_to_type_l.bind("<Button-1>", self.set_room_capacity_to_type_dialog)

        set_room_type_to_type_l = ttk.Label(room_dashboard_links_lf, text='Change current room type',
                                            style="link.TLabel")
        set_room_type_to_type_l.grid(column=1, row=1, sticky="w")
        set_room_type_to_type_l.bind("<Button-1>", self.set_room_type_to_type_dialog)

        # ================================================ Room info ===============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Room Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_room_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Room ID', 'Room Number', 'Room Type', 'Room Availability', 'Room Capacity',
                                      'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FAFAFA", relief="flat")
        self.info_content_lf.pack(side="top", fill="both", expand=True)

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_room_information_module).pack(side="top", fill="x")

    def dashboard_content_interface(self):
        self.change_button_color()
        self.dashboard_b.configure(fg='#395A68', image=self.dashboard_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Tenant info ===============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Sales Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_sales_dashboard_module).pack(fill="x")

        # Filter
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right", anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20, date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right", anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_sales_dashboard_module).pack(side="top", fill="x")

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
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Tenant Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_tenant_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Tenant ID', 'Tenant Name', 'Status', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_tenant_information_module).pack(side="top", fill="x")

    def assessment_content_interface(self):
        self.change_button_color()
        self.assessment_b.configure(fg='#395A68', image=self.assessment_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Payment info ===============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Assessment Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_assessment_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Assessment ID', 'Tenant Name', 'Assessment Description', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # Filter Tenant ID

        self.tenant_id_filter_sp = ttk.Spinbox(info_title_lf, from_=0, to=99999, wrap=True)
        self.tenant_id_filter_sp.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Tenant ID: ", style="h2_small.TLabel").pack(side="right",
                                                                                   anchor="nw", padx=5, pady=5)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat",
                  command=self.show_assessment_information_module).pack(side="top", fill="x")

    def payment_content_interface(self):
        self.change_button_color()
        self.payments_b.configure(fg='#395A68', image=self.payment_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Payment info ===============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Payment Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_payment_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Payment ID', 'Tenant Name', 'Payment Description', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # Filter Tenant ID

        self.tenant_id_filter_sp = ttk.Spinbox(info_title_lf, from_=0, to=99999, wrap=True)
        self.tenant_id_filter_sp.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Tenant ID: ", style="h2_small.TLabel").pack(side="right",
                                                                                   anchor="nw", padx=5, pady=5)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_payment_information_module).pack(side="top", fill="x")

    def booking_content_interface(self):
        self.change_button_color()
        self.booking_b.configure(fg='#395A68', image=self.booking_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Payment info ===============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Booking Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_booking_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Booking ID', 'Tenant Name', 'Tenant Email', 'Booking Status', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right", anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20, date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right", anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_booking_information_module).pack(side="top", fill="x")

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
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Discount Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_discount_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Discount ID', 'Discount Code', 'Discount Amount', 'Discount Status',
                                      'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="x")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_discount_information_module).pack(side="top", fill="x")

    def account_settings_content_interface(self):
        self.change_button_color()
        self.accounts_b.configure(fg='#395A68', image=self.account_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

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

        if self.admin_access_bool:
            self.admin_access_status_l = ttk.Label(description_lf, text="On", style="on.TLabel")
            self.admin_access_status_l.grid(column=1, row=1, sticky="w")

            account_settings_links_lf = tk.LabelFrame(account_settings_lf, bg="#FFFFFF", relief="flat")
            account_settings_links_lf.pack(side="top", anchor="nw", pady=10)

            change_username_password_l = ttk.Label(account_settings_links_lf, text='Change username and password',
                                                   style="link.TLabel")
            change_username_password_l.pack(side="top", anchor="w")
            change_username_password_l.bind("<Button-1>", self.change_username_password_dialog)
        else:
            self.admin_access_status_l = ttk.Label(description_lf, text="Off", style="off.TLabel")
            self.admin_access_status_l.grid(column=1, row=1, sticky="w")

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
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Employee Information',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(info_title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_employee_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Employee ID', 'Employee Name', 'Role', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Show more info ==============================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        self.info_content_lf.pack(side="top", fill="both")

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#4C8404", relief="flat", command=self.show_employee_information_module).pack(side="top", fill="x")

    def action_history_interface(self):
        self.change_button_color()
        self.action_history_b.configure(fg='#395A68', image=self.action_history_active_im_resized)

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

        ttk.Label(tenant_dashboard_label_lf, text='Action History Dashboard',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(tenant_dashboard_label_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        tenant_dashboard_links_lf = tk.LabelFrame(tenant_dashboard_lf, bg="#FFFFFF", relief="flat")
        tenant_dashboard_links_lf.pack(side="top", anchor="nw", pady=10)

        clear_action_history_l = ttk.Label(tenant_dashboard_links_lf, text='Clear action history', style="link.TLabel")
        clear_action_history_l.pack(side="top", anchor="w")
        clear_action_history_l.bind("<Button-1>", self.clear_action_history_request)

        # ================================================ Action History ==============================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Action History',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456", bg="#FFFFFF", relief="flat",
                  command=self.show_action_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Action ID', 'Action Description', 'Current User', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Room info content ===========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FAFAFA", relief="flat")
        self.info_content_lf.pack(side="top", fill="both", expand=True)

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#4C8404", relief="flat", command=self.show_action_information_module).pack(side="top", fill="x")

    def notif_content_interface(self):
        self.change_button_color()
        self.notif_b.configure(fg='#395A68', image=self.notif_active_im_resized)

        # Clean widgets in the master window
        Content_control.destroy_content(self.content_lf)

        # ================================================ Notification ================================================
        info_lf = tk.LabelFrame(self.content_lf, bg="#FFFFFF")
        info_lf.pack(side="top", fill="x")

        info_title_lf = tk.LabelFrame(info_lf, bg="#FFFFFF", relief="flat")
        info_title_lf.pack(side="top", fill="x")

        ttk.Label(info_title_lf, text='Notifications',
                  style="h1.TLabel").pack(side="left", anchor="nw")

        ttk.Label(info_title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        refresh_b_lf = tk.LabelFrame(info_title_lf, bd=1, bg="#585456", relief="flat")
        refresh_b_lf.pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(refresh_b_lf, text="Refresh", font="OpenSans, 10", fg="#585456",
                  bg="#FFFFFF", relief="flat", command=self.show_notif_information_module).pack(fill="x")

        # Filter Order By
        self.order_by_cb = ttk.Combobox(info_title_lf)
        self.order_by_cb['values'] = ('Notif ID', 'Notif Subject', 'Notif Description', 'Date Created')
        self.order_by_cb['state'] = 'readonly'
        self.order_by_cb.current(0)
        self.order_by_cb.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Order by:", style="h2_small.TLabel").pack(side="right",
                                                                                 anchor="nw", padx=5, pady=5)

        # Filter Date
        self.dashboard_filter_to = DateEntry(info_title_lf, width=20,
                                             date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_to.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="to", style="h2_small.TLabel").pack(side="right",
                                                                          anchor="nw", padx=5, pady=5)

        self.dashboard_filter_from = DateEntry(info_title_lf, width=20,
                                               date_pattern="MM/dd/yy", borderwidth=2)
        self.dashboard_filter_from.pack(side="right", anchor="nw", padx=5, pady=5)

        ttk.Label(info_title_lf, text="Date:", style="h2_small.TLabel").pack(side="right",
                                                                             anchor="nw", padx=5, pady=5)

        # Insert values to Date Entry
        self.dashboard_filter_from.delete(0, "end")
        self.dashboard_filter_from.insert(0, fday_month_str)

        self.dashboard_filter_to.delete(0, "end")
        self.dashboard_filter_to.insert(0, date_str)

        # ================================================ Notification content ========================================
        self.info_content_lf = tk.LabelFrame(info_lf, bg="#FAFAFA", relief="flat")
        self.info_content_lf.pack(side="top", fill="both", expand=True)

        tk.Button(self.info_content_lf, text="Show more", font="OpenSans, 10", fg="#FFFFFF",
                  bg="#89CFF0", relief="flat", command=self.show_notif_information_module).pack(side="top", fill="x")

    # Home
    def show_room_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FAFAFA", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview",
                                      yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Room ID", "Room Number", "Description", "Type", "Availability", "Capacity",
                                     "Room Price", "Amenities Price", "Current Occupants")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Room ID", anchor="center", width=80)
        self.info_tree.column("Room Number", anchor="center", width=80)
        self.info_tree.column("Description", anchor="center", width=0, stretch=False)
        self.info_tree.column("Type", anchor="w", width=120)
        self.info_tree.column("Availability", anchor="w", width=80)
        self.info_tree.column("Capacity", anchor="center", width=80)
        self.info_tree.column("Room Price", anchor="center", width=80)
        self.info_tree.column("Amenities Price", anchor="center", width=80)
        self.info_tree.column("Current Occupants", anchor="center", width=90)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.info_tree.heading("Room Number", text="Room Number", anchor="center")
        self.info_tree.heading("Description", text="Description", anchor="w")
        self.info_tree.heading("Type", text="Type", anchor="w")
        self.info_tree.heading("Availability", text="Availability", anchor="w")
        self.info_tree.heading("Capacity", text="Capacity", anchor="center")
        self.info_tree.heading("Room Price", text="Room Price", anchor="center")
        self.info_tree.heading("Amenities Price", text="Amenities Price", anchor="center")
        self.info_tree.heading("Current Occupants", text="Current Occupants", anchor="center")

        self.info_tree.pack(side="top", fill="both")

        # Initialize method for inserting items in a list
        self.room_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on a room to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        self.footer_lf = tk.LabelFrame(self.info_tree_lf, bg="#FFFFFF", relief="flat")
        self.footer_lf.pack(side="top", fill="x")

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
        self.info_tree["columns"] = ("Tenant ID", "Tenant Name", "Status", "Room ID", "Balance", "Email",
                                     "Date created")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Tenant ID", anchor="center", width=80)
        self.info_tree.column("Tenant Name", anchor="w", width=120)
        self.info_tree.column("Status", anchor="w", width=80)
        self.info_tree.column("Room ID", anchor="center", width=80)
        self.info_tree.column("Balance", anchor="w", width=80)
        self.info_tree.column("Email", anchor="w", width=80)
        self.info_tree.column("Date created", anchor="w", width=80)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Tenant ID", text="Tenant ID", anchor="center")
        self.info_tree.heading("Tenant Name", text="Tenant Name", anchor="w")
        self.info_tree.heading("Status", text="Status", anchor="w")
        self.info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.info_tree.heading("Balance", text="Balance", anchor="w")
        self.info_tree.heading("Email", text="Email", anchor="w")
        self.info_tree.heading("Date created", text="Date created", anchor="w")

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

    # Dashboard
    def show_sales_dashboard_module(self):
        Content_control.destroy_content(self.info_content_lf)

        pandasdb = mysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database="hmsdatabase",
                                 use_pure=True)

        query = "Select p.payment_amount FROM payment p WHERE date_created >= '" \
                + self.dashboard_filter_from.get() + "' AND date_created <= '" \
                + self.dashboard_filter_to.get() + "' AND admin_id = '" + self.admin_id_str + "';"

        df = pd.read_sql(query, pandasdb)
        pandasdb.close()

        print("Payments dataframe")
        print(df)

        width = self.master.winfo_screenmmwidth()

        fig = Figure(figsize=(width / 25.4, 5), dpi=75)
        ax1 = fig.add_subplot(111)
        ax1.plot(df, marker="o", label="payment amount in PHP")
        ax1.set_title("Payments Dashboard")
        ax1.set_xlabel("No. of payments")
        ax1.set_ylabel("Payment amounts in Philippine Peso")
        ax1.legend()

        canvas = FigureCanvasTkAgg(fig, self.info_content_lf)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", padx=10, pady=10, fill="both", expand=True)

        # Info section
        info_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", fill="x", expand=True)

        ttk.Label(info_lf, text='Payments Information\n',
                  style="on.TLabel").grid(column=0, row=0, columnspan=2, rowspan=2, sticky="w")

        ttk.Label(info_lf, text='Total Number of Payments: ',
                  style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=len(df.index), style="on.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Total Amount of Payments: ',
                  style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=df['payment_amount'].sum(), style="on.TLabel").grid(column=1, row=3, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="x", expand=True)

        tk.Button(buttons_lf, text="Generate report", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  image=self.report_im_resized, compound="left", relief="flat",
                  command=self.generate_sales_report_request).pack(side="left", padx=10, pady=10)

    # Assessment
    def show_assessment_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Assessment ID", "Tenant ID", "Tenant Name", "Assessment Amount", "Room ID",
                                     "Admin ID", "Basic User ID", "Assessment Description",
                                     "Date created", "Tenant Email")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Assessment ID", anchor="center", width=80)
        self.info_tree.column("Tenant ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Tenant Name", anchor="w", width=80)
        self.info_tree.column("Assessment Amount", anchor="center", width=80)
        self.info_tree.column("Room ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Admin ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Basic User ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Assessment Description", anchor="w", width=80)
        self.info_tree.column("Date created", anchor="w", width=80)
        self.info_tree.column("Tenant Email", anchor="w", width=0, stretch=False)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Assessment ID", text="Assessment ID", anchor="center")
        self.info_tree.heading("Tenant ID", text="Tenant ID", anchor="center")
        self.info_tree.heading("Tenant Name", text="Tenant Name", anchor="w")
        self.info_tree.heading("Assessment Amount", text="Assessment Amount", anchor="center")
        self.info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.info_tree.heading("Admin ID", text="Admin ID", anchor="center")
        self.info_tree.heading("Basic User ID", text="Basic User ID", anchor="center")
        self.info_tree.heading("Assessment Description", text="Assessment Description", anchor="w")
        self.info_tree.heading("Date created", text="Date created", anchor="w")
        self.info_tree.heading("Tenant Email", text="Tenant Email", anchor="w")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.assessment_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on an assessment to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.assessment_info_section)

    # Payment
    def show_payment_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Payment ID", "Tenant ID", "Tenant Name", "Payment Amount", "Room ID",
                                     "Admin ID", "Basic User ID", "Discount Code", "Payment Description",
                                     "Date created", "Tenant Email")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Payment ID", anchor="center", width=80)
        self.info_tree.column("Tenant ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Tenant Name", anchor="w", width=80)
        self.info_tree.column("Payment Amount", anchor="center", width=80)
        self.info_tree.column("Room ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Admin ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Basic User ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Discount Code", anchor="center", width=80)
        self.info_tree.column("Payment Description", anchor="w", width=80)
        self.info_tree.column("Date created", anchor="w", width=80)
        self.info_tree.column("Tenant Email", anchor="w", width=0, stretch=False)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Payment ID", text="Payment ID", anchor="center")
        self.info_tree.heading("Tenant ID", text="Tenant ID", anchor="center")
        self.info_tree.heading("Tenant Name", text="Tenant Name", anchor="w")
        self.info_tree.heading("Payment Amount", text="Payment Amount", anchor="center")
        self.info_tree.heading("Room ID", text="Room ID", anchor="center")
        self.info_tree.heading("Admin ID", text="Admin ID", anchor="center")
        self.info_tree.heading("Basic User ID", text="Basic User ID", anchor="center")
        self.info_tree.heading("Discount Code", text="Discount Code", anchor="center")
        self.info_tree.heading("Payment Description", text="Payment Description", anchor="w")
        self.info_tree.heading("Date created", text="Date created", anchor="w")
        self.info_tree.heading("Tenant Email", text="Tenant Email", anchor="w")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.payment_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on a payment to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.payment_info_section)

    # Booking
    def show_booking_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = ("Booking ID", "Tenant Name", "Tenant Email", "Admin ID", "Booking Status",
                                     "Date Created")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Booking ID", anchor="center", width=80)
        self.info_tree.column("Tenant Name", anchor="w", width=80)
        self.info_tree.column("Tenant Email", anchor="w", width=80)
        self.info_tree.column("Admin ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Booking Status", anchor="w", width=80)
        self.info_tree.column("Date Created", anchor="center", width=80)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Booking ID", text="Booking ID", anchor="center")
        self.info_tree.heading("Tenant Name", text="Tenant Name", anchor="w")
        self.info_tree.heading("Tenant Email", text="Tenant Email", anchor="w")
        self.info_tree.heading("Admin ID", text="Admin ID", anchor="center")
        self.info_tree.heading("Booking Status", text="Booking Status", anchor="w")
        self.info_tree.heading("Date Created", text="Date Created", anchor="center")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.booking_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on an info to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.booking_info_section)

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
        self.info_tree.column("Discount ID", anchor="center", width=80)
        self.info_tree.column("Discount Code", anchor="w", width=80)
        self.info_tree.column("Discount Amount", anchor="center", width=80)
        self.info_tree.column("Discount Status", anchor="center", width=80)
        self.info_tree.column("Date created", anchor="center", width=80)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Discount ID", text="Discount ID", anchor="center")
        self.info_tree.heading("Discount Code", text="Discount Code", anchor="w")
        self.info_tree.heading("Discount Amount", text="Discount Amount (%)", anchor="center")
        self.info_tree.heading("Discount Status", text="Discount Status", anchor="center")
        self.info_tree.heading("Date created", text="Date created", anchor="center")

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
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            Content_control.destroy_content(self.info_content_lf)

            self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
            self.info_tree_lf.pack(side="left", fill="both", expand=True)

            info_tree_scr = tk.Scrollbar(self.info_tree_lf)
            info_tree_scr.pack(side="right", fill="y")

            # Create treeview
            self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview",
                                          yscrollcommand=info_tree_scr.set)
            self.info_tree["columns"] = ("ID", "Name", "Password", "Role", "Date created")

            # Create columns
            self.info_tree.column("#0", width=0, stretch=False)
            self.info_tree.column("ID", anchor="center", width=80)
            self.info_tree.column("Name", anchor="w", width=120)
            self.info_tree.column("Password", anchor="w", width=120)
            self.info_tree.column("Role", anchor="w", width=120)
            self.info_tree.column("Date created", anchor="w", width=120)

            # Create headings
            self.info_tree.heading("#0", text="", anchor="w")
            self.info_tree.heading("ID", text="ID", anchor="center")
            self.info_tree.heading("Name", text="Name", anchor="w")
            self.info_tree.heading("Password", text="Password", anchor="w")
            self.info_tree.heading("Role", text="Role", anchor="w")
            self.info_tree.heading("Date created", text="Date created", anchor="w")

            self.info_tree.pack(side="top", fill="x")

            # Initialize method for inserting items in a list
            self.employee_info_treeview_request()

            self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
            self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

            tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                     bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

            ttk.Label(self.info_buttons_lf, text="Click on an account to open this section!",
                      style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")
            # Bind the treeview to database_view_info method
            self.info_tree.bind("<ButtonRelease-1>", self.employee_info_section)

    # Action History
    def show_action_information_module(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            Content_control.destroy_content(self.info_content_lf)

            self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
            self.info_tree_lf.pack(side="left", fill="both", expand=True)

            info_tree_scr = tk.Scrollbar(self.info_tree_lf)
            info_tree_scr.pack(side="right", fill="y")

            # Create treeview
            self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
            self.info_tree["columns"] = (
                "Action ID", "Action Description", "Admin ID", "Current User", "Privilege Access", "Date Created")

            # Create columns
            self.info_tree.column("#0", width=0, stretch=False)
            self.info_tree.column("Action ID", anchor="center", width=80)
            self.info_tree.column("Action Description", anchor="w")
            self.info_tree.column("Admin ID", anchor="c", width=0, stretch=False)
            self.info_tree.column("Current User", anchor="center", width=80)
            self.info_tree.column("Privilege Access", anchor="center", width=0, stretch=False)
            self.info_tree.column("Date Created", anchor="w", width=80)

            # Create headings
            self.info_tree.heading("#0", text="", anchor="w")
            self.info_tree.heading("Action ID", text="Action ID", anchor="center")
            self.info_tree.heading("Action Description", text="Action Description", anchor="w")
            self.info_tree.heading("Admin ID", text="Admin ID", anchor="center")
            self.info_tree.heading("Current User", text="Current User", anchor="center")
            self.info_tree.heading("Privilege Access", text="Privilege Access", anchor="center")
            self.info_tree.heading("Date Created", text="Date Created", anchor="w")

            self.info_tree.pack(side="top", fill="x")

            # Initialize method for inserting items in a list
            self.action_info_treeview_request()

            self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
            self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

            tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                     bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

            ttk.Label(self.info_buttons_lf, text="Click on an action to open this section!",
                      style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

            # Bind the treeview to database_view_info method
            self.info_tree.bind("<ButtonRelease-1>", self.action_info_section)

    # Notif
    def show_notif_information_module(self):
        Content_control.destroy_content(self.info_content_lf)

        self.info_tree_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_tree_lf.pack(side="left", fill="both", expand=True)

        info_tree_scr = tk.Scrollbar(self.info_tree_lf)
        info_tree_scr.pack(side="right", fill="y")

        # Create treeview
        self.info_tree = ttk.Treeview(self.info_tree_lf, style="default.Treeview", yscrollcommand=info_tree_scr.set)
        self.info_tree["columns"] = (
            "Notif ID", "Notif Subject", "Description", "Admin ID", "Date Created")

        # Create columns
        self.info_tree.column("#0", width=0, stretch=False)
        self.info_tree.column("Notif ID", anchor="center", width=80)
        self.info_tree.column("Notif Subject", anchor="w", width=80)
        self.info_tree.column("Description", anchor="center", width=80)
        self.info_tree.column("Admin ID", anchor="center", width=0, stretch=False)
        self.info_tree.column("Date Created", anchor="w", width=80)

        # Create headings
        self.info_tree.heading("#0", text="", anchor="w")
        self.info_tree.heading("Notif ID", text="Notif ID", anchor="center")
        self.info_tree.heading("Notif Subject", text="Notif Subject", anchor="w")
        self.info_tree.heading("Description", text="Description", anchor="center")
        self.info_tree.heading("Admin ID", text="Admin ID", anchor="center")
        self.info_tree.heading("Date Created", text="Date Created", anchor="w")

        self.info_tree.pack(side="top", fill="x")

        # Initialize method for inserting items in a list
        self.notif_info_treeview_request()

        self.info_buttons_lf = tk.LabelFrame(self.info_content_lf, bg="#FFFFFF", relief="flat")
        self.info_buttons_lf.pack(side="left", pady=5, padx=10, anchor="e")

        tk.Label(self.info_buttons_lf, image=self.empty_im_resized,
                 bg="#FFFFFF").pack(side="top", pady=5, padx=10, anchor="center")

        ttk.Label(self.info_buttons_lf, text="Click on a notif to open this section!",
                  style="h2_small.TLabel").pack(side="top", pady=5, padx=10, anchor="center")

        # Bind the treeview to database_view_info method
        self.info_tree.bind("<ButtonRelease-1>", self.notif_info_section)

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

        ttk.Label(forms_lf, text="optional", image=self.exclamation_im_resized, compound="left",
                  style="small_info.TLabel", justify="left").grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, padx=2.5, pady=2.5, row=3, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Reserved', 'Available', 'Fully Occupied', 'Maintenance')
        self.room_availability_cb.current(1)
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

        ttk.Label(forms_lf, text='Amenity price', style="h2.TLabel",
                  justify="left").grid(column=0, row=8, padx=2.5, pady=2.5, sticky="w")

        self.amenity_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.amenity_price_sp.grid(column=1, row=8, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=9, sticky="w")

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

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=2)

        ttk.Label(forms_lf, text='ex. Basic, Suite', style="small_info.TLabel",
                  justify="left").grid(column=1, row=3, sticky="w")

        ttk.Label(forms_lf, text='Room availability', style="h2.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, pady=2.5, sticky="w")

        self.room_availability_cb = ttk.Combobox(forms_lf)
        self.room_availability_cb['values'] = ('Reserved', 'Available', 'Fully Occupied', 'Maintenance')
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

        ttk.Label(forms_lf, text='Amenity price', style="h2.TLabel",
                  justify="left").grid(column=0, row=8, padx=2.5, pady=2.5, sticky="w")

        self.amenity_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.amenity_price_sp.grid(column=1, row=8, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=9, sticky="w")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # Insert values to entry widgets
        self.room_number_sp.insert(0, values[1])
        self.room_description_e.insert(0, values[2])
        self.room_type_cb.insert(0, values[3])
        self.room_availability_cb.insert(0, values[4])
        self.room_capacity_sp.insert(0, values[5])
        self.room_price_sp.insert(0, values[6])
        self.amenity_price_sp.insert(0, values[7])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.modify_basic_im_resized, compound="left",
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

        ttk.Label(forms_lf, text="optional", image=self.exclamation_im_resized, compound="left",
                  style="small_info.TLabel", justify="left").grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text='Room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=3, padx=2.5, pady=2.5, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb.grid(column=1, row=3, sticky="w")

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

        ttk.Label(forms_lf, text='Amenity price', style="h2.TLabel",
                  justify="left").grid(column=0, row=8, padx=2.5, pady=2.5, sticky="w")

        self.amenity_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.amenity_price_sp.grid(column=1, row=8, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=1, row=9, sticky="w")

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
        self.room_type_cb.insert(0, values[3])
        self.room_availability_cb.insert(0, values[4])
        self.room_capacity_sp.insert(0, values[5])
        self.room_price_sp.insert(0, values[6])
        self.amenity_price_sp.insert(0, values[7])

        # Disable widgets
        self.room_description_e.config(state="disabled")
        self.room_type_cb.config(state="disabled")
        self.room_availability_cb.config(state="disabled")
        self.room_capacity_sp.config(state="disabled")
        self.room_price_sp.config(state="disabled")
        self.amenity_price_sp.config(state="disabled")

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left", command=self.create_room_request).pack(side="left")

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
        self.room_price_sp.grid(column=1, row=0, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=2, row=0, sticky="w")

        ttk.Label(forms_lf, text='Room Type', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=1)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Set price", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.set_room_price_to_type_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to set the room price \naccording to room type!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def set_room_amenities_to_type_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Set amenity price")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Set amenity price',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", pady=10, fill="both", expand=True)

        ttk.Label(forms_lf, text='Amenity price', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.amenity_price_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.amenity_price_sp.grid(column=1, row=0, sticky="w")

        ttk.Label(forms_lf, text='per person', style="small_info.TLabel",
                  justify="left").grid(column=2, row=0, sticky="w")

        ttk.Label(forms_lf, text='Room Type', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=1)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Set price", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.set_amenities_price_to_type_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to set the amenity price \naccording to room type!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def set_room_capacity_to_type_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Set room capacity")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Set room capacity',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", pady=10, fill="both", expand=True)

        ttk.Label(forms_lf, text='Room capacity', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.room_capacity_sp = ttk.Spinbox(forms_lf, from_=0, to=99999, wrap=True)
        self.room_capacity_sp.grid(column=1, row=0, sticky="w")

        ttk.Label(forms_lf, text='Room Type', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=1)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Set capacity", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.set_room_capacity_to_type_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to set the room capacity \naccording to room type!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def set_room_type_to_type_dialog(self, event):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Set room prices")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Set room type',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", pady=10, fill="both", expand=True)

        ttk.Label(forms_lf, text='New room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.new_room_type_cb = ttk.Combobox(forms_lf)
        self.new_room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.new_room_type_cb.grid(column=1, row=0)

        ttk.Label(forms_lf, text='Current room type', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.room_type_cb = ttk.Combobox(forms_lf)
        self.room_type_cb['values'] = ('Large Single', 'Single Type', 'Shared Type')
        self.room_type_cb.grid(column=1, row=1)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Set room type", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.set_room_type_to_type_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to set a new room type \naccording to current room type!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def create_room_transaction_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create transaction")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        amount_to_be_paid = int(values[6]) + int(values[7])

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

        ttk.Label(forms1_lf, text='Payment Description', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.payment_description_cb = ttk.Combobox(forms1_lf, width=30)
        self.payment_description_cb['values'] = ('Confirmation fee',)
        self.payment_description_cb['state'] = 'readonly'
        self.payment_description_cb.current(0)
        self.payment_description_cb.grid(column=1, row=0, sticky="w")
        self.payment_description_cb.bind("<<ComboboxSelected>>", self.change_payment_information)

        tk.Button(forms1_lf, text=" Transaction info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.payment_transaction_help).grid(column=2, row=0, sticky="w")

        # Apply discount section
        ttk.Label(forms1_lf, text='Discount Code', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, rowspan=2, padx=2.5, pady=20, sticky="w")

        self.discount_code_e = ttk.Entry(forms1_lf, width=30)
        self.discount_code_e.grid(column=1, row=1, rowspan=2, sticky="w")

        apply_b_lf = tk.LabelFrame(forms1_lf, bd=1, bg="#585456", relief="flat")
        apply_b_lf.grid(column=2, row=1, rowspan=2, padx=5, sticky="w")

        tk.Button(apply_b_lf, text="Apply", font="OpenSans, 10", fg="#585456", bg="#FFFFFF",
                  relief="flat", command=self.apply_discount_request).pack(fill="x")

        # Payment information section
        ttk.Label(forms1_lf, text='Payment Information',
                  style="on.TLabel").grid(column=0, row=3, padx=2.5, sticky="w")

        ttk.Label(forms1_lf, text='Room price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=values[6], style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=4, sticky="w")

        ttk.Label(forms1_lf, text='Amenities price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=5, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=values[7], style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=5, sticky="w")

        ttk.Label(forms1_lf, text='Discount (%) ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, sticky="w")

        self.discount_l = ttk.Label(forms1_lf, text="None applied", style="small_info.TLabel", justify="left")
        self.discount_l.grid(column=1, row=6, sticky="w")

        ttk.Label(forms1_lf, text='Total amount  to be paid: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=7, padx=2.5, sticky="w")

        self.amount_to_be_paid_l = ttk.Label(forms1_lf, text=amount_to_be_paid,
                                             style="small_info.TLabel", justify="left")
        self.amount_to_be_paid_l.grid(column=1, row=7, sticky="w")

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
        self.payment_amount_sp.insert(0, amount_to_be_paid)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.create_room_transaction_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create transaction!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def create_room_assessment_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create Assessment")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        amount_to_be_paid = int(values[6]) + int(values[7])

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create Assessment',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms1_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms1_lf.pack(side="top", fill="both", pady=15, expand=True)

        ttk.Label(forms1_lf, text='Payment Description', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.payment_description_cb = ttk.Combobox(forms1_lf, width=30)
        self.payment_description_cb['values'] = ('Confirmation fee',)
        self.payment_description_cb['state'] = 'readonly'
        self.payment_description_cb.current(0)
        self.payment_description_cb.grid(column=1, row=0, sticky="w")
        self.payment_description_cb.bind("<<ComboboxSelected>>", self.change_payment_information)

        tk.Button(forms1_lf, text=" Transaction info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.payment_transaction_help).grid(column=2, row=0, sticky="w")

        # Payment information section
        ttk.Label(forms1_lf, text='Payment Information',
                  style="on.TLabel").grid(column=0, row=3, padx=2.5, sticky="w")

        ttk.Label(forms1_lf, text='Room price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=4, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=values[6], style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=4, sticky="w")

        ttk.Label(forms1_lf, text='Amenities price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=5, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=values[7], style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=5, sticky="w")

        ttk.Label(forms1_lf, text='Total amount  to be paid: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, sticky="w")

        self.amount_to_be_paid_l = ttk.Label(forms1_lf, text=amount_to_be_paid,
                                             style="small_info.TLabel", justify="left")
        self.amount_to_be_paid_l.grid(column=1, row=6, sticky="w")

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
        self.payment_amount_sp.insert(0, amount_to_be_paid)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.create_room_assessment_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create assessment!",
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

        tk.Button(title_lf, text=" Status info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.tenant_status_transaction_help).pack(side="right", anchor="ne", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Tenant Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_name_e = ttk.Entry(forms_lf, width=60)
        self.tenant_name_e.grid(column=1, row=0)
        self.tenant_name_e.focus()

        ttk.Label(forms_lf, text='Tenant Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.tenant_email_e = ttk.Entry(forms_lf, width=60)
        self.tenant_email_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text="optional", image=self.exclamation_im_resized, compound="left",
                  style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text='Tenant Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=3, padx=2.5, pady=2.5, sticky="w")

        self.tenant_status_cb = ttk.Combobox(forms_lf)
        self.tenant_status_cb['values'] = ("Newly registered", "Application", "Confirmation", 'Processing',
                                           "Monthly rental fee", 'Inactive', "Delinquent")
        self.tenant_status_cb.current(0)
        self.tenant_status_cb.grid(column=1, row=3, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create account", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
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

        tk.Button(title_lf, text=" Status info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.tenant_status_transaction_help).pack(side="right", anchor="ne", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Tenant Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_name_e = ttk.Entry(forms_lf, width=60)
        self.tenant_name_e.grid(column=1, row=0)
        self.tenant_name_e.focus()

        ttk.Label(forms_lf, text='Tenant Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.tenant_email_e = ttk.Entry(forms_lf, width=60)
        self.tenant_email_e.grid(column=1, row=1)

        ttk.Label(forms_lf, text="optional", image=self.exclamation_im_resized, compound="left",
                  style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text='Tenant Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=3, padx=2.5, pady=2.5, sticky="w")

        self.tenant_status_cb = ttk.Combobox(forms_lf)
        self.tenant_status_cb['values'] = ("Newly registered", "Application", "Confirmation", 'Processing',
                                           "Monthly rental fee", 'Inactive', "Delinquent")
        self.tenant_status_cb.current(0)
        self.tenant_status_cb.grid(column=1, row=3, sticky="w")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # Insert values to entry widgets
        self.tenant_name_e.insert(0, values[1])
        self.tenant_email_e.insert(0, values[5])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.modify_basic_im_resized, compound="left",
                  command=self.modify_tenant_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to modify tenant account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def create_tenant_transaction_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create transaction")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create transaction',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(title_lf, text=" Transaction info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.payment_transaction_help).pack(side="right", anchor="ne", padx=5, pady=5)

        forms1_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms1_lf.pack(side="top", fill="both", pady=15, expand=True)

        ttk.Label(forms1_lf, text='Payment Description', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.payment_description_cb = ttk.Combobox(forms1_lf, width=30)
        self.payment_description_cb['values'] = ('Application fee', 'Processing fee', 'Monthly rental fee')
        self.payment_description_cb.current(0)
        self.payment_description_cb.grid(column=1, row=0, sticky="w")
        self.payment_description_cb.bind("<<ComboboxSelected>>", self.change_payment_information)

        # Apply discount section
        ttk.Label(forms1_lf, text='Discount Code', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, rowspan=2, padx=2.5, pady=20, sticky="w")

        self.discount_code_e = ttk.Entry(forms1_lf, width=30)
        self.discount_code_e.grid(column=1, row=1, rowspan=2, sticky="w")

        apply_b_lf = tk.LabelFrame(forms1_lf, bd=1, bg="#585456", relief="flat")
        apply_b_lf.grid(column=2, row=1, rowspan=2, padx=5, sticky="w")

        tk.Button(apply_b_lf, text="Apply", font="OpenSans, 10", fg="#585456", bg="#FFFFFF",
                  relief="flat", command=self.apply_discount_request).pack(fill="x")

        # Payment information section
        ttk.Label(forms1_lf, text='Payment Information',
                  style="on.TLabel").grid(column=0, row=3, padx=2.5, sticky="w")

        self.payment_description_l = ttk.Label(forms1_lf, text='Application fee: ', style="small_info.TLabel",
                                               justify="left")
        self.payment_description_l.grid(column=0, row=4, padx=2.5, sticky="w")

        self.application_fee_l = ttk.Label(forms1_lf, text=500, style="small_info.TLabel", justify="left")
        self.application_fee_l.grid(column=1, row=4, sticky="w")

        ttk.Label(forms1_lf, text='-------------------------',
                  style="on.TLabel").grid(column=0, row=5, padx=2.5, sticky="w")

        ttk.Label(forms1_lf, text='Room price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=0, style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=6, sticky="w")

        ttk.Label(forms1_lf, text='Amenities price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=7, padx=2.5, sticky="w")

        self.amenities_cost_l = ttk.Label(forms1_lf, text=0, style="small_info.TLabel", justify="left")
        self.amenities_cost_l.grid(column=1, row=7, sticky="w")

        ttk.Label(forms1_lf, text='Discount (%) ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=8, padx=2.5, sticky="w")

        self.discount_l = ttk.Label(forms1_lf, text="None applied", style="small_info.TLabel", justify="left")
        self.discount_l.grid(column=1, row=8, sticky="w")

        ttk.Label(forms1_lf, text='Total amount  to be paid: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=9, padx=2.5, sticky="w")

        self.amount_to_be_paid_l = ttk.Label(forms1_lf, text=500,
                                             style="small_info.TLabel", justify="left")
        self.amount_to_be_paid_l.grid(column=1, row=9, sticky="w")

        forms2_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms2_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms2_lf, text='Tenant ID', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        ttk.Label(forms2_lf, text=self.tenant_id, style="small_info.TLabel",
                  justify="left").grid(column=1, row=0, sticky="w")

        ttk.Label(forms2_lf, text='Payment Amount', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.payment_amount_sp = ttk.Spinbox(forms2_lf, from_=0, to=99999, wrap=True)
        self.payment_amount_sp.grid(column=1, row=1, sticky="w")
        self.payment_amount_sp.insert(0, 500)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.create_tenant_transaction_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create transaction!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def create_assessment_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create assessment")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Create assessment',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(title_lf, text=" Assessment info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.payment_transaction_help).pack(side="right", anchor="ne", padx=5, pady=5)

        forms1_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms1_lf.pack(side="top", fill="both", pady=15, expand=True)

        ttk.Label(forms1_lf, text='Payment Description', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.payment_description_cb = ttk.Combobox(forms1_lf, width=30)
        self.payment_description_cb['values'] = ('Application fee', 'Processing fee', 'Monthly rental fee')
        self.payment_description_cb.current(0)
        self.payment_description_cb.grid(column=1, row=0, sticky="w")
        self.payment_description_cb.bind("<<ComboboxSelected>>", self.change_payment_information)

        # Payment information section
        ttk.Label(forms1_lf, text='Assessment Information',
                  style="on.TLabel").grid(column=0, row=3, padx=2.5, sticky="w")

        self.payment_description_l = ttk.Label(forms1_lf, text='Application fee: ', style="small_info.TLabel",
                                               justify="left")
        self.payment_description_l.grid(column=0, row=4, padx=2.5, sticky="w")

        self.application_fee_l = ttk.Label(forms1_lf, text=500, style="small_info.TLabel", justify="left")
        self.application_fee_l.grid(column=1, row=4, sticky="w")

        ttk.Label(forms1_lf, text='-------------------------',
                  style="on.TLabel").grid(column=0, row=5, padx=2.5, sticky="w")

        ttk.Label(forms1_lf, text='Room price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=6, padx=2.5, sticky="w")

        self.room_cost_l = ttk.Label(forms1_lf, text=0, style="small_info.TLabel", justify="left")
        self.room_cost_l.grid(column=1, row=6, sticky="w")

        ttk.Label(forms1_lf, text='Amenities price: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=7, padx=2.5, sticky="w")

        self.amenities_cost_l = ttk.Label(forms1_lf, text=0, style="small_info.TLabel", justify="left")
        self.amenities_cost_l.grid(column=1, row=7, sticky="w")

        ttk.Label(forms1_lf, text='Total amount  to be paid: ', style="small_info.TLabel",
                  justify="left").grid(column=0, row=9, padx=2.5, sticky="w")

        self.amount_to_be_paid_l = ttk.Label(forms1_lf, text=500,
                                             style="small_info.TLabel", justify="left")
        self.amount_to_be_paid_l.grid(column=1, row=9, sticky="w")

        forms2_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms2_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms2_lf, text='Tenant ID', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        ttk.Label(forms2_lf, text=self.tenant_id, style="small_info.TLabel",
                  justify="left").grid(column=1, row=0, sticky="w")

        ttk.Label(forms2_lf, text='Payment Amount', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.payment_amount_sp = ttk.Spinbox(forms2_lf, from_=0, to=99999, wrap=True)
        self.payment_amount_sp.grid(column=1, row=1, sticky="w")
        self.payment_amount_sp.insert(0, 500)

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.create_assessment_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create assessment!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def send_assessment_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Send digital assessment")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x", pady=10)

        ttk.Label(title_lf, text='Send digital assessment',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(forms_lf, text='Tenant Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_email_e = ttk.Entry(forms_lf, width=30)
        self.tenant_email_e.grid(column=1, row=0)
        self.tenant_email_e.insert(0, values[10])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Send receipt", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.send_assessment_email_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to send assessment via email",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # Payment
    def send_receipt_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Send digital receipt")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x", pady=10)

        ttk.Label(title_lf, text='Send digital receipt',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(forms_lf, text='Tenant Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_email_e = ttk.Entry(forms_lf, width=30)
        self.tenant_email_e.grid(column=1, row=0)
        self.tenant_email_e.insert(0, values[11])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text="Send receipt", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.send_receipt_email_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to send receipt via email",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    # Booking
    def register_tenant_account_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Register tenant account")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        # ================================================ Main interface ==============================================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Register tenant account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        tk.Button(title_lf, text=" Status info", font=("OpenSans", 10), fg='#585456', bg="#FFFFFF", relief="flat",
                  image=self.exclamation_im_resized, compound="left",
                  command=self.tenant_status_transaction_help).pack(side="right", anchor="ne", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        ttk.Label(forms_lf, text='Tenant Name', style="h2.TLabel",
                  justify="left").grid(column=0, row=0, padx=2.5, pady=2.5, sticky="w")

        self.tenant_name_e = ttk.Entry(forms_lf, width=60)
        self.tenant_name_e.grid(column=1, row=0)
        self.tenant_name_e.insert(0, values[1])

        ttk.Label(forms_lf, text='Tenant Email', style="h2.TLabel",
                  justify="left").grid(column=0, row=1, padx=2.5, pady=2.5, sticky="w")

        self.tenant_email_e = ttk.Entry(forms_lf, width=60)
        self.tenant_email_e.grid(column=1, row=1)
        self.tenant_email_e.insert(0, values[2])

        ttk.Label(forms_lf, text="optional", image=self.exclamation_im_resized, compound="left",
                  style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(forms_lf, text='Tenant Status', style="h2.TLabel",
                  justify="left").grid(column=0, row=3, padx=2.5, pady=2.5, sticky="w")

        self.tenant_status_cb = ttk.Combobox(forms_lf)
        self.tenant_status_cb['values'] = ("Newly registered", "Application", "Confirmation", 'Active', 'Inactive',
                                           "Delinquent")
        self.tenant_status_cb.current(0)
        self.tenant_status_cb.grid(column=1, row=3, sticky="w")

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Register account", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
                  command=self.register_tenant_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to register the tenant account!",
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

        tk.Button(buttons_lf, text="Create", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.add_basic_im_resized, compound="left",
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

        tk.Button(buttons_lf, text="Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#89CFF0", relief="flat",
                  image=self.modify_basic_im_resized, compound="left",
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

        tk.Button(buttons_lf, text=" Continue", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  image=self.add_admin_im_resized, compound="left",
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

        tk.Button(buttons_lf, text=" Create", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  image=self.add_admin_im_resized, compound="left",
                  command=self.create_employee_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to create an\n employee account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

        print(event)

    def modify_employee_dialog(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Create employee account")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Modify employee account',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='admin',
                  style="small.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        forms_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        forms_lf.pack(side="top", fill="both", expand=True)

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

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

        # Insert values to entry widgets
        self.employee_username_e.insert(0, values[1])
        self.employee_password_e.insert(0, values[2])
        self.employee_role_e.insert(0, values[3])

        buttons_lf = tk.LabelFrame(main_lf, padx=20, pady=20, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", fill="both", expand=True)

        tk.Button(buttons_lf, text=" Modify", font="OpenSans, 10", fg="#FFFFFF", bg="#4C8404", relief="flat",
                  image=self.modify_admin_im_resized, compound="left",
                  command=self.modify_employee_request).pack(side="left")

        ttk.Label(buttons_lf, text="Click here to modify an\n employee account!",
                  style="small_info.TLabel").pack(side="left", padx=10)

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

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

        self.admin_access_password_e = ttk.Entry(forms_lf, width=60, show="*")
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
        elif not self.signin_password_e.get():
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

                self.admin_access_bool = True
                self.basic_user_access_bool = False

                # Instantiate methods
                self.admin_get_current_user()

                # Set temporary basic user id
                self.basic_user_id_str = "0"

                # Record action history
                self.action_description = "Admin Sign in"
                self.action_history_request()

                # Go to main interface
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
        elif not self.signin_password_e.get():
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

                self.admin_access_bool = False
                self.basic_user_access_bool = True

                # Instantiate create_widgets method
                self.basic_user_get_id_request()
                self.basic_user_get_current_user()

                # Record action history
                self.action_description = "Basic User Sign in"
                self.action_history_request()

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

        # Converts the tuple into string
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
        elif not self.signup_password_e.get():
            self.invalid_input()
        elif not self.signup_email_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO admin (username, password, email, date_created, time_created)"
                                      "VALUES (%s,%s,%s,%s,%s)", (self.signup_username_e.get(),
                                                                  self.signup_password_e.get(),
                                                                  self.signup_email_e.get(), date_str, time_str))

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
        elif not self.room_type_cb.get():
            self.invalid_input()
        elif not self.room_availability_cb.get():
            self.invalid_input()
        elif not self.room_capacity_sp.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO room (room_number, room_description, room_type, room_availability,"
                                      " room_capacity, admin_id, room_price, amenities_price) VALUES (%s,%s,%s,%s,%s,"
                                      "%s,%s,%s)",
                                      (self.room_number_sp.get(), self.room_description_e.get(),
                                       self.room_type_cb.get(),
                                       self.room_availability_cb.get(), self.room_capacity_sp.get(), self.admin_id_str,
                                       self.room_price_sp.get(), self.amenity_price_sp.get()))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Room is  created")

                self.dialog_box_top.destroy()

            except Exception as e:
                self.invalid_input()
                print(e)

    def modify_room_request(self):
        if not self.room_number_sp.get():
            self.invalid_input()
        elif not self.room_availability_cb.get():
            self.invalid_input()
        elif not self.room_capacity_sp.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("UPDATE room SET room_number = '"
                                      + self.room_number_sp.get() + "', room_description = '"
                                      + self.room_description_e.get() + "', room_type = '"
                                      + self.room_type_cb.get() + "', room_availability = '"
                                      + self.room_availability_cb.get() + "', room_capacity = '"
                                      + self.room_capacity_sp.get() + "', room_price = '"
                                      + self.room_price_sp.get() + "', amenities_price = '"
                                      + self.amenity_price_sp.get() + "' WHERE room_id = '"
                                      + self.room_id + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Room information is modified")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def room_info_treeview_request(self):
        Content_control.clear_treeview(self.info_tree)
        # Connect to database
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() in ['Room ID', 'Date Created']:
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False ORDER BY r.room_id ASC;")
        elif self.order_by_cb.get() == 'Room Number':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False ORDER BY r.room_number ASC;")
        elif self.order_by_cb.get() == 'Room Type':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False ORDER BY r.room_type ASC;")
        elif self.order_by_cb.get() == 'Room Availability':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False ORDER BY r.room_availability ASC;")
        elif self.order_by_cb.get() == 'Room Capacity':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False ORDER BY r.room_capacity ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT r.room_id, r.room_number, r.room_description, r.room_type, "
                                  "r.room_availability, r.room_capacity, r.room_price, r.amenities_price, "
                                  "r.current_occupants FROM room r where admin_id = '"
                                  + str(self.admin_id_str) + "' AND deleted = False;")

        rooms = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in rooms:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7], record[8]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7], record[8]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def set_room_price_to_type_request(self):
        if not self.room_price_sp.get():
            self.invalid_input()
        elif not self.room_type_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE room SET room_price='" + self.room_price_sp.get() + "' WHERE admin_id='" +
                                      str(self.admin_id_str) + "' and room_type='" + self.room_type_cb.get() + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Set room price successfully")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def set_amenities_price_to_type_request(self):
        if not self.amenity_price_sp.get():
            self.invalid_input()
        elif not self.room_type_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE room SET amenities_price='" + self.amenity_price_sp.get() +
                                      "' WHERE admin_id='" +
                                      str(self.admin_id_str) + "' and room_type='" + self.room_type_cb.get() + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Set room price successfully")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def set_room_capacity_to_type_request(self):
        if not self.room_capacity_sp.get():
            self.invalid_input()
        elif not self.room_type_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE room SET room_capacity='" + self.room_capacity_sp.get() +
                                      "' WHERE admin_id='" + self.admin_id_str + "' and room_type='"
                                      + self.room_type_cb.get() + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Set room capacity successfully")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def set_room_type_to_type_request(self):
        if not self.new_room_type_cb.get():
            self.invalid_input()
        elif not self.room_type_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE room SET room_type='" + self.new_room_type_cb.get() +
                                      "' WHERE admin_id='" + str(self.admin_id_str) + "' and room_type='"
                                      + self.room_type_cb.get() + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Changed room type successfully")

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def create_room_transaction_request(self):
        if not self.tenant_id_sp.get():
            self.invalid_input()
        elif not self.payment_amount_sp.get():
            self.invalid_input()
        else:
            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")
            print(values)

            capacity = int(values[5])
            current_occupant = int(values[8])

            if capacity <= current_occupant:
                messagebox.showerror("Error", "The room is currently fully occupied.")
            else:
                self.database_connect()

                self.mycursor.execute(
                    "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '"
                    + self.admin_id_str + "' AND tenant_id = '" + self.tenant_id_sp.get() + "';")

                # Converts the tuple into integer
                balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

                if capacity > current_occupant + 1:
                    # Room will not be fully occupied

                    # Insert values to payment
                    self.mycursor.execute("INSERT INTO payment (payment_amount, room_id, tenant_id, admin_id, "
                                          "basic_user_id, date_created, time_created, discount_code, "
                                          "payment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                          (self.payment_amount_sp.get(), self.room_id, self.tenant_id_sp.get(),
                                           self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                           self.discount_code_e.get(), self.payment_description_cb.get()))

                    # Update tenant_status to confirmation
                    self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                          + str(float(balance) - float(self.payment_amount_sp.get())) +
                                          "', tenant_status = 'Confirmation', room_id = '"
                                          + self.room_id + "' WHERE tenant_id = '"
                                          + self.tenant_id_sp.get() + "' AND admin_id = '"
                                          + self.admin_id_str + "';")

                    # Update room column
                    self.mycursor.execute("UPDATE room SET current_occupants = '"
                                          + str(current_occupant + 1) + "' WHERE room_id = '"
                                          + self.room_id + "' AND admin_id = '" + self.admin_id_str + "';")

                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Payment is created")

                else:
                    # Room will be fully occupied

                    # Insert values to payment
                    self.mycursor.execute("INSERT INTO payment (payment_amount, room_id, tenant_id, admin_id, "
                                          "basic_user_id, date_created, time_created, discount_code, "
                                          "payment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                          (self.payment_amount_sp.get(), str(self.room_id),
                                           self.tenant_id_sp.get(),
                                           self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                           self.discount_code_e.get(), self.payment_description_cb.get()))

                    # Update room to be Fully Occupied
                    self.mycursor.execute("UPDATE room SET room_availability = 'Fully Occupied', "
                                          "current_occupants = '"
                                          + str(current_occupant + 1) + "' WHERE room_id = '"
                                          + self.room_id + "' AND admin_id = '" + self.admin_id_str + "';")

                    # Update tenant to confirmation
                    self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                          + str(float(balance) - float(self.payment_amount_sp.get())) +
                                          "', tenant_status = 'Confirmation', room_id = '"
                                          + self.room_id + "' WHERE tenant_id = '"
                                          + self.tenant_id_sp.get() + "' AND admin_id = '"
                                          + self.admin_id_str + "';")

                    # Insert to notif that room is_status is changed to fully occupied
                    self.mycursor.execute("INSERT INTO notif (notif_subject, notif_description, "
                                          "date_created, time_created, admin_id) VALUES (%s,%s,%s,%s,%s)",
                                          ('Room Availability',
                                           ('Room ' + self.room_id + ' is already Fully Occupied'), date_str, time_str,
                                           self.admin_id_str))
                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Payment is created")

        # ================================ Discount applied ============================================================
        if self.discount_applied_bool:
            self.database_connect()

            self.mycursor.execute(
                "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '"
                + self.admin_id_str + "' AND tenant_id = '" + self.tenant_id_sp.get() + "';")

            # Converts the tuple into integer
            balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

            self.mycursor.execute("INSERT INTO payment (payment_amount, tenant_id, admin_id, basic_user_id, "
                                  "date_created, time_created, discount_code, payment_description) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.discount_reduction, self.tenant_id_sp.get(),
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.discount_code_e.get(), "Discount applied"))
            # Update balance
            self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                  + str(float(balance) - float(self.discount_reduction)) +
                                  "' WHERE tenant_id = '" + self.tenant_id_sp.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "';")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            print("Discount is applied.")
        else:
            print("Discount is not applied.")

        self.dialog_box_top.destroy()

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
            confirmation = messagebox.askokcancel("Confirm deletion", "Are you sure you want to delete this "
                                                                      "value?")
            if confirmation:
                self.database_connect()
                # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

                # Grab record number
                selected = self.info_tree.focus()

                # Grab record values
                values = self.info_tree.item(selected, "values")

                self.mycursor.execute("UPDATE room SET deleted = True WHERE room_id = '"
                                      + values[0] + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Removed room successfully")
            else:
                pass

        except Exception as e:
            self.invalid_input()
            print(e)

    def create_room_assessment_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        # Connect to database
        self.database_connect()

        self.mycursor.execute(
            "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '" + self.admin_id_str + "' AND tenant_id = '"
            + self.tenant_id_sp.get() + "';")

        # Converts the tuple into integer
        balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

        if not self.payment_amount_sp.get():
            self.invalid_input()
        elif self.payment_description_cb.get() == "Confirmation fee":
            # Insert values to assessment
            self.mycursor.execute("INSERT INTO assessment (assessment_amount, room_id, tenant_id, admin_id, "
                                  "basic_user_id, date_created, time_created, assessment_description) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.payment_amount_sp.get(), values[0], self.tenant_id_sp.get(),
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.payment_description_cb.get()))

            self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                  + str(float(balance) + float(self.payment_amount_sp.get())) + "' WHERE tenant_id = '"
                                  + self.tenant_id_sp.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "';")

            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Assessment is  created")

            self.dialog_box_top.destroy()
        else:
            pass

        # Record action history
        self.action_description = "Assessment created for tenant id " + str(self.tenant_id_sp.get()) + "."
        self.action_history_request()

    # Dashboard
    def generate_sales_report_request(self):
        pandasdb = mysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database="hmsdatabase",
                                 use_pure=True)

        query = "Select p.payment_id, p.payment_amount, p.tenant_id, t.tenant_name, p.date_created FROM payment p " \
                "INNER JOIN tenant t WHERE p.date_created >= '" \
                + self.dashboard_filter_from.get() + "' AND p.date_created <= '" \
                + self.dashboard_filter_to.get() + "' AND p.tenant_id = t.tenant_id AND p.admin_id = '" \
                + self.admin_id_str + "';"

        df = pd.read_sql(query, pandasdb)
        pandasdb.close()

        print("Payments dataframe")
        print(df.sum())

        file = filedialog.asksaveasfilename(defaultextension=".xlsx")
        df.to_excel(file)

    # Tenant
    def create_tenant_request(self):
        if not self.tenant_name_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("INSERT INTO tenant (tenant_name, tenant_email, tenant_status, date_created, "
                                      "time_created, admin_id) VALUES (%s,%s,%s,%s,%s,%s)",
                                      (self.tenant_name_e.get(), self.tenant_email_e.get(), self.tenant_status_cb.get(),
                                       date_str, time_str, self.admin_id_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Tenant's account is created")

                # Record action history
                self.action_description = "Tenant named" + self.tenant_name_e.get() + "is created."
                self.action_history_request()

                self.dialog_box_top.destroy()

            except Exception as e:
                self.invalid_input()
                print(e)

    def modify_tenant_request(self):
        if not self.tenant_name_e.get():
            self.invalid_input()
        elif not self.tenant_status_cb.get():
            self.invalid_input()
        else:
            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")
            print(values)
            print("inactive")

            if self.tenant_status_cb.get() == 'Inactive':
                try:
                    self.database_connect()
                    self.mycursor.execute("UPDATE room SET current_occupants = current_occupants - 1, "
                                          "room_availability = 'Available' WHERE room_id = '"
                                          + values[3] + "' AND admin_id = '" + self.admin_id_str + "';")

                    self.mycursor.execute("UPDATE tenant SET tenant_name = '"
                                          + self.tenant_name_e.get() + "', tenant_email= '"
                                          + self.tenant_email_e.get() + "', tenant_status = '"
                                          + self.tenant_status_cb.get() + "', room_id = 'None'  WHERE tenant_id = '"
                                          + self.tenant_id + "';")

                    self.mycursor.execute("INSERT INTO notif (notif_subject, notif_description, "
                                          "date_created, admin_id) VALUES (%s,%s,%s,%s)",
                                          ('Modify tenant',
                                           ('Tenant information of ' + self.tenant_name_e.get() + ' is modified.'),
                                           date_str, self.admin_id_str))

                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Tenant information is modified successfully")

                    self.dialog_box_top.destroy()

                except Exception as e:
                    self.invalid_input()
                    print(e)

            else:
                try:
                    self.database_connect()

                    self.mycursor.execute("UPDATE tenant SET tenant_name = '"
                                          + self.tenant_name_e.get() + "', tenant_email= '"
                                          + self.tenant_email_e.get() + "', tenant_status = '"
                                          + self.tenant_status_cb.get() + "'  WHERE tenant_id = '"
                                          + self.tenant_id + "';")

                    self.mycursor.execute("INSERT INTO notif (notif_subject, notif_description, "
                                          "date_created, admin_id) VALUES (%s,%s,%s,%s)",
                                          ('Modify tenant',
                                           ('Tenant information of ' + self.tenant_name_e.get() + ' is modified.'),
                                           date_str, self.admin_id_str))

                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Tenant information is modified successfully")

                    self.dialog_box_top.destroy()

                except Exception as e:
                    self.invalid_input()
                    print(e)

    def tenant_info_treeview_request(self):
        Content_control.clear_treeview(self.info_tree)
        # Connect to database
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Tenant ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT t.tenant_id, t.tenant_name, t.tenant_status, t.room_id,"
                                  "t.tenant_balance, t.tenant_email, t.date_created, t.time_created FROM tenant t "
                                  "WHERE t.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND t.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY t.tenant_id DESC;")
        elif self.order_by_cb.get() == 'Tenant Name':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT t.tenant_id, t.tenant_name, t.tenant_status, t.room_id,"
                                  "t.tenant_balance, t.tenant_email, t.date_created, t.time_created FROM tenant t "
                                  "WHERE t.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND t.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY t.tenant_name ASC;")
        elif self.order_by_cb.get() == 'Status':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT t.tenant_id, t.tenant_name, t.tenant_status, t.room_id,"
                                  "t.tenant_balance, t.tenant_email, t.date_created, t.time_created FROM tenant t "
                                  "WHERE t.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND t.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY t.tenant_status ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT t.tenant_id, t.tenant_name, t.tenant_status, t.room_id,"
                                  "t.tenant_balance, t.tenant_email, t.date_created, t.time_created FROM tenant t "
                                  "WHERE t.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND t.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY t.date_created ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT t.tenant_id, t.tenant_name, t.tenant_status, t.room_id,"
                                  "t.tenant_balance, t.tenant_email, t.date_created, t.time_created FROM tenant t "
                                  "WHERE t.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND t.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False;")

        tenants = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in tenants:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]), tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]), tags=("evenrow",))
            count += 1

        self.mycursor.close()

    def remove_tenant_account_request(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                confirmation = messagebox.askokcancel("Confirm deletion", "Are you sure you want to delete this "
                                                                          "value?")
                if confirmation:

                    # Grab record number
                    selected = self.info_tree.focus()

                    # Grab record values
                    values = self.info_tree.item(selected, "values")

                    self.database_connect()

                    if values[3] == 'None':
                        # self.mycursor.execute("DELETE FROM tenant WHERE tenant_id = '" + self.tenant_id + "';")
                        self.mycursor.execute("UPDATE tenant SET deleted = True WHERE tenant_id = '"
                                              + self.tenant_id + "';")

                        self.db1.commit()
                        self.db1.close()
                        self.mycursor.close()

                        messagebox.showinfo("Success", "Removed tenant account successfully")
                    else:
                        # self.mycursor.execute("DELETE FROM tenant WHERE tenant_id = '" + self.tenant_id + "';")
                        self.mycursor.execute("UPDATE tenant SET deleted = True WHERE tenant_id = '"
                                              + self.tenant_id + "';")

                        self.mycursor.execute("UPDATE room SET current_occupants = current_occupants - 1, "
                                              "room_availability = 'Available' WHERE room_id = '"
                                              + values[3] + "' AND admin_id = '" + self.admin_id_str + "';")

                        self.db1.commit()
                        self.db1.close()
                        self.mycursor.close()

                        messagebox.showinfo("Success", "Deleted tenant account successfully")

                # Turn off admin access if account is basic user
                self.basic_user_status()

            except Exception as e:
                messagebox.showinfo("Error", "Unsuccessful in removing account")
                print(e)

    def create_tenant_transaction_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        # Connect to database
        self.database_connect()

        if not self.payment_amount_sp.get():
            self.invalid_input()

        elif self.payment_description_cb.get() == "Application fee":
            self.mycursor.execute("INSERT INTO payment (payment_amount, tenant_id, admin_id, "
                                  "basic_user_id, date_created, time_created, discount_code, payment_description) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.payment_amount_sp.get(), self.tenant_id,
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.discount_code_e.get(), self.payment_description_cb.get()))

            # Update balance
            self.mycursor.execute("UPDATE tenant SET tenant_status = 'Application', tenant_balance = '"
                                  + str(float(values[4]) - float(self.payment_amount_sp.get())) +
                                  "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                  + self.admin_id_str + "';")

            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Transaction is  created")
            print("Application")

        elif self.payment_description_cb.get() == "Processing fee":
            print(values[3])
            if values[3] == 'None':
                messagebox.showerror("Error", "Cannot proceed with the payment. "
                                              "No Room ID available, please pay Confirmation fee first.")
            else:
                self.database_connect()

                # Insert data
                self.mycursor.execute("INSERT INTO payment (payment_amount, room_id, tenant_id, "
                                      "admin_id, basic_user_id, date_created, time_created, discount_code, "
                                      "payment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), values[3], str(self.tenant_id),
                                       self.admin_id_str, str(self.basic_user_id_str), date_str, time_str,
                                       self.discount_code_e.get(), self.payment_description_cb.get()))
                # Update balance
                self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                      + str(float(values[4]) - float(self.payment_amount_sp.get())) +
                                      "', tenant_status = 'Processing' WHERE tenant_id = '"
                                      + str(self.tenant_id) + "' AND admin_id = '"
                                      + self.admin_id_str + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Payment is created")

        elif self.payment_description_cb.get() == "Monthly rental fee":
            print(values[3])
            if values[3] == 'None':
                messagebox.showerror("Error", "Cannot proceed with the payment. "
                                              "No Room ID available, please pay Confirmation fee\n"
                                              "and Processing fee first.")
            else:
                self.database_connect()

                # Insert data
                self.mycursor.execute("INSERT INTO payment (payment_amount, room_id, tenant_id, "
                                      "admin_id, basic_user_id, date_created, time_created, discount_code, "
                                      "payment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), values[3], str(self.tenant_id),
                                       self.admin_id_str, str(self.basic_user_id_str), date_str, time_str,
                                       self.discount_code_e.get(), self.payment_description_cb.get()))
                # Update balance
                self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                      + str(float(values[4]) - float(self.payment_amount_sp.get())) +
                                      "', tenant_status = 'Monthly rental fee' WHERE tenant_id = '"
                                      + str(self.tenant_id) + "' AND admin_id = '"
                                      + self.admin_id_str + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Payment is created")

        else:
            self.database_connect()
            self.mycursor.execute("INSERT INTO payment (payment_amount, tenant_id, admin_id, "
                                  "basic_user_id, date_created, time_created, discount_code, payment_description) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.payment_amount_sp.get(), self.tenant_id,
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.discount_code_e.get(), self.payment_description_cb.get()))
            # Update balance
            self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                  + str(float(values[4]) - float(self.payment_amount_sp.get())) +
                                  "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                  + self.admin_id_str + "';")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Transaction is  created")

        # ================================ Discount applied ============================================================
        if self.discount_applied_bool:
            print(self.discount_applied_bool)
            self.database_connect()

            self.mycursor.execute(
                "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '" + self.admin_id_str +
                "' AND tenant_id = '" + self.tenant_id + "';")

            # Converts the tuple into integer
            balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

            self.mycursor.execute("INSERT INTO payment (payment_amount, tenant_id, admin_id, basic_user_id, "
                                  "date_created, time_created, discount_code, payment_description) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.discount_reduction, self.tenant_id,
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.discount_code_e.get(), "Discount applied"))
            # Update balance
            self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                  + str(float(balance) - float(self.discount_reduction)) +
                                  "' WHERE tenant_id = '" + self.tenant_id + "' AND admin_id = '"
                                  + self.admin_id_str + "';")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            print("Discount is applied.")
        else:
            print("Discount is not applied.")

        self.dialog_box_top.destroy()

    def create_assessment_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        # Connect to database
        self.database_connect()

        if not self.payment_amount_sp.get():
            self.invalid_input()
        elif self.payment_description_cb.get() == "Application fee":
            try:
                # Insert values to assessment
                self.mycursor.execute("INSERT INTO assessment (assessment_amount, tenant_id, admin_id, "
                                      "basic_user_id, date_created, time_created, assessment_description) "
                                      "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), self.tenant_id,
                                       self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                       self.payment_description_cb.get()))

                self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                      + str(int(values[4]) + int(self.payment_amount_sp.get())) +
                                      "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                      + self.admin_id_str + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Assessment is  created")
                print("Application")

                self.dialog_box_top.destroy()

            except Exception as e:
                self.invalid_request()
                print(e)
        elif self.payment_description_cb.get() == "Processing fee":
            if values[3] == 'None':
                messagebox.showerror("Error", "Cannot proceed with the payment. "
                                              "No Room ID available, please pay Confirmation fee first.")
            else:
                self.database_connect()
                # Insert values to assessment
                self.mycursor.execute("INSERT INTO assessment (assessment_amount, room_id, tenant_id, "
                                      "admin_id, basic_user_id, date_created, time_created, "
                                      "assessment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), values[3], str(self.tenant_id),
                                       self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                       self.payment_description_cb.get()))

                # Update balance
                self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                      + str(int(values[4]) + int(self.payment_amount_sp.get())) +
                                      "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                      + self.admin_id_str + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Assessment is created")

                self.dialog_box_top.destroy()
        elif self.payment_description_cb.get() == "Monthly rental fee":
            if values[3] == 'None':
                messagebox.showerror("Error", "Cannot proceed with the payment. "
                                              "No Room ID available, please pay Confirmation fee\n"
                                              "and Processing fee first.")
            else:
                self.database_connect()

                # Insert values to assessment
                self.mycursor.execute("INSERT INTO assessment (assessment_amount, room_id, tenant_id, "
                                      "admin_id, basic_user_id, date_created, time_created, "
                                      "assessment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (self.payment_amount_sp.get(), values[3], str(self.tenant_id),
                                       self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                       self.payment_description_cb.get()))
                # Update balance
                self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                      + str(int(values[4]) + int(self.payment_amount_sp.get())) +
                                      "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                      + self.admin_id_str + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Assessment is created")

                self.dialog_box_top.destroy()
        else:
            self.database_connect()
            # Insert values to assessment
            self.mycursor.execute("INSERT INTO assessment (assessment_amount, room_id, tenant_id, "
                                  "admin_id, basic_user_id, date_created, time_created, "
                                  "assessment_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.payment_amount_sp.get(), values[3], str(self.tenant_id),
                                   self.admin_id_str, self.basic_user_id_str, date_str, time_str,
                                   self.payment_description_cb.get()))

            # Update balance
            self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                  + str(int(values[4]) + int(self.payment_amount_sp.get())) +
                                  "' WHERE tenant_id = '" + str(self.tenant_id) + "' AND admin_id = '"
                                  + self.admin_id_str + "';")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Assessment is created")

            self.dialog_box_top.destroy()

        # Record action history
        self.action_description = "Assessment created for tenant id " + str(self.tenant_id) + "."
        self.action_history_request()

    # Assessment
    def assessment_info_treeview_request(self):
        try:
            # Connect to database
            self.database_connect()

            # Conditions for tenant ID
            if not self.tenant_id_filter_sp.get():
                print("tenant id filter empty")
                # Conditions for order by filter
                if self.order_by_cb.get() == 'Assessment ID':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' ORDER BY a.assessment_id DESC;")
                elif self.order_by_cb.get() == 'Tenant Name':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' ORDER BY t.tenant_name ASC;")
                elif self.order_by_cb.get() == 'Assessment Description':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' ORDER BY a.assessment_description ASC;")
                elif self.order_by_cb.get() == 'Date Created':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' ORDER BY a.date_created ASC;")
                else:
                    print('Safety condition')
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "';")
            else:
                print("tenant id filter not empty")
                # Conditions for order by filter
                if self.order_by_cb.get() == 'Assessment ID':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' AND a.tenant_id = '"
                                          + self.tenant_id_filter_sp.get() + "' ORDER BY a.assessment_id DESC;")
                elif self.order_by_cb.get() == 'Tenant Name':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' AND a.tenant_id = '"
                                          + self.tenant_id_filter_sp.get() + "' ORDER BY t.tenant_name ASC;")
                elif self.order_by_cb.get() == 'Assessment Description':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' AND a.tenant_id = '"
                                          + self.tenant_id_filter_sp.get() + "' ORDER BY a.assessment_description ASC;")
                elif self.order_by_cb.get() == 'Date Created':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' AND a.tenant_id = '"
                                          + self.tenant_id_filter_sp.get() + "' ORDER BY a.date_created ASC;")
                else:
                    print('Safety condition')
                    self.mycursor.execute("SELECT a.assessment_id, a.tenant_id, t.tenant_name, a.assessment_amount, "
                                          "a.room_id, a.admin_id, a.basic_user_id, "
                                          "a.assessment_description, a.date_created, a.time_created, "
                                          "t.tenant_email FROM assessment a INNER JOIN tenant t ON "
                                          "a.tenant_id = t.tenant_id WHERE a.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                          + self.admin_id_str + "' AND a.tenant_id = '"
                                          + self.tenant_id_filter_sp.get() + "';")

            assessments = self.mycursor.fetchall()
            print(assessments)

            # Create configure for striped rows
            self.info_tree.tag_configure("oddrow", background="#FFFFFF")
            self.info_tree.tag_configure("evenrow", background="#FAFAFA")

            count = 0
            for record in assessments:
                if count % 2 == 0:
                    self.info_tree.insert(parent="", index="end", iid=count, text="",
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10]),
                                          tags=("oddrow",))
                else:
                    self.info_tree.insert(parent="", index="end", iid=count, text="",
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10]),
                                          tags=("evenrow",))
                count += 1

            if count <= 0:
                messagebox.showerror("Error", "Database request unsuccessful! \n Please check your internet connection"
                                              "\nor check for invalid input.")
            else:
                pass

            self.db1.commit()
            self.mycursor.close()
            self.db1.close()
        except Exception as e:
            messagebox.showerror("Error", "Database request unsuccessful! \n Please check your internet connection \n"
                                          "or check for invalid input.")
            print(e)

    def remove_assessment_request(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                confirmation = messagebox.askokcancel("Confirm deletion", "Are you sure you want to delete this "
                                                                          "value?\n\nDeletion of this value might "
                                                                          "delete values that are tethered to it.\n\n"
                                                                          "- Deletion of this assessment will result "
                                                                          "to deduction of balance incurred during "
                                                                          "this assessment")
                if confirmation:
                    self.database_connect()

                    # Grab record number
                    selected = self.info_tree.focus()

                    # Grab record values
                    values = self.info_tree.item(selected, "values")

                    self.mycursor.execute(
                        "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '" + self.admin_id_str +
                        "' AND tenant_id = '" + values[1] + "';")

                    # Converts the tuple into integer
                    balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

                    self.mycursor.execute("DELETE FROM assessment WHERE assessment_id = '"
                                          + values[0] + "' AND admin_id = '" + self.admin_id_str + "';")

                    # Update balance
                    self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                          + str(balance - int(values[3])) +
                                          "' WHERE tenant_id = '" + values[1] + "' AND admin_id = '"
                                          + self.admin_id_str + "';")
                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Removed assessment successfully")

                    # Turn off admin access if account is basic user
                    self.basic_user_status()

            except Exception as e:
                self.invalid_input()
                print(e)

    # def download_receipt_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.save_file_dialog = filedialog.asksaveasfile(filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
                                                         defaultextension='.pdf',
                                                         title="Save file")
        print(type(self.save_file_dialog))
        receipt_pdf = FPDF()
        receipt_pdf.set_font('helvetica', '', 10)
        receipt_pdf.add_page()

        # create a cell
        receipt_pdf.cell(200, 10, txt="Digital copy of receipt", border=1, ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DormBuilt, Inc.", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DLSU-HSC Dormbuilt Ladies Dormitory", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="Congressional Ave., Dasmarinas, Cavite", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt=" ", ln=1, align='C')
        receipt_pdf.cell(200, 10, txt=("Received from: " + self.current_user), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Transaction Date: " + values[9]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Payment ID: " + values[0]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant ID: " + values[1]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Name: " + values[2]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Email: " + values[11]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Discount Code: " + values[7]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Amount of Payment: P" + values[3]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Payment Description: " + values[8]), ln=1, align='L')

        # save the pdf with name .pdf
        receipt_pdf.output(dest='F', name=self.save_file_dialog.name)

    def download_assessment_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.save_file_dialog = filedialog.asksaveasfile(filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
                                                         defaultextension='.pdf',
                                                         title="Save file")
        print(type(self.save_file_dialog))
        receipt_pdf = FPDF()
        receipt_pdf.set_font('helvetica', '', 10)
        receipt_pdf.add_page()

        # create a cell
        receipt_pdf.cell(200, 10, txt="Digital copy of receipt", border=1, ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DormBuilt, Inc.", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DLSU-HSC Dormbuilt Ladies Dormitory", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="Congressional Ave., Dasmarinas, Cavite", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt=" ", ln=1, align='C')
        receipt_pdf.cell(200, 10, txt=("Received from: " + self.current_user), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Transaction Date: " + values[8]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Assessment ID: " + values[0]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant ID: " + values[1]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Name: " + values[2]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Email: " + values[10]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Assessment amount: P" + values[3]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Payment Description: " + values[7]), ln=1, align='L')

        # save the pdf with name .pdf
        receipt_pdf.output(dest='F', name=self.save_file_dialog.name)

    def send_assessment_email_request(self):
        if not self.tenant_email_e.get():
            self.invalid_input()
        elif self.tenant_email_e.get() == "None":
            self.invalid_input()
        else:
            try:
                self.download_assessment_request()

                body = '''Good Day! Below is an attachment for the digital copy of 
                your payment for Dormbuilt, Inc. Thank you!
                
                This email is an automated message, please don't reply.
                '''

                sender = 'pongodev0914@gmail.com'
                pwd = 'Bin@1110010010'
                # put the email of the receiver here
                receiver = self.tenant_email_e.get()

                # Set up the MIME
                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = 'This email has an attachment, a pdf file'

                message.attach(MIMEText(body, 'plain'))

                pdfname = self.save_file_dialog.name

                # open the file in binary
                binary_pdf = open(pdfname, 'rb')

                payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                # payload = MIMEBase('application', 'pdf', Name=pdfname)
                payload.set_payload(binary_pdf.read())

                # encoding the binary into base64
                encoders.encode_base64(payload)

                # add header with pdf name
                payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                message.attach(payload)

                # use gmail with port
                session = smtplib.SMTP('smtp.gmail.com', 587)

                # enable security
                session.starttls()

                # login with mail_id and password
                session.login(sender, pwd)

                text = message.as_string()
                session.sendmail(sender, receiver, text)
                session.quit()
                print('Mail Sent')

                self.dialog_box_top.destroy()

            except Exception as e:
                messagebox.showerror("Error", "Please check your internet connection or Authentication error\nis "
                                              "detected, please contact the system administrator to allow\naccess"
                                              "of email to new devices.")
                print(e)

    # Payment
    def payment_info_treeview_request(self):
        try:
            # Connect to database
            self.database_connect()

            # Conditions for tenant ID
            if not self.tenant_id_filter_sp.get():
                print("tenant id filter empty")
                # Conditions for order by filter
                if self.order_by_cb.get() == 'Payment ID':
                    print(self.order_by_cb.get())
                    self.mycursor.execute("SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, "
                                          "p.room_id, p.admin_id, p.basic_user_id, p.discount_code, "
                                          "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                                          "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                                          "WHERE p.date_created >= '"
                                          + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                                          + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                                          + self.admin_id_str + "' ORDER BY p.payment_id DESC;")
                elif self.order_by_cb.get() == 'Tenant Name':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' ORDER BY t.tenant_name ASC;")
                elif self.order_by_cb.get() == 'Payment Description':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '" +
                        self.admin_id_str + "' ORDER BY p.payment_description ASC;")
                elif self.order_by_cb.get() == 'Date Created':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' ORDER BY p.date_created ASC;")
                else:
                    print('Safety condition')
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "';")
            else:
                print("tenant id filter not empty")
                # Conditions for order by filter
                if self.order_by_cb.get() == 'Payment ID':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' AND p.tenant_id = '"
                        + self.tenant_id_filter_sp.get() + "' ORDER BY p.payment_id DESC;")
                elif self.order_by_cb.get() == 'Tenant Name':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' AND p.tenant_id = '"
                        + self.tenant_id_filter_sp.get() + "' ORDER BY t.tenant_name ASC;")
                elif self.order_by_cb.get() == 'Payment Description':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '" +
                        self.admin_id_str + "' AND p.tenant_id = '"
                        + self.tenant_id_filter_sp.get() + "' ORDER BY p.payment_description ASC;")
                elif self.order_by_cb.get() == 'Date Created':
                    print(self.order_by_cb.get())
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id "
                        "WHERE p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' AND p.tenant_id = '"
                        + self.tenant_id_filter_sp.get() + "' ORDER BY p.date_created ASC;")
                else:
                    print('Safety condition')
                    self.mycursor.execute(
                        "SELECT p.payment_id, p.tenant_id, t.tenant_name, p.payment_amount, p.room_id, "
                        "p.admin_id, p.basic_user_id, p.discount_code, "
                        "p.payment_description, p.date_created, p.time_created, t.tenant_email FROM "
                        "payment p INNER JOIN tenant t ON p.tenant_id = t.tenant_id WHERE "
                        "p.date_created >= '"
                        + self.dashboard_filter_from.get() + "' AND p.date_created <= '"
                        + self.dashboard_filter_to.get() + "' AND p.admin_id = '"
                        + self.admin_id_str + "' AND p.tenant_id = '"
                        + self.tenant_id_filter_sp.get() + "';")

            payments = self.mycursor.fetchall()
            print(payments)

            # Create configure for striped rows
            self.info_tree.tag_configure("oddrow", background="#FFFFFF")
            self.info_tree.tag_configure("evenrow", background="#FAFAFA")

            count = 0
            for record in payments:
                if count % 2 == 0:
                    self.info_tree.insert(parent="", index="end", iid=count, text="",
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10], record[11]),
                                          tags=("oddrow",))
                else:
                    self.info_tree.insert(parent="", index="end", iid=count, text="",
                                          values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                                  record[6], record[7], record[8], record[9], record[10], record[11]),
                                          tags=("evenrow",))
                count += 1

            if count <= 0:
                messagebox.showerror("Error", "Database request unsuccessful! \n Please check your internet connection"
                                              "\nor check for invalid input.")
            else:
                pass

            self.db1.commit()
            self.mycursor.close()
            self.db1.close()
        except Exception as e:
            messagebox.showerror("Error", "Database request unsuccessful! \n Please check your internet connection \n"
                                          "or check for invalid input.")
            print(e)

    def remove_payment_request(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                confirmation = messagebox.askokcancel("Confirm deletion", "Are you sure you want to delete this "
                                                                          "value?\n\nDeletion of this value might "
                                                                          "delete values that are tethered to it.\n\n"
                                                                          "- Deletion of this assessment will result "
                                                                          "to addition of balance incurred during\n\n"
                                                                          "this payment")
                if confirmation:
                    self.database_connect()

                    # Grab record number
                    selected = self.info_tree.focus()

                    # Grab record values
                    values = self.info_tree.item(selected, "values")

                    self.mycursor.execute(
                        "SELECT DISTINCT tenant_balance FROM tenant where admin_id = '" + self.admin_id_str +
                        "' AND tenant_id = '" + values[1] + "';")

                    # Converts the tuple into integer
                    balance = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

                    self.mycursor.execute("DELETE FROM payment WHERE payment_id = '" + values[0] + "' AND admin_id = '"
                                          + self.admin_id_str + "';")

                    # Change balance and tenant status according to payment
                    if values[8] == 'Application fee':
                        self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                              + str(balance + int(values[3])) +
                                              "', tenant_status = 'Newly registered' WHERE tenant_id = '"
                                              + values[1] + "' AND admin_id = '" + self.admin_id_str + "';")
                    elif values[8] == 'Confirmation fee':
                        self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                              + str(balance + int(values[3])) +
                                              "', tenant_status = 'Application', room_id = 'None' WHERE tenant_id = '"
                                              + values[1] + "' AND admin_id = '" + self.admin_id_str + "';")
                        self.mycursor.execute("UPDATE room SET current_occupants = current_occupants - 1, "
                                              "room_availability = 'Available' WHERE room_id = '"
                                              + values[4] + "' AND admin_id = '" + self.admin_id_str + "';")
                    elif values[8] == 'Processing fee':
                        self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                              + str(balance + int(values[3])) +
                                              "', tenant_status = 'Confirmation' WHERE tenant_id = '"
                                              + values[1] + "' AND admin_id = '" + self.admin_id_str + "';")
                    else:
                        self.mycursor.execute("UPDATE tenant SET tenant_balance = '"
                                              + str(balance + int(values[3])) + "' WHERE tenant_id = '"
                                              + values[1] + "' AND admin_id = '" + self.admin_id_str + "';")
                    print(values[8])
                    self.db1.commit()
                    self.db1.close()
                    self.mycursor.close()

                    messagebox.showinfo("Success", "Removed payment successfully")

                    # Turn off admin access if account is basic user
                    self.basic_user_status()

            except Exception as e:
                self.invalid_input()
                print(e)

    def download_receipt_request(self):
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.save_file_dialog = filedialog.asksaveasfile(filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")),
                                                         defaultextension='.pdf',
                                                         title="Save file")
        print(type(self.save_file_dialog))
        receipt_pdf = FPDF()
        receipt_pdf.set_font('helvetica', '', 10)
        receipt_pdf.add_page()

        # create a cell
        receipt_pdf.cell(200, 10, txt="Digital copy of receipt", border=1, ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DormBuilt, Inc.", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="DLSU-HSC Dormbuilt Ladies Dormitory", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt="Congressional Ave., Dasmarinas, Cavite", ln=1, align='C')
        receipt_pdf.cell(200, 8, txt=" ", ln=1, align='C')
        receipt_pdf.cell(200, 10, txt=("Received from: " + self.current_user), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Transaction Date: " + values[9]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Payment ID: " + values[0]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant ID: " + values[1]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Name: " + values[2]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Tenant Email: " + values[11]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Discount Code: " + values[7]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Amount of Payment: P" + values[3]), ln=1, align='L')
        receipt_pdf.cell(200, 10, txt=("Payment Description: " + values[8]), ln=1, align='L')

        # save the pdf with name .pdf
        receipt_pdf.output(dest='F', name=self.save_file_dialog.name)

    def send_receipt_email_request(self):
        if not self.tenant_email_e.get():
            self.invalid_input()
        elif self.tenant_email_e.get() == "None":
            self.invalid_input()
        else:
            try:
                self.download_receipt_request()

                body = '''Good Day! Below is an attachment for the digital copy of 
                your payment for Dormbuilt, Inc. Thank you!
                
                This email is an automated message, please don't reply.
                '''

                sender = 'pongodev0914@gmail.com'
                pwd = 'Bin@1110010010'
                # put the email of the receiver here
                receiver = self.tenant_email_e.get()

                # Set up the MIME
                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = 'This email has an attachment, a pdf file'

                message.attach(MIMEText(body, 'plain'))

                pdfname = self.save_file_dialog.name

                # open the file in binary
                binary_pdf = open(pdfname, 'rb')

                payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                # payload = MIMEBase('application', 'pdf', Name=pdfname)
                payload.set_payload(binary_pdf.read())

                # encoding the binary into base64
                encoders.encode_base64(payload)

                # add header with pdf name
                payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                message.attach(payload)

                # use gmail with port
                session = smtplib.SMTP('smtp.gmail.com', 587)

                # enable security
                session.starttls()

                # login with mail_id and password
                session.login(sender, pwd)

                text = message.as_string()
                session.sendmail(sender, receiver, text)
                session.quit()
                print('Mail Sent')

                self.dialog_box_top.destroy()

            except Exception as e:
                messagebox.showerror("Error", "Please check your internet connection or Authentication error\nis "
                                              "detected, please contact the system administrator to allow\naccess"
                                              "of email to new devices.")
                print(e)

    # Booking
    def booking_info_treeview_request(self):
        Content_control.clear_treeview(self.info_tree)
        # Connect to database
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Booking ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.booking_id DESC;")
        elif self.order_by_cb.get() == 'Tenant Name':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.tenant_name ASC;")
        elif self.order_by_cb.get() == 'Tenant Email':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.tenant_email ASC;")
        elif self.order_by_cb.get() == 'Booking Status':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.booking_status ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.date_created ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT b.booking_id, b.tenant_name, b.tenant_email, "
                                  "b.admin_id, b.booking_status, b.date_created, b.time_created FROM booking b WHERE "
                                  "b.date_created >= '" + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' " + self.admin_id_str + "';")

        bookings = self.mycursor.fetchall()
        print(bookings)

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in bookings:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

    def register_tenant_request(self):
        if not self.tenant_name_e.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("INSERT INTO tenant (tenant_name, tenant_email, tenant_status, date_created, "
                                      "time_created, admin_id) VALUES (%s,%s,%s,%s,%s,%s)",
                                      (self.tenant_name_e.get(), self.tenant_email_e.get(), self.tenant_status_cb.get(),
                                       date_str, time_str, self.admin_id_str))

                self.mycursor.execute("UPDATE booking SET booking_status = 'Registered already' WHERE booking_id = '"
                                      + self.booking_id + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Tenant's account is created")

                self.dialog_box_top.destroy()

            except Exception as e:
                self.invalid_input()
                print(e)

    def remove_booking_request(self):
        try:
            self.database_connect()
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            self.mycursor.execute("DELETE FROM booking WHERE booking_id = '" + values[0] + "';")
            # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()

            messagebox.showinfo("Success", "Removed booking successfully")

        except Exception as e:
            self.invalid_request()
            print(e)

    # Discount
    def create_discount_request(self):
        if not self.discount_code_e.get():
            self.invalid_input()
        elif not self.discount_amount_sp.get():
            self.invalid_input()
        elif not self.discount_status_cb.get():
            self.invalid_input()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO discount (discount_code, discount_amount, admin_id,"
                                      " basic_user_id, date_created, time_created, discount_status) VALUES "
                                      "(%s,%s,%s,%s,%s,%s,%s)", (self.discount_code_e.get(),
                                                                 self.discount_amount_sp.get(), self.admin_id_str,
                                                                 self.basic_user_id_str, date_str, time_str,
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
        elif not self.discount_amount_sp.get():
            self.invalid_input()
        elif not self.discount_status_cb.get():
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
        Content_control.clear_treeview(self.info_tree)
        # Connect to database
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Discount ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY d.discount_id DESC;")
        elif self.order_by_cb.get() == 'Discount Code':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY d.discount_code ASC;")
        elif self.order_by_cb.get() == 'Discount Amount':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY d.discount_amount ASC;")
        elif self.order_by_cb.get() == 'Discount Status':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY d.discount_status ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY d.date_created ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT d.discount_id, d.discount_code, d.discount_amount, "
                                  "d.discount_status, d.date_created, d.time_created FROM discount d "
                                  "WHERE d.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND d.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = ' "
                                  + self.admin_id_str + "';")

        discount = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in discount:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("evenrow",))
            count += 1

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
                    self.discount_applied_bool = False
                    tk.messagebox.showerror("Error", "Invalid Discount Code")
                else:
                    self.mycursor.execute(
                        "SELECT DISTINCT discount_amount FROM discount where discount_code = '"
                        + self.discount_code_e.get() + "' and admin_id = '" + str(self.admin_id_str) + "';")

                    # Converts the tuple into integer
                    discount_amount = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                    discounted_price = (int(self.amount_to_be_paid_l.cget("text")) -
                                        (int(self.amount_to_be_paid_l.cget("text")) * discount_amount / 100))

                    self.discount_reduction = (int(self.amount_to_be_paid_l.cget("text")) * discount_amount/100)

                    self.amount_to_be_paid_l.config(text=discounted_price)
                    self.discount_l.config(text=discount_amount)
                    self.payment_amount_sp.delete(0, "end")
                    self.payment_amount_sp.insert(0, discounted_price)

                    self.discount_applied_bool = True

                self.db1.close()
                self.mycursor.close()
            except Exception as e:
                self.invalid_request()
                print(e)

    # Accounts
    def change_username_password_request(self):
        if not self.change_username_e.get():
            self.invalid_input()
        elif not self.change_password_e.get():
            self.invalid_input()
        elif not self.admin_access_bool:
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

            # Turn off admin access
            if self.basic_user_access_bool:
                self.admin_access_bool = False
            else:
                "Basic User Sign in is = False"

    def create_employee_request(self):
        if not self.employee_username_e.get():
            self.invalid_input()
        elif not self.employee_password_e.get():
            self.invalid_input()
        elif not self.employee_role_e.get():
            self.invalid_input()
        elif not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("INSERT INTO basic_user (admin_id, username, password, role, date_created, "
                                      "time_created) VALUES (%s,%s,%s,%s,%s,%s)", (self.admin_id_str,
                                                                                   self.employee_username_e.get(),
                                                                                   self.employee_password_e.get(),
                                                                                   self.employee_role_e.get(),
                                                                                   date_str, time_str))

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Employee Account is  created")

                self.dialog_box_top.destroy()

                # Turn off admin access if account is basic user
                self.basic_user_status()

            except Exception as e:
                self.invalid_input()
                print(e)

    def modify_employee_request(self):
        if not self.employee_username_e.get():
            self.invalid_input()
        elif not self.employee_password_e.get():
            self.invalid_input()
        elif not self.employee_role_e.get():
            self.invalid_input()
        elif not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                self.database_connect()
                self.mycursor.execute("UPDATE basic_user SET username = '"
                                      + self.employee_username_e.get() + "', password = '"
                                      + self.employee_password_e.get() + "', role = '"
                                      + self.employee_role_e.get() + "'  WHERE basic_user_id = '"
                                      + self.employee_id + "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Employee Account is successfully modified")

                # Turn off admin access if account is basic user
                self.basic_user_status()

                self.dialog_box_top.destroy()
            except Exception as e:
                self.invalid_input()
                print(e)

    def employee_info_treeview_request(self):
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Employee ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.basic_user_id, b.username, b.password, b.role, b.date_created, "
                                  "b.time_created FROM basic_user b WHERE b.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND b.admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.basic_user_id DESC;")
        elif self.order_by_cb.get() == 'Employee Name':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.basic_user_id, b.username, b.password, b.role, b.date_created, "
                                  "b.time_created FROM basic_user b WHERE b.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND b.admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.username ASC;")
        elif self.order_by_cb.get() == 'Role':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.basic_user_id, b.username, b.password, b.role, b.date_created, "
                                  "b.time_created FROM basic_user b WHERE b.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND b.admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.role ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT b.basic_user_id, b.username, b.password, b.role, b.date_created, "
                                  "b.time_created FROM basic_user b WHERE b.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND b.admin_id = ' "
                                  + self.admin_id_str + "' ORDER BY b.date_created ASC;")
        else:
            print("Safety Condition")
            self.mycursor.execute("SELECT b.basic_user_id, b.username, b.password, b.role, b.date_created, "
                                  "b.time_created FROM basic_user b WHERE b.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND b.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND b.admin_id = ' "
                                  + self.admin_id_str + "';")

        employees = self.mycursor.fetchall()

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in employees:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

        # Turn off admin access if account is basic user
        self.basic_user_status()

    def remove_employee_account_request(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
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

                messagebox.showinfo("Success", "Removed account successfully")

                # Turn off admin access if account is basic user
                self.basic_user_status()

                self.account_settings_content_interface()
            except Exception as e:
                self.invalid_input()
                print(e)

    # Action History
    def action_info_treeview_request(self):
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Action ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT a.action_id, a.action_description, a.admin_id, a.user_current, "
                                  "a.privilege_access, a.date_created, a.time_created, a.basic_user_id FROM "
                                  "action_history a WHERE a.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                  + self.admin_id_str + "' ORDER BY a.action_id DESC;")
        elif self.order_by_cb.get() == 'Action Description':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT a.action_id, a.action_description, a.admin_id, a.user_current, "
                                  "a.privilege_access, a.date_created, a.time_created, a.basic_user_id FROM "
                                  "action_history a WHERE a.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                  + self.admin_id_str + "' ORDER BY a.action_description ASC;")
        elif self.order_by_cb.get() == 'Current User':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT a.action_id, a.action_description, a.admin_id, a.user_current, "
                                  "a.privilege_access, a.date_created, a.time_created, a.basic_user_id FROM "
                                  "action_history a WHERE a.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                  + self.admin_id_str + "' ORDER BY a.user_current ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT a.action_id, a.action_description, a.admin_id, a.user_current, "
                                  "a.privilege_access, a.date_created, a.time_created, a.basic_user_id FROM "
                                  "action_history a WHERE a.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                  + self.admin_id_str + "' ORDER BY a.date_created ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT a.action_id, a.action_description, a.admin_id, a.user_current, "
                                  "a.privilege_access, a.date_created, a.time_created, a.basic_user_id FROM "
                                  "action_history a WHERE a.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND a.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND a.admin_id = '"
                                  + self.admin_id_str + "';")

        actions = self.mycursor.fetchall()
        print(actions)

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in actions:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]), tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7]), tags=("evenrow",))
            count += 1

        self.db1.commit()
        self.mycursor.close()
        self.db1.close()

        # Turn off admin access if account is basic user
        self.basic_user_status()

    def action_history_request(self):
        try:
            self.database_connect()

            # Record action to action history
            self.mycursor.execute("INSERT INTO action_history (action_description, admin_id, user_current, "
                                  "privilege_access, date_created, time_created, basic_user_id) "
                                  "VALUES (%s,%s,%s,%s,%s,%s,%s)", (self.action_description, self.admin_id_str,
                                                                    self.current_user, str(self.admin_access_bool),
                                                                    date_str, time_str, self.basic_user_id_str))
            self.db1.commit()
            self.db1.close()
            self.mycursor.close()
            print("Action history is recorded successfully")
        except Exception as e:
            self.invalid_input()
            print(e)

    def remove_action_request(self):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                self.database_connect()
                # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=0;")

                # Grab record number
                selected = self.info_tree.focus()

                # Grab record values
                values = self.info_tree.item(selected, "values")

                self.mycursor.execute("DELETE FROM action_history WHERE action_id = '" + values[0] +
                                      "';")
                # self.mycursor.execute("SET FOREIGN_KEY_CHECKS=1;")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Removed action successfully")

                # Turn off admin access if account is basic user
                self.basic_user_status()

            except Exception as e:
                self.invalid_request()
                print(e)

    def clear_action_history_request(self, event):
        if not self.admin_access_bool:
            self.admin_access_validation_dialog()
        else:
            try:
                self.database_connect()

                self.mycursor.execute("DELETE FROM action_history WHERE admin_id = '" + self.admin_id_str +
                                      "';")
                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Cleared action history successfully")

                # Turn off admin access if account is basic user
                self.basic_user_status()

            except Exception as e:
                self.invalid_request()
                print(e)

        print(event)

    # Notif
    def notif_info_treeview_request(self):
        Content_control.clear_treeview(self.info_tree)
        # Connect to database
        self.database_connect()

        # Conditions for order by filter
        if self.order_by_cb.get() == 'Notif ID':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT n.notif_id, n.notif_subject, n.notif_description, n.admin_id, "
                                  "n.date_created, n.time_created FROM notif n WHERE n.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND n.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY n.notif_id DESC;")
        elif self.order_by_cb.get() == 'Notif Subject':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT n.notif_id, n.notif_subject, n.notif_description, n.admin_id, "
                                  "n.date_created, n.time_created FROM notif n WHERE n.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND n.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY n.notif_subject ASC;")
        elif self.order_by_cb.get() == 'Notif Description':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT n.notif_id, n.notif_subject, n.notif_description, n.admin_id, "
                                  "n.date_created, n.time_created FROM notif n WHERE n.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND n.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY n.notif_description ASC;")
        elif self.order_by_cb.get() == 'Date Created':
            print(self.order_by_cb.get())
            self.mycursor.execute("SELECT n.notif_id, n.notif_subject, n.notif_description, n.admin_id, "
                                  "n.date_created, n.time_created FROM notif n WHERE n.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND n.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False ORDER BY n.date_created ASC;")
        else:
            print('Safety condition')
            self.mycursor.execute("SELECT n.notif_id, n.notif_subject, n.notif_description, n.admin_id, "
                                  "n.date_created, n.time_created FROM notif n WHERE n.date_created >= '"
                                  + self.dashboard_filter_from.get() + "' AND n.date_created <= '"
                                  + self.dashboard_filter_to.get() + "' AND admin_id = '"
                                  + self.admin_id_str + "' AND deleted = False;")

        notif = self.mycursor.fetchall()
        print(notif)

        # Create configure for striped rows
        self.info_tree.tag_configure("oddrow", background="#FFFFFF")
        self.info_tree.tag_configure("evenrow", background="#FAFAFA")

        count = 0
        for record in notif:
            if count % 2 == 0:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("oddrow",))
            else:
                self.info_tree.insert(parent="", index="end", iid=count, text="",
                                      values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                      tags=("evenrow",))
            count += 1

        self.mycursor.close()
        self.db1.close()

    def remove_notif_request(self):
        confirmation = messagebox.askokcancel("Confirm deletion", "Are you sure you want to delete this "
                                                                  "value?")
        if confirmation:

            # Grab record number
            selected = self.info_tree.focus()

            # Grab record values
            values = self.info_tree.item(selected, "values")

            try:
                self.database_connect()

                self.mycursor.execute("UPDATE notif SET deleted = True WHERE notif_id = '" + values[0] + "';")

                self.db1.commit()
                self.db1.close()
                self.mycursor.close()

                messagebox.showinfo("Success", "Removed notif successfully")

            except Exception as e:
                self.invalid_request()
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
        elif not self.admin_access_password_e.get():
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
                self.admin_access_bool = True
                self.dialog_box_top.destroy()

            self.db1.close()
            self.mycursor.close()

    # ================================================ Content control =================================================
    def change_button_color(self):
        self.home_b.configure(fg='#7c8084', image=self.home_inactive_im_resized)
        self.dashboard_b.configure(fg='#7c8084', image=self.dashboard_inactive_im_resized)
        self.tenants_b.configure(fg='#7c8084', image=self.tenant_inactive_im_resized)
        self.assessment_b.configure(fg='#7c8084', image=self.assessment_inactive_im_resized)
        self.payments_b.configure(fg='#7c8084', image=self.payment_inactive_im_resized)
        self.booking_b.configure(fg='#7c8084', image=self.booking_inactive_im_resized)
        self.discounts_b.configure(fg='#7c8084', image=self.discount_inactive_im_resized)
        self.accounts_b.configure(fg='#7c8084', image=self.account_inactive_im_resized)
        self.action_history_b.configure(fg='#7c8084', image=self.action_history_inactive_im_resized)
        self.notif_b.configure(fg='#7c8084', image=self.notif_inactive_im_resized)

    def change_payment_information(self, event):
        amount_to_be_paid = 500
        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        if self.payment_description_cb.get() == "Application fee":
            amount_to_be_paid = 500
            self.payment_description_l.config(text="Application fee: ")
            self.application_fee_l.config(text=amount_to_be_paid)
            self.room_cost_l.config(text=0)
            self.amenities_cost_l.config(text=0)
        elif self.payment_description_cb.get() == "Confirmation fee":
            amount_to_be_paid = int(values[6]) + int(values[7])
        elif self.payment_description_cb.get() == "Processing fee":
            try:
                # Get the value room and amenities price
                self.database_connect()
                self.mycursor.execute(
                    "SELECT DISTINCT r.room_price FROM room r WHERE r.room_id = '"
                    + values[3] + "' AND admin_id = '" + str(self.admin_id_str) + "';")

                # Converts the tuple into integer
                room_price = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

                self.mycursor.execute(
                    "SELECT DISTINCT r.amenities_price FROM room r WHERE r.room_id = '"
                    + values[3] + "' AND admin_id = '" + str(self.admin_id_str) + "';")

                # Converts the tuple into integer
                amenities_price = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                amount_to_be_paid = (((room_price + amenities_price) * 2) + 1500)

                self.payment_description_l.config(text="Processing fee: ")
                self.application_fee_l.config(text=amount_to_be_paid)
                self.room_cost_l.config(text=room_price)
                self.amenities_cost_l.config(text=amenities_price)
            except Exception as e:
                messagebox.showerror("Error", "Cannot proceed with the payment. Please connect to the internet or \n"
                                              "if there is no Room ID available, please pay Confirmation fee first.")
                print(e)

        elif self.payment_description_cb.get() == "Monthly rental fee":
            try:
                # Get the value room and amenities price
                self.database_connect()
                self.mycursor.execute(
                    "SELECT DISTINCT r.room_price FROM room r WHERE r.room_id = '"
                    + values[3] + "' AND admin_id = '" + str(self.admin_id_str) + "';")

                # Converts the tuple into integer
                room_price = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())

                self.mycursor.execute(
                    "SELECT DISTINCT r.amenities_price FROM room r WHERE r.room_id = '"
                    + values[3] + "' AND admin_id = '" + str(self.admin_id_str) + "';")

                # Converts the tuple into integer
                amenities_price = functools.reduce(lambda sub, ele: sub * 10 + ele, self.mycursor.fetchone())
                amount_to_be_paid = room_price + amenities_price

                self.payment_description_l.config(text="Monthly rental fee: ")
                self.application_fee_l.config(text=amount_to_be_paid)
                self.room_cost_l.config(text=room_price)
                self.amenities_cost_l.config(text=amenities_price)
            except Exception as e:
                messagebox.showerror("Error", "Cannot proceed with the payment. Please connect to the internet or \n"
                                              "if there is no Room ID available, please pay Confirmation fee first.")
                print(e)
        else:
            amount_to_be_paid = 0

        self.amount_to_be_paid_l.config(text=amount_to_be_paid)
        self.payment_amount_sp.delete(0, "end")
        self.payment_amount_sp.insert(0, amount_to_be_paid)

        print(event)

    def basic_user_status(self):
        if self.basic_user_access_bool:
            self.admin_access_bool = False
        else:
            "Basic User Sign in is = False"

    def tenant_status_transaction_help(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Tenant status")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Tenant status',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        content_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        content_lf.pack(side="top", fill="both", pady=15, expand=True)

        # Payment transaction information section
        ttk.Label(content_lf, text='Newly Registered - ', style="on.TLabel").grid(column=0, row=0, pady=2.5, sticky="w")

        ttk.Label(content_lf, text="Tenant's account is newly registered.",
                  style="h2_small.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(content_lf, text='Application - ', style="on.TLabel").grid(column=0, row=1, pady=2.5, sticky="w")

        ttk.Label(content_lf, text='Tenant issued payment for application fee.',
                  style="h2_small.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(content_lf, text='Confirmation - ', style="on.TLabel").grid(column=0, row=2, pady=2.5, sticky="w")

        ttk.Label(content_lf, text='Tenant issued payment for confirmation fee.',
                  style="h2_small.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(content_lf, text='Active - ', style="on.TLabel").grid(column=0, row=3, pady=2.5, sticky="w")

        ttk.Label(content_lf, text='Tenant are in active lease, and are complete in payments.',
                  style="h2_small.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(content_lf, text='Inactive - ', style="on.TLabel").grid(column=0, row=4, pady=2.5, sticky="w")

        ttk.Label(content_lf, text="Tenant's lease are inactive, and are no longer renting in the dorm.",
                  style="h2_small.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(content_lf, text='Delinquent - ', style="on.TLabel").grid(column=0, row=5, pady=2.5, sticky="w")

        ttk.Label(content_lf, text='Tenant are delinquent in payment.',
                  style="h2_small.TLabel").grid(column=1, row=5, sticky="w")

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def payment_transaction_help(self):
        self.dialog_box_top = tk.Toplevel(self.master)
        self.dialog_box_top.title("Payment transactions")
        self.dialog_box_top.configure(bg="#FFFFFF")
        self.dialog_box_top.resizable(False, False)

        # ================================================ Widgets for resetting password ==========================
        main_lf = tk.LabelFrame(self.dialog_box_top, bg="#FFFFFF")
        main_lf.pack(padx=15, pady=15, fill="both", expand=True)

        title_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        title_lf.pack(side="top", fill="x")

        ttk.Label(title_lf, text='Payment transactions',
                  style="h1.TLabel").pack(side="left", anchor="nw")
        ttk.Label(title_lf, text='basic',
                  style="small_basic.TLabel").pack(side="left", anchor="nw", padx=5, pady=5)

        content_lf = tk.LabelFrame(main_lf, bg="#FFFFFF", relief="flat")
        content_lf.pack(side="top", fill="both", pady=15, expand=True)

        # Payment transaction information section
        ttk.Label(content_lf, text='Application fee - ', style="on.TLabel").grid(column=0, row=0, sticky="nw")

        ttk.Label(content_lf, text='DormBuilt, Inc. requires a fee for tenants that are interested in booking rooms. \n'
                                   'Application fee amounts to 500 pesos only.',
                  style="h2_small.TLabel").grid(column=1, row=0, rowspan=3, sticky="w")

        ttk.Label(content_lf, text='Confirmation fee - ', style="on.TLabel").grid(column=0, row=3, sticky="nw")

        ttk.Label(content_lf, text='After payment of the application fee. A confirmation fee is required - 1 month \n'
                                   'cost of room and amenities. Application and Confirmation Fee are both part of the\n'
                                   'initial payment required by DormBuilt, Inc.',
                  style="h2_small.TLabel").grid(column=1, row=3, rowspan=4, sticky="w")

        ttk.Label(content_lf, text='Processing fee - ', style="on.TLabel").grid(column=0, row=7, sticky="nw")

        ttk.Label(content_lf, text='After the initial payment, tenants are then required of payment for Processing \n'
                                   'fee - One thousand and five hundred pesos plus 2 month security deposit on both\n'
                                   'the cost of room and amenities.',
                  style="h2_small.TLabel").grid(column=1, row=7, rowspan=4, sticky="w")

        ttk.Label(content_lf, text='Monthly rental - ', style="on.TLabel").grid(column=0, row=11, sticky="nw")

        ttk.Label(content_lf, text='A monthly fee of equal to the cost of room and amenities are required from the\n '
                                   'tenant.', style="h2_small.TLabel").grid(column=1, row=11, rowspan=4, sticky="w")

        # Disables underlying window
        self.dialog_box_top.grab_set()

        self.dialog_box_top.mainloop()

    def room_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)
        Content_control.destroy_content(self.footer_lf)

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

        ttk.Label(room_info_label_lf, text='Amenities Price: ',
                  style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(room_info_label_lf, text=values[7], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Type: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(room_info_label_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(room_info_label_lf, text='Current Occupants: ',
                  style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(room_info_label_lf, text=values[8], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Availability: ',
                  style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(room_info_label_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=7, sticky="w")

        ttk.Label(room_info_label_lf, text='Room Description: ',
                  style="small_info.TLabel").grid(column=0, row=8, sticky="w")

        ttk.Label(room_info_label_lf, text=values[2],
                  style="small_info.TLabel").grid(column=1, row=8, columnspan=2, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Create assessment", font="OpenSans, 12", fg="#FFFFFF", bg="#082B7D",
                  relief="flat", image=self.assessment_im_resized, compound="left", justify="left",
                  command=self.create_room_assessment_dialog).pack(side="top", pady=5, fill="x")

        tk.Button(buttons_lf, text=" Create transaction", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.create_im_resized, compound="left", justify="left",
                  command=self.create_room_transaction_dialog).pack(side="top", pady=5, fill="x")

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

        # ================================================ Room graphical representation ===============================
        availability = "None"
        availability_im = None
        # Condition for tenant capacity
        if values[5] == "1":
            img = self.single_bed_im_resized
            capacity = "1 Tenant Capacity"
        else:
            img = self.double_bed_im_resized
            capacity = "2 or more Tenant Capacity"

        # Condition for room availability
        if values[4] == "Reserved":
            availability_im = self.reserved_im_resized
            availability = "Reserved"
        if values[4] == "Available":
            availability_im = self.available_im_resized
            availability = "Available"
        if values[4] == "Fully Occupied":
            availability_im = self.full_im_resized
            availability = "Fully Occupied"
        if values[4] == "Maintenance":
            availability_im = self.maintenance_im_resized
            availability = "Maintenance"

        # Condition for room availability

        footer_title_lf = tk.LabelFrame(self.footer_lf, bg="#FFFFFF", relief="flat")
        footer_title_lf.pack(side="top", fill="x")

        ttk.Label(footer_title_lf, text=('Room Number: ' + values[1]),
                  style="h2_on.TLabel").grid(column=0, row=0, columnspan=2, pady=10, sticky="w")

        tk.Label(footer_title_lf, image=img,
                 bg="#FFFFFF").grid(column=0, row=1)

        ttk.Label(footer_title_lf, text=capacity,
                  style="h1_body.TLabel").grid(column=0, row=2, padx=10)

        tk.Label(footer_title_lf, image=availability_im,
                 bg="#FFFFFF").grid(column=1, row=1)

        ttk.Label(footer_title_lf, text=availability,
                  style="h1_body.TLabel").grid(column=1, row=2, padx=10)

        print(event)

    def employee_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Employee Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")

        self.employee_id = values[0]

        ttk.Label(info_lf, text='ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Name: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Password: ',
                  style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Role: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Date created: : ', style="small_info.TLabel").grid(column=0, row=3,
                                                                                    sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=4,
                                                                                  sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Buttons
        modify_b_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        modify_b_lf.pack(side="top", pady=5, fill="x")

        tk.Button(modify_b_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left",
                  justify="left", command=self.modify_employee_dialog).pack(side="top", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51", relief="flat",
                  image=self.remove_im_resized, compound="left",
                  command=self.remove_employee_account_request).pack(side="top", pady=5, fill="x")

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

        ttk.Label(info_lf, text='Room ID: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Tenant Balance: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(info_lf, text='Email: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(info_lf, text=values[6], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(info_lf, text=values[7], style="small_info.TLabel").grid(column=1, row=7, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Create assessment", font="OpenSans, 12", fg="#FFFFFF", bg="#082B7D",
                  relief="flat", image=self.assessment_im_resized, compound="left", justify="left",
                  command=self.create_assessment_dialog).pack(side="top", pady=5, fill="x")

        tk.Button(buttons_lf, text=" Create transaction", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.create_im_resized, compound="left", justify="left",
                  command=self.create_tenant_transaction_dialog).pack(side="top", pady=5, fill="x")

        edit_file_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        edit_file_lf.pack(side="top", pady=5, fill="x")

        tk.Button(edit_file_lf, text=" Edit file", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.edit_im_resized, compound="left", justify="left",
                  command=self.modify_tenant_account_dialog).pack(side="top", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51", relief="flat",
                  image=self.remove_im_resized, compound="left",
                  command=self.remove_tenant_account_request).pack(side="top", pady=5, fill="x")

        print(event)

    def assessment_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Assessment Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(info_lf, text='Assessment ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Tenant ID: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Tenant Name: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Tenant Email: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[10], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Assessment amount: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(info_lf, text='Room ID: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(info_lf, text=values[8], style="small_info.TLabel").grid(column=1, row=7, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=8, sticky="w")

        ttk.Label(info_lf, text=values[9], style="small_info.TLabel").grid(column=1, row=8, sticky="w")

        ttk.Label(info_lf, text='Assessment description: ', style="small_info.TLabel").grid(column=0, row=9, sticky="w")

        ttk.Label(info_lf, text=values[7], style="small_info.TLabel").grid(column=1, row=9, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Send assessment", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.receipt_im_resized, compound="left",
                  command=self.send_assessment_dialog).pack(side="top", pady=5, fill="x")

        download_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        download_lf.pack(side="top", pady=5, fill="x")

        tk.Button(download_lf, text=" Save assessment", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.download_im_resized, compound="left",
                  justify="left", command=self.download_assessment_request).pack(fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_assessment_request).pack(side="top", pady=5, fill="x")

        print(event)

    def payment_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Payment Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(info_lf, text='Payment ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Tenant ID: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Tenant Name: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Tenant Email: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[11], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Payment amount: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(info_lf, text='Room ID: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(info_lf, text='Discount code: ', style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(info_lf, text=values[7], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(info_lf, text=values[9], style="small_info.TLabel").grid(column=1, row=7, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=8, sticky="w")

        ttk.Label(info_lf, text=values[10], style="small_info.TLabel").grid(column=1, row=8, sticky="w")

        ttk.Label(info_lf, text='Payment description: ', style="small_info.TLabel").grid(column=0, row=9, sticky="w")

        ttk.Label(info_lf, text=values[8], style="small_info.TLabel").grid(column=1, row=9, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Send receipt", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.receipt_im_resized, compound="left",
                  command=self.send_receipt_dialog).pack(side="top", pady=5, fill="x")

        download_lf = tk.LabelFrame(buttons_lf, bd=1, bg="#585456", relief="flat")
        download_lf.pack(side="top", pady=5, fill="x")

        tk.Button(download_lf, text=" Save receipt", font="OpenSans, 12", fg="#7C8084",
                  bg="#FFFFFF", relief="flat", image=self.download_im_resized, compound="left",
                  justify="left", command=self.download_receipt_request).pack(fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_payment_request).pack(side="top", pady=5, fill="x")

        print(event)

    def booking_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Booking Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        self.booking_id = values[0]

        ttk.Label(info_lf, text='Booking ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Tenant Name: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Tenant Email: ', style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Admin ID: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Booking Status: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[6], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Register tenant", font="OpenSans, 12", fg="#FFFFFF", bg="#89CFF0",
                  relief="flat", image=self.create_tenant_basic_im_resized, compound="left",
                  command=self.register_tenant_account_dialog).pack(side="top", pady=5, fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_booking_request).pack(side="top", pady=5, fill="x")

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

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

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

    def action_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Action History Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(info_lf, text='Action ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Action Description: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Admin ID: ',
                  style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Current User: ', style="small_info.TLabel").grid(column=0, row=3, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=3, sticky="w")

        ttk.Label(info_lf, text='Basic User ID: ', style="small_info.TLabel").grid(column=0, row=4, sticky="w")

        ttk.Label(info_lf, text=values[6], style="small_info.TLabel").grid(column=1, row=4, sticky="w")

        ttk.Label(info_lf, text='Privilege Access: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=7, sticky="w")

        ttk.Label(info_lf, text=values[6], style="small_info.TLabel").grid(column=1, row=7, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_action_request).pack(side="top", pady=5, fill="x")

        print(event)

    def notif_info_section(self, event):
        Content_control.destroy_content(self.info_buttons_lf)

        ttk.Label(self.info_buttons_lf, text='Notif Information',
                  style="on.TLabel").pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        info_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        info_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        # Grab record number
        selected = self.info_tree.focus()

        # Grab record values
        values = self.info_tree.item(selected, "values")
        print(values)

        ttk.Label(info_lf, text='Notif ID: ', style="small_info.TLabel").grid(column=0, row=0, sticky="w")

        ttk.Label(info_lf, text=values[0], style="small_info.TLabel").grid(column=1, row=0, sticky="w")

        ttk.Label(info_lf, text='Notif Subject: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[1], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Notif Description: ', style="small_info.TLabel").grid(column=0, row=1, sticky="w")

        ttk.Label(info_lf, text=values[2], style="small_info.TLabel").grid(column=1, row=1, sticky="w")

        ttk.Label(info_lf, text='Admin ID: ',
                  style="small_info.TLabel").grid(column=0, row=2, sticky="w")

        ttk.Label(info_lf, text=values[3], style="small_info.TLabel").grid(column=1, row=2, sticky="w")

        ttk.Label(info_lf, text='Date created: ', style="small_info.TLabel").grid(column=0, row=5, sticky="w")

        ttk.Label(info_lf, text=values[4], style="small_info.TLabel").grid(column=1, row=5, sticky="w")

        ttk.Label(info_lf, text='Time created: ', style="small_info.TLabel").grid(column=0, row=6, sticky="w")

        ttk.Label(info_lf, text=values[5], style="small_info.TLabel").grid(column=1, row=6, sticky="w")

        # Buttons
        buttons_lf = tk.LabelFrame(self.info_buttons_lf, bg="#FFFFFF", relief="flat")
        buttons_lf.pack(side="top", pady=5, padx=10, anchor="nw", fill="x")

        tk.Button(buttons_lf, text=" Remove", font="OpenSans, 12", fg="#FFFFFF", bg="#BD1E51",
                  relief="flat", image=self.remove_im_resized, compound="left",
                  command=self.remove_notif_request).pack(side="top", pady=5, fill="x")

        print(event)

    # ================================================ Static Methods ==================================================
    @staticmethod
    def invalid_input():
        messagebox.showerror("Error", "Invalid or no input.")

    @staticmethod
    def invalid_request():
        messagebox.showerror("Error", "Database request unsuccessful! \n Please your internet connection.")

    @staticmethod
    def generate_user_manual():
        webbrowser.open_new(r"https://drive.google.com/file/d/1ccYBQGcj2_DGzWNsOd_MgljaN9oLJUSu/view?usp=sharing")

    @staticmethod
    def generate_faqs():
        webbrowser.open_new(r"https://drive.google.com/file/d/1sOV-5pio4OOzGihje-nhDksITuQGJFUy/view?usp=sharing")

    @staticmethod
    def user_ratings():
        webbrowser.open_new(r"https://forms.gle/WwUhJdmagMNMgJ9s6")

    @staticmethod
    def developer_information():
        webbrowser.open_new(r"https://drive.google.com/file/d/17REEVoNwuCFHGVorARgzM8rNrAfojNYj/view?usp=sharing")

    @staticmethod
    def button_clicked():
        showinfo(title='Information',
                 message='This action is currently under development!')


if __name__ == "__main__":
    win = tk.Tk()
    initialize = Window(win)

    win.mainloop()
