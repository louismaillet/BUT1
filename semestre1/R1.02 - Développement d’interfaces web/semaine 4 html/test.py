# On modifie la fonction pour gérer les cas où le joueur entre une colonne ou une ligne invalide (en dehors de 0, 1, ou 2).
# Si c'est le cas, on lui demandera de rejouer.

# Réinitialiser le plateau pour le nouvel exemple
plateau = [[" " for _ in range(3)] for _ in range(3)]

# Coups simulés incluant un coup invalide (colonne 4)
coups_predefinis = [(0, 0), (1, 4), (0, 1), (2, 2), (0, 2)]  # Coup invalide à (1, 4)

def jouer_morpion_simule_verification(coups):
    joueur_actuel = "X"
    gagnant = None
    tour = 0

    while not gagnant and not verifier_nul(plateau):
        afficher_plateau(plateau)
        ligne, colonne = coups[tour]  # Jouer les coups prédéfinis
        print(f"Joueur {joueur_actuel} tente de jouer en ({ligne}, {colonne})")
        
        # Vérifier si le coup est dans les limites du plateau
        if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
            print(f"Coup invalide ! ({ligne}, {colonne}) est hors des limites. Veuillez réessayer.")
            tour += 1
            continue

        # Jouer le coup s'il est valide
        if jouer(plateau, joueur_actuel, ligne, colonne):
            gagnant = verifier_gagnant(plateau)
            if gagnant:
                print(f"Félicitations ! Le joueur {gagnant} a gagné !")
            elif verifier_nul(plateau):
                print("Match nul !")
            # Changer de joueur
            joueur_actuel = "O" if joueur_actuel == "X" else "X"
        else:
            print("Coup déjà joué, veuillez réessayer.")
        
        tour += 1

    afficher_plateau(plateau)

# Lancer le jeu avec un coup invalide
jouer_morpion_simule_verification(coups_predefinis)
