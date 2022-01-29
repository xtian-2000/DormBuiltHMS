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
        style.configure('h2.TLabel', font=("Times New Roman", 15), foreground='#585456', background="#FFFFFF")

        # ================================================ Style for Frame =============================================
        style.configure('Basic.TFrame', background="#FFFFFF")

        # ================================================ Style for LabelFrame ========================================
        style.configure('Basic.TLabelframe', background="#FFFFFF")

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def delete_entry(self):
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, "end")
