USE beauty_salon
GO

If(object_id('EtlCustomer') is not null) Drop View EtlCustomer;
GO
CREATE VIEW EtlCustomer
AS
SELECT DISTINCT
	[Imie_i_nazwisko] = REPLACE(CONCAT_WS(' ',Imie,Nazwisko),'  ',' ')
FROM BE_beauty_salon.dbo.Klient;
go
MERGE INTO Klient as TT
	USING EtlCustomer as ST
		ON TT.Imie_i_nazwisko = ST.Imie_i_nazwisko
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.Imie_i_nazwisko
					);

Drop View EtlCustomer;
SELECT * FROM Klient