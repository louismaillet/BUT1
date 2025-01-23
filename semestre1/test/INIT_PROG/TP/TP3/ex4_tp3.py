#4.1  
def nb_pair(liste):
    """une fonction qui retourne la somme des nombres pairs d’une liste d’entiers.

    Args:
        liste (list): une liste de nombres

    Returns:
        int: la somme des nombres pair
    """    
    resultat = 0
    # a chaque iteration, resultat contient la somme des nombres pairs deja passé
    for nombre in liste:
        if nombre%2 == 0:
            resultat += nombre

    return resultat 

#4.2
def der_voy(mot):
    """une fonction qui retourne la dernière voyelle d’une chaîne de caractères.

    Args:
        mot (str): un mot (lol) 

    Returns:
        str : retorune la derniere voyelle qui est dans le mot
    """    
    resultat = "" 
    # a chaque iteration, resultat contient la derniere voyelle observée

    for lettre in mot :
        if lettre in "aeiouy" or "AEIOUY" :
            resultat = lettre
    if resultat == "" :
        resultat = None

    return resultat

#4.3
def nb_nega(liste):
    """la proportion de nombre negatif et positif

    Args:
        liste (list): une liste de nombre positif et negatif

    Returns:
        resultat (Float) : retourne la proportion de nombre negatif 
    """    
    nombre_nega = 0
    nombre_posi = 1
    # a chaque iteration, nombre_posi et nombre_nega contient le nombre respectif deja passé
    resultat = 0
    for nombre in liste :
        if nombre < 0 :
            nombre_nega += 1
        else :
            nombre_posi += 1
    if nombre_posi == 0 :
        resultat == 1
    elif nombre_nega == 0:
        resultat = 0
    else :
        resultat = nombre_nega/ nombre_posi 

    
    return resultat 



def test_tout():
    assert nb_pair([1,2,3,4,5,6,7,8,9,10]) == 30 #test1
    assert nb_pair([-1,-2,2,1]) == 0#test2
    assert nb_pair([1]) == 0#test3
    assert nb_pair([]) == 0 #test4
def test_voy():
    assert der_voy("huwu") == 'u' #test1
    assert der_voy("QUOICOUBAKA") == 'A' #test2
    assert der_voy("kakouuuuuuuuuuuuuuuuu") == 'u'#test3
    assert der_voy("") == None #test4
def test_nega():
    assert nb_nega([0,1,2]) == 0
    assert nb_nega([4,-1,-2,2]) == 0.5
    assert nb_nega([]) == 0
    assert nb_nega([-1,-2]) == 1
