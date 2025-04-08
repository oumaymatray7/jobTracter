import re
from datetime import datetime


def est_date_valide(date_str):
    """
    Vérifie si la date est au format AAAA-MM-JJ.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def est_email_valide(email):
    """
    Vérifie si l'email est au format standard.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def champs_obligatoires_remplis(data, champs_obligatoires):
    """
    Vérifie que certains champs (par nom ou index) ne sont pas vides.
    """
    for champ in champs_obligatoires:
        if not data[champ].strip():
            return False
    return True


def nettoyer_texte(texte):
    """
    Nettoie le texte (supprime les espaces avant/après).
    """
    return texte.strip()
