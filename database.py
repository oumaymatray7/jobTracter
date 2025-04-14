import sqlite3

DB_NAME = "jobtracker.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entreprise TEXT NOT NULL,
            poste TEXT NOT NULL,
            lien_annonce TEXT,
            date_candidature TEXT,
            statut TEXT,
            reponse TEXT,
            commentaire TEXT
        )
    """)
    conn.commit()
    conn.close()


def ajouter_candidature(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO candidatures 
        (entreprise, poste, lien_annonce, date_candidature, statut, reponse, commentaire)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()


def lire_candidatures():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidatures ORDER BY date_candidature DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def modifier_candidature(id, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE candidatures SET 
            entreprise = ?, 
            poste = ?, 
            lien_annonce = ?, 
            date_candidature = ?, 
            statut = ?, 
            reponse = ?, 
            commentaire = ?
        WHERE id = ?
    """, (*data, id))
    conn.commit()
    conn.close()


def supprimer_candidature(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM candidatures WHERE id = ?", (id,))
    conn.commit()
    conn.close()
def init_db():
    conn = sqlite3.connect("recrutement.db")
    cursor = conn.cursor()

    # Créer la table users si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()



def check_credentials(username, password):
    conn = sqlite3.connect("recrutement.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
def register_user(username, password):
    conn = sqlite3.connect("recrutement.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True  # Inscription réussie
    except sqlite3.IntegrityError:
        return False  # Nom d'utilisateur déjà existant
    finally:
        conn.close()
    