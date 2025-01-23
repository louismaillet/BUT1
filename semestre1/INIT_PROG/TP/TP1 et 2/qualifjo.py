def qualifjo(record, course, classement, sexe):
    """permet de savoir si un joueur est qualifié.e au jo 

    Args:
        record (float): record au 100m
        course (int): nombre de course gagné
        classement (int): classement du joueur actuelle
        sexe (int): le genre de la personne 1 = femme 0 = homme


    Returns:
        bool: retourne true si je joueur est qualifié.e ou false 
    """
    res = False
    if sexe == 0 :
        if (record <= 12 and course >= 3) or classement == 1 :
            res = True
    else :
        if (record <= 15 and course >= 3) or classement == 1 :
            res = True
    return res 
    


def testqualifjo():
    assert qualifjo(10.23,4,8,0) == True #test 1
    assert qualifjo(13.23,4,8,0) == False #test 1
    assert qualifjo(18.23,4,1,0) == True #test 1
    assert qualifjo(14.23,4,8,1) == True #test 1
    assert qualifjo(10.23,6,4,1) == True #test 1
