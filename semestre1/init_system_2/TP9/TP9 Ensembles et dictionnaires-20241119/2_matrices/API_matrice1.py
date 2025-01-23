""" Matrices : API n 1 """


def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    return nb_lignes,nb_colonnes,[valeur_par_defaut for x in range(nb_lignes*nb_colonnes)]



def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    la_matrice[2][colonne + la_matrice[1]*ligne] = nouvelle_valeur
    return la_matrice


    


def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return la_matrice[0]


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return la_matrice[1]


matrice = (2,4,[1,2,3,4,
                5,6,7,8])
def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return la_matrice[2][colonne + la_matrice[1]*ligne]
    

#fonction pour l'affichage
def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    f = open(nom_fichier, 'r')
    matrice = []
    i = 0
    for ligne in f:
        matrice.append(ligne.split(','))
        matrice[i] = matrice[i][:-1]
        i += 1
    matrice = sum(matrice, [])
    f.close()
    return matrice
        



def sauve_matrice(la_matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    f = open(nom_fichier, 'w')
    for i in range(la_matrice[0]):
        for j in range(la_matrice[1]):
            f.write(str(get_val(la_matrice, i, j)) + ',')
        f.write('\n')
    f.close()
    return None
sauve_matrice(matrice, 'matrice.csv')


def get_ligne2(matrice, ligne):
    """ to do"""
    liste = []
    for i in range(matrice[1]):
        liste.append(get_val(matrice, ligne, i))
    return liste

def get_colonne2(matrice, colonne):
    """ to do"""
    liste = []
    for i in range(matrice[0]):
        liste.append(get_val(matrice, i, colonne))
    return liste

def get_diagonale_principale(matrice):
    """ to do"""
    liste = []
    for i in range(matrice[0]):
        liste.append(get_val(matrice, i, i))
    return liste

def get_diagonale_secondaire(matrice):
    liste = []
    for i in range(matrice[0]):
        liste.append(get_val(matrice, matrice[0]-1-i, i ))
    return liste

def transpose(matrice):
    """ renvoie la transposée de la matrice passée en argument
    """
    liste = []
    for i in range(0, matrice[1], -1):
        liste.append(get_colonne2(matrice, i))
    return matrice[1], matrice[0], liste

transpose(matrice)
listee = (2,4,[1,2,3,4,
               5,6,7,8])

liste2 = (5,5,[1,2,3,4,5,
               6,7,8,9,10,
               11,12,13,14,15,
               16,17,18,19,20,
               21,22,23,24,25])

    
print(transpose(listee))
print(transpose(liste2))