import tkinter as tk
from tkinter import ttk

COLORS = {
    "background": "#f2f6fc",
    "primary": "#2f80ed",
    "secondary": "#56cc9d",
    "text": "#1f2d3d",
    "white": "#ffffff",
    "danger": "#eb5757",
    "gray": "#e0e0e0"
}

FONT = ("Segoe UI", 10)

def appliquer_styles(root):
    style = ttk.Style(root)
    root.configure(bg=COLORS["background"])
    style.theme_use("clam")

    style.configure("Treeview",
                    background=COLORS["white"],
                    foreground=COLORS["text"],
                    rowheight=25,
                    fieldbackground=COLORS["white"],
                    font=FONT)

    style.map("Treeview", background=[('selected', COLORS["primary"])])

    style.configure("Treeview.Heading",
                    font=("Segoe UI", 10, "bold"),
                    background=COLORS["primary"],
                    foreground=COLORS["white"])

    style.configure("TButton",
                    font=("Segoe UI", 10, "bold"),
                    padding=6,
                    background=COLORS["primary"],
                    foreground=COLORS["white"])

    style.map("TButton", background=[("active", COLORS["secondary"])])

    style.configure("TLabel",
                    font=FONT,
                    background=COLORS["background"],
                    foreground=COLORS["text"])

    style.configure("TEntry", font=FONT, padding=4)
