use BE_beauty_salon
go

bulk insert Produkt from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\produkty2.bulk' with (fieldterminator='|')

bulk insert Klient from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\klienci2.bulk' with (fieldterminator='|')

bulk insert Reklamodawca from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\reklamodawcy2.bulk' with (fieldterminator='|')

bulk insert Salon from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\salony2.bulk' with (fieldterminator='|')

bulk insert Usluga from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\uslugi2.bulk' with (fieldterminator='|')

bulk insert Reklama from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\reklamy2.bulk' with (fieldterminator='|')

bulk insert Wizyta from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\wizyty2.bulk' with (fieldterminator='|')

bulk insert Produkt_ilosc from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\produkty_ilosc2.bulk' with (fieldterminator='|')

bulk insert Usluga_wizyta from 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\uslugi_wizyty2.bulk' with (fieldterminator='|')

select * from Reklamodawca 
select * from Produkt
select * from Klient
select * from Produkt_ilosc
select * from Usluga_wizyta
select * from Wizyta
