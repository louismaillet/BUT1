SELECT NomEquipe 
FROM EQUIPES;

SELECT DirecteurSportif 
FROM EQUIPES;

SELECT NomCoureur, PrenomCoureur 
FROM COUREURS;

SELECT NomEquipe 
FROM COUREURS 
WHERE NomCoureur = 'ULLRICH';

SELECT NomCoureur 
FROM COUREURS 
WHERE NomEquipe = 'COFIDIS';

SELECT NomCoureur, PrenomCoureur 
FROM COUREURS 
WHERE CodePays = 'FRA';

SELECT TempsRealise 
FROM TEMPS 
join COUREURS on TEMPS.NumCoureur = COUREURS.NumCoureur 
WHERE NomCoureur = 'JALABERT' and NumEtape = 3;

SELECT TempsRealise 
FROM TEMPS 
join COUREURS on TEMPS.NumCoureur = COUREURS.NumCoureur 
join EQUIPES on COUREURS.NomEquipe = EQUIPES.NomEquipe 
join ETAPES on TEMPS.NumEtape = ETAPES.NumEtape 
WHERE DirecteurSportif = 'Manolo SAIZ' and VilleDepart = 'Rouen';

SELECT distinct PAYS.NPays 
FROM PAYS 
join COUREURS on PAYS.CodePays = COUREURS.CodePays 
join TEMPS on COUREURS.NumCoureur = TEMPS.NumCoureur 
join ETAPES on TEMPS.NumEtape = ETAPES.NumEtape 
WHERE VilleArrivee = 'Plumelec';

SELECT COUREURS.NomCoureur, AUTRESCOUREURS.NomCoureur 
FROM COUREURS 
join COUREURS AUTRESCOUREURS on COUREURS.CodePays = AUTRESCOUREURS.CodePays 
WHERE COUREURS.NumCoureur < AUTRESCOUREURS.NumCoureur;

SELECT PrenomCoureur, NomCoureur 
FROM COUREURS 
WHERE CodePays = 'FRA';

SELECT NomCoureur, PrenomCoureur 
FROM COUREURS 
WHERE PrenomCoureur like 'J%';

SELECT NomCoureur 
FROM COUREURS 
order by NomCoureur;

SELECT ETAPES.NumEtape, TempsRealise, NomCoureur 
FROM TEMPS 
join COUREURS on TEMPS.NumCoureur = COUREURS.NumCoureur 
join ETAPES on TEMPS.NumEtape = ETAPES.NumEtape 
order by ETAPES.NumEtape, TempsRealise, NomCoureur;


