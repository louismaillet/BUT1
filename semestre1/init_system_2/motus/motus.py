from random import randint

def mot():
    with open("mot.txt", "r") as f:
        mots = f.readlines()
    mot_aleatoire = mots[randint(0, len(mots) - 1)].strip()
    return mot_aleatoire

def afficher_mot(mot, lettres_trouvees):
    for lettre in mot:
        if lettre in lettres_trouvees:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print()

def motus():
    mot_ale = mot()
    mot_ale = mot_ale.lower()
    lettres_trouvees = set()
    essais = 0
    max_essais = 6
    
    while essais < max_essais:
        afficher_mot(mot_ale, lettres_trouvees)
        mot_choisis = input('Choisis un mot : ').lower()
        if len(mot_choisis) != len(mot_ale):
            print("Le mot doit avoir", len(mot_ale), "lettres")
        else:
            essais += 1
            lettres_trouvees.update([mot_choisis[i] for i in range(len(mot_choisis)) if mot_choisis[i] == mot_ale[i]])
            
            for lettre in mot_choisis:
                if lettre in mot_ale and lettre not in lettres_trouvees:
                    print(f"La lettre {lettre} est dans le mot mais pas à la bonne place.")
            
            if mot_choisis == mot_ale:
                print("Bravo ! Vous avez trouvé le mot en", essais, "essais.")
                break
    else:
        print("Désolé, vous avez épuisé vos essais. Le mot était", mot_ale)

motus()

             