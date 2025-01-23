scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
def max_score(l_score, l_joueurs, joueur):
    """la fonction retourne le meilleur score de joueur dans la liste des scores

    Args:
        l_score (list): liste de scores a valeur entiere positive
        l_joueurs (list): Liste des joueurs associés aux scores
        joueur (str): le nom du joueur dont on veux connaitre le score maximale
    Returns:
        int: le meilleur score du joueur
    """
    max=None
    # A chaque tour de boucle ka variable max contient le score maximale de joueur parmis les scores deja parcourus
    for i in range(len(l_score)):
        if l_joueurs[i] == joueur:
            if max is None or max < l_score[i]:
                max = l_score[i]
    return max

def test_max_score():
    
#def calcule_score(nom, liste_scores, liste_joueurs):
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

def meilleur_score_decroissant(liste_score):
    for i in range(1,len(liste_score)):
        if liste_score[i-1] < liste_score[i]:
            return False
    return True
def test_meilleur_score_decroissant():
    assert meilleur_score_decroissant([352100, 325410, 312785, 220199, 127853]) == True
    assert meilleur_score_decroissant([352100, 325410, 312785, 220199, 127853, 127853]) == True