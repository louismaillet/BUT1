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
print(modifier_prix(courses_morticia, " bave de crapeau ", 18))

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

def menu():
    course = {}
    while True:
        print("----------------------------------------")
        print("Menu :") 
        print("1. Ajouter un article")
        print("2. Supprimer un article")
        print("3. Modifier le prix d'un article")
        print("4. Afficher le montant total")
        print("5. Afficher l'article le plus cher")
        print("6. Voir la liste des courses")
        print("7. Quitter")
        print("----------------------------------------")
        option = input("Choisissez une option : ")
        print("\n")
        if option == "1":
            article = input("Entrez le nom de l'article : ")
            prix = float(input("Entrez le prix de l'article : "))
            ajoute_article_dico(course, article, prix)
        elif option == "2":
            article = input("Entrez le nom de l'article : ")
            supprimer_article_dico(course, article)
        elif option == "3":
            article = input("Entrez le nom de l'article : ")
            prix = float(input("Entrez le nouveau prix de l'article : "))
            modifier_prix(course, article, prix)
        elif option == "4":
            print(montant_total(course))
        elif option == "5":
            print(plus_cher(course))
        elif option == "6":
            print(course)
        elif option == "7":
            print("Au revoir !")
            break
        else :
            print("Veuillez entrer une option valide.")
        print("\n")
        input("Appuyez sur Entrée pour continuer...")
        print("\n")
        print("\n")
        
        
        


menu()


