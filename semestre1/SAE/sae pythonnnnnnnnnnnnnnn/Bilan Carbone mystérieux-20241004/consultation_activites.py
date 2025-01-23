

# Ici vos fonctions dédiées aux interactions
# ici votre programme principal
def programme_principal():
    fichier = input("quelle fichier voulez-vous ouvrir ?")
    while fichier != "votre fichier n'existe pas":
        fichier = input("quelle fichier voulez-vous ouvrir")
        print(compter_personnes_differentes(fichier))
    print(compter_personnes_differentes(fichier))

def compter_personnes_differentes(fichier_csv):
    try:
        personnes = []
        f = open(fichier_csv, 'r')
        f.readline()
        for ligne in f :
            personne = ligne.split(',')[0]
            if personne not in personnes:
                personnes.append(personne)  

        return len(personnes)
    except :
        return print("votre fichier n'existe pas")
    



programme_principal()