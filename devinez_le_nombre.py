import random


def jouer(minimum=1, maximum=100, essais_max=None):
    """Lance une partie de 'Devinez le nombre'.

    minimum, maximum : bornes de la plage (incluses)
    essais_max       : nombre d'essais autorisés (None = illimité)
    """
    nombre_secret = random.randint(minimum, maximum)
    essais = 0
    trouve = False

    print("Bienvenue au jeu Devinez le nombre !")
    print(f"Je pense à un nombre entre {minimum} et {maximum}. Pouvez-vous deviner lequel ?")
    if essais_max:
        print(f"Vous avez {essais_max} essais.")

    while not trouve:
        # Limite d'essais (personnalisation)
        if essais_max and essais >= essais_max:
            print(f"Perdu ! Vous avez utilisé vos {essais_max} essais. Le nombre était {nombre_secret}.")
            break

        saisie = input("Entrez votre estimation : ")

        # Conversion en entier, avec gestion des saisies invalides
        try:
            estimation = int(saisie)
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
            continue

        if estimation < minimum or estimation > maximum:
            print(f"Le nombre doit être compris entre {minimum} et {maximum}.")
            continue

        essais += 1

        if estimation > nombre_secret:
            print("Votre estimation est trop élevée. Essayez à nouveau.")
        elif estimation < nombre_secret:
            print("Votre estimation est trop basse. Essayez à nouveau.")
        else:
            print("Félicitations ! Vous avez deviné le bon nombre !")
            print(f"Vous l'avez trouvé en {essais} essai(s).")
            trouve = True


def lire_entier(message, defaut):
    """Demande un entier ; renvoie la valeur par défaut si l'utilisateur appuie sur Entrée."""
    saisie = input(message)
    if saisie.strip() == "":
        return defaut
    try:
        return int(saisie)
    except ValueError:
        print(f"Valeur invalide, on garde {defaut}.")
        return defaut


if __name__ == "__main__":
    personnaliser = input("Voulez-vous personnaliser la partie ? (o/n) : ").strip().lower()

    if personnaliser == "o":
        mini = lire_entier("Borne minimale (Entrée = 1) : ", 1)
        maxi = lire_entier("Borne maximale (Entrée = 100) : ", 100)
        if mini >= maxi:
            print("Plage invalide, on revient à 1-100.")
            mini, maxi = 1, 100
        limite = lire_entier("Nombre d'essais autorisés (Entrée = illimité) : ", 0)
        jouer(mini, maxi, limite if limite > 0 else None)
    else:
        jouer()
