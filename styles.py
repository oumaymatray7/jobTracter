import tkinter as tk
from tkinter import ttk

# Dictionnaire de couleurs pour les modes clair et sombre
COLORS = {
    # Mode clair
    "background": "#f4f6f9",  # Fond clair
    "primary": "#007bff",  # Bleu clair pour les éléments principaux
    "secondary": "#28a745",  # Vert pour les éléments secondaires
    "text": "#333333",  # Texte foncé
    "white": "#e5e555",  # Blanc pur
    "danger": "#e53e3e",  # Rouge vif pour les alertes
    "gray": "#e5e5e5",  # Gris clair pour le fond des tableaux ou bordures
    
    # Mode sombre
    "dark_background": "#181818",  # Fond sombre
    "dark_text": "#f0f0f0",  # Texte clair sur fond sombre
    "dark_primary": "#1c7ed6",  # Bleu foncé pour les boutons et éléments principaux
    "dark_secondary": "#38b2ac",  # Vert menthe secondaire pour le contraste
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
