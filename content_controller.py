import tkinter as tk
from tkinter import ttk


class Content_control(tk.Tk, ttk.LabelFrame, ttk.Entry, ttk.Label, tk.Button, tk.Toplevel, ttk.Treeview):

    def destroy_content(self):
        for child in self.winfo_children():
            child.destroy()

    def clear_treeview(self=ttk.Treeview):
        for widget in self.get_children():
            self.delete(widget)

    def change_button_state(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(relief="flat", state="active")
