import tkinter as tk  # Importer tkinter
from tkinter import ttk  # Ajouter cet import pour ttk

# Dictionnaire de couleurs pour les modes clair et sombre
COLORS = {
    "background": "#f2f6fc",  # clair
    "primary": "#2f80ed",
    "secondary": "#56cc9d",
    "text": "#1f2d3d",
    "white": "#ffffff",
    "danger": "#eb5757",
    "gray": "#e0e0e0",
    
    # Sombre
    "dark_background": "#333333",
    "dark_text": "#ffffff",
    "dark_primary": "#1e4db6",
    "dark_secondary": "#45b29d",
}

FONT = ("Segoe UI", 10)

def appliquer_styles(root, dark_mode=False):
    style = ttk.Style(root)

    if dark_mode:
        root.configure(bg="#333333")  # Fond sombre
        for widget in root.winfo_children():
            widget.config(bg="#333333", fg="white")
    else:
        root.configure(bg="#f2f6fc")  # Fond clair
        for widget in root.winfo_children():
            widget.config(bg="#f2f6fc", fg="black")
