-- TP 1
-- Nom:  , Prenom: 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner la liste des panels dont fait partie Caroline BOURIER.
select distinct nomPan
from CONSTITUER
NAtural join PANEL 
NAtural join SONDE
where nomsond = 'BOURIER' and prenomSond = 'Caroline';

SElect distinct nompan
From PANEL
natural join CONSTITUER
WHere numsond in (select distinct numsond
from SONDE
where nomsond = 'BOURIER' and prenomSond = 'Caroline');

SElect distinct nompan
From PANEL
natural join CONSTITUER
WHere EXISTS (select distinct numsond
from SONDE
where CONSTITUER.numSond = SONDE.numsond and nomsond = 'BOURIER' and prenomSond = 'Caroline');

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- +-----------------+
-- = Reponse question 1.



-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont un des sondés est de la tranche d'âge 70 à 120 ans?
Select nomPan 
From PANEL 
natural join CONSTITUER
natural join SONDE
natural join CARACTERISTIQUE
natural join TRANCHE
where valdebut >= 70 and valfin <= 120;

Select nomPan 
from PANEL
natural join CONSTITUER
WHERE numSond IN (SELECT numSond FROM SONDE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE WHERE  valdebut >= 70 and valfin <= 120);

Select nomPan 
from PANEL
natural join CONSTITUER
WHERE EXISTS (SELECT numSond FROM SONDE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE WHERE CONSTITUER.numSond = SONDE.numSond AND valdebut >= 70 and valfin <= 120);


-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | France global 2 |
-- +-----------------+
-- = Reponse question 2.



-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés de la tranche d'age 70-120 ans qui sont ouvriers?

SELECT  nomsond ,prenomSond
FROM SONDE 
NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE NATURAL JOIN CATEGORIE
WHERE intitulecat = 'ouvriers' AND valdebut >= 70 and valfin <= 120;

SELECT nomsond ,prenomSond
FROM SONDE 
NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE
WHERE idcat IN (SELECT idcat FROM CATEGORIE WHERE intituleCat = 'ouvriers') AND valdebut >= 70 and valfin <= 120;

SELECT nomsond, prenomSond
FROM SONDE 
NATURAL JOIN CARACTERISTIQUE 
NATURAL JOIN TRANCHE
WHERE EXISTS (
    SELECT 1 
    FROM CATEGORIE 
    WHERE CATEGORIE.idcat = CARACTERISTIQUE.idcat 
    AND intituleCat = 'ouvriers' 
    AND valdebut >= 70 
    AND valfin <= 120
);

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | ERYS      | Imane      |
-- | BERRGAIES | Claire     |
-- | JABAT     | Rose       |
-- | WALLOCHE  | Marion     |
-- | LENUJA    | Pauline    |
-- | etc...
-- = Reponse question 3.



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les ouvriers qui portent le prénom Olivier?

SELECT  nomsond ,prenomSond
FROM SONDE 
NATURAL JOIN CARACTERISTIQUE NATURAL JOIN CATEGORIE
WHERE prenomSond = 'Olivier' AND intitulecat = 'ouvriers';

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | THALOUERD | Olivier    |
-- | POTRININ  | Olivier    |
-- +-----------+------------+
-- = Reponse question 4.



-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les tranches d'âge qui comportent une ou plusieurs femmes nées un 25 avril?

SELECT distinct valDebut, valFin
FROM TRANCHE
NATURAL JOIN CARACTERISTIQUE NATURAL JOIN SONDE 
WHERE sexe = 'F' AND  DAY(dateNaisSond) = '25' AND MONTH(dateNaisSond) = '4' ;


-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+--------+
-- | valDebut | valFin |
-- +----------+--------+
-- | 40       | 49     |
-- +----------+--------+
-- = Reponse question 5.



-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés prénommés Jean qui appartiennent à au moins 2 panels différents? 

SELECT prenomSond, nomSond
FROM SONDE
WHERE prenomSond = 'Jean'
AND numSond IN (
    SELECT numSond
    FROM CONSTITUER
    GROUP BY numSond
    HAVING COUNT(DISTINCT numPan) >= 2
);
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+----------+
-- | prenomSond | nomSond  |
-- +------------+----------+
-- | Jean       | DILY     |
-- | Jean       | JATECHU  |
-- | Jean       | PIETIENE |
-- | Jean       | FAL      |
-- | Jean       | BOYEGHE  |
-- +------------+----------+
-- = Reponse question 6.



