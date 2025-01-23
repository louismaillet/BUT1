drop table RESERVATIONS;
drop table CLIENTS;
drop table VOYAGES;

create table CLIENTS 
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table VOYAGES
(Code Varchar2(60) primary key,
VilleDepart VarChar2(30),
VilleArrivee VarChar2(30),
Depart Date,
Retour Date,
Prix Number(8,2));

create table RESERVATIONS (
Id Number(4) , 
Code Varchar2(60),
DateReserv Date,
foreign key (Id) references CLIENTS(Id) on delete cascade,
foreign key (Code) references VOYAGES (Code) on delete cascade);

insert into Clients values ( 1, 'Dupont', 'Jean', 'Orleans');
insert into Clients values ( 2, 'Durand', 'Paul', 'Orleans');
insert into Clients values ( 3, 'Martin', 'Pierre', 'Paris');
insert into Clients values ( 4, 'Auger', 'Marcel', 'Paris');
insert into Clients values ( 5, 'Smith', 'Peter', 'Londres');
insert into Clients values ( 6, 'Barnes', 'Jane', 'Berlin');
insert into Clients values ( 7, 'Freud', 'Florian', 'Berlin');

insert into Voyages values ('V100', 'Paris', 'Amsterdam',  to_date('01-08-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-08-2019-14:30','DD-MM-YYYY-HH24:MI'),200.00);
insert into Voyages values ('V200', 'Paris', 'Rio de Janeiro',  to_date('01-12-2019-11:30','DD-MM-YYYY-HH24:MI'), to_date('07-12-2019-16:30','DD-MM-YYYY-HH24:MI'),2000.00);
insert into Voyages values ('V300', 'Prague', 'Amsterdam',  to_date('01-10-2019-8:30','DD-MM-YYYY-HH24:MI'), to_date('10-08-2019-15:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V140', 'Paris', 'Amsterdam',  to_date('01-11-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-11-2019-14:30','DD-MM-YYYY-HH24:MI'),100.00);
insert into Voyages values ('V400', 'Lisbonne', 'Madrid',  to_date('01-03-2020-12:30','DD-MM-YYYY-HH24:MI'), to_date('07-03-2020-18:30','DD-MM-YYYY-HH24:MI'),400.00);
insert into Voyages values ('V500', 'Paris', 'Madrid',  to_date('01-04-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-04-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V600', 'Berlin', 'Madrid',  to_date('01-05-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);

insert into Reservations values (6, 'V100', to_date('01-07-2019-18:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V100', to_date('01-06-2019-8:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V200', to_date('01-05-2019-21:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V400', to_date('01-11-2019-18:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (2, 'V400', to_date('01-11-2019-21:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V140', to_date('01-06-2019-9:25','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (4, 'V300', to_date('01-05-2019-12:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V100', to_date('01-05-2019-19:25','DD-MM-YYYY-HH24:MI'));

-- 1
select VilleArrivee from Voyages where VilleDepart = 'Paris';
    
-- 2
select * from Voyages where VilleArrivee = 'Amsterdam';

-- 3
select VilleDepart, Depart from Voyages where VilleArrivee = 'Amsterdam';

-- 4
select c.Nom, c.Prenom, v.VilleArrivee, v.Prix
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
order by c.Nom, v.Prix desc;

-- 5
select c.Nom, c.Ville, r.Code
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
where c.Ville = v.VilleDepart;

-- 6
insert into Voyages values ('V700', 'Paris', 'Tokyo', to_date('01-10-2024-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-10-2024-20:30','DD-MM-YYYY-HH24:MI'), 1500.00);

-- 7
select VilleDepart, VilleArrivee, Depart
from Voyages
where Depart > sysdate + interval '3' month
order by Depart;

-- 8
select distinct VilleDepart as Villes from Voyages
union
select distinct VilleArrivee as Villes from Voyages;

-- 9
select * from Clients where Ville <> 'Paris';

-- 10
select c.*
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
where v.VilleDepart = 'Paris' and c.Ville <> 'Paris';

-- 11
 Trouver les clients qui n’ont aucune r´eservation.
 select 





























-- 11
select * from Clients where Id not in (select Id from Reservations);

-- 12
select * from Voyages where Code not in (select Code from Reservations);

-- 13
select c.*
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
where v.VilleDepart = 'Paris'
group by c.Id, c.Nom, c.Prenom, c.Ville
having count(distinct v.VilleArrivee) = 1 and max(v.VilleArrivee) = 'Amsterdam';

-- 14
select c.*
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
where v.VilleArrivee in ('Amsterdam', 'Rio de Janeiro')
group by c.Id, c.Nom, c.Prenom, c.Ville
having count(distinct v.VilleArrivee) = 2;

-- 15
select distinct c.*
from Clients c
join Reservations r on c.Id = r.Id
join Voyages v on r.Code = v.Code
where v.VilleArrivee in ('Amsterdam', 'Rio de Janeiro');

-- 16
select c1.Nom as Client1, c2.Nom as Client2, c1.Ville
from Clients c1
join Clients c2 on c1.Ville = c2.Ville and c1.Id < c2.Id;

-- 17
select v1.Code as Voyage1, v2.Code as Voyage2, v1.Prix
from Voyages v1
join Voyages v2 on v1.Prix = v2.Prix and v1.Code < v2.Code;

-- 18
select c.*
from Clients c
join Reservations r on c.Id = r.Id
group by c.Id, c.Nom, c.Prenom, c.Ville
having count(r.Code) >= 2;

-- 19
select c.*
from Clients c
join Reservations r on c.Id = r.Id
group by c.Id, c.Nom, c.Prenom, c.Ville
having count(r.Code) = 1;

-- 20
select c1.Nom as Client1, c2.Nom as Client2, r1.Code as Voyage1, r2.Code as Voyage2, r1.DateReserv
from Reservations r1
join Reservations r2 on r1.DateReserv = r2.DateReserv and r1.Id < r2.Id
join Clients c1 on r1.Id = c1.Id
join Clients c2 on r2.Id = c2.Id;

-- 21
select c1.Nom as Client1, c2.Nom as Client2, r1.Code, r1.DateReserv
from Reservations r1
join Reservations r2 on r1.Code = r2.Code and r1.DateReserv = r2.DateReserv and r1.Id < r2.Id
join Clients c1 on r1.Id = c1.Id
join Clients c2 on r2.Id = c2.Id;
