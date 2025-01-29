-- TP 2
-- Nom:  , Prenom: 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont ne fait pas partie Louane DJARA?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 1.
SELECT distinct nompan
From PANEL 
Where idPan not in(SELECT idPan
from SONDE NATURAL JOIN CONSTITUER NATURAL JOIN PANEL
Where prenomSond = 'Louane' and nomSond = 'DJARA');

-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les prénoms de sondé commençant par un A qui n'apparaissent pas dans la tranche d'age 20-29 ans? Classez ces noms par ordre alphabétique.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | prenomSond |
-- +------------+
-- | Alice      |
-- | Allan      |
-- | Amaury     |
-- | Ambre      |
-- | Anaïs      |
-- | etc...
-- = Reponse question 2.

SELECT distinct prenomSond
From SONDE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE
where prenomSond LIKE 'A%' and prenomSond not in (SELECT prenomSond 
                                        FROM TRANCHE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN SONDE
                                        WHERE valDebut = 20 and valFin = 29 )
ORDER BY prenomSond;

-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les panels dont tous les sondés ont moins de 60 ans? Rappel: CURDATE() donne la date du jour et DATEDIFF(d1,d2) 
--   donne le nombre de jours entre d1 et d2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 3.

SELECT nomPan
FROM PANEL
WHERE idPan NOT IN (
    SELECT idPan
    FROM CONSTITUER
    NATURAL JOIN SONDE
    WHERE DATEDIFF(CURDATE(), dateNaisSond) / 365.25 >= 60
);



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories qui comportent des personnes nées en 1979? On rappelle que YEAR(d) donne l'année de la date d 
--  sous la forme d'un entier.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------------------------------+
-- | intituleCat                                     |
-- +-------------------------------------------------+
-- | Cadres, professions intellectuelles supérieures |
-- | Professions intermédiaires                      |
-- | Employés                                        |
-- | Ouvriers                                        |
-- | Inactifs ayant déjà travaillé                   |
-- +-------------------------------------------------+
-- = Reponse question 4.

SELECT DISTINCT intituleCat
FROM CATEGORIE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN SONDE
WHERE YEAR(dateNaisSond) = 1979;


-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les sondés nés en 2001 qui appartiennent aux panels France global 1 et France global 2?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+------------+
-- | nomSond    | prenomSond |
-- +------------+------------+
-- | TRISAULOLU | Elise      |
-- | MAMIAT     | Mathieu    |
-- | NEUSIL     | Theo       |
-- +------------+------------+
-- = Reponse question 5.

SELECT DISTINCT nomSond, prenomSond
FROM SONDE NATURAL JOIN CONSTITUER NATURAL JOIN PANEL p1
WHERE YEAR(dateNaisSond) = 2001 AND p1.nomPan = 'France global 1'
AND numSond IN (
    SELECT numSond
    FROM CONSTITUER NATURAL JOIN PANEL p2
    WHERE p2.nomPan = 'France global 2'
);

-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés nés en 1979 qui ont la même date de naissance?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+----------+------------+
-- | nomSond | prenomSond | nomSond  | prenomSond |
-- +---------+------------+----------+------------+
-- | DASA    | Maxime     | PEKARDAC | Bilal      |
-- +---------+------------+----------+------------+
-- = Reponse question 6.



SELECT s1.nomSond, s1.prenomSond, s2.nomSond, s2.prenomSond
FROM SONDE s1 NATURAL JOIN SONDE s2
WHERE s1.dateNaisSond = s2.dateNaisSond AND YEAR(s1.dateNaisSond) = 1979;





