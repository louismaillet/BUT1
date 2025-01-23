import oiseaux
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert oiseaux.recherche_oiseau(...)==...

def test_recherche_par_famille():
    assert oiseaux.recherche_par_famille(...)==...

def test_oiseau_le_plus_observe():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau" # verifie que le nom de l'oiseau le plus observe est bien "Moineau" parmis la liste observations1
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle" # verifie que le nom de l'oiseau le plus observe    est bien "Tourterelle" parmis la liste observations2
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange" # verifie que le nom de l'oiseau le plus observe est bien "Mésange" parmis la liste observations3
    assert oiseaux.oiseau_le_plus_observe([])==None # verifie que la fonction retourne bien None si la liste est vide

def test_est_liste_observations():
    assert oiseaux.est_liste_observations(...)==...

def test_max_observations():
    assert oiseaux.max_observations(...)==...

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(...)==...

def test_total_famille():
    assert oiseaux.total_famille(...)==...


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(...)==...

def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...



