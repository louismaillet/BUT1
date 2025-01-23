""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre, liste_options):
    """ 
    Affiche un menu avec un titre et une liste d'options.
    Args:
        titre (str): Le titre du menu.
        liste_options (list): La liste des options du menu.
    """

    ligne = '+' + '-' * (len(titre) + 2) + '+'
    print(ligne)
    print("| " + titre + " |")
    print(ligne)
    for i in range(len(liste_options)):
        print(f"{i+1} -> {liste_options[i]}")
    

def demander_nombre(message, borne_max):
    
    """
    Demande à l'utilisateur de saisir un nombre et vérifie qu'il est valide.
    Args:
        message (str): Le message à afficher pour demander le nombre.
        borne_max (int): La valeur maximale que le nombre peut prendre.
    Returns:
        int: Le nombre saisi par l'utilisateur qui est valide.
    """

    a = input(message)
    if not a.isdecimal() or int(a) != float(a) or int(a) < 1 or int(a) > borne_max:
        return None
    else :
        return int(a)

def menu(titre, liste_options):
    afficher_menu(titre, liste_options)
    demande = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+']:', len(liste_options))
    return demande

def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département", 
                     "Quitter"]
    liste_communes = []
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
            while True:
                fichier = input("Choisissez le nom du fichier à charger : ")
                try:
                    liste_communes = charger_fichier_population(fichier)
                    print(f"Il y a {len(liste_communes)} communes dans le fichier.")
                    break
                except:
                    print("Veuillez entrer un nom de fichier valide.")
        
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
            while True:
                nom_pop = input("Choisissez le nom de la ville dont vous voulez connaître la population : ")
                try:
                    pop = population_d_une_commune(liste_communes, nom_pop)
                    print(f"La population de {nom_pop} est de {pop} habitants.")
                    break
                except:
                    print("Veuillez entrer un nom de ville valide.")
        
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        else:
            break
        input("Appuyez sur Entrée pour continuer.")
    print("Merci, au revoir!")




def charger_fichier_population(nom_fic):
    """
    Charge un fichier CSV contenant les populations des communes.
    Args:
        nom_fic (str): Le nom du fichier CSV à charger.
    Returns:
        list: Une liste de tuple contenant les informations des communes.
    """
    liste_pop = []
    try:
        f = open(nom_fic, 'r')
        f.readline()
        for ligne in f:
            ligne = ligne.split(';')
        liste_pop.append((ligne[0], ligne[1], int(ligne[-1])))
        
    except :
        print("Erreur lors de la lecture du fichier")
    return liste_pop

def population_d_une_commune(liste_pop, nom_commune):
    """
    Retourne la population d'une commune donnée.
    Args:
        liste_pop (list): La liste des populations des communes.
        nom_commune (str): Le nom de la commune dont on veut connaître la population.
    Returns:
        int: La population de la commune si elle est trouvée, sinon None.
    """
    try :

        for commune in liste_pop:
            if commune[1] == nom_commune:
                return commune[2]
            
                
    except :
        print("Erreur lors de la recherche de la commune")

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    """
    Retourne une liste des communes dont le nom commence par une chaîne donnée.
    Args:
        liste_pop (list): La liste des populations des communes.
        debut_nom (str): Le début du nom des communes à rechercher.
    Returns:
        list: Une liste des communes dont le nom commence par la chaîne donnée.
    """
    liste_communes = []
    try:
        for commune in liste_pop:
            if commune[1][:(len(debut_nom))] == debut_nom : #if commune[1] == startswith(debut_nom):
                liste_communes.append(commune)
        return liste_communes
    except:
        print("Erreur lors de la recherche des communes")    

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    ...

def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    ...

def place_top(commune, liste_pop):
    ...

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
programme_principal()
