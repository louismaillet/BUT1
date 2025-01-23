<<<<<<< HEAD
def 
=======
def mini(liste):
    mini = None 
    for elt in liste:
        if mini == None :
            mini = elt
        elif mini > elt :
            mini = elt
    return mini
def ecart_nb(liste):
    """calcule l'ecart entre les deux nombre les plus eloignes

    Args:
        liste (lst): une liste d'element

    Returns:
        int: retourne l'ecart 
    """
    min = None
    max = None
    # a chaque iteration, max contient le plus grand nombre de la liste
    # a chaque iteration, min contient le plus petit nombre de la liste
    for elt in liste:
        if min == None :
            min = elt
            max = elt
        elif min > elt :
             min = elt
        elif max < elt :
            max = elt
    if min == None :
        resultat = None
    else : 
        resultat = max - min
    return resultat
def sup_dix(liste): 
    """donne le nombre de nombre superieur a 10

    Args:
        liste (list): une liste de nombre   
   
    Returns:   
        int: nombre de valeur sup a 10   
    """    
    res= 0
    for nombre in liste :
        if nombre >10 :
            res += 1 
    return res 
def moy_nega(liste):
    res = 0
    nombre = 0
    for elt in liste :
        if elt < 0 :
            res += elt
            nombre += 1
    resultat = res / nombre
    if res ==0:
        resultat == 0
        
    return resultat

def test_mini():
    assert mini([1,2,3,4,5,6,7,8,9]) == 1
    assert mini ([4,5,6,12,3,78,9]) == 3
    assert mini ([]) == None
    assert mini ([-1,-3,6]) == -3
def test_ecart():
    assert ecart_nb([]) == None
    assert ecart_nb([1,2,3,4,5,6]) == 5
    assert ecart_nb([2,3,4,5,6,8,1,11]) == 10
    assert ecart_nb([2,3,4,-5,6,8,1,10]) == 15
def test_sup_dix():
    assert sup_dix([]) == 0
    assert sup_dix([11,11,1,1,1,11,11,11,11,11]) == 7
    assert sup_dix([1,2,3,4,5,6,7,8,9]) == 0
    assert sup_dix([-11,2,5,-4,6,15]) == 1
def test_moy():
    assert moy_nega([-1,-2,-3]) == -2
    assert moy_nega([-2,-2,-10,-1,-5]) == -4
    assert moy_nega([-1,-2,1,15]) == -1.5


>>>>>>> a2e742e280cb6b1a07788b524700a3dedeaef181
