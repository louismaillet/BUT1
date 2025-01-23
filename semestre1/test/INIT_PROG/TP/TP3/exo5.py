#exercice 5.1
def som_n_entier(n):
    """une fonction qui fait la somme des n premiers entiers

    Args:
        n (int): nombre entier positif

    Returns:
        int: valeur
    """    
    resultat = 0
    for i in range(n+1):
        resultat += i
    return resultat

som_n_entier(4)

def test_som():
    assert som_n_entier(4) == 10 #test 1
    assert som_n_entier(0) == 0 #test 2
    assert som_n_entier(12) == 78 #test 3
    assert som_n_entier(100) == 5050 #test4



#exercice 5.2
def suite_Syracuse(n, val_init):

    """ c'est la suite de syracuse implemente en python

    Returns:
        int: le resultat de la suite jusqu'a Un
    """    
    Un = val_init
    for i in range(n):  
        if Un % 2 == 0:  
            Un = Un // 2  
        else:
            Un = 3 * Un + 1   
    return Un

suite_Syracuse(4,6)
def test_suite():
    assert suite_Syracuse(2,6) == 10 #test1
    assert suite_Syracuse(4,6) == 16 #test2
    assert suite_Syracuse(0,6) == 6 # test3
    assert suite_Syracuse(6,15) == 53 # test4
    assert suite_Syracuse(12,13) == 1