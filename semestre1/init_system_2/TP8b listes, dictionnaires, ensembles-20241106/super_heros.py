
def intelligence_moyenne(dico):
    """ la fonction renvoie la moyenne des intelligences des super-héros du dictionnaire dico
    Args:
        dico (dict): un dictionnaire dont les valeurs sont des tuples de trois éléments
    Returns:
        float: la moyenne des intelligences des super-héros du dictionnaire dico
    """
    if len(dico) == 0:
        return None, 'il sont tous nuls'
    total_intelligence = 0
    for stats in dico.values():
        total_intelligence += stats[1]
    return total_intelligence / len(dico)


def kikelplusfort(dico):
    """ la fonction renvoie le super-héros le plus fort du dictionnaire dico
    Args:
        dico (dict): un dictionnaire dont les valeurs sont des tuples de trois éléments
    Returns:
        str: le super-héros le plus fort du dictionnaire dico
    """
    if len(dico) == 0:
        return None
    max_force = 0
    super_hero = ''
    for hero, stats in dico.items():
        if stats[0] > max_force:
            max_force = stats[0]
            super_hero = hero
    return super_hero
    
def combienDeCretins(dico):
    """ la fonction renvoie le nombre de personnages dont l'intelligence est strictement inférieure à la moyenne
    Args:
        dico (dict): un dictionnaire dont les valeurs sont des tuples de trois éléments
    Returns:
        int: le nombre de personnages dont l'intelligence est strictement inférieure à la moyenne
    """
    moyenne_intelligence = intelligence_moyenne(dico)
    if moyenne_intelligence is None:
        return 0
    cpt = 0
    for stats in dico.values():
        if stats[1] < moyenne_intelligence:
            cpt += 1
    return cpt
