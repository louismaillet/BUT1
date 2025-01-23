def trouver_dans_la_liste(liste, element):
    i = 0
    est_trouve = False
    while i < len(liste) and not est_trouve:
        if liste[i] == element:
            est_trouve = True
        i += 1
    return est_trouve
def cumuler_jusqua_seuil(dico, seuil):
    total = 0
    i = 0 
    while i < len(dico) and total < seuil:
        total += dico[i]
        i += 1
    return total


