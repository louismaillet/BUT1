""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice2 as matrice_api
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrice_api.affiche(mat))

def get_diagonale_principal(matrice):
    m = []
    for i in range(matrice_api.get_nb_lignes(matrice)):
        m.append(matrice_api.get_val(matrice, i, i))
    return m

print(get_diagonale_principal(mat))

def get_diagonale_secondaire(matrice):
    m = []
    for i in range(matrice_api.get_nb_lignes(matrice)):
        m.append(matrice_api.get_val(matrice, i, matrice_api.get_nb_colonnes(matrice) - 1 - i))
    return m
print(get_diagonale_secondaire(mat))


def transpose(matrice):
    m = []
    for i in range(matrice_api.get_nb_colonnes(matrice)):
        ligne = []
        for j in range(matrice_api.get_nb_lignes(matrice)):
            ligne.append(matrice_api.get_val(matrice, j, i))
        m.append(ligne)
    return m

tp_mat = transpose(mat)
print(matrice_api.affiche(tp_mat))

def is_triangulaire_inf(matrice):
    for _ in range(matrice_api.get_nb_lignes(matrice)):
        if [0] * matrice_api.get_nb_colonnes(matrice) != get_diagonale_principal(matrice):
            return False
        else :
            if matrice_api.get_nb_lignes(matrice) >= 0 :
                del(matrice[0])
                for i in range(matrice_api.get_nb_lignes(matrice)): 
                    del(matrice[i][-i-1])
    return True


        

m = [[0, 6,5], [0, 0, 5], [0, 0, 0]]

print(is_triangulaire_inf(m))
def test_is_triangulaire_inf():
    assert is_triangulaire_inf([[0, 0, 0], [1, 0, 0], [1, 1, 0]]) == False
    assert is_triangulaire_inf([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True
    assert is_triangulaire_inf([[0, 6,5], [0, 0, 5], [0, 0, 0]]) == True   
    


def is_triangulaire_sup(matrice): 
    for _ in range(matrice_api.get_nb_lignes(matrice)):
        if [0] * matrice_api.get_nb_colonnes(matrice) != get_diagonale_secondaire(matrice):
            return False
        else :
            if matrice_api.get_nb_lignes(matrice) >= 0 :
                del(matrice[0])
                for i in range(matrice_api.get_nb_lignes(matrice)): 
                    del(matrice[i][i])
    return True

def test_is_triangulaire_sup():
    assert is_triangulaire_sup([[0, 0, 0], [1, 0, 0], [1, 1, 0]]) == False
    assert is_triangulaire_sup([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True
    assert is_triangulaire_sup([[0, 6,5], [0, 0, 5], [0, 0, 0]]) == False



def somme(matrice1, matrice2):
    m = []
    for i in range(matrice_api.get_nb_lignes(matrice1)):
        ligne = []
        for j in range(matrice_api.get_nb_colonnes(matrice1)):
            ligne.append(matrice_api.get_val(matrice1, i, j) + matrice_api.get_val(matrice2, i, j))
        m.append(ligne)
    return m

def produit(matrice1, matrice2):
    if matrice_api.get_nb_colonnes(matrice1) != matrice_api.get_nb_lignes(matrice2) :
        return 'error'
    m = []
    pass