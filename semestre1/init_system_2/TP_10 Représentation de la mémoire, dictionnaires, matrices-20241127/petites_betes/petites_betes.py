""" Correction Exercice 4 petites bêtes TP 10 """

ma_liste_pokemon =[("Bulbizarre", {"Plante", "Poison"}, "001. png"),
                   ("Herbizarre", {"Plante", "Poison"}, "002. png"),
                   ("Abo", {"Poison"}, "023. png"),
                   ("Jungko", {"Plante"}, "254. png")]

def pokemon_par_famille(liste_pokemon):
    """ détermine le dictionnaire de clefs : nom de famille
        et de valeurs l'ensemble des pokemon de cette famille

    Args:
        liste_pokemon (list): liste de tuples (nom_poke, ensemble des familles, image)

    Returns:
        dict: le dictionnaire nom_famille ensemble des noms de pokemon de cette famille
    """
    dico_famille = {}
    for nom_poke, familles, _ in liste_pokemon:
        for nom in familles:
            if nom in dico_famille:
                dico_famille[nom].add(nom_poke)
            else:
                dico_famille[nom] = {nom_poke}
    return dico_famille

def test_pokemon_par_famille():
    assert pokemon_par_famille(ma_liste_pokemon) == {'Plante': {'Bulbizarre', 'Herbizarre', 'Jungko'},
                                                     'Poison': {'Bulbizarre', 'Herbizarre', 'Abo'}}
    print("Test de la fonction pokemon_par_famille : ok")