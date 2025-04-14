import tkinter as tk
from tkinter import ttk, messagebox
from database import register_user 

def register_user_window():
    window = tk.Tk()
    window.title("Créer un compte – JobTracker")
    window.geometry("400x280")
    window.resizable(False, False)

    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    ttk.Label(frame, text="Nom d'utilisateur").grid(row=0, column=0, pady=10, sticky="w")
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=0, column=1)

 
    ttk.Label(frame, text="Mot de passe").grid(row=1, column=0, pady=10, sticky="w")
    password_entry = ttk.Entry(frame, show="*", width=30)
    password_entry.grid(row=1, column=1)


    ttk.Label(frame, text="Confirmer le mot de passe").grid(row=2, column=0, pady=10, sticky="w")
    confirm_entry = ttk.Entry(frame, show="*", width=30)
    confirm_entry.grid(row=2, column=1)

 
    def register():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        confirm = confirm_entry.get().strip()

        if not username or not password or not confirm:
            messagebox.showwarning("Champs requis", "Tous les champs sont obligatoires.")
            return
        if password != confirm:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return

        
        success = register_user(username, password)
        if success:
            messagebox.showinfo("Succès", f"Utilisateur '{username}' enregistré avec succès.")
            window.destroy()
        else:
            messagebox.showerror("Erreur", f"Le nom d'utilisateur '{username}' est déjà utilisé.")

    ttk.Button(frame, text="S'inscrire", command=register).grid(row=3, columnspan=2, pady=20)

    window.mainloop()
