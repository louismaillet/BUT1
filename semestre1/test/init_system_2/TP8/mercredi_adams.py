# modelisation de Mercredi : un dictionnaire { article ( str ) : prix (float ) }
courses_morticia = { " bave de crapeau " :17 , " oeufs de dragon " :157 ," lézards " :17 , " ketchup " :2 , " sel " :1}

def ajoute_article_dico(dico, article, prix) :
    """
    ajoute l'article au dictionnaire
    Args:
        dico (dict): dictionnaire des articles et des prix
        article (str): article à ajouter
        prix (float): prix de l'article
    Returns:
        dico (dict): dictionnaire des articles et des prix changé
    """
    dico[article] = prix
    return dico

def supprimer_article_dico(dico, article) :
    """
    supprime l'article du dictionnaire
    Args:
        dico (dict): dictionnaire des articles et des prix
        article (str): article à supprimer
    Returns:
        dico (dict): dictionnaire des articles et des prix changé
    """
    dico.pop(article)
    return dico

def modifier_prix(dico, article, prix) :
    """ 
    modifie le prix de l'article dans le dictionnaire
    Args:
        dico (dict): dictionnaire des articles et des prix
        article (str): article à modifier
        prix (float): nouveau prix de l'article
    Returns:
        dico (dict): dictionnaire des articles et des prix changé"""
    for art in dico.keys():
        if art == article :
            dico[article] = prix
    return dico

def montant_total(dico):
    """
    Calcule le montant total des valeurs dans un dictionnaire.

    Args:
        dico (dict): Un dictionnaire contenant des valeurs .

    Returns:
        float: Le montant total des valeurs dans le dictionnaire.
    """
    montant = 0
    for valeur in dico.values():
        montant += valeur
    return montant

def plus_cher(dico):
    """
    Trouve la clé avec la valeur la plus élevée dans un dictionnaire.

    Args:
        dico (dict): Un dictionnaire où les clés sont des éléments et les valeurs sont des nombres.

    Returns:
        La clé avec la valeur la plus élevée. Si le dictionnaire est vide, retourne None.
    """
    if len(dico) == 0:
        return None
    max = list(dico.keys())[0]
    for cle, valeur in dico.items():
        if valeur > dico[max] :
            max = cle
    return max
