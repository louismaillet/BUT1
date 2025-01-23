# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    """_summary_

    Returns:
        _type_: _description_
    """
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # je vérifie la longueur
        if len(mot_de_passe) < 8:
            longueur_ok = False;
        else:
            longueur_ok = True
        # je vérifie s'il y a un chiffre
        chiffre_ok = False
        for lettre in mot_de_passe:
            if lettre.isdigit():
                chiffre_ok = True
        # je vérifie qu'il n'y a pas d'espace
        sans_espace = True
        for lettre in mot_de_passe:
            if lettre == " ":
                sans_espace = False
        # Je gère l'affichage
        if not longueur_ok:
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok:
            print("Votre mot de passe doit comporter au moins un chiffre")
        elif not sans_espace:
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

#dialogue_mot_de_passe()

# je pense que ca fonctionnne mais elle n'est vraiment pas optimise

def longueur_ok(mdp) :
    """retourne si une chaine de caractere est plus grande que 8

    Args:
        mdp (srt): un mot de passe

    Returns:
        bool: retourne True si c'est plus que 8 False sinon
    """
    return len(mdp) >= 8

def chiffre_ok(mdp):
    """
    Vérifie si le mot de passe contient au moins un chiffre.

    Args:
        mdp (str): un mot de passe

    Returns:
        bool: retourne True si le mot de passe contient au moins un chiffre, False sinon
    """

    for cara in mdp:
        if cara.isdigit():
            return True
    return False

def sans_espace(mdp):
    """
    Vérifie si le mot de passe ne contient pas d'espaces.

    Args:
        mdp (str): un mot de passe

    Returns:
        bool: retourne True si le mot de passe ne contient pas d'espaces, False sinon
    """
    for cara in mdp:
        if cara == " ":
            return False
    return True

def au_mois_3_chiffres(mdp):
    """
    Vérifie si le mot de passe contient au moins 3 chiffres.

    Args:
        mdp (str): un mot de passe

    Returns:
        bool: retourne True si le mot de passe contient au moins 3 chiffres, False sinon
    """
    nb_chiffres = 0
    for cara in mdp:
        if cara.isdigit():
            nb_chiffres += 1
    return nb_chiffres >= 3

def chiffre_suite(mdp):
    """
    Vérifie si le mot de passe contient une suite de 2 chiffres.

    Args:
        mdp (str): un mot de passe

    Returns:
        bool: retourne True si le mot de passe contient une suite de 2 chiffres, False sinon
    """
    for i in range(len(mdp)-1):
        if mdp[i].isdigit() and mdp[i+1].isdigit():
            return False
    return True

def chiffre_mini_unique(mdp):
    """
    Vérifie si le mot de passe contient au maximum une fois le plus petit chiffre.
    Args:
        mdp (str): un mot de passe
    Returns:
        bool: retourne True si le mot de passe contient au maximum une fois le plus petit chiffre, False sinon
    """
    chiffres = []
    for cara in mdp:
        if cara.isdigit():
            chiffres.append(int(cara))
    if len(chiffres) == 0:
        return True
    mini = min(chiffres)
    chiffres.remove(mini)
    return mini not in chiffres
    
def check_mdp():
    login = input("entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")
        elif not au_mois_3_chiffres(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins 3 chiffre")
        elif not chiffre_suite(mot_de_passe) :
            print("Votre mot de passe ne doit pas comporter une suite de 2 chiffres")
        elif not chiffre_mini_unique(mot_de_passe) :
            print("Votre mot de passe doit comporter au maximum une fois le plus petit chiffre")

        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return login, mot_de_passe
    


def ecris_mdp():
    login, mot_de_passe = check_mdp()
    association = {}
    f = open("mdpUltraSecret.txt", "a")
    association[login] = mot_de_passe
    for cle, valeur in association.items():
        if login == cle:
            association[login] = mot_de_passe
    f.write(f"{login} : {mot_de_passe}\n")
    print(association)

ecris_mdp()
e