import random
import string

def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

if __name__ == "__main__":
    longueur = int(input("Longueur du mot de passe : "))
    print("🔐 Votre mot de passe généré :", generer_mot_de_passe(longueur))
