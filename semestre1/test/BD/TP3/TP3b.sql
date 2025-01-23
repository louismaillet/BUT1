- @ SCRIPTS/CreateDropPeintres





--- BASE - For complementary queries
drop table  EXPOSITIONTABLEAUX;
drop table GALERIES;
drop table TABLEAUX;
drop table PEINTRES;


create table PEINTRES (
nomP Varchar2(20) primary key,
dateN date,
ecole Varchar2(20));

create table TABLEAUX(
nomP Varchar2(20),
titreTab VarChar2(30) ,
valeurEstimee number (10,2),
type VarChar2(10),
constraint KTableaux primary key (nomP, titreTab),
constraint KFPeintreExisteInTableaux foreign key (nomP) references  PEINTRES (nomP) on delete cascade);


create table GALERIES
(IdSalle number(3) primary key,
nomSalle VarChar2(20),
superfice number(4),
ville VarChar2(15));

create table EXPOSITIONTABLEAUX
(IdSalle number(3),
nomP Varchar2(20),
titreTab VarChar2(30) ,
dateDebut date,
dateFin date,
constraint KEXPO primary key (IdSalle,nomP,titreTab),
constraint KFTableauxExisteInExpo foreign key (nomP,titreTab) references  TABLEAUX (nomP,titreTab) on delete cascade,
constraint KFSalleExisteInExpo foreign key (IdSalle) references GALERIES(IdSalle) on delete cascade);


-- @ SCRIPTS/instancePeintres

insert into PEINTRES values ('Monet', to_date('14-11-1840','dd-mm-yyyy'), 'impressionisme');

insert into PEINTRES values('Renoir', to_date('25-02-1841','dd-mm-yyyy'), 'impressionisme');

insert into PEINTRES values('Fragonard', to_date('05-04-1732','dd-mm-yyyy'), 'rococo');

insert into PEINTRES values('Picasso', to_date('25-10-1881','dd-mm-yyyy'), 'cubisme');

insert into PEINTRES values ('Toulouse-Lautrec', to_date('24-11-1864','dd-mm-yyyy'), 'art nouveau');



insert into TABLEAUX values ('Picasso','Guernica', 10000000 ,'huile');
insert into TABLEAUX values ('Picasso','Le sculpteur',800000 ,'huile');
insert into TABLEAUX values ('Renoir','Jeunes filles aux piano', 5000000 ,'huile');

insert into TABLEAUX values ('Monet','Nympheas',10000000 ,'huile');
insert into TABLEAUX values ('Toulouse-Lautrec' ,'Femme a sa toillette',10000000 ,'aquarelle');
insert into TABLEAUX values ('Toulouse-Lautrec', 'Moulin Rouge La Goulue',10000000 ,'affiche');

insert into GALERIES values (1, 'Orangerie', 6300, 'Paris');
insert into GALERIES values (2, 'Jeu de pomme', 1200, 'Paris');
insert into GALERIES values (3, 'Maison des Consuls', 200, 'Saint-Cere');
insert into GALERIES values (4, 'Gil Batisde', 100, 'Orleans');
insert into GALERIES values (5, 'Frac', 500, 'Orleans');


insert into EXPOSITIONTABLEAUX values (5,  'Picasso','Le sculpteur', to_date('24-11-2013','dd-mm-yyyy'), to_date('24-01-2014','dd-mm-yyyy'));
insert into EXPOSITIONTABLEAUX values (5,  'Toulouse-Lautrec' ,'Femme a sa toillette', to_date('24-11-2013','dd-mm-yyyy'), to_date('24-01-2014','dd-mm-yyyy'));

insert into EXPOSITIONTABLEAUX values (1,  'Renoir','Jeunes filles aux piano', to_date('24-12-2013','dd-mm-yyyy'), to_date('24-02-2014','dd-mm-yyyy'));

insert into EXPOSITIONTABLEAUX values (1,  'Monet','Nympheas', to_date('24-12-2000','dd-mm-yyyy'), to_date('24-02-2020','dd-mm-yyyy'));

insert into EXPOSITIONTABLEAUX values (2,  'Picasso','Le sculpteur', to_date('24-11-2014','dd-mm-yyyy'), to_date('24-01-2015','dd-mm-yyyy'));

insert into EXPOSITIONTABLEAUX values (3,  'Toulouse-Lautrec' ,'Femme a sa toillette', to_date('24-04-2013','dd-mm-yyyy'), to_date('24-07-2014','dd-mm-yyyy'));
















































