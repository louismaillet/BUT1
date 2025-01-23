matrice1 = {
    (0, 0): 'A', (0, 1): 'B', (0, 2): 'E',
    (1, 0): 'C', (1, 1): 'D', (1, 2): 'F'
}
def compte_lignes(matrice):

    
    return list(matrice.keys())[len(matrice)-1][1] +1
print(compte_lignes(matrice1))
    

