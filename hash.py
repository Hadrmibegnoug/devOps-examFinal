
import os
import hashlib

def calculer_hash_fichier(chemin_fichier):
    """Calcule le hash SHA-256 d’un fichier."""
    h = hashlib.sha256()
    try:
        with open(chemin_fichier, "rb") as f:
            for bloc in iter(lambda: f.read(4096), b""):
                h.update(bloc)
        return h.hexdigest()
    except Exception as e:
        print(f"Erreur lors du calcul du hash pour {chemin_fichier}: {e}")
        return None
    
def lister_fichiers_et_hashs(dossier):
    """Liste tous les fichiers d’un dossier et calcule leur hash."""
    fichiers_hashs = {}
    for racine, _, fichiers in os.walk(dossier):
        for nom in fichiers:
            chemin = os.path.join(racine, nom)
            hash_fichier = calculer_hash_fichier(chemin)
            if hash_fichier:
                fichiers_hashs.setdefault(hash_fichier, []).append(chemin)
    return fichiers_hashs

def afficher_fichiers_duplicats(fichiers_hashs):
    """Affiche les fichiers qui ont le même hash (contenu identique)."""
    trouve = False
    for hash_val, fichiers in fichiers_hashs.items():
        if len(fichiers) > 1:
            trouve = True
            print(f"\nHash: {hash_val}")
            for f in fichiers:
                print(f"  - {f}")
    if not trouve:
        print("Aucun fichier dupliqué trouvé.")

if __name__ == "__main__":
    dossier = input("Entrez le chemin du dossier à analyser : ")
    fichiers_hashs = lister_fichiers_et_hashs(dossier)
    afficher_fichiers_duplicats(fichiers_hashs)
