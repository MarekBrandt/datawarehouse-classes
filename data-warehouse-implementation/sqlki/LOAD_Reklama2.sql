USE beauty_salon
GO

If (object_id('dbo.SurveysTemp') is not null) DROP TABLE dbo.SurveysTemp;
CREATE TABLE dbo.SurveysTemp(adID varchar(10), adIsCause varchar(3), adSeen varchar(3), points varchar(2), visitId varchar(10));
go

BULK INSERT dbo.SurveysTemp
    FROM 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\ankiety2.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK
    );

go

If(object_id('EtlAdvertisment') is not null) Drop View EtlAdvertisment;
go 
CREATE VIEW EtlAdvertisment
AS
SELECT DISTINCT
	t1.Typ as [Typ],
    CASE
        WHEN t1.ID_Uslugi IS NOT NULL THEN 'Usluga'
        ELSE 'Salon'
    END as [Rodzaj],
    CASE
        WHEN t2.points < 3 THEN '<3'
        WHEN t2.points >= 3 and t2.points < 5 THEN '<3,5)'
        WHEN t2.points >= 5 and t2.points < 7 THEN '<5,7)'
        WHEN t2.points >= 7 THEN '>7'
    END AS [Ocena]
FROM BE_beauty_salon.dbo.Reklama as t1
JOIN dbo.SurveysTemp as t2 on t2.adID = t1.ID_Reklamy
go


MERGE INTO Reklama AS R1
	USING EtlAdvertisment AS R2
		ON R2.Typ = R1.Typ
        AND R2.Rodzaj = R1.Rodzaj
        AND R2.Ocena = R1.Ocena
			WHEN Not Matched
				THEN 
					INSERT Values(
					R2.Typ,
                    R2.Rodzaj,
					R2.Ocena
					);

Drop table dbo.SurveysTemp;
Drop View EtlAdvertisment