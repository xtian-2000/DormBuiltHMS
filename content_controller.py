import tkinter as tk
from tkinter import ttk


class Content(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button, tk.Toplevel, ttk.Treeview):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()
