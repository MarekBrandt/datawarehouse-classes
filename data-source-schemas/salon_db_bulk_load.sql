use SalonBeauty
go

bulk insert Produkt from 'C:\Users\marek\Desktop\Dane\produkty.bulk' with (fieldterminator='|')

bulk insert Klient from 'C:\Users\marek\Desktop\Dane\klienci.bulk' with (fieldterminator='|')

bulk insert Reklamodawca from 'C:\Users\marek\Desktop\Dane\reklamodawcy.bulk' with (fieldterminator='|')

bulk insert Salon from 'C:\Users\marek\Desktop\Dane\salony.bulk' with (fieldterminator='|')

bulk insert Usluga from 'C:\Users\marek\Desktop\Dane\uslugi.bulk' with (fieldterminator='|')

bulk insert Reklama from 'C:\Users\marek\Desktop\Dane\reklamy.bulk' with (fieldterminator='|')

bulk insert Wizyta from 'C:\Users\marek\Desktop\Dane\wizyty.bulk' with (fieldterminator='|')

bulk insert Produkt_ilosc from 'C:\Users\marek\Desktop\Dane\produkty_ilosc.bulk' with (fieldterminator='|')

bulk insert Usluga_wizyta from 'C:\Users\marek\Desktop\Dane\uslugi_wizyty.bulk' with (fieldterminator='|')

select * from Produkt
select * from Klient
select * from Produkt_ilosc
select * from Usluga_wizyta
select * from Wizyta
