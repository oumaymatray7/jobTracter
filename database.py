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
