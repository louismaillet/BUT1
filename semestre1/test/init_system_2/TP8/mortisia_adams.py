# modelisation de Morticia : une liste de str et une liste de nombres
courses_morticia = [ " bave de crapeau " , " oeufs de dragon " , " lézards " , " ketchup " , " sel " ]
facture_morticia = [17 , 157 , 17 , 2 , 1]

def ajoute_article(course, facture, article, prix) :
    """
    ajoute l'article à la liste de course et le prix à la facture
    Args:
        course (list): liste des articles
        facture (list): liste des prix
        article (str): article à ajouter
        prix (int): prix de l'article
    Returns:
        course (list): liste des articles changé
        facture (list): liste des prix changé
    """
    course.append(article)
    facture.append(prix)
    return course, facture

def supprimer_article(course, facture, article) :
    """ 
    supprime l'article de la liste de course et de la facture
    Args:
        course (list): liste des articles
        facture (list): liste des prix
        article (str): article à supprimer
    Returns:
        course (list): liste des articles changé
        facture (list): liste des prix changé
    """
    for i in range(len(course)) :
        if course[i] == article :
            course.pop(i)
            facture.pop(i)
            break
    return course, facture

def modifier_prix(course, facture, article, prix) :
    """
    modifie le prix de l'article dans la facture
    Args:
        course (list): liste des articles
        facture (list): liste des prix
        article (str): article à modifier
        prix (int): nouveau prix de l'article
    Returns:
        facture (list): liste des prix changé
        course (list): liste des articles changé
    """
    for i in range(len(course)) :
        if course[i] == article :
            facture[i] = prix
            break
    return course, facture

def montant_total(facture) :
    """
    calcule le montant total de la facture
    Args:
        facture (list): liste des prix
    Returns:
        total (int): montant total de la facture
    """
    total = 0
    for i in range(len(facture)) :
        total += facture[i]
    return total

def plus_cher(course, facture) :
    """
    renvoie l'article le plus cher de la liste de course
    Args:
        course (list): liste des articles
        facture (list): liste des prix
    Returns:
        article (str): article le plus cher
    """
    if len(course) == 0 :
        return None
    article = course[0]
    prix = facture[0]
    for i in range(len(facture)) :
        if facture[i] > prix :
            article = course[i]
            prix = facture[i]
    return article












