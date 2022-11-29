use beauty_salon
Go

insert into Reklamodawca values ('Ulotex','0123456789', 'ulotki','kulinarna')
insert into Reklamodawca values ('Billbordex','9481059312', 'billboardy','samochodowa')
insert into Reklamodawca values ('Internotex','6497358246', 'reklamy internetowe','salony pieknosci')

insert into Reklama values ('ulotka','Salon','<3,5)')
insert into Reklama values ('reklama internetowa','Salon','<7,10)')
insert into Reklama values ('billboard','Usluga','<5,7)')

insert into Klient values ('Piotr Garbowski')
insert into Klient values ('Marek Brandt')
insert into Klient values ('Darek Garbowski')

insert into Junk values ('Niska','TAK','TAK','TAK')
insert into Junk values ('Srednia','NIE','NIE','NIE')
insert into Junk values ('Wysoka','TAK','TAK','NIE')

insert into Data_ values ('1000-1-1',1000,'Styczen',1)
insert into Data_ values ('2021-10-10',2021,'Pazdziernik',10)
insert into Data_ values ('2021-10-17',2021,'Pazdziernik',17)

insert into Wizyta_w_salonie values (1,3,3,3,'2021-10-10','1000-1-1','2021-10-17',1,500,0,30,470,1,0)
insert into Wizyta_w_salonie values (2,2,3,2,'2021-10-10','2021-10-10','2021-10-17',0,0,0,0,0,0,0)
insert into Wizyta_w_salonie values (3,1,1,1,'2021-10-17','1000-1-1','2021-10-17',1,50,1,10,40,1,1)