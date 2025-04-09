import os
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

from database import (ajouter_candidature, lire_candidatures,
                      modifier_candidature, supprimer_candidature)
from styles import appliquer_styles


class JobTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JobTracker – Suivi des Candidatures")
        self.root.geometry("1000x600")  # Adjusted window size for better layout
        self.root.resizable(True, True)

        # Initialiser en mode clair
        self.light_mode = True
        appliquer_styles(self.root, self.light_mode)

        # === Ajouter un bouton pour basculer en Dark Mode ===
        self.toggle_button = ttk.Button(
            root, text="Mode Sombre", command=self.toggle_mode
        )
        self.toggle_button.place(x=900, y=10)  # Positionner le bouton en haut à droite

        # === Chargement des icônes ===
        self.icons = {}

        def charger_image(nom_fichier, size=(18, 18), color=None):
            path = os.path.join(os.path.dirname(__file__), "assets", nom_fichier)
            if os.path.exists(path):
                img = Image.open(path).convert("RGBA").resize(size)
                if color:
                    r, g, b = color
                    pixels = img.getdata()
                    new_pixels = [(r, g, b, p[3]) if p[3] > 0 else p for p in pixels]
                    img.putdata(new_pixels)
                return ImageTk.PhotoImage(img)
            return None

        icon_color = (0, 0, 0)  # Noir pour harmoniser
        self.icons["logo"] = charger_image("logo.png", size=(90, 90))
        self.icons["add"] = charger_image("add.png", size=(16, 16), color=icon_color)
        self.icons["edit"] = charger_image("edit_icon.webp", size=(16, 16), color=icon_color)
        self.icons["delete"] = charger_image("delete.png", size=(16, 16), color=icon_color)

        if self.icons["logo"]:
            logo_label = ttk.Label(root, image=self.icons["logo"])
            logo_label.image = self.icons["logo"]
            logo_label.place(x=125, y=10)

        # === Formulaire gauche ===
        self.frame_form = ttk.LabelFrame(root, text="Nouvelle candidature")
        self.frame_form.place(x=10, y=10, width=350, height=480)

        self.labels = [
            "Entreprise", "Poste", "Lien annonce",
            "Date (AAAA-MM-JJ)", "Statut", "Réponse", "Commentaire"
        ]
        self.entries = {}

        for i, label in enumerate(self.labels):
            ttk.Label(self.frame_form, text=label).grid(row=i, column=0, sticky="w", pady=5, padx=5)
            entry = ttk.Entry(self.frame_form, width=40)  # Increased width for entries
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[label] = entry

        # === Boutons ===
        ttk.Button(self.frame_form, text="Ajouter", image=self.icons["add"], compound="left", command=self.ajouter, width=15).grid(row=7, column=0, pady=10)
        ttk.Button(self.frame_form, text="Modifier", image=self.icons["edit"], compound="left", command=self.modifier, width=15).grid(row=7, column=1)
        ttk.Button(self.frame_form, text="Supprimer", image=self.icons["delete"], compound="left", command=self.supprimer, width=15).grid(row=8, column=0)
        ttk.Button(self.frame_form, text="Vider", command=self.vider_formulaire, width=15).grid(row=8, column=1)

        # === Zone tableau + recherche ===
        self.frame_table = ttk.LabelFrame(root, text="Candidatures enregistrées")
        self.frame_table.place(x=370, y=10, width=620, height=480)

        self.search_var = tk.StringVar()
        ttk.Label(self.frame_table, text="🔍 Rechercher :").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.entry_search = ttk.Entry(self.frame_table, textvariable=self.search_var, width=40)
        self.entry_search.grid(row=0, column=1, padx=5, pady=8, sticky="w")
        self.entry_search.bind("<KeyRelease>", self.rechercher_candidatures)

        self.tree = ttk.Treeview(
            self.frame_table,
            columns=("id", "entreprise", "poste", "lien", "date", "statut", "reponse", "commentaire"),
            show="headings"
        )
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.tree.heading("id", text="ID")
        self.tree.heading("entreprise", text="Entreprise")
        self.tree.heading("poste", text="Poste")
        self.tree.heading("lien", text="Lien")
        self.tree.heading("date", text="Date")
        self.tree.heading("statut", text="Statut")
        self.tree.heading("reponse", text="Réponse")
        self.tree.heading("commentaire", text="Commentaire")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("entreprise", width=150)  # Adjusted column width
        self.tree.column("poste", width=150)  # Adjusted column width
        self.tree.column("lien", width=200)  # Adjusted column width
        self.tree.column("date", width=100)
        self.tree.column("statut", width=100)
        self.tree.column("reponse", width=100)
        self.tree.column("commentaire", width=200)  # Adjusted column width

        self.tree.bind("<Double-1>", self.remplir_formulaire_depuis_tableau)

        self.afficher_candidatures()

    # === Méthodes ===

    def get_form_data(self):
        return tuple(entry.get() for entry in self.entries.values())

    def get_selected_item_id(self):
        selected = self.tree.focus()
        if not selected:
            return None
        return self.tree.item(selected)["values"][0]

    def afficher_candidatures(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in lire_candidatures():
            self.tree.insert("", "end", values=row)

    def ajouter(self):
        data = self.get_form_data()
        if data[0] and data[1]:
            for row in self.tree.get_children():
                if self.tree.item(row)["values"][1] == data[0] and self.tree.item(row)["values"][2] == data[1]:
                    messagebox.showwarning("Doublon", "Cette candidature existe déjà.")
                    return
            ajouter_candidature(data)
            messagebox.showinfo("Succès", "Candidature ajoutée.")
            self.vider_formulaire()
            self.afficher_candidatures()
        else:
            messagebox.showerror("Erreur", "Champs 'Entreprise' et 'Poste' obligatoires.")

    def modifier(self):
        selected_id = self.get_selected_item_id()
        if not selected_id:
            messagebox.showwarning("Attention", "Sélectionnez une candidature à modifier.")
            return
        data = self.get_form_data()
        modifier_candidature(selected_id, data)
        messagebox.showinfo("Succès", "Candidature modifiée.")
        self.vider_formulaire()
        self.afficher_candidatures()

    def supprimer(self):
        selected_id = self.get_selected_item_id()
        if not selected_id:
            messagebox.showwarning("Attention", "Sélectionnez une candidature à supprimer.")
            return
        if messagebox.askyesno("Confirmation", "Supprimer cette candidature ?"):
            supprimer_candidature(selected_id)
            messagebox.showinfo("Supprimé", "Candidature supprimée.")
            self.vider_formulaire()
            self.afficher_candidatures()

    def vider_formulaire(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def remplir_formulaire_depuis_tableau(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected)["values"]
        for i, key in enumerate(self.entries):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i + 1])

    def rechercher_candidatures(self, event=None):
        query = self.search_var.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in lire_candidatures():
            if query in str(row[1]).lower() or query in str(row[2]).lower() or query in str(row[5]).lower():
                self.tree.insert("", "end", values=row)

    def toggle_mode(self):
        self.light_mode = not self.light_mode
        # Appliquer le style approprié en fonction du mode
        appliquer_styles(self.root, self.light_mode)

        # Changer le texte du bouton
        if self.light_mode:
            self.toggle_button.config(text="Mode Sombre")
        else:
            self.toggle_button.config(text="Mode Clair")
