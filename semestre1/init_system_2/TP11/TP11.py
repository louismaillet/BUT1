#TP11

def somme(tuple):
    s = 0
    for prix in tuple.values():
        s += prix
    return s/len(tuple)

def final(dico):
    prix_a_payer = somme(dico)
    for personne,prix in dico.items():
        if prix-prix_a_payer > 0:
            print(personne,'doit recevoir',prix-prix_a_payer,'euros')
        else:
            print(personne,'doit payer',prix-prix_a_payer,'euros')
    


t = {'Pierre': 92, 'Paul': 100, 'Marie': 15, 'Anna': 0}
final(t)
print (somme(t))


#2
ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida',
 'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
 'Gaston':'Beatrice','Henri':'Firmin'}

def les_amoureux(dico):
    a = dict()
    for nom,amoureux in dico.items():
        if amoureux in dico.keys():
            if dico[amoureux] == nom and nom not in a.values():
                a[nom] = amoureux
                
    return a
print(les_amoureux(ATM))

def soupirant(dico,nom):
    a = dict()
    for nom1,amoureux in dico.items():
        if amoureux == nom:
            a[nom1] = amoureux
    return a

print (soupirant(ATM,'Beatrice'))

#3
matrice = [[1,2,3],[4,5,6],[7,8,9]]


def sous_matrice(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
   """renvoie une sous-matrice de la matrice


   Args:
       matrice (list): une liste de listes
       nb_lignes (int): nombre de lignes de la sous-matrice
       nb_colonnes (int): nombres de colonnes de la sous-matrice
       position_haut (int): position de la ligne de départ
       position_gauche (int): position de la colonne de départ


   Returns:
       list: une sous-matrice de la liste
   """   
   if nb_lignes+position_haut > len(matrice) or nb_colonnes+position_gauche > len(matrice[0]):
       return None
   liste = []
   for i in range(position_haut, nb_lignes+position_haut):
       liste.append([])
       for j in range(position_gauche, nb_colonnes+position_gauche):
           liste[i].append(matrice[i][j])
   return liste


def colle_sous_matrice(matrice, sous_matrice, ligne_haut, colonne_gauche):
   """place une sous-matrice dans la matrice à la position (ligne_haut, colonne_gauche)


   Args:
       matrice (list): une liste de listes
       sous_matrice (list): une liste de listes, plus petite ou égale à la matrice
       ligne_haut (int): position de la ligne de départ
       colonne_gauche (int): position de la colonne de départ


   Returns:
       _type_: _description_
   """   
   if ligne_haut + len(sous_matrice) > len(matrice) or colonne_gauche + len(sous_matrice[0]) > len(matrice[0]):
       return None
   indice1_sm = -1
   for i in range(ligne_haut, ligne_haut+len(sous_matrice)):
       indice1_sm += 1
       indice2_sm = 0
       for j in range(colonne_gauche, colonne_gauche+len(sous_matrice[0])):
           matrice[i][j] = sous_matrice[indice1_sm][indice2_sm]
           indice2_sm += 1
   return matrice
          
print(colle_sous_matrice([[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]], [[0, 0, 0], [1, 1, 1]], 1, 1))

print(sous_matrice(matrice,2,2,0,0))    


#Exercice 4
def suite_Syracuse(n):

    """ c'est la suite de syracuse implemente en python

    Returns:
        int: le resultat de la suite jusqu'a Un
    """    
    Un = 0
    for i in range(n):  
        if Un % 2 == 0:  
            Un = Un // 2  
        else:
            Un = 3 * Un + 1   
    return Un

