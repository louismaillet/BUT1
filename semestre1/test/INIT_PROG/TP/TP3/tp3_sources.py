# exercice 1
def pair_sup_impair(entree):
    """cette fonction prends en parametre un liste et renvoie si il y a 
    plus de nombre impaire ou paire / renvoie True si il y a plus de pair


    Args:
        entree (list) : liste de nombre a analyser

    Returns:
        (bool) : retourn True si il y a plus de nombre paire que impaire
        et False si l'inverse
    """
    nb_pair = 0
    nb_impair = 0
    # au début de chaque tour de boucle
    # xxx = 0,0,1,2,3,3,4 || 1,1,1,2,2,2 
    # yyy = 0,1,1,1,1,3,3 || 0,1,2,2,3,4
    for nombre in entree:
        if nombre % 2 == 0:
            nb_pair += 1
        else:
            nb_impair += 1
    return nb_pair >= nb_impair


def test_pair_sup_impair():
    assert pair_sup_impair([1,4,6,-2,-5,3,10]) == True
    assert pair_sup_impair([0,0,0]) == True
    assert pair_sup_impair([1,2,3]) == False 
    assert pair_sup_impair([-1,-2]) == True


# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = float("inf")
    # au début de chaque tour de boucle res est le plus petit élément
    # cela bugger car cella prends le plus petit nombre au dessus de la valeur 
    
    # déjà énuméré supérieur à valeur
    for elem in liste_nombres:
        if valeur < elem < res:
            res = elem
    if res == float('inf'):
        res = None 
    return res
min_sup([-2, 12, 7, 3, 9, 2, 1, 4, 9], 5)

def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = " "  

    for c2 in phrase:
        if c1 == ' ' and c2 != ' ':  
            resultat += 1
        c1 = c2


    return resultat


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus
    assert nb_mots("     ") == 0  # celui ci non plus


