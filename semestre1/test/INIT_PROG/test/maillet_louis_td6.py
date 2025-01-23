def est_triee(liste):
    """
    Vérifie si une liste est triée dans l'ordre croissant.
    Args:
        liste (list): La liste des éléments à vérifier.
    Returns:
        bool: True si la liste est triée dans l'ordre croissant, False sinon.
    """
    i = 0
    res = True
    while i < len(liste) - 1:
        if liste[i] > liste[i + 1]:
            res = False
        i += 1
    return res

def est_palindrome(chaine):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    Args:
        chaine (str): La chaîne de caractères à vérifier.
    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    debut = 0
    fin = len(chaine) - 1
    while debut < fin:
        if chaine[debut] != chaine[fin]:
            return False
        debut += 1
        fin -= 1
    return True
