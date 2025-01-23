
def algo1(a,b,c,d):
    """cette fonction retourne le plus petit des nombre a,b,c,d

    Args:
        a (int): nombre a
        b (int): nombre b
        c (int): nombre c
        d (int): nombre d

    Returns:
        int:le plus petit des 4 nombres
    """    
    if a<b :
        res = a
    else :
        res = b
    if res > c :
        res = c
    if res > d :
        res = d
    return res 

def algo2(mot):

    """calcule si il y a plus ou moins de voyelles ou de consonnes dans le mot (si nombre positif plus de voyelles)

    Args:
        mot (str) : le mot demandé

    Returns:
        bool: combien il y a de voyelle en plus que de consonne

    """
    res = 0 
    for caractere in mot :
        if caractere in "aeiouy" :
            res += 1
        else :
            res -= 1
    if res >0 :
        return True
    return False
def testalgo1():
    assert algo1(1,2,3,4) == 1 # erreur test 1
    assert algo1(1,2,8,4) == 1 # erreur test 2
    assert algo1(7,8,3,4) == 3 # erreur test 3

def testalgo2() :
    assert algo2("bonjour") == False # erreur test 1
    assert algo2("") == False # erreur test 1
    assert algo2("ouou") == True # erreur test 3



testalgo1()
testalgo2()

