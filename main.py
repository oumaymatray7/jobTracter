import tkinter as tk

from database import create_database
from ui import JobTrackerApp


def main():
    # Créer la base de données si elle n'existe pas
    create_database()

    # Lancer l'application Tkinter
    root = tk.Tk()
    app = JobTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
