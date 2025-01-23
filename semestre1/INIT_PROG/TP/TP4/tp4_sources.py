def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    prec = ''  # caractère précédent dans la chaine

    for lettre in chaine:
        if lettre == prec:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
        prec = lettre
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max

def plus_long_plat(chaine):
    """calcule la plus long chaine de caractere

    Args:
        chaine (str): une chaine de caractere

    Returns:
        int: retourne le nombre de fois que un caractere a ete repeter de suite
    """
    lg_max =0
    lg_actu =1
    if len(chaine) == 0:
        return 0
    
    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i-1]:
            lg_actu += 1


        else:
            if lg_actu > lg_max:
                lg_max = lg_actu
            lg_actu = 1
    if lg_actu > lg_max:  # cas du dernier plateau
        lg_max = lg_actu
    
        
    return lg_max

def test_plateau():

    assert plus_long_plat("aaaaehgehekemvrvmrnrnfn")== 4 # test avec une chaine de 4 lettres identiques
    assert plus_long_plat("") == 0 # test avec une chaine vide
    assert plus_long_plat("azertyuiopqsdfghjklmwxcvbn") == 1 # test avec une chaine de 1 lettre
    assert plus_long_plat("abceeeabc")==3 # test avec une chaine de 3 lettres identiques
    assert plus_long_plat("aaeettddd") == 3# test avec une chaine de 3 lettres identiques
    assert plus_long_plat("aba") == 1 





def plus_peuplee(population, liste_villes):
    """retourne le nom de la ville la plus peuplée de la liste

    Args:
        liste_villes (list): une liste de noms de villes
        population (list): une liste de population des villes
    Returns:
        """
    max_population = population[0]
    max_ville = liste_villes[0]
    # a chaque iteration, max_population contient la plus grande population de la liste
    # a chaque iteration, max_ville contient le nom de la ville la plus grande population de la liste
    for i in range(1, len(population)):
        if population[i] > max_population:
            max_population = population[i]
            max_ville = liste_villes[i]
    return max_ville

liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux", "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]
def test_ville_plus_peupler():
    assert plus_peuplee(population, liste_villes) == "Tours" # test avec une liste de villes avec une population maximale


def chaine_en_nombre(chaine):
    """retourne le nombre de chiffres dans une chaine

    Args:
        chaine (str): une chaine de caractères
    Returns:
        int: le nombre de chiffres dans la chaine"""
    resultat = 0
    # a chaque iteration, resultat contient la somme des chiffres de la chaine
        
    for i in range(len(chaine)):
        if chaine[i] == "0":
            resultat = resultat * 10  + 0
        elif chaine[i] == "1":
            resultat = resultat * 10 + 1
        elif chaine[i] == "2":
            resultat = resultat * 10 + 2
        elif chaine[i] == "3":
            resultat = resultat * 10 + 3
        elif chaine[i] == "4":
            resultat = resultat * 10 + 4
        elif chaine[i] == "5":
            resultat = resultat * 10 + 5
        elif chaine[i] == "6":
            resultat = resultat * 10 + 6
        elif chaine[i] == "7":
            resultat = resultat * 10 + 7
        elif chaine[i] == "8":
            resultat = resultat * 10 + 8
        elif chaine[i] == "9":
            resultat = resultat * 10 + 9
        elif chaine[i] not in "-+1234567890" :
            return None
    if len(chaine) == 0:
        resultat =  None
    elif chaine[0] == "-" :
        resultat = -resultat
    
    return resultat

def test_chaine_en_nombre():
    assert chaine_en_nombre("1234") == 1234 # test avec une chaine de 4 chiffres
    assert chaine_en_nombre("2021") == 2021 # test avec une chaine de 4 chiffres
    assert chaine_en_nombre("") == None # test avec une chaine de 1 chiffre
    assert chaine_en_nombre("-1000") == -1000 # test avec une chaine de 4 chiffres
    assert chaine_en_nombre("ab5") == None # test avec une chaine de 1 chiffre
    assert chaine_en_nombre("-58914") == -58914 # test avec une chaine de 5 chiffre negatif



def meme_debut_de_mot(liste , lettre):
    """retourne une nouvelle liste avec les mots de la liste qui commencent par la lettre

    Args:
        liste (list): une liste de mots
        lettre (str): une lettre
    Returns:
        list: une nouvelle liste avec les mots qui commencent par la lettre
    """
    liste_fini = []
    # a chaque iteration, resultat contient la nouvelle liste avec les mots qui commencent par la lettre
    for i in range(len(liste)):
        if liste[i][0] == lettre:
            liste_fini.append(liste[i])
    return liste_fini

def test_meme_debut_de_mot():
    assert meme_debut_de_mot(["Abeille", "Amarante", "Amelie", "Anas", "Antonia"], "A") == ["Abeille", "Amarante", "Amelie", "Anas", "Antonia"] # test avec une liste de mots qui commencent par la lettre "A"
    assert meme_debut_de_mot(["Bonjour", "Hello", "Salut", "Coucou", "Au revoir","Bonjour"], "B") == ["Bonjour","Bonjour"] # test avec une liste de mots

    
def decoupage_en_mot(mot):
    """retourne une liste avec les mots de la chaine séparés par des espaces

    Args:
        mot (str): une chaine de caractères
    Returns:
    list: une nouvelle liste avec les mots qui sont séparés par des espaces
    """
    resultat = []
    mot_courant = ""
    # a chaque iteration, mot_courant contient le mot courant qui est en cours de construction
    for lettre in mot:
        if lettre.isalpha():
            mot_courant += lettre
        else:
            if mot_courant!= "":
                resultat.append(mot_courant)
                mot_courant = ""
    if mot_courant!= "":
        resultat.append(mot_courant)
    return resultat

def test_decoupage_en_mot():
    assert decoupage_en_mot("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!") == ["Cela", "fait", "déjà", "jours", "jours", "à", "l", "IUT", "O", "Cool"] # test avec un texte simple
    assert decoupage_en_mot("(3*2)+1") == [] # test avec une expression arithmétique
    assert decoupage_en_mot("Bonjour tout le monde!") == ["Bonjour", "tout", "le", "monde"] # test avec un texte avec des

def trouver_mots_commence_par_lettre(texte, lettre):
    """retourne une liste avec les mots de la chaine qui commencent par la lettre

    Args:
        texte (str): une chaine de caractères
        lettre (str): une lettre
    Returns:
        list: une nouvelle liste avec les mots qui commencent par la lettre
        """
    mots = decoupage_en_mot(texte)
    resultat = meme_debut_de_mot(mots, lettre)
    return resultat

def ajoute_true_false(nombre):
 lst = [True] * nombre 
 if lst[0] == True and lst[1] == True:
    lst[0] = False
    lst[1] = False
 return lst


def test_trouver_mots_commence_par_lettre():
    assert trouver_mots_commence_par_lettre("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!", "C") == ["Cela", "Cool"] # test avec un texte simple
    assert trouver_mots_commence_par_lettre("(3*2)+1", "3") == [] # test avec une expression arithmétique
    assert trouver_mots_commence_par_lettre("Bonjour tout le monde!", "B") == ["Bonjour"] # test avec un texte avec des espaces
    assert trouver_mots_commence_par_lettre("Here Here",'H') == ["Here", 'Here'] # test avec Here

def initialise_liste(N):
    """ 
    initialise une liste de boolean de taille N avec tous les éléments à True

    Args:
        N (int): la taille de la liste
    Returns:
        list: une liste de boolean de taille N avec tous les éléments à True    """
    lst = [True] * (N)

    if len(lst) > 0 :
        lst[0] = False  
    if len(lst) > 1 :
        lst[1] = False   
    return lst

def test_initialise_liste():
    assert initialise_liste(5) == [False, False, True, True, True] # test avec un nombre pair
    assert initialise_liste(3) == [False, False, True ] # test avec un nombre impair
    assert initialise_liste(0) == [] # test avec un nombre nul
    assert initialise_liste(-5) == [] # test avec un nombre négatif

def x_met_false(x, liste):
    """ 
    Met les multiples de x à False dans une liste de booléens.

    Args:
        x (int): Le nombre dont les multiples doivent être mis à False.
        liste (list): Une liste de booléens représentant si un nombre est potentiellement premier ou non.
    
    Returns:
        list: La même liste avec les multiples de x mis à False.
    """
    for i in range(2 * x, len(liste), x): 
        liste[i] = False
    
    return liste

def test_x_met_false():
    assert x_met_false(2, [False, False, True, True, True]) == [False, False, True, True, False] # test avec un nombre pair
    assert x_met_false(3, [False, False, True, True, True, True,True]) == [False, False, True, True, True, True, False] # test avec un nombre impair


def crible_premiers_entiers(N): 
    """ 
    Retourne une liste des nombres premiers inférieurs ou égaux à N

    Args:
        N (int): la valeur jusqu'à laquelle on veut trouver les nombres premiers
    Returns:
        list: une liste des nombres premiers inférieurs ou égaux à N    """
    
    lst = []
    liste_true = initialise_liste(N)
    if N < 2:
        return lst
    for i in range(2, N):
        if x_met_false(i,liste_true)[i]:
            lst.append(i)

    return lst
            
#crible_premiers_entiers(10)
def test_crible_premiers_entiers():
    assert crible_premiers_entiers(10) == [2, 3, 5, 7] # test avec un nombre pair
    assert crible_premiers_entiers(5) == [2, 3] # test avec un nombre impair
    assert crible_premiers_entiers(0) == [] # test avec un nombre nul
    assert crible_premiers_entiers(20) == [2, 3, 5, 7, 11, 13, 17, 19] # test avec un nombre négatif
    assert crible_premiers_entiers(8) == [2, 3, 5, 7] # test avec un nombre pair et un nombre de division pair
    
    

