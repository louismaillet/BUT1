scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
#4.1
def max_score(l_score, l_joueurs, joueur):
    """la fonction retourne le meilleur score de joueur dans la liste des scores

    Args:
        l_score (list): liste de scores a valeur entiere positive
        l_joueurs (list): Liste des joueurs associés aux scores
        joueur (str): le nom du joueur dont on veux connaitre le score maximale
    Returns:
        int: le meilleur score du joueur
    """
    maximum = None
    if len(l_score) == len(l_joueurs) and joueur in l_joueurs:

        # A chaque tour de boucle la variable max contient le score maximale du joueur parmis les scores deja parcourus
        for i in range(len(l_score)):
            if l_joueurs[i] == joueur:
                if maximum is None or maximum < l_score[i]:
                    maximum = l_score[i]
    return maximum

def test_max_score():
    assert max_score(scores, joueurs, "Batman") == 352100 # test avec un joueurs qui a plusieurs scores batman qui doit renvoyer 352100
    assert max_score(scores, joueurs, "Robin") == 325410 # test avec un joueurs qui a un seul scores robin qui doit renvoyer 325410
    assert max_score(scores, joueurs, "test") == None # test avec un joueurs qui n'existe pas test qui doit renvoyer None
    assert max_score([],[],"coucou") == None # test avec deux liste vide qui doit renvoyer None
#4.2
def tri_max_score(l_score):
    """verifie si la liste des scores est trié dans l'ordre decroissant
    Args:
        l_score (list): une liste de scores 
    Returns:
        bool: True si la liste est trié dans l'ordre decroissant, False sinon
    """
    for i in range(len(l_score)-1):
        if l_score[i] < l_score[i+1]:
            return False
    return True
def test_tri_max_score():
    assert tri_max_score(scores) == True # test avec une liste trié dans l'ordre decroissant qui doit renvoyer True
    assert tri_max_score([5, 3, 0, 0, 0]) == True # test avec une liste trié dans l'ordre decroissant qui doit renvoyer True
    assert tri_max_score([2, 3, 2, 1]) == False # test avec une liste non trié dans l'ordre decroissant qui doit renvoyer False
    assert tri_max_score([]) == True # test avec une liste vide qui doit renvoyer True
    assert tri_max_score([5]) == True # test avec une liste d'un seul element qui doit renvoyer True
    
#4.3
def nb_meilleur_score_joueur(l_joueurs, joueur):
    """retourne le nombre de meilleur score d'un joueur
    Args:
        l_joueurs (list): liste des joueurs associés aux scores
        joueur (str): le nom du joueur dont on veux connaitre le nombre de meilleur score
    Returns:
        int: le nombre de meilleur score du joueur inscit en parametre 
    """
    cpt = 0

    if joueur in l_joueurs:

        # A chaque tour de boucle la variable cpt contient le nombre de meilleur score du joueur parmis les scores deja parcourus
        for i in range(len(l_joueurs)):
            if l_joueurs[i] == joueur:
                cpt += 1
    return cpt 

def test_nb_meilleur_score_joueur():
    assert nb_meilleur_score_joueur( joueurs, "Batman") == 3 # test avec un joueurs qui a plusieurs scores batman qui doit renvoyer 3
    assert nb_meilleur_score_joueur( joueurs, "Robin") == 1 # test avec un joueurs qui a un seul scores robin qui doit renvoyer 1
    assert nb_meilleur_score_joueur( joueurs, "test") == 0 # tesrt avec un joueurs qui n'existe pas test qui doit renvoyer 0
    assert nb_meilleur_score_joueur([],"coucou") == 0 # test avec deux liste vide qui doit renvoyer 0
    

#4.4
def classement_joueur_meilleur_score( l_joueurs, joueur ):
    """retourne le meilleur classement d'un joueur si le joueur n'existe pas retourne None
    Args:
        l_joueurs (list): liste des joueurs triée dans l'ordre du mieux classés au moins bien classés
        joueur (str): le nom du joueur dont on veux connaitre le classement
    Returns:
        int: le meilleur classement du joueur
    """
    # A chaque tour de boucle la variable on verifie si l_joueurs[i] est egale a joueur si oui on retourne son classement
    if joueur in l_joueurs:

        for i in range(len(l_joueurs)):
            if l_joueurs[i] == joueur:
                return  i+1
    
    return None
    

def test_classement_joueur_meilleur_score():
    assert classement_joueur_meilleur_score( joueurs, "Batman") == 1 # test avec un joueurs qui a plusieurs scores batman qui doit renvoyer 1
    assert classement_joueur_meilleur_score( joueurs, "Robin") == 2 # test avec un joueurs qui a un seul scores robin qui doit renvoyer 2
    assert classement_joueur_meilleur_score( joueurs, "test") == None # test avec un joueurs qui n'existe pas test qui doit renvoyer None
    assert classement_joueur_meilleur_score([],"coucou") == None # test avec deux listes vide qui doit renvoyer None
#4.5
def indice_insertion(score, l_score):
    """retourne l'indice d'insertion d'un score dans une liste de scores triée dans l'ordre decroissant
    Args:
        score (int): le score a inserer
        l_score (list): liste des scores triée dans l'ordre decroissant
    Returns:
        int: l'indice d'insertion
    """
    # A chaque tour de boucle on verifie si le score est superieur au score actuel
    for i in range(len(l_score)):
        if score > l_score[i]:
            return i
    
    return len(l_score)

def test_indice_insertion():
    assert indice_insertion(314570, [352100, 325410, 312785, 220199, 127853]) == 2 # test avec un score qui doit etre placé en un indice 2
    assert indice_insertion(352101, [352100, 325410, 312785, 220199, 127853]) == 0 # test avec un score qui doit etre placé en un indice 0
    assert indice_insertion(127852, [352100, 325410, 312785, 220199, 127853]) == 5 # test avec un score qui doit etre placé en un indice 5
    assert indice_insertion(0, [352100, 325410, 312785, 220199, 127853]) == 5 # te avec un score qui doit etre placé en un indice 5
    assert indice_insertion(0, []) == 0 # test avec une liste vide et le nombre doit etre placé en un indice 0

#4.6
def ajout_score(score_joueur, nom_joueur, scores, joueurs):
    """retourne rien mais change les listes scores et joueurs en ajoutant le score et le nom du joueur
    Args:
        score_joueur (int): le score du joueur
        nom_joueur (str): le nom du joueur
        scores (list): une liste des scores
        joueurs (list): une liste des joueurs
    Returrns:
        Rien
    
    """
    indice = indice_insertion(score_joueur, scores)
    scores.insert(indice, score_joueur)
    joueurs.insert(indice, nom_joueur)

def test_ajout_score():
    # Ajout des tests pour la fonction ajout_score
    # Test avec un score à insérer au milieu de la liste
    scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ["Batman", "Robin", "Batman", "Joker", "Batman"]
    ajout_score(314570, "test", scores, joueurs)
    assert scores == [352100, 325410, 314570, 312785, 220199, 127853]
    assert joueurs == ["Batman", "Robin", "test", "Batman", "Joker", "Batman"] 

    # Test avec un score à insérer à la fin de la liste
    scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ["Batman", "Robin", "Batman", "Joker", "Batman"]
    ajout_score(0, "test", scores, joueurs)
    assert scores == [352100, 325410, 312785, 220199, 127853, 0]
    assert joueurs == ["Batman", "Robin", "Batman", "Joker", "Batman", "test"]

    # Test avec une liste vide
    scores = []
    joueurs = []
    ajout_score(0, "test", scores, joueurs)
    assert scores == [0]
    assert joueurs == ["test"]

    

    
#def test_calcule_score(nom, liste_scores, liste_joueurs):
#    """Ajoute le score d'un joueur à la liste des scores et le nom à la liste des joueurs
#    Args:
#        nom (str): le nom du joueur
#        liste_scores (int): une liste des scores
#        liste_joueurs (list): une liste des joueurs
#    Returns:
#        int : le meilleur score du joueur ou none si pas de score
#        """
#    score_final = None
#    # a chaque tour de boucle score final contient le meilleurs score passée du joueur chercher
#    for i in range(len(scores)):
#        if liste_joueurs[i] == nom:
#            if score_final is None or score_final < liste_scores[i]:
#                score_final = liste_scores[i]
#    return score_final
#
#def test_calcule_score():
#
#    assert calcule_score("Batman", [352100, 325410, 312785, 220199, 127853], ["Batman", "Robin", "Batman", "Joker", "Batman"]) == 352100
#    assert calcule_score("Robin", [352100, 325410, 312785, 220199, 127853], ["Batman", "Robin", "Batman", "Joker", "Batman"]) == 325410
#    assert calcule_score("Joker", [], []) == None
#    assert calcule_score("", [], []) == None
#    assert calcule_score("coucou", [352100, 325410, 312785, 220199, 127853],["Batman", "Robin", "Batman", "Joker", "Batman"]) == None
