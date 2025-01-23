
# ==========================
# La maison qui rend fou
# ==========================
qrf1={"Abribus":"Astus", "Jeancloddus":"Abribus",
"Plexus":"Gugus","Astus":None, "Gugus":"Plexus",
"Saudepus":None}
mqrf2={"Abribus" : "Astus", "Jeancloddus":None,
        "Plexus":"Saudepus", "Astus":"Gugus",
        "Gugus":"Plexus", "Saudepus":None}

def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    guichet_final = mqrf[guichet]
    while guichet_final != None:
        guichet = guichet_final
        guichet_final = mqrf[guichet]
    return guichet
print(quel_guichet(qrf1, "Abribus"))
print( quel_guichet(mqrf2, "Abribus"))




def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    guichet_final = mqrf[guichet]
    nb_visite = 1
    while guichet_final != None:
        guichet = guichet_final
        guichet_final = mqrf[guichet]
        nb_visite += 1
    return guichet, nb_visite
print(quel_guichet_v2(qrf1, "Saudepus"))
print( quel_guichet_v2(mqrf2, "Abribus"))

def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    guichet_final = mqrf[guichet]
    nb_visite = 1
    while guichet_final != None:
        guichet = guichet_final
        guichet_final = mqrf[guichet]
        nb_visite += 1
        if nb_visite > len(mqrf):
            return None
    return guichet, nb_visite


mqrf3 = {
    "Abribus": "Astus",
    "Jeancloddus": "Astus",
    "Plexus": "Jeancloddus",
    "Astus": "Gugus",
    "Gugus": "Plexus",
    "Saudepus": "Bielorus"
}
    
print(quel_guichet_v3(mqrf3, "Abribus"))
print( quel_guichet_v3(mqrf2, "Abribus"))
    

