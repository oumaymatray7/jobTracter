import tkinter as tk
from tkinter import ttk

# 🎨 Palette de couleurs
COLORS = {
    "background": "#f7f9fc",
    "primary": "#2f80ed",
    "secondary": "#56cc9d",
    "text": "#333333",
    "white": "#ffffff",
    "danger": "#eb5757",
    "gray": "#dfe6e9"
}

# 🅰️ Style global de police
FONT = ("Segoe UI", 10)

def appliquer_styles(root):
    """
    Applique les styles aux composants Tkinter via ttk.Style
    """
    style = ttk.Style(root)
    root.configure(bg=COLORS["background"])
    
    # Choisir un thème compatible avec les couleurs
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
                    font=FONT,
                    padding=6,
                    background=COLORS["primary"],
                    foreground=COLORS["white"])

    style.map("TButton",
              background=[("active", COLORS["secondary"])])

    style.configure("TLabel",
                    font=FONT,
                    background=COLORS["background"],
                    foreground=COLORS["text"])

    style.configure("TEntry",
                    padding=5,
                    font=FONT)
