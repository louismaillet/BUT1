# modelisation de F é tide : une liste de tuples
courses_morticia = [( " bave de crapeau " , 17) , ( " oeufs de dragon " , 157) , ( " lézards " , 17) , ( " ketchup " , 2) , ( " sel " , 1) ]



def ajoute_article(course, article, prix) :
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
    course.append((article, prix))
    return course
def supprimer_article(course, article) :
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
        if course[i][0] == article :
            course.pop(i)
            break
    return course

def modifier_article(course, article, prix) :
    """
    modifie le prix de l'article dans la liste de course  
    Args:
        course (list) : liste des articles
        article (str) : article à modifier
        prix (int) : nouveau prix de l'article
    Returns:
        course (list) : liste des articles changé
    """
    for i in range(len(course)) :
        if course[i][0] == article :
            course[i] = (article, prix)
            break
    return course
def montant_article(course):
    """
    renvoie le montant total de la liste de course
    Args:
        course (list): liste des articles
    Returns:
        montant (int): montant total
    """
    montant = 0
    for i in range(len(course)) :
        montant += course[i][1]
    return montant
def plus_cher(course) :
    """
    renvoie l'article le plus cher de la liste de course
    Args:
        course (list): liste des articles
    Returns:
        article (str): article le plus cher
    """
    if len(course) == 0 :
        return None
    article = course[0]
    prix = course[0][1]
    for i in range(len(course)) :
        if course[i][1] > prix :
            article = course[i]
            prix = course[i][1]
    return article[0]













