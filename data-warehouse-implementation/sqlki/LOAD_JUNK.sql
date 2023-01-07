USE beauty_salon
GO

INSERT INTO [dbo].[Junk] 
SELECT s, p, q, r
FROM 
	  (
		VALUES 
			  ('Niska')
			, ('Srednia')
			, ('Wysoka')
			, ('Bardzo Wysoka')
	  ) 
	AS Kwota_rachunku(s)
	
	, (
		VALUES 
			  ('tak')
			, ('nie')
	  ) 
	AS Czy_widzial_reklame(p)
	
	, (
		VALUES 
			  ('tak')
			, ('nie')
	  ) 
	AS Czy_zarezerwowal_kolejna(q)

	, (
		VALUES 
			  ('tak')
			, ('nie')
	  ) 
	AS Czy_przyszla_z_powodu_reklamy(r);

	SELECT * from Junk