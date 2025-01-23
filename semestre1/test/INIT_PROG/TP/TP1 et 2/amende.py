def amende(vitesse, limite):
    """calcule les consequence d'un exces de vitesse

    Args:
        limite (float): limite autorise 
        vitesse (float): vitesse au dessus de la vitesse reglementaire

    Returns:
        int: retourne 3 valeur le prix de l'amende, les points perdu, suspension de permis
    """   
    res = (0,0,0)
    if vitesse-limite == 0:
        res = (0,0,0) 
    elif vitesse-limite < 20 :
        if limite < 50 :
            res = (68,1,0)
        res = (135,1,0)
    elif vitesse-limite < 30 :
        res = (135,2,0)
    elif vitesse-limite < 40 :
        res = (135,3,3)
    elif vitesse-limite < 50 :
        res = (135,4,3)
    else :
        res = (1500,6,3)
    return res
    

def testamende():
    assert amende(130,130) == (0,0,0) #test 1 
    assert amende(135,100) == (135,3,3) #test 1
    assert amende(55,50) == (135,1,0) #test 1