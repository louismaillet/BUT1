import mortisia_adams as mortisia
import mercredi_adams as mercredi
import fetide_adams as fetide

def test_ajoute_article() :
    facture = []
    course = []
    assert mortisia.ajoute_article(course, facture, "pain", 1) == (["pain"], [1])
    assert mortisia.ajoute_article(course, facture, "beurre", 2) == (["pain", "beurre"], [1, 2])
    
    assert mercredi.ajoute_article_dico({}, "pain", 1) == {"pain": 1}
    assert mercredi.ajoute_article_dico({"pain": 1}, "beurre", 2) == {"pain": 1, "beurre": 2}

    assert fetide.ajoute_article([], "pain", 1) == [("pain", 1)]
    assert fetide.ajoute_article([("pain", 1)], "beurre", 2) == [("pain", 1), ("beurre", 2)]


def test_supprimer_article() :
    facture = [1, 2]
    course = ["pain", "beurre"]
    assert mortisia.supprimer_article(course, facture, "pain") == (["beurre"], [2])
    assert mortisia.supprimer_article(course, facture, "beurre") == ([], [])
    assert mortisia.supprimer_article(course, facture, "pain") == ([] , [])

    assert mercredi.supprimer_article_dico({"pain": 1, "beurre": 2}, "pain") == {"beurre": 2}
    assert mercredi.supprimer_article_dico({"pain": 1, "beurre": 2}, "beurre") == {"pain": 1}

    assert fetide.supprimer_article([("pain", 1), ("beurre", 2)], "pain") == [("beurre", 2)]
    assert fetide.supprimer_article([("pain", 1), ("beurre", 2)], "beurre") == [("pain", 1)]
    assert fetide.supprimer_article([("pain", 1)], "beurre") == [("pain", 1)]
    assert fetide.supprimer_article([], "beurre") == []

def test_modifier_prix() :
    facture = [1, 2]
    course = ["pain", "beurre"]
    assert mortisia.modifier_prix(course, facture, "pain", 3) == (["pain", "beurre"], [3, 2])
    assert mortisia.modifier_prix(course, facture, "beurre", 4) == (["pain", "beurre"], [3, 4])
    assert mortisia.modifier_prix(course, facture, "p" , 5) == (["pain", "beurre"], [3, 4])

    assert mercredi.modifier_prix({"pain": 1, "beurre": 2}, "pain", 3) == {"pain": 3, "beurre": 2}
    assert mercredi.modifier_prix({"pain": 1, "beurre": 2}, "beurre", 4) == {"pain": 1, "beurre": 4}
    facture = []
    course = []
    assert mortisia.modifier_prix(course, facture, "pain", 6) == ([] , [])
    assert mercredi.modifier_prix({}, "pain", 6) == {}

    assert fetide.modifier_article([("pain", 1), ("beurre", 2)], "pain", 3) == [("pain", 3), ("beurre", 2)]
    assert fetide.modifier_article([("pain", 1), ("beurre", 2)], "beurre", 4) == [("pain", 1), ("beurre", 4)]
    assert fetide.modifier_article([("pain", 1), ("beurre", 2)], "p", 5) == [("pain", 1), ("beurre", 2)]
    assert fetide.modifier_article([], "pain", 6) == []

def test_montant_total():
    facture = [1, 2]
    assert mortisia.montant_total(facture) == 3
    facture = []
    assert mortisia.montant_total(facture) == 0
    facture = [1, 2, 3]
    assert mortisia.montant_total(facture) == 6

    assert mercredi.montant_total({"pain": 1, "beurre": 2}) == 3
    assert mercredi.montant_total({"pain": 1}) == 1
    assert mercredi.montant_total({}) == 0

    assert fetide.montant_article([("pain", 1), ("beurre", 2)]) == 3
    assert fetide.montant_article([("pain", 1)]) == 1
    assert fetide.montant_article([]) == 0

def test_plus_cher():
    assert mortisia.plus_cher([], []) == None
    assert mortisia.plus_cher(["pain"], [1]) == "pain"
    assert mortisia.plus_cher(["pain", "beurre"], [1, 2]) == "beurre"

    assert mercredi.plus_cher({"pain": 1}) == "pain"
    assert mercredi.plus_cher({"pain": 1, "beurre": 2}) == "beurre"
    assert mercredi.plus_cher({}) == None

    assert fetide.plus_cher([("pain", 1)]) == "pain"
    assert fetide.plus_cher([("pain", 1), ("beurre", 2)]) == "beurre"
    assert fetide.plus_cher([]) == None


