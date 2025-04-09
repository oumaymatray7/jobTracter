import tkinter as tk
from tkinter import ttk

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

    # Appliquer les couleurs de base
    if dark_mode:
        root.configure(background=COLORS["dark_background"])  # Fond sombre
        style.configure("TButton",
                        background=COLORS["dark_primary"],  # Boutons sombres
                        foreground=COLORS["white"],  # Texte en blanc
                        font=("Segoe UI", 10, "bold"))
        style.configure("Treeview",
                        background=COLORS["dark_background"],  # Arrière-plan sombre
                        foreground=COLORS["dark_text"],  # Texte clair
                        rowheight=25,
                        fieldbackground=COLORS["dark_background"])  # Fond des cellules sombre
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 10, "bold"),
                        background=COLORS["dark_primary"],  # Fond des en-têtes
                        foreground=COLORS["white"])  # Texte blanc dans les en-têtes
        style.configure("TLabel", background=COLORS["dark_background"], foreground=COLORS["dark_text"])
        style.configure("TEntry", font=FONT, padding=4, fieldbackground=COLORS["dark_background"])

    else:
        root.configure(background=COLORS["background"])  # Fond clair
        style.configure("TButton",
                        background=COLORS["primary"],  # Boutons clairs
                        foreground=COLORS["white"],  # Texte blanc
                        font=("Segoe UI", 10, "bold"))
        style.configure("Treeview",
                        background=COLORS["white"],  # Arrière-plan clair
                        foreground=COLORS["text"],  # Texte foncé
                        rowheight=25,
                        fieldbackground=COLORS["white"])  # Fond des cellules clair
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 10, "bold"),
                        background=COLORS["primary"],  # Fond des en-têtes
                        foreground=COLORS["white"])  # Texte blanc dans les en-têtes
        style.configure("TLabel", background=COLORS["background"], foreground=COLORS["text"])
        style.configure("TEntry", font=FONT, padding=4)
    
    style.map("Treeview", background=[('selected', COLORS["primary"])])
    style.map("TButton", background=[("active", COLORS["secondary"])])
