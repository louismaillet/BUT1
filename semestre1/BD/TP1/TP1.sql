drop table Commande;
drop table Colis;
drop table Client;

CREATE TABLE Client(
    CodeClient INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    adresse VARCHAR(50),
    email VARCHAR(50),
    refPointDist number(5),
    constraint cleclients PRIMARY KEY(codeCl)
);
CREATE TABLE Commande(
    refCom number(20) PRIMARY KEY,
    dateCommande DATE,
    codeCl number(10)
);
alter table Commande add constraint clientExiste foreign key (codeCl) references Client(codeCl);

CREATE TABLE Colis(
    refCom number(12),
    numColis number(2),
    indicateur VARCHAR2(1) default('N') check (indicateur IN ('O', 'N')),
    constraint clecolis PRIMARY KEY(refCom, numColis)
);


INSERT INTO Client VALUES (1, 'Doe', 'John', '123 Main St', 'john.doe@example.com', 100);
INSERT INTO Client VALUES (2, 'Smith', 'Jane', '456 Elm St', 'jane.smith@example.com', 50);
INSERT INTO Client VALUES (3, 'Johnson', 'Paul', '789 Oak St', 'paul.johnson@example.com', 200);

INSERT INTO Commande VALUES (1, 2022-01-01, 1);
INSERT INTO Commande VALUES (2, 2022-02-01, 2);
INSERT INTO Commande VALUES (3, 2022-03-01, 3);

INSERT INTO Colis VALUES (1, 1, 'O');
INSERT INTO Colis VALUES (1, 2, 'N');
INSERT INTO Colis VALUES (2, 1, 'O');
INSERT INTO Colis VALUES (2, 2, 'O');

commit;

SELECT nom, prenom FROM Client;

SELECT designation 
FROM Articles 
WHERE prix > 50;

SELECT adresse 
FROM Client 
WHERE nom = 'Smith' AND prenom = 'Bob';

SELECT adresse 
FROM Client 
WHERE nom = 'Smith' AND prenom = 'Jane';

SELECT prix designation 
FROM Articles 
WHERE nom = 'Smith' AND prenom = 'Bob';

SELECT designation, prix, numColis, quantite
FROM Articles, Commande, Colis
WHERE Articles.refCom = '200'