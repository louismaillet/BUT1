# fichier de tests de la SAE 1.01 partie 1
# bilan carbone d'activités mystères en septembre 2024

# on importe toutes les fonctions et données définies dans le fichier bilan_carbone
# l'appel de ces fonctions et données doit être préfixé par bc. 
import bilan_carbone as bc  


# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_avant():
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 67.1, 'type4')) == True
    assert bc.est_avant(('Alexandre', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 67.2, 'type4')) == True
    assert bc.est_avant(('Mucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('b', '2024-09-03', 70.08, 'type3'), ('a', '2024-09-02', 67.2, 'type3')) == False
def test_annee():
    assert bc.annee(('Lucas', '2024-09-01', 67.2, 'type3')) == '2024'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'
    assert bc.annee(('Lucas', '0000-09-01', 67.2, 'type3')) == '0000'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'

def test_annee_mois():
    assert bc.annee_mois(('Lucas', '2024-10-01', 67.2, 'type3')) == '2024-10'
    assert bc.annee_mois(('Lucas', '2023-09-01', 67.2, 'type3')) == '2023-09'
    assert bc.annee_mois(('Lucas', '0000-09-01', 67.2, 'type3')) == '0000-09'
    assert bc.annee_mois(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999-12'


def test_max_emmission():
    assert bc.max_emmission([]) == None
    assert bc.max_emmission(bc.liste1) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste2) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste3) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste4) == ('David', '2024-09-27', 21, 'type2')
def test_filtre_par_prenom():
    assert bc.filtre_par_prenom([], 'Lucas') == []
    assert bc.filtre_par_prenom([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')], 'Lucas') == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.filtre_par_prenom(bc.liste1, 'David') == [('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 21, 'type2'), ('David', '2024-09-28', 17, 'type3'), ('David', '2024-09-29', 23, 'type4')]
    assert bc.filtre_par_prenom(bc.liste2, 'Christophe') == [('Christophe', '2024-09-26', 15, 'type1'), ('Christophe', '2024-09-27', 19, 'type2'),('Christophe', '2024-09-28', 14, 'type3'),('Christophe', '2024-09-29', 20, 'type4'),]

def test_filtre():
    assert bc.filtre([], 3, 'type1') == []
    assert bc.filtre(bc.liste3, 1, '2024-09-29') == [('David', '2024-09-29', 23, 'type4'), ('Guillaume', '2024-09-29', 22, 'type4')]
    assert bc.filtre(bc.liste1, 3, 'type3') == [('Christophe', '2024-09-28', 14, 'type3'),('David', '2024-09-28', 17, 'type3'),('Guillaume', '2024-09-28', 16, 'type3')]
    assert bc.filtre(bc.liste2, 2, 17) == [('Guillaume', '2024-09-26', 17, 'type1'),('David', '2024-09-28', 17, 'type3'),]
    

def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78

def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    
def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('a', '2024-09-01', 67.2, 'type3'), ('b', '2024-09-03', 70.08, 'type3'), ('a', '2024-09-02', 67.2, 'type3')]) == False
    


def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']


def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']


def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2


def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type4')], 'type4') == '2024-09-02'
    assert bc.premiere_apparition_type([
        ('Christophe', '2024-09-26', 15, 'type1'),
        ('Christophe', '2024-09-27', 19, 'type2'),
        ('Christophe', '2024-09-28', 14, 'type3'),
        ('Christophe', '2024-09-29', 20, 'type4'),
        ('David', '2024-09-26', 18, 'type1'),
        ('David', '2024-09-27', 21, 'type2'),
        ('David', '2024-09-28', 17, 'type3'),
        ('David', '2024-09-29', 23, 'type4'),
        ('Guillaume', '2024-09-26', 17, 'type1'),
        ('Guillaume', '2024-09-27', 20, 'type2'),
        ('Guillaume', '2024-09-28', 16, 'type3'),
        ('Guillaume', '2024-09-29', 22, 'type4'),
    ], 'type4') == '2024-09-29'



def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')

def test_charger_activite():
    bc.sauver_activites('activites.csv',bc.liste6)
    assert bc.charger_activites('activites.csv') == bc.liste6
    

    bc.sauver_activites('activites.csv',bc.liste5)
    assert bc.charger_activites('activites.csv') == bc.liste5

    bc.sauver_activites('activites.csv',bc.liste4)
    assert bc.charger_activites('activites.csv') == bc.liste4
    bc.sauver_activites('activites.csv',bc.liste3)
    assert bc.charger_activites('activites.csv') == bc.liste3
    bc.sauver_activites('activites.csv',bc.liste2)
    assert bc.charger_activites('activites.csv') == bc.liste2

def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None

def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96

# ---------------------------------------------------------------------------------------------
# Ajoutez ici les tests manquants (vos propres fonctions le cas échéant)
# ---------------------------------------------------------------------------------------------

