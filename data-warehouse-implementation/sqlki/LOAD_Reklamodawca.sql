USE beauty_salon
GO

If(object_id('EtlAdvertiser') is not null) Drop View EtlAdvertiser;
go 
CREATE VIEW EtlAdvertiser
AS
SELECT DISTINCT
	[Nazwa],
	[NIP],
	[Specjalizacja],
	[Glowna_Tematyka]
FROM BE_beauty_salon.dbo.Reklamodawca
go


MERGE INTO Reklamodawca AS R1
	USING EtlAdvertiser AS R2
		ON R2.NIP = R1.NIP
			WHEN Not Matched
				THEN 
					INSERT Values(
					R2.Nazwa,
					R2.NIP,
					R2.Specjalizacja,
					R2.Glowna_Tematyka,
					1
					)
			WHEN Matched
				AND (R2.Specjalizacja <> R1.Specjalizacja)
				OR (R2.Glowna_Tematyka <> R1.Glowna_Tematyka)
			THEN UPDATE
				SET R1.jestAktualne = 0
			WHEN Not Matched BY Source
			THEN UPDATE
				SET R1.jestAktualne = 0
			;


INSERT INTO Reklamodawca(
	Nazwa, 
	NIP, 
	Specjalizacja, 
	Glowna_tematyka, 
	jestAktualne
	)
	SELECT 
		Nazwa, 
		NIP, 
		Specjalizacja, 
		Glowna_tematyka, 
		1
	FROM EtlAdvertiser
	EXCEPT
	SELECT 
		Nazwa, 
		NIP, 
		Specjalizacja, 
		Glowna_tematyka, 
		1
	FROM Reklamodawca;
Drop View EtlAdvertiser

SELECT * FROM Reklamodawca order by Nazwa