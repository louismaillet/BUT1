# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieurs on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if len(liste_observations) == 0:
        return None
    oiseau_max = liste_observations[0]
    # a chanque iteration oiseau_max contient le nom de l'oiseau le plus observe parmi les elements de la liste deja parcourus
    for observation in liste_observations:
        if observation[1] > oiseau_max[1]: 
            oiseau_max = observation
            
    return oiseau_max[0]


def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieurs on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if len(liste_observations) == 0:
        return None
    oiseau_max = liste_observations[0]
    for i in range(1, len(liste_observations)):
        if liste_observations[i][1] > oiseau_max[1]:
            oiseau_max = liste_observations[i]
            
    return oiseau_max[0]
def recherche_oiseau(nom_oiseau, liste_observation):
    """
    Recherche un oiseau dans une liste d'observations.
    Args:
        nom_oiseau (str): Le nom de l'oiseau à rechercher.
        liste_observation (list): Une liste de tuples où chaque tuple contient des informations sur un oiseau.
    Returns:
        tuple: Le tuple contenant les informations de l'oiseau si trouvé, sinon None.
    """
    for oiseau in liste_observation :
        if oiseau[0] == nom_oiseau :
            return oiseau
    return None
    
def recherche_par_famille(famille, liste_oisseaux):
    
#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)
