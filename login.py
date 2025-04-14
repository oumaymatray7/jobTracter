import tkinter as tk
from tkinter import ttk, messagebox
from database import check_credentials
from styles import setup_styles
from ui import JobTrackerApp
from register import register_user_window  # ✅ Import de la fonction pour s'inscrire

def show_login_window():
    root = tk.Tk()
    root.title("🔐 Connexion – JobTracker")
    root.geometry("400x300")
    root.resizable(False, False)

    setup_styles()

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)

    # Champ utilisateur
    ttk.Label(frame, text="Nom d'utilisateur").grid(row=0, column=0, pady=10, sticky="w")
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=0, column=1)

    # Champ mot de passe
    ttk.Label(frame, text="Mot de passe").grid(row=1, column=0, pady=10, sticky="w")
    password_entry = ttk.Entry(frame, show="*", width=30)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Champs requis", "Veuillez remplir tous les champs.")
            return

        if check_credentials(username, password):
            messagebox.showinfo("Bienvenue", f"Bienvenue {username} !")
            root.destroy()
            app_root = tk.Tk()
            app = JobTrackerApp(app_root)
            app_root.mainloop()
        else:
            messagebox.showerror("Échec", "Identifiants incorrects.")

    # Bouton Se connecter
    ttk.Button(frame, text="Se connecter", command=login).grid(row=2, columnspan=2, pady=20)

    # ✅ Bouton Créer un compte
    ttk.Button(frame, text="Créer un compte", command=register_user_window).grid(row=3, columnspan=2, pady=5)

    root.mainloop()
