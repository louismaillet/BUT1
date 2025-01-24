# coding: utf-8
"""
            SAE1.02 SERPIUT'O
         BUT1 Informatique 2024-2025

    Module serpent.py
    Ce module implémente l'API permettant de gérer les informations des joueurs (idenfier à leur serpent)
"""

#& C:/Users/mka19/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/mka19/OneDrive/Documents/BUTInformatique/SAEIAJeu/source/serpent.py
#/bin/python /home/iut45/Etudiants/o22406805/Documents/SAE_serpiuto/source/arene.py
def Serpent(nom_joueur:str, num_joueur:int,points:int=0,positions:list=None,tps_s:int=0,tps_p:int=0,tps_m:int=0,direction:str='N')->dict:
    """Créer un joueur avec toutes les informations le concernant.

    Args:
        nom_joueur (str): nom du joueur
        num_joueur (int): numero du joueur
        points (int, optional): nombre de points attribués au joueur. Defaults to 0.
        positions (list, optional): la liste des positions occupées par le serpent sur l'arène. Defaults to None.
        tps_s (int, optional): temps restant pour le bonus surpuissance. Defaults to 0.
        tps_p (int, optional): temps restant pour le bonus protection. Defaults to 0.
        tps_m (int, optional): temps restant pour le bonus mange-mur. Defaults to 0.
        direction (str, optional): dernière direction prise par le serpent. Defaults to 'N'.

    Returns:
        dict: une dictionnaire contenant les informations du serpent
    """    
    return {
        "nom_serp": nom_joueur,
        "num_serp": num_joueur,
        "points_serp": points,
        "positions_serp": positions,
        "tps_s_serp": tps_s,
        "tps_p_serp": tps_p,
        "tps_m_serp": tps_m,
        "direction_serp": direction}


def get_nom(serpent:dict)->str:
    """retourne le nom du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: le nom du joueur associé à ce serpent
    """    
    return serpent['nom_serp'] 

def get_num_joueur(serpent:dict)->int:
    """retourne le numéro du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le numéro du joueur associé à ce serpent
    """   
    return serpent['num_serp']

def get_points(serpent:dict)->int:
    """retourne le nombre de points du joueur associé au serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de points du joueur associé à ce serpent
    """   
    return serpent['points_serp']

def get_liste_pos(serpent:dict)->list:
    """retourne la liste des positions occupées par le serpent sur l'arène. La première position étant la tête du serpent

    Args:
        serpent (dict): le serpent considéré

    Returns:
        list: la liste des positions occupées par le serpent
    """    
    
    return serpent['positions_serp']

def get_queue(serpent:dict)->[int,int]:
    """retourne la position (lig,col) de la queue du serpent dans l'arène

    Args:
        serpent (dict): le serpent considéré

    Returns:
        [int,int]: la position lig,col du la queue du serpent
    """    
    return [serpent["positions_serp"][-1][0],serpent["positions_serp"][-1][1]]

def get_derniere_direction(serpent:dict)->str:
    """retourne la dernière direction choisie par le joueur pour se déplacer

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: un des caractère N S E O
    """    
    return serpent['direction_serp']
    
def get_bonus(serpent:dict)->list:
    """retourne une liste contenant les bonus obtenus par le joueur
        c'est-à-dire ceux pour lesquels le temps restant est supérieur à 0

    Args:
        serpent (dict): le serpent considéré

    Returns:
        list: la liste des bonus du joueur
    """    
    bonus = []

    if serpent['tps_s_serp'] > 0:
        bonus.append(-3)
    if serpent['tps_p_serp'] > 0:
        bonus.append(-5)
    if serpent['tps_m_serp'] > 0:
        bonus.append(-4)
    return bonus

def ajouter_points(serpent:dict,nb_points:int):
    """ajoute (ou enlève) des points à un serpent

    Args:
        serpent (dict): le serpent considéré
        nb_points (int): le nombre de points à ajouter (si négatif enlève des points)
    """    
    serpent["points_serp"] += nb_points
    
def set_liste_pos(serpent:dict, tete:list):
    """initialise la liste des positions d'un serpent

    Args:
        serpent (dict): le serpent considéré
        tete (list): la liste des positions occupées par ce serpent
    """   
    serpent["positions_serp"] = tete

def set_derniere_direction(serpent:dict, direction:str):
    """Met à jout la dernière direction utilisée par le serpent (utile pour l'affichage)

    Args:
        serpent (dict): le serpent considéré
        direction (str): un des caractère N S E O
    """
    serpent['direction_serp'] = direction

def to_str(serpent:dict)->str:
    """produit une chaine de caractères contenant les informations principales d'un serpent sour la forme
    Joueur 1 -> 143 s:0 m:4 p:0
    où Joueur 1 est le nom du joueur, après la flèche se trouve le nombre de point
    puis le temps restant de chaque bonus (supuissante, mange mur et protection)

    Args:
        serpent (dict): le serpent considéré

    Returns:
        str: la chaine de caractères donnant les informations principales d'un serpent 
    """    
    str_final = get_nom(serpent) + "-> " + str(get_points(serpent)) + " s:" + str(get_temps_surpuissance(serpent)) + " m:" + str(get_temps_mange_mur(serpent)) + " p:" + str(get_temps_protection(serpent))
    return str_final

def get_temps_protection(serpent:dict)->int:
    """indique le temps restant pour le bonus protection

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """    
    return serpent['tps_p_serp']
    
def get_temps_mange_mur(serpent:dict)->int:
    """indique le temps restant pour le bonus mange mur

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """
    return serpent['tps_m_serp']   
    
def get_temps_surpuissance(serpent:dict)->int:
    """indique le temps restant pour le bonus surpuissance

    Args:
        serpent (dict): le serpent considéré

    Returns:
        int: le nombre de tours restant pour ce bonus
    """   
    return serpent['tps_s_serp']
    
def ajouter_temps_protection(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus protection

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """    
    serpent["tps_p_serp"] = get_temps_protection(serpent) + temps
    return serpent["tps_p_serp"]
    
def ajouter_temps_mange_mur(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus mange mur

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """  
    serpent["tps_m_serp"] = get_temps_mange_mur(serpent) + temps
    return serpent["tps_m_serp"]

def ajouter_temps_surpuissance(serpent:dict, temps:int)->int:
    """ajoute du temps supplémentaire pour le bonus surpuissance

    Args:
        serpent (dict): le serpent considéré
        temps (int): le nombre de tours à ajouter

    Returns:
        int: le nombre de tours total restant pour ce bonus
    """    
    serpent["tps_s_serp"] = get_temps_surpuissance(serpent) + temps
    return serpent["tps_s_serp"]
    
def maj_temps(serpent:dict):
    """Décrémente les temps restant pour les bonus de ce serpent
    Attention les temps ne peuvent pas être négatif

    Args:
        serpent (dict): le serpent considéré
    """    
    if get_temps_protection(serpent) > 0:
        serpent['tps_p_serp'] -= 1
    if get_temps_mange_mur(serpent) > 0:
        serpent['tps_m_serp'] -= 1
    if get_temps_surpuissance(serpent) > 0:
        serpent['tps_s_serp'] -= 1

def serpent_2_str(serpent:dict, sep=";")->str:
    """Sérialise un serpent sous la forme d'une chaine de caractères
    contenant 2 lignes.
    nom_j;num_j;nb_point;tps_surpuissance;tps_mange_mur;tps_protection
    lig1;col1;lig2;col2;...
    La première ligne donne les informations autres que la liste des positions du serpent
    la deuxième ligne donné la liste des position du serpent en commençant par la tête
    Args:
        serpent (dict): le serpent considéré
        sep (str, optional): le caractère séparant les informations du serpent. Defaults to ";".

    Returns:
        str: la chaine de caractères contenant les toutes informations du serpent
    """    
    premier_phrase = get_nom(serpent) + sep + str(get_num_joueur(serpent)) + sep + str(get_points(serpent)) + \
          sep + str(get_temps_surpuissance(serpent)) + sep +  str(get_temps_mange_mur(serpent)) + sep + str(get_temps_protection(serpent)) + sep + get_derniere_direction(serpent)
    deuxieme_phrase = "" 
    for pos in get_liste_pos(serpent):
        deuxieme_phrase += str(pos[0]) + sep + str(pos[1]) + sep
    deuxieme_phrase = deuxieme_phrase[:-1]
    return premier_phrase + "\n" + deuxieme_phrase + "\n"

def serpent_from_str(la_chaine, sep=";")->dict:
    """Reconstruit un serpent à partir d'une chaine de caractères
       telle que celle produite par la fonction précédente ("serp1";"1";"10";"4";"3";"2";"S\n1;1;1;2;1;3\n")
    Args:
        la_chaine (_type_): la chaine de caractères contenant les informations du serpent
        sep (str, optional): le caractère servant à séparer les informations du serpent. Defaults to ";".

    Returns:
        dict: Le serpent représenté dans la chaine de caractères
        
    """
    lignes = la_chaine.split("\n")
    ligne1 = lignes[0].split(sep)
    ligne2 = lignes[1].split(sep)
    
    lst_pos = []
    for i in range(0, len(ligne2), 2):
        lst_pos.append((int(ligne2[i]), int(ligne2[i + 1])))
    
    return {
        'nom_serp': ligne1[0], 
        'num_serp': int(ligne1[1]), 
        'points_serp': int(ligne1[2]), 
        'positions_serp': lst_pos, 
        'tps_s_serp': int(ligne1[3]), 
        'tps_p_serp': int(ligne1[4]), 
        'tps_m_serp': int(ligne1[5]), 
        'direction_serp': ligne1[6]
    }




def copy_serpent(serpent:dict)->dict:
    """fait une copie du serpent passer en paramètres
    Attention à bien faire une copie de la liste des positions
    

    Args:
        serpent (dict): le serpent à recopier

    Returns:
        dict: la copie du serpent passé en paramètres

    """
    serpent_copie = {"nom_serp":serpent["nom_serp"],'num_serp':serpent['num_serp'],'points_serp':serpent['points_serp'],'positions_serp':None,'tps_s_serp' : serpent['tps_s_serp'],
                     'tps_p_serp' : serpent['tps_p_serp'],'tps_m_serp' : serpent['tps_m_serp'],'direction_serp' : serpent['direction_serp']}
    
    if serpent['positions_serp'] is not None :
        liste_pos = []

        for pos in serpent['positions_serp']:
            liste_pos.append(pos)
        serpent_copie['positions_serp'] = liste_pos
    return serpent_copie

def test_serpent():
    """teste les fonctions du module serpent
    """    
    assert Serpent("Joueur 1",1,0,[],0,0,0,'N') == {'nom_serp': 'Joueur 1', 'num_serp': 1, 'points_serp': 0, 'positions_serp': [], 'tps_s_serp': 0, 'tps_p_serp': 0, 'tps_m_serp': 0, 'direction_serp': 'N'}
    serpent = Serpent("Joueur 1",1,0,[],0,0,0,'N')
    assert get_nom(serpent) == "Joueur 1"
    assert get_num_joueur(serpent) == 1
    assert get_points(serpent) == 0
    assert get_liste_pos(serpent) == []
    assert get_derniere_direction(serpent) == 'N'
    assert get_bonus(serpent) == []
    ajouter_points(serpent,10)
    assert get_points(serpent) == 10
    set_liste_pos(serpent,[(1,1),(1,2),(1,3)])
    assert get_liste_pos(serpent) == [(1,1),(1,2),(1,3)]
    set_derniere_direction(serpent,'S')
    assert get_derniere_direction(serpent) == 'S'
    assert to_str(serpent) == "Joueur 1-> 10 s:0 m:0 p:0"
    assert get_temps_protection(serpent) == 0
    assert get_temps_mange_mur(serpent) == 0
    assert get_temps_surpuissance(serpent) == 0
    ajouter_temps_protection(serpent,3)
    assert get_temps_protection(serpent) == 3
    ajouter_temps_mange_mur(serpent,4)
    assert get_temps_mange_mur(serpent) == 4
    ajouter_temps_surpuissance(serpent,5)
    assert get_temps_surpuissance(serpent) == 5
    maj_temps(serpent)
    assert get_temps_protection(serpent) == 2
    assert get_temps_mange_mur(serpent) == 3
    assert get_temps_surpuissance(serpent) == 4
    assert serpent_2_str(serpent) == "Joueur 1;1;10;4;3;2;S\n1;1;1;2;1;3\n"
    serpent2 = serpent_from_str("Joueur 1;1;10;4;3;2;S\n1;1;1;2;1;3\n")
    serpent2 = copy_serpent(serpent)
    assert serpent2 == serpent
#test_serpent()