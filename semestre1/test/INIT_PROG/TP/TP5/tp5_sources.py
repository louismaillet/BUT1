def mystere(liste, valeur):
    """revoie l'indice de la quatrieme occurance de valeur dans la listes

    Args:
        liste (list): liste de nombre enthier
        valeur (int): un nombre enthier

    Returns:
        int: l'indice de la quatrieme valeur
    """
    xxx = 0
    yyy = 0
    # a chaque tour de boucle, yyy vaut le nombre de fois qya ete apercu valeur dans la liste deja parcourue
    # a chaque tour de boucle, xxx contient le nombre d'element deja parcourue dans la liste 
    for i in range(len(liste)):
        if liste[i] == valeur:
            yyy += 1
            if yyy > 3:
                return xxx
        xxx += 1
    return None
#2.2 xxx est retourner quand 
#exercice 2
def occurence_premier_chiffre(phrase): 
    """retourne la premiere occurence du premier chiffre dans la phrase

    Args:
        phrase (str) : une phrase

    Returns:
        int: la premiere occurrence du premier chiffre dans la liste
    """
    # pour chaque element de la liste 
    for i in range(len(phrase)):
        if phrase[i] in "1234567890" :
            return i
    return None


def test_occurence_premier_chiffre():
    assert occurence_premier_chiffre("abc123def") == 3 # je veifie si "abc123def" me renvoie bien 3
    assert occurence_premier_chiffre("123abc") == 0 # je veifie si "123abc" me renvoie bien 0
    assert occurence_premier_chiffre("1234567890") == 0 # je verifie si "1234567890" renvoie 0
    assert occurence_premier_chiffre("azerty") == None # je verifie si "azerty" == None

def population_ville(ville, liste_villes, population):
    """retourne la population de la ville la plus grande

    Args:
        ville (str) : une ville
        liste_villes (list) : une liste de villes
        population (list) : une liste de population

    Returns:
        int: la population de la ville la plus grande
    """
    # pour chaque element de la liste 
    for i in range(len(liste_villes)):
        if liste_villes[i] == ville:
            return population[i]
    return None

def test_population_ville():
    assert population_ville("Blois", liste_villes, population) == 45871 # je veifie si "Blois" me renvoie bien 45871
    assert population_ville("Orléanss", liste_villes, population) == None    # je veifie si "Orléanss" me renvoie bien None
    assert population_ville("Vierzon", liste_villes, population) == 25725 # je verifie si "Vierzon" me renvoie bien 25725
    assert population_ville("Lille", liste_villes, population) == None # je verifie si "Lille" == None
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

def est_triée(lst):
    """retourne True si la liste est triée, False sinon

    Args:
        lst (list): une liste

    Returns:
        bool: True si la liste est triée, False sinon
    """
    # pour chaque element de la liste 
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def test_est_triée():
    assert est_triée([0,1,2,4,5]) == True
    assert est_triée([0]) == True
    assert est_triée([]) == True
    assert est_triée([4,3,4,5,6]) == False

def somme_depasse_seuil(liste, seuil):
    """retourne si la somme des valeur depasse le seuil"""
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
        if somme > seuil:
            return True
    return False

def test_somme_depasse_seuil():
    assert somme_depasse_seuil([], 100) == False
    assert somme_depasse_seuil([50], 0) == True
    assert somme_depasse_seuil([10,20,30,40,50], 200) == False
    assert somme_depasse_seuil([10,20,30,40,50], 500) == False


#Écrire une fonction qui vérifie qu’une chaîne de caractères correspond à une adresse e-mail potentielle. C’est-à-dire qu’elle ne contient pas d’espace, quelle contient un et un seul @ suivi d’au moins un point. De plus la chaîne ne doit pas commencer par un @ ni se terminer par un point.

def email_detecte(email):
    """retourne True si la chaîne de caractères correspond à une adresse e-mail potentielle, False sinon

    Args:
        email (str): une chaîne de caractères

    Returns:
        bool: True si la chaîne est une adresse e-mail, False sinon
    """
    cpt1 = 0
    
    if email == "" or email[0] == "@" or email[len(email)-1] == "." :
            return False
    # a chaque tour de boucle cp1 contien le nombre d'@ deja passée
    for i in range(len(email)):
        if email[i] == " ":
            return False
        if email[i] == "@":
            cpt1 += 1 
            if cpt1 > 1:
                return False    
        if email[i] == "." :
            if email[i-1] == "@" :
                return False
    return True   
def test_email_detecte():
    assert email_detecte("test@gmail.com") == True
    assert email_detecte("test@.com") == False
    assert email_detecte("") == False


# ---------------------------------------


# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
def calcule_score(nom, liste_scores, liste_joueurs):
    """Ajoute le score d'un joueur à la liste des scores et le nom à la liste des joueurs
    Args:
        nom (str): le nom du joueur
        score (int): une liste des scores
        joueurs (list): une liste des joueurs
    Returns:
        int : le meilleur score du joueur ou none si pas de score
        """
    score_final = None
    # a chaque tour de boucle score final contient le meilleurs score passée du joueur chercher
    for i in range(len(scores)):
        if liste_joueurs[i] == nom:
            if score_final is None or score_final < liste_scores[i]:
                score_final = liste_scores[i]
    return score_final

calcule_score("Joker", [], [])
def test_calcule_score():

    assert calcule_score("Batman", [352100, 325410, 312785, 220199, 127853], ["Batman", "Robin", "Batman", "Joker", "Batman"]) == 352100
    assert calcule_score("Robin", [352100, 325410, 312785, 220199, 127853], ["Batman", "Robin", "Batman", "Joker", "Batman"]) == 325410
    assert calcule_score("Joker", [], []) == None
    assert calcule_score("", [], []) == None
    assert calcule_score("coucou", [352100, 325410, 312785, 220199, 127853],["Batman", "Robin", "Batman", "Joker", "Batman"]) == None

def 