def initialise_liste_bool(N):
    """ 
    initialise une liste de boolean de taille N avec tous les éléments à True avec les deux premiers éléments à False.

    Args:
        N (int): la taille de la liste -1
    Returns:
        list: une liste de boolean de taille N+1 avec tous les éléments à True sauf les deux premiers éléments à False."""
    lst = [] 

    if N>=0:
        lst = [True] * (N+1)  # initialise la liste avec des True de longeur n+1
        lst[0] = False  
        if len(lst) > 1 : #verifie si la liste est plus grande que 1
            lst[1] = False  
        
    return lst

def test_initialise_liste_bool():
    assert initialise_liste_bool(4) == [False, False, True, True, True] # test avec un nombre pair et renvoie [False, False, True, True, False]
    assert initialise_liste_bool(3) == [False, False, True,True] # test avec un nombre impair et renvoie [False, False, True,False]
    assert initialise_liste_bool(0) == [False] # test avec 1 et renvoie [False]
    assert initialise_liste_bool(1) == [False,False] # test avec un nombre négatif et renvoie [False, False]
    assert initialise_liste_bool(-5) == [] # test avec un nombre négatif et renvoie []

def x_met_false(x, liste):
    """ 
    Met les multiples de x à False dans une liste de booléens.

    Args:
        x (int): Le nombre dont les multiples doivent être mis à False.
        liste (list): Une liste de booléens représentant si un nombre est potentiellement premier ou non.
    
    Returns:
        list: La même liste avec les multiples de x mis à False.
    """
    liste_copie = liste.copy()
    if liste_copie[x] == False:
        liste_copie[x] = True  # on ne change pas les multiples de x qui sont déjà à False
    for i in range(2 * x, len(liste_copie), x): 
        liste_copie[i] = False
    
    return liste_copie

def test_x_met_false():
    assert x_met_false(2, [False, False, True, True, True]) == [False, False, True, True, False] # test avec un nombre pair
    assert x_met_false(3, [False, False, True, True, True, True,True]) == [False, False, True, True, True, True, False] # test avec un nombre impair


def crible_premiers_entiers(N): 
    """ 
    Retourne une liste des nombres premiers inférieurs ou égaux à N

    Args:
        N (int): la valeur jusqu'à laquelle on veut trouver les nombres premiers
    Returns:
        list: une liste des nombres premiers inférieurs ou égaux à N   """ 
    
    lst = []
    liste_true = initialise_liste_bool(N)
    for i in range(2, N+1):
        # a chaque iteration, on met les multiples de i à False dans la liste_true
        if liste_true[i] == True:
            liste_true = x_met_false(i, liste_true)
            lst.append(i)

    return lst
            

def test_crible_premiers_entiers(): 
    assert crible_premiers_entiers(10) == [2, 3, 5, 7] # test avec un nombre pair 10 et renvoier [2, 3, 5, 7]
    assert crible_premiers_entiers(5) == [2, 3,5] # test avec un nombre impair 5 et renvoier [2, 3,5]
    assert crible_premiers_entiers(0) == [] # test avec un nombre nul et renvoier []
    assert crible_premiers_entiers(20) == [2, 3, 5, 7, 11, 13, 17, 19] # test avec un nombre 20 et renvoier [2, 3, 5, 7, 11, 13, 17, 19]
    assert crible_premiers_entiers(8) == [2, 3, 5, 7] # test avec un nombre pair 8 et renvoier [2, 3, 5, 7]