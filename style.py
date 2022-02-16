import tkinter as tk
from tkinter import ttk


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button, tk.Toplevel, ttk.Treeview):

    def widget_styles(self):
        # Configure styles for widgets
        style = ttk.Style(self)

        # ================================================ Style for Treeview ========================================
        style.configure("default.Treeview", background="#D3D3D3", font=("OpenSans", 12), foreground="black"
                        , rowheight=25, bd=10, fieldbackground="#FFFFFF")
        style.configure("default.Treeview.Heading", font=("OpenSans", 12, "bold"), foreground="green")
        style.map("default.Treeview", background=[("selected", "green")])

        # ================================================ Style for Label =============================================
        style.configure('h1.TLabel', font=("Times New Roman", 20, "bold"), foreground='#395A68', background="#FFFFFF")
        style.configure('h2.TLabel', font=("OpenSans", 12), foreground='#585456', background="#FFFFFF")
        style.configure('h1_body.TLabel', font=("Times New Roman", 15), foreground='#585456', background="#FFFFFF")
        style.configure('small.TLabel', font=("Times New Roman", 10), foreground='#FFFFFF', background="#4C8404")
        style.configure('small_basic.TLabel', font=("Times New Roman", 10), foreground='#FFFFFF', background="#89CFF0")
        style.configure('small_info.TLabel', font=("Times New Roman", 10), foreground='#585456', background="#FFFFFF")
        style.configure('h2_small.TLabel', font=("OpenSans", 10), foreground='#585456', background="#FFFFFF")
        style.configure('link.TLabel', font=("Times New Roman", 10), foreground='Blue', background="#FFFFFF")
        style.configure('on.TLabel', font=("Times New Roman", 10), foreground='#4C8404', background="#FFFFFF")
        style.configure('off.TLabel', font=("Times New Roman", 10), foreground='#BD1E51', background="#FFFFFF")

        # ================================================ Style for Frame =============================================
        style.configure('Basic.TFrame', background="#FFFFFF")

        # ================================================ Style for LabelFrame ========================================
        style.configure('Basic.TLabelframe', background="#FFFFFF")

        # ================================================ Style for Entry ========================================
        style.configure('Basic.TEntry', background="#FFFFFF", borderwidth=3)





