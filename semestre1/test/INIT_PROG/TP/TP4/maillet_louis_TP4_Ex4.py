#exo4 
def meme_debut_de_mot(liste , lettre):
    """retourne une nouvelle liste avec les mots de la liste qui commencent par la lettre

    Args:
        liste (list): une liste de mots
        lettre (str): une lettre
    Returns:
        list: une nouvelle liste avec les mots qui commencent par la lettre
    """
    liste_fini = []
    # a chaque iteration, liste_fini contient la nouvelle liste avec les mots qui commencent par la lettre cherchee 
    for i in range(len(liste)):
        if liste[i][0] == lettre:
            liste_fini.append(liste[i])
    return liste_fini

def test_meme_debut_de_mot():
    assert meme_debut_de_mot(["Abeille", "Amarante", "Amelie", "Anas", "Antonia"], "A") == ["Abeille", "Amarante", "Amelie", "Anas", "Antonia"] # test avec une liste de mots qui commencent par la lettre "A"
    assert meme_debut_de_mot(["Bonjour", "Hello", "Salut", "Coucou", "Au revoir","Bonjour"], "B") == ["Bonjour","Bonjour"] # test avec une liste de mots
    assert meme_debut_de_mot(["abceeeabc", "abcabcabc"], "a") == ["abceeeabc", "abcabcabc"] # test avec une liste de mots qui commencent par la lettre "a"
    assert meme_debut_de_mot(["abceeeabc", "abcabcabc"], "b") == [] # test avec une liste de mots qui sera vide
    assert meme_debut_de_mot([], "c") == [] # test avec une liste de mots qui sera vide
    assert meme_debut_de_mot([" abceeeabc", "abcabcabc"], "") == [] # test avec une liste de mots qui sera vide