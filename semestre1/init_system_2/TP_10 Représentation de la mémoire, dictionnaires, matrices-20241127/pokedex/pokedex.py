"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for nom,_ in pokedex :
        if pokemon == nom :
            return True
    return False


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    attaques = set()
    for nom,attaque in pokedex :
        if nom == pokemon :
            attaques.add(attaque)
    return attaques


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    nb = 0
    for _,att in pokedex :
        if att == attaque :
            nb += 1
    return nb


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    max = ''
    max_nb = 0
    for nom,att in pokedex :
        if nombre_de_v1(att, pokedex) > max_nb :
            max = att
            max_nb = nombre_de_v1(att, pokedex)
    return max

# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for pok in pokedex.keys() :
        if pokemon == pok :
            return True 
    return False

def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    nb = 0
    for att in pokedex.values() :
        if attaque in att :
            nb += 1
    return nb


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    compteur = {}
    for attaques in pokedex.values():
        for att in attaques:
            if att in compteur:
                compteur[att] += 1
            else:
                compteur[att] = 1
    max_attaque = None
    max_count = 0
    for attaque, count in compteur.items():
        if count > max_count:
            max_attaque = attaque
            max_count = count
    return max_attaque

print(attaque_preferee_v2({
        'Dragon': {'Carmache','Colimucus', 'Palkia'},
        'Sol': {'Carmache','Carmache'},
        'Eau': {'Palkia'}}))

    

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex.values():
        print(poke)
        if pokemon in poke :
            return True
    return False

def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    res = set()
    for att,poke in pokedex.items():
        if pokemon in poke :
            res.add(att)
    return res



def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    for att,pokemon in pokedex.items():
        if att == attaque :
            return len(pokemon)
    return 0

def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    if len(pokedex) == 0 :
        return None
    max = 0
    for att,pokemon in pokedex.items():
        if len(pokemon) > max :
            max = len(pokemon)
            res = att
    return res

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    pokedex_v2 = {}
    for nom,att in pokedex_v1 :
        if nom in pokedex_v2 :
            pokedex_v2[nom].add(att)
        else :
            pokedex_v2[nom] = {att}
    return pokedex_v2
    


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    pokedex_v3 = {}
    for att,pokemon in pokedex_v2.items():
        for poke in pokemon :
            if poke in pokedex_v3 :
                pokedex_v3[poke].add(att)
            else :
                pokedex_v3[poke] = {att}
    return pokedex_v3

print(v2_to_v3({
        'Carmache': {'Dragon', 'Sol'},
        'Colimucus': {'Dragon'},
        'Palkia': {'Eau', 'Dragon'}}))

