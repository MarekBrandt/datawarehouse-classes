create DATABASE SalonBeauty
GO

USE SalonBeauty
GO

CREATE TABLE Produkt
(
    ID_Produktu INTEGER PRIMARY KEY,
	Nazwa varchar(100),
	Marka varchar(20),
	Typ varchar(50),
	Cena_sprzedazy float,
)
GO

CREATE TABLE Klient
(
    ID_Klienta INTEGER PRIMARY KEY,
	Imie varchar(20),
	Nazwisko varchar(50),
	Rok_urodzenia integer,
)
GO

CREATE TABLE Reklamodawca
(
	ID_Reklamodawcy int primary key,
	Adres_mailowy varchar(100) check (Adres_mailowy like '%@%'),
	Nazwa varchar(100),
	NIP char(10),
	Specjalizacja varchar(20),
	Glowna_tematyka varchar(50),
)
GO

CREATE TABLE Salon
(
	ID_Salonu integer primary key,
	Miasto varchar(20),
	Ulica varchar(20),
	Numer_budynku integer,
	Numer_telefonu varchar(11),
)
GO

CREATE TABLE Usluga
(
	ID_Uslugi integer primary key,
	Nazwa varchar(20),
	Cena float,
)
GO

CREATE TABLE Reklama
(
	ID_Reklamy integer primary key,
	ID_Uslugi integer references Usluga,
	ID_Salonu integer not null references Salon,
	ID_Reklamodawcy integer not null references Reklamodawca,
	Typ varchar(20),
	Cena float,
)
GO

CREATE TABLE Wizyta
(
	ID_Wizyty integer primary key,
	ID_Salonu integer not null references Salon,
	ID_Klienta integer not null references Klient,
	Data_rezerwacji date,
	Data_wizyty date,
	Data_odwolania date,
	Kwota float,
)
GO

CREATE TABLE Produkt_ilosc
(
	ID_Wizyty integer not null references Wizyta,
	ID_Produktu integer not null references Produkt,
	Ilosc integer,
	primary key(ID_Wizyty, ID_Produktu),
)
GO

CREATE TABLE Usluga_wizyta
(
	ID_Uslugi integer not null references Usluga,
	ID_Wizyty integer not null references Wizyta,
	primary key (ID_Uslugi, ID_Wizyty),
)
GO