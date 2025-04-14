
import tkinter as tk
from tkinter import ttk, messagebox  
from database import check_credentials  
from styles import setup_styles        
from ui import JobTrackerApp           

def show_login_window():
    # Création ... de la :::fenêtre 
    root = tk.Tk()
    root.title("🔐 Connexion – JobTracker")   
    root.geometry("400x300")                  
    root.resizable(False, False)               # Désactive le redimensionnement

    setup_styles()  # Applique les styles depuis le fichier styles.py

    # Crée un cadre de  les champs de saisie
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)

    # Champ Nom d'utilisateur 
    ttk.Label(frame, text="Nom d'utilisateur").grid(row=0, column=0, pady=10, sticky="w")
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=0, column=1)

    # Champ Mot de passe
    ttk.Label(frame, text="Mot de passe").grid(row=1, column=0, pady=10, sticky="w")
    password_entry = ttk.Entry(frame, show="*", width=30)  # show="*" masque le mot de passe
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()  # Récupère 
        password = password_entry.get()  

        # controle de saisie 
        if not username or not password:
            messagebox.showwarning("Champs requis", "Veuillez remplir tous les champs.")
            return

        # Vérifie les identifiants avec la base de données
        if check_credentials(username, password):
            messagebox.showinfo("Bienvenue", f"Bienvenue {username} !")
            root.destroy() 

            app_root = tk.Tk()
            app = JobTrackerApp(app_root)
            app_root.mainloop()
        else:
           
            messagebox.showerror("Échec", "Identifiants incorrects.")

    
    ttk.Button(frame, text="Se connecter", command=login).grid(row=2, columnspan=2, pady=20)

    
    root.mainloop()
