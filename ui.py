import tkinter as tk
from tkinter import messagebox, ttk

from database import (ajouter_candidature, lire_candidatures,
                      modifier_candidature, supprimer_candidature)
from styles import appliquer_styles


class JobTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JobTracker – Suivi des Candidatures")
        self.root.geometry("1000x500")
        self.root.resizable(False, False)

        # 🎨 Appliquer les styles personnalisés
        appliquer_styles(self.root)

        # === BARRE DE RECHERCHE ===
        self.search_var = tk.StringVar()
        ttk.Label(root, text="🔎 Rechercher (Entreprise / Poste / Statut) :").place(x=370, y=0)
        self.entry_search = ttk.Entry(root, textvariable=self.search_var, width=40)
        self.entry_search.place(x=620, y=0)
        self.entry_search.bind("<KeyRelease>", self.rechercher_candidatures)

        # === FORMULAIRE ===
        self.frame_form = ttk.LabelFrame(root, text="Nouvelle candidature")
        self.frame_form.place(x=10, y=10, width=350, height=480)

        self.labels = [
            "Entreprise", "Poste", "Lien annonce",
            "Date (AAAA-MM-JJ)", "Statut", "Réponse", "Commentaire"
        ]
        self.entries = {}

        for i, label in enumerate(self.labels):
            ttk.Label(self.frame_form, text=label).grid(row=i, column=0, sticky="w", pady=5, padx=5)
            entry = ttk.Entry(self.frame_form, width=30)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[label] = entry

        # === BOUTONS ===
        ttk.Button(self.frame_form, text="Ajouter", command=self.ajouter).grid(row=7, column=0, pady=10)
        ttk.Button(self.frame_form, text="Modifier", command=self.modifier).grid(row=7, column=1)
        ttk.Button(self.frame_form, text="Supprimer", command=self.supprimer).grid(row=8, column=0)
        ttk.Button(self.frame_form, text="Vider", command=self.vider_formulaire).grid(row=8, column=1)

        # === TABLEAU DES CANDIDATURES ===
        self.tree = ttk.Treeview(
            root,
            columns=("id", "entreprise", "poste", "lien", "date", "statut", "reponse", "commentaire"),
            show="headings"
        )
        self.tree.place(x=370, y=30, width=620, height=450)

        # En-têtes
        self.tree.heading("id", text="ID")
        self.tree.heading("entreprise", text="Entreprise")
        self.tree.heading("poste", text="Poste")
        self.tree.heading("lien", text="Lien")
        self.tree.heading("date", text="Date")
        self.tree.heading("statut", text="Statut")
        self.tree.heading("reponse", text="Réponse")
        self.tree.heading("commentaire", text="Commentaire")

        # Colonnes
        self.tree.column("id", width=30, anchor="center")
        self.tree.column("entreprise", width=100)
        self.tree.column("poste", width=100)
        self.tree.column("lien", width=150)
        self.tree.column("date", width=80)
        self.tree.column("statut", width=80)
        self.tree.column("reponse", width=80)
        self.tree.column("commentaire", width=150)

        # Double clic → remplir formulaire
        self.tree.bind("<Double-1>", self.remplir_formulaire_depuis_tableau)

        # Charger les données au démarrage
        self.afficher_candidatures()

    # === ACTIONS ===

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
        if data[0] and data[1]:  # entreprise & poste obligatoires
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
            self.entries[key].insert(0, values[i + 1])  # i+1 pour ignorer l'ID

    def rechercher_candidatures(self, event=None):
        query = self.search_var.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in lire_candidatures():
            entreprise = str(row[1]).lower()
            poste = str(row[2]).lower()
            statut = str(row[5]).lower()

            if query in entreprise or query in poste or query in statut:
                self.tree.insert("", "end", values=row)
