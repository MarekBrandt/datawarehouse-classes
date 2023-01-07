USE beauty_salon
GO

If (object_id('dbo.SurveysTemp') is not null) DROP TABLE dbo.SurveysTemp;
CREATE TABLE dbo.SurveysTemp(adID varchar(10), adIsCause varchar(3), adSeen varchar(3), points varchar(2), visitId varchar(10));
go

BULK INSERT dbo.SurveysTemp
    FROM 'C:\Users\marek\Desktop\datawarehouse-classes\data-warehouse-implementation\sqlki\Dane\ankiety.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    TABLOCK
    );
go

If(object_id('EtlVisits') is not null) Drop View EtlVisits;
GO
CREATE VIEW EtlVisits
AS
SELECT
        [ID_Klienta] = klient.ID_Klienta,
        [ID_Reklamy] = reklamaDW.ID_Reklamy,
        [ID_Reklamodawcy] = reklamodawcaDW.ID_Reklamodawcy,
        [ID_Junk] = junk.ID_Junk,
        [Data_Rezerwacji] = wizyta.Data_rezerwacji,
        [Data_Wizyty] = wizyta.Data_wizyty,
        CASE
            WHEN wizyta.Data_odwolania is not null then wizyta.Data_odwolania
            else '1000-1-1'
        END AS [Data_Odwolania],
        CASE
            WHEN junk.Czy_widzial_reklame = 'tak' then 1
            else 0
        END as [Czy_Widziala_Reklame],
        [Kwota_Rachunku] = wizyta.Kwota,
        CASE
            WHEN junk.Czy_przyszla_z_powodu_reklamy = 'tak' then 1
            else 0
        END as [Czy_Przyszla_Z_Powodu_Reklamy],
        (SELECT count(*)
        FROM dbo.SurveysTemp as ankietka
        WHERE reklamaSource.ID_Reklamy = ankietka.adID)/reklamaSource.Cena as [Cena_Pozyskania_Klienta],
        CASE
            WHEN junk.Czy_zarezerwowal_kolejna = 'tak' then 1
            else 0
        END as [Czy_Zarezerwowal_Kolejna],
        CASE
            WHEN reklamaSource.ID_Uslugi is null then 0
            when (SELECT count(*)  from BE_beauty_salon.dbo.Usluga_wizyta
         as uw WHERE uw.ID_Wizyty = wizyta.ID_Wizyty and reklamaSource.ID_Uslugi = uw.ID_Uslugi) > 0 then 1
            else 0
        END as [Czy_Kupil_Zareklamowana_Usluge]
    FROM BE_beauty_salon.dbo.Wizyta as wizyta
    JOIN BE_beauty_salon.dbo.Klient as klientSource on wizyta.ID_Klienta = klientSource.ID_Klienta
    JOIN dbo.Klient as klient on klient.Imie_i_nazwisko = REPLACE(CONCAT_WS(' ',klientSource.Imie,klientSource.Nazwisko),'  ',' ')
    JOIN dbo.SurveysTemp as ankieta on wizyta.ID_Wizyty = ankieta.visitId
    JOIN BE_beauty_salon.dbo.Reklama as reklamaSource on reklamaSource.ID_Reklamy = ankieta.adID
    JOIN dbo.Reklama as reklamaDW on 
        reklamaDW.Typ = reklamaSource.Typ 
        and (
            CASE
                WHEN reklamaSource.ID_Uslugi is not null then 'Usluga'
                ELSE 'Salon'
            END
            ) = reklamaDW.Rodzaj
        and (
            CASE
                WHEN ankieta.points < 3 THEN '<3'
                WHEN ankieta.points >= 3 and ankieta.points < 5 THEN '<3,5)'
                WHEN ankieta.points >= 5 and ankieta.points < 7 THEN '<5,7)'
                WHEN ankieta.points >= 7 THEN '>7'
            END
        ) = reklamaDW.Ocena
    JOIN BE_beauty_salon.dbo.Reklamodawca as reklamodawcaSource on reklamaSource.ID_Reklamodawcy = reklamodawcaSource.ID_Reklamodawcy
    JOIN dbo.Reklamodawca as reklamodawcaDW on reklamodawcaDW.NIP = reklamodawcaSource.NIP
    JOIN dbo.Junk as junk on 
        junk.Czy_widzial_reklame = ankieta.adSeen 
        and junk.Czy_przyszla_z_powodu_reklamy = ankieta.adIsCause 
        and (       
            CASE
                WHEN 
                (SELECT COUNT(*) AS [nastepnychWizyt]
                    FROM BE_beauty_salon.dbo.Wizyta w2
                    WHERE wizyta.ID_Klienta = w2.ID_Klienta and wizyta.Data_wizyty < w2.Data_wizyty)
             = 0 then 'nie'
                else 'tak'
            END
        ) = junk.Czy_zarezerwowal_kolejna 
        and (
            CASE
                WHEN wizyta.Kwota < 50 THEN 'Niska'
                WHEN wizyta.Kwota >= 50 and wizyta.Kwota < 150 THEN 'Srednia'
                WHEN wizyta.Kwota >= 150 and wizyta.Kwota < 250 THEN 'Wysoka'
                WHEN wizyta.Kwota >= 250 THEN 'Bardzo Wysoka'
            END
        ) = junk.Kwota_rachunku_przedzial
    

    go

    MERGE INTO Wizyta_w_salonie as TT
	USING EtlVisits as ST
		ON 	TT.ID_Klienta = ST.ID_Klienta
		AND TT.ID_Reklamy = ST.ID_Reklamy
		AND TT.ID_Reklamodawcy = ST.ID_Reklamodawcy
		AND TT.ID_Junk = ST.ID_Junk
		AND TT.Data_Rezerwacji = ST.Data_Rezerwacji
		AND TT.Data_Odwolania = ST.Data_Odwolania
		AND TT.Data_Wizyty = ST.Data_Wizyty
        AND TT.Czy_widziala_reklame = ST.Czy_Widziala_Reklame
        AND TT.Kwota_Rachunku = ST.Kwota_Rachunku
        AND TT.Czy_Przyszla_Z_Powodu_Reklamy = ST.Czy_Przyszla_Z_Powodu_Reklamy
        AND TT.Cena_Pozyskania_Klienta = ST.Cena_Pozyskania_Klienta
        AND TT.Czy_Zarezerwowal_kolejna = ST.Czy_Zarezerwowal_Kolejna
        AND TT.Czy_kupil_zareklamowana_usluge = ST.Czy_Kupil_Zareklamowana_Usluge
			WHEN Not Matched
				THEN
					INSERT
					Values (
						  ST.ID_Klienta
						, ST.ID_Reklamy
						, ST.ID_Reklamodawcy
						, ST.ID_Junk
						, ST.Data_Rezerwacji
						, ST.Data_Odwolania
						, ST.Data_Wizyty
						, ST.Czy_Widziala_Reklame
						, ST.Kwota_Rachunku
						, ST.Czy_Przyszla_Z_Powodu_Reklamy
                        , ST.Cena_Pozyskania_Klienta
                        , ST.Czy_Zarezerwowal_Kolejna
                        , ST.Czy_Kupil_Zareklamowana_Usluge

					)
			;

Drop table dbo.SurveysTemp;
Drop view EtlVisits;