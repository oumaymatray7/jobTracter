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

        # ✅ Appliquer les styles globaux
        appliquer_styles(self.root)

        # --- Formulaire de saisie ---
        self.frame_form = tk.LabelFrame(root, text="Nouvelle candidature", padx=10, pady=10)
        self.frame_form.place(x=10, y=10, width=350, height=480)

        self.labels = [
            "Entreprise",
            "Poste",
            "Lien annonce",
            "Date (AAAA-MM-JJ)",
            "Statut",
            "Réponse",
            "Commentaire"
        ]
        self.entries = {}

        for i, label in enumerate(self.labels):
            tk.Label(self.frame_form, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.frame_form, width=35)
            entry.grid(row=i, column=1)
            self.entries[label] = entry

        # --- Boutons d'action ---
        tk.Button(self.frame_form, text="Ajouter", width=15, command=self.ajouter).grid(row=7, column=0, pady=10)
        tk.Button(self.frame_form, text="Modifier", width=15, command=self.modifier).grid(row=7, column=1)
        tk.Button(self.frame_form, text="Supprimer", width=15, command=self.supprimer).grid(row=8, column=0)
        tk.Button(self.frame_form, text="Vider", width=15, command=self.vider_formulaire).grid(row=8, column=1)

        # --- Tableau des candidatures ---
        self.tree = ttk.Treeview(
            root,
            columns=("id", "entreprise", "poste", "lien", "date", "statut", "reponse", "commentaire"),
            show="headings"
        )
        self.tree.place(x=370, y=10, width=620, height=470)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)

        self.tree.bind("<Double-1>", self.remplir_formulaire_depuis_tableau)

        # --- Afficher les données au démarrage ---
        self.afficher_candidatures()

    def get_form_data(self):
        """
        Récupère les données saisies dans le formulaire.
        """
        return tuple(entry.get() for entry in self.entries.values())

    def get_selected_item_id(self):
        """
        Récupère l'ID de la ligne sélectionnée dans le tableau.
        """
        selected = self.tree.focus()
        if not selected:
            return None
        return self.tree.item(selected)["values"][0]

    def ajouter(self):
        data = self.get_form_data()
        if data[0] and data[1]:  # entreprise & poste obligatoires
            ajouter_candidature(data)
            messagebox.showinfo("Succès", "Candidature ajoutée.")
            self.vider_formulaire()
            self.afficher_candidatures()
        else:
            messagebox.showerror("Erreur", "Champs 'Entreprise' et 'Poste' obligatoires.")

    def afficher_candidatures(self):
        """
        Recharge toutes les candidatures depuis la base dans le tableau.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in lire_candidatures():
            self.tree.insert("", "end", values=row)

    def remplir_formulaire_depuis_tableau(self, event):
        """
        Lors du double clic sur une ligne → remplir les champs du formulaire.
        """
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected)["values"]
        for i, key in enumerate(self.entries):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i + 1])  # i+1 pour ignorer l'id

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
        """
        Vide tous les champs du formulaire.
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END)
