# coding: utf-8
"""
            SAE1.02 SERPIUT'O
         BUT1 Informatique 2024-2025

    Module IA.py
    Ce module implémente toutes les fonctions ainsi que l'IA de votre serpent
"""
import partie
import argparse
import client
import random
import arene
import serpent
import matrice
import case
direction_prec='X' # variable indiquant la décision précédente prise par le joueur. A mettre à jour soi-même

####################################################################
### A partir d'ici, implémenter toutes les fonctions qui vous seront 
### utiles pour prendre vos décisions
### Toutes vos fonctions devront être documentées
####################################################################

def directions_possibles(l_arene:dict,num_joueur:int)->str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur

    Returns:
        str: une chaine composée de NOSE qui indique les directions
            pouvant être prise par le joueur. Attention il est possible
            qu'aucune direction ne soit possible donc la fonction peut retourner la chaine vide
    """
    res=''
    mat=l_arene["matrice"]
    nb_lig=matrice.get_nb_lignes(mat)
    nb_col=matrice.get_nb_colonnes(mat)
    lig_dep,col_dep=serpent.get_liste_pos(l_arene["serpents"][num_joueur-1])[0] # position de la tête du serpent
    for dir in 'NOSE':
        delta_lig,delta_col=arene.DIRECTIONS[dir] # recupere les deltat (-1,0) ....
        lig_arr=lig_dep+delta_lig
        col_arr=col_dep+delta_col
        if lig_arr<0 or lig_arr>=nb_lig or col_arr<0 or col_arr>=nb_col: # si on sort de l'arène
            continue
        if case.est_mur(matrice.get_val(mat,lig_arr,col_arr)): # si c'est un mur
            continue
        if case.get_proprietaire(matrice.get_val(mat,lig_arr,col_arr))==num_joueur: # si c'est une boite du joueur
            continue
        res+=dir
    return res 

def trouver_cases_distance(coordonné, dist_max, l_arene):
    """
    Retourne la liste des cases accessibles à partir de la coordonnée donnée
    Args:
        coordonné (tuple): les coordonnées du point de départ
        dist_max (int): la distance maximale à laquelle
        l_arene (dict): l'arène considérée
    Returns:
        list: la liste des cases accessibles
    

    """
    cases_accessibles = []
    
    longueur = l_arene["matrice"]["nb_lig"]
    hauteur = l_arene["matrice"]["nb_col"]
    x, y = coordonné
    for i in range(longueur):
        for j in range(hauteur):
            if abs(x - i) + abs(y - j) <= dist_max:
                cases_accessibles.append((i, j))

    
    return cases_accessibles

def objets_voisinage(l_arene:dict, num_joueur:int, dist_max:int)->dict:
    """Retourne un dictionnaire indiquant pour chaque direction possible, 
        les objets ou boites pouvant être mangés par le serpent du joueur et
        se trouvant dans le voisinage de la tête du serpent 

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur considéré
        dist_max (int): le nombre de cases maximum qu'on s'autorise à partir du point de départ

    Returns:
       dict: un dictionnaire dont les clés sont des directions et les valeurs une liste de triplets
            (distance, val_objet, prop) où distance indique le nombre de cases jusqu'à l'objet et id_objet
            val_obj indique la valeur de l'objet ou de la boite et prop indique le propriétaire de la boite
    """
    

    pos_objets = dict()  # Dictionnaire 
    case_depart = serpent.get_liste_pos(l_arene["serpents"][num_joueur-1])[0]  # Position de départ du serpent (la tete)
    liste_cases = trouver_cases_distance(case_depart, dist_max, l_arene)  # Cases accessibles à une distance max 

    for (ligne, col) in liste_cases:  # Parcourir chaque case accessible
        if arene.get_val_boite(l_arene, ligne, col) != 0 or arene.est_bonus(l_arene, ligne, col):  # Si la case contient une boîte ou un bonus
            file_attente = [(case_depart, '')]  # Initialiser la file d'attente
            visitees = set()  # Ensemble pour suivre les positions visitées

            while file_attente:  # Tant que la file d'attente n'est pas vide
                (pos_actuelle, chemin) = file_attente.pop(0)  # Extraire la première position de la file
                if pos_actuelle in visitees:  # verifie si elle est pas deja visitée
                    continue
                visitees.add(pos_actuelle)  # ajoute au positions visitées

                if pos_actuelle == (ligne, col):  # Si position est recherchée
                    if len(chemin) <= dist_max:  # Si la distance est inférieure ou égale à la distance max
                        pos_objets[chemin] = (len(chemin), arene.get_val_boite(l_arene, ligne, col), arene.get_proprietaire(l_arene, ligne, col))  # Ajouter l'objet trouvé
                        break  # Sortir de la boucle car l'objet est trouvé et donc inutile de continuer
                    
                for direction in 'NOSE':  # Parcourir les directions possibles
                    delta_lig, delta_col = arene.DIRECTIONS[direction] # recupere les deltat (-1,0) ....
                    prochaine_pos = (pos_actuelle[0] + delta_lig, pos_actuelle[1] + delta_col)  # Calculer la prochaine position pour savoir dans quelle direction aller

                    if prochaine_pos in visitees:  # Si déjà visitée, passer
                        continue 
                    if prochaine_pos[0] < 0 or prochaine_pos[0] >= l_arene["matrice"]["nb_lig"] or prochaine_pos[1] < 0 or prochaine_pos[1] >= l_arene["matrice"]["nb_col"]:  # Si hors limites
                        continue
                    if case.est_mur(matrice.get_val(l_arene["matrice"], prochaine_pos[0], prochaine_pos[1])):  #si c'est un mur
                        continue
                    
                    file_attente.append((prochaine_pos, chemin + direction))  

    return pos_objets 

def type_et_longueur(item):
    """
    Fonction pour trier les objets en fonction de leur type et de la longueur de la direction.
    Args:
        item: Tuple contenant les informations de l'objet.
    Returns:
        Tuple: Tuple contenant la valeur de l'objet et la longueur de la direction.
    """
    direction, (distance, val_objet, prop) = item
    return (val_objet, len(direction))

def trier_objet(dico_objet: dict) -> list:
    """
    Trie les objets en fonction de leur type (valeur) et de la longueur de la direction.

    Args:
        dico_objet (dict): Dictionnaire des objets avec les directions comme clés.

    Returns:
        list: Liste triée des objets.
    """
    return sorted(dico_objet.items(), key=type_et_longueur)

def plus_proche_boite_bonus(l_arene:dict, num_joueur:int, dist_max:int):
    """renvoie la liste de chaque bonus le plus proche de nous (une seule boite 1, une seule boite 2, un seul bonus plus, un seul bonus multiplier, 
    un seul bonus surpuissance, un seul bonus mange-mur, un seul bonus protection ) dans le cas où il y en a un autour de nous 

    Args:
        l_arene (dict): l'arene considérée
        num_joueur (int): numéro du joueur
        dist_max (int): distance max à laquelle on cherche des objets

    Returns:
        list : liste des objets 
    """
    liste_unique = []
    dico_toute_pose = objets_voisinage(l_arene, num_joueur, dist_max)
    liste_triée = trier_objet(dico_toute_pose)
    if len(dico_toute_pose) == 0:
        return liste_unique
    i = 0
    for i in range(-5,3):
        for j in range(len(dico_toute_pose)):
            if liste_triée[j][1][1]==i:
                liste_unique.append(liste_triée[j])
                break
    return liste_unique

def plus_proche_boite_serpent(l_arene:dict, num_joueur:int, dist_max:int): 
    """renvoie la liste de chaque boite de serpent (hormis notre joueur) le plus proche de nous dans le cas où il y en a un autour de nous 

    Args:
        l_arene (dict): l'arene considérée
        num_joueur (int): numéro du joueur
        dist_max (int): distance max à laquelle on cherche des objets

    Returns:
        list : liste des serpents 
    """
    liste_unique = []
    liste_carree = [1,2,4,8,16,32,64,128,256]
    dico_toute_pose = objets_voisinage(l_arene, num_joueur, dist_max)
    liste_triée = trier_objet(dico_toute_pose)
    if len(dico_toute_pose) == 0:
        return liste_unique
    i = 0
    for i in liste_carree:
        for j in range(len(dico_toute_pose)):
            if liste_triée[j][1][1]==i and liste_triée[j][1][2]!= num_joueur and liste_triée[j][1][2] != 0 :
                liste_unique.append(liste_triée[j])
                break
    return liste_unique    

def plus_proche_boite_spe(l_arene:dict, num_joueur:int, dist_max:int, spe:int): 
    """renvoie la liste de chaque bonus de numero spe le plus proche de nous dans le cas où il y en a un autour de nous 

    Args:
        l_arene (dict): l'arene considérée
        num_joueur (int): numéro du joueur
        dist_max (int): distance max à laquelle on cherche des objets

    Returns:
        list : liste des objets 
    """
    liste_unique = []
    dico_toute_pose = objets_voisinage(l_arene, num_joueur, dist_max)
    liste_triée = trier_objet(dico_toute_pose)
    if len(dico_toute_pose) == 0:
        return liste_unique
    for j in range(len(dico_toute_pose)):
        if liste_triée[j][1][1]==spe and liste_triée[j][1][2]==0:
            liste_unique.append(liste_triée[j])
            break
    for position in liste_unique:
        if position== "":
            liste_unique.remove(position)
    return liste_unique

def premier_50_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2,directions_possibles):
    """renvoie une position vers laquelle le serpent doit aller
    si la tete du serpent vaut 2 ou plus, il va aller chercher des
    boites de 2, sinon il prend une direction aleatoire parmi celles possibles, si aucune n'est possible il prend une direction aléatoire.
    si la tete vaut moins que 2, il va aller chercher des
    boites de 1, sinon il prend une direction aleatoire parmi celles possibles, si aucune n'est possible il prend une direction aléatoire.
    
    args :

    num_joueur (int): numero du joueur
    arene_partie (dict): l'arene de la partie
    liste_boite_manger_1 (list) : liste des boites de valeurs 1 autour du joueur num_joueur
    liste_boite_manger_2 (list) : liste des boites de valeurs 2 autour du joueur num_joueur
    directions_possibles (str) : chaine de caractères avec les lettres des positions possibles

    return :
     str : une lettre symbolisant la direction que doit prendre le serpent 
    """
    if arene.get_val_boite(arene_partie, arene.get_serpent(arene_partie, num_joueur)[0][0], arene.get_serpent(arene_partie, num_joueur)[0][1]) >= 2: # Si la valeur de la boîte est supérieure ou égale à 2
        if liste_boite_manger_2 and liste_boite_manger_2[0][0][0] in arene.DIRECTIONS: # Si une boîte de valeur 2 est trouvée
            
            direction = liste_boite_manger_2[0][0][0]
            if direction in directions_possibles: #Si la direction est possible
                return direction
            else :
                return random.choice("NSEO")
    
    if liste_boite_manger_1 and liste_boite_manger_1[0][0][0] in arene.DIRECTIONS:
        direction = liste_boite_manger_1[0][0][0]
        
        if direction in directions_possibles:
            return direction
        return random.choice("NSEO")
    elif directions_possibles:
        return random.choice(directions_possibles)
    else:
        return 'N'
    
def deuxieme_75_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2, liste_boite_manger_plus, liste_boite_manger_mult, directions_possibles):
   """renvoie une position vers laquelle le serpent doit aller
    si la tete du serpent vaut 4 ou plus, 
    il va aller chercher des bonus de multiplications si il y en a autour, sinon il prend une direction aleatoire parmi celles possibles, si aucune n'est possible il utilise la fonction premier_50_tours.
    sinon il va aller chercher des bonus plus si il y en a autour, sinon il prend une direction aleatoire parmi celles possibles, si aucune n'est possible il utilise la fonction premier_50_tours.
    si la tete vaut moins que 4, il va utiliser le programme premier_50_tours
    
    args :

    num_joueur (int): numero du joueur
    arene_partie (dict): l'arene de la partie
    liste_boite_manger_1 (list) : liste des boites de valeurs 1 autour du joueur num_joueur
    liste_boite_manger_2 (list) : liste des boites de valeurs 2 autour du joueur num_joueur
    list_boite_manger_plus (list) :liste des bonus de valeurs -1 autour du joueur num_joueur
    list_boite_manger_mult (list) :liste des bonus de valeurs -2 autour du joueur num_joueur
    directions_possibles (str) : chaine de caractères avec les lettres des positions possibles

    return :
     str : une lettre symbolisant la direction que doit prendre le serpent 
    """
   if arene.get_val_boite(arene_partie, arene.get_serpent(arene_partie, num_joueur)[0][0], arene.get_serpent(arene_partie, num_joueur)[0][1]) >= 4:
        if liste_boite_manger_mult and liste_boite_manger_mult[0][0][0] in arene.DIRECTIONS:
            direction = liste_boite_manger_mult[0][0][0]
            if direction in directions_possibles:
                return direction
            else :
                return premier_50_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2, directions_possibles)
            
        elif liste_boite_manger_plus and liste_boite_manger_plus[0][0][0] in arene.DIRECTIONS:
            direction = liste_boite_manger_plus[0][0][0]
            if direction in directions_possibles:
                return direction
            else :
                return premier_50_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2, directions_possibles)
        else:
            return premier_50_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2, directions_possibles)
   else:
        return premier_50_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2, directions_possibles)

def troisieme_50_tours(num_joueur,arene_partie, liste_boite_manger_1 , liste_boite_manger_2,liste_boite_manger_plus,liste_boite_manger_mult,liste_boite_manger_serp,directions_possibles):
    """renvoie une position vers laquelle le serpent doit aller
    si la tete du serpent vaut 4 ou plus, 
    il va aller chercher des serpents autour de lui si il y en a autour, sinon il va utiliser le programme deuxieme_50_tours
    
    args :

    num_joueur (int): numero du joueur
    arene_partie (dict): l'arene de la partie
    liste_boite_manger_1 (list) : liste des boites de valeurs 1 autour du joueur num_joueur
    liste_boite_manger_2 (list) : liste des boites de valeurs 2 autour du joueur num_joueur
    list_boite_manger_plus (list) :liste des bonus de valeurs -1 autour du joueur num_joueur
    list_boite_manger_mult (list) :liste des bonus de valeurs -2 autour du joueur num_joueur
    list_boite_manger_serp (list) :liste des serpents autour du joueur num_joueur
    directions_possibles (str) : chaine de caractères avec les lettres des positions possibles

    return :
     str : une lettre symbolisant la direction que doit prendre le serpent 
    """
    if arene.get_val_boite(arene_partie, arene.get_serpent(arene_partie, num_joueur)[0][0], arene.get_serpent(arene_partie, num_joueur)[0][1]) >= 4:
        if liste_boite_manger_serp :
            if liste_boite_manger_serp[0][0][0] in arene.DIRECTIONS:
                direction = liste_boite_manger_serp[0][0][0]
                if direction in directions_possibles:
                    return direction
                else :
                    return deuxieme_75_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2,liste_boite_manger_plus,liste_boite_manger_mult,directions_possibles)
            else :
                return deuxieme_75_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2,liste_boite_manger_plus,liste_boite_manger_mult,directions_possibles)
            
        else : 
            return deuxieme_75_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2,liste_boite_manger_plus,liste_boite_manger_mult,directions_possibles)
    return deuxieme_75_tours(num_joueur, arene_partie, liste_boite_manger_1, liste_boite_manger_2,liste_boite_manger_plus,liste_boite_manger_mult,directions_possibles)

def mon_IA(num_joueur:int, la_partie:dict)->str:
    """Fonction principale de l'IA qui renvoie la direction que doit prendre le serpent
    Args:
        num_joueur (int): le numéro du joueur
        la_partie (dict): la partie considérée
    Returns:
        str: la direction que doit prendre le serpent
    """
    directions_possibles = arene.directions_possibles(partie.get_arene(la_partie), num_joueur)
    temps_total_partie = partie.get_duree_totale(la_partie)
    temps_restant = partie.get_temps_restant(la_partie)
    arene_partie = partie.get_arene(la_partie)
    liste_boite_manger_1 = plus_proche_boite_spe(arene_partie, num_joueur, 10, 1)
    liste_boite_manger_2 = plus_proche_boite_spe(arene_partie, num_joueur, 10, 2)
    liste_boite_manger_plus = plus_proche_boite_spe(arene_partie, num_joueur, 10, -1)
    liste_boite_manger_mult = plus_proche_boite_spe(arene_partie, num_joueur, 10, -2)
    liste_boite_manger_serp = plus_proche_boite_serpent(arene_partie, num_joueur, 10)
    if temps_total_partie - temps_restant <= 50:
        return premier_50_tours(num_joueur,arene_partie, liste_boite_manger_1 , liste_boite_manger_2,directions_possibles)
    
    elif temps_total_partie - temps_restant <= 75:
        return deuxieme_75_tours(num_joueur,arene_partie, liste_boite_manger_1 , liste_boite_manger_2,liste_boite_manger_plus, liste_boite_manger_mult,directions_possibles)
    else : 
        return troisieme_50_tours(num_joueur,arene_partie, liste_boite_manger_1 , liste_boite_manger_2,liste_boite_manger_plus, liste_boite_manger_mult,liste_boite_manger_serp,directions_possibles)            

if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu,_=le_client.prochaine_commande()
        if ok:
            la_partie=partie.partie_from_str(le_jeu)
            actions_joueur=mon_IA(int(id_joueur),la_partie)
            if actions_joueur is None:
                actions_joueur = 'N'  # Valeur par défaut si aucune direction n'est trouvée
            le_client.envoyer_commande_client(actions_joueur)
    le_client.afficher_msg("terminé")


