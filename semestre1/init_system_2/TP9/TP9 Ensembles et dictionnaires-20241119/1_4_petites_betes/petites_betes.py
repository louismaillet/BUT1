"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    res = set()
    for pokemon in pokedex : # complexité O(n)
        res.add(pokemon[1])
    return res
    

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    res = 0 
    for _,f in pokedex : # complexité O(n)
        if f == famille :  # complexité O(1)
            res += 1
    return res

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    dico = {}
    for _,f in pokedex : # complexité O(n)
        if f in dico : # complexité O(1)
            dico[f] += 1
        else :
            dico[f] = 1
    return dico


def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_final = {} 
    for pokemon,famille in pokedex : # complexité O(n)
        if famille in dico_final : # complexité O(1)
            dico_final[famille].add(pokemon)
        else :
            dico_final[famille] = {pokemon}
    return dico_final


def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    max = None
    dico = frequences_famille(pokedex) # complexité O(n)
    for famille,nb in dico.items() :
        if max == None or nb > dico[max] :
            max = famille
    return max




    


# ==========================
# Petites bêtes (la suite)
# ==========================
mon_pokedex = {
    "Bulbizarre": {"Plante", "Poison"},
    "Aeromite": {"Poison", "Insecte"},
    "Abo": {"Poison"}
}

def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    res = set()
    for famille in pokedex.values() : # complexité O(n)
        res.update(famille)
    return res
print(toutes_les_familles_v2(mon_pokedex))


    

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    cpt = 0 
    for pokemon,nombre in  pokedex.items() :
        if famille in nombre :
            cpt += 1
    return cpt

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    dico = {}
    for famille in toutes_les_familles_v2(pokedex) : # complexité O(n)
        dico[famille] = nombre_pokemons_v2(pokedex,famille)
    return dico

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico = {}
    for pokemon, familles in pokedex.items(): # complexité O(n)
        for famille in familles: # complexité O(1)
            if famille in dico: # complexité O(1)
                dico[famille].add(pokemon)
            else:
                dico[famille] = {pokemon}
    return dico


def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    max_famille = None
    max_count = 0
    for famille in toutes_les_familles_v2(pokedex): # complexité O(n)
        count = nombre_pokemons_v2(pokedex, famille) # complexité O(n)
        if count > max_count:
            max_count = count
            max_famille = famille
    return max_famille
