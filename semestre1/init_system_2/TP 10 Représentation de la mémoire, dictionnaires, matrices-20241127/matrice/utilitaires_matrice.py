""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice2 as matrice
mat = matrice.affiche([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def get_diagonale_principal(matrice):
    m = []
    for i in range(matrice.get_nb_lignes(matrice)):
        m.append(matrice.get_val(matrice, i, i))
    return m

print(get_diagonale_principal(mat)) # [1, 5, 9]