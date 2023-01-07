use master
GO
Drop database if exists beauty_salon
create database beauty_salon
GO
use beauty_salon
GO
create table Reklamodawca(
	ID_Reklamodawcy INTEGER PRIMARY KEY IDENTITY,
	Nazwa varchar(50),
	NIP varchar(10),
	Specjalizacja varchar(30),
	Glowna_tematyka varchar(30),
	jestAktualne integer,
)

create table Reklama(
	ID_Reklamy INTEGER PRIMARY KEY IDENTITY,
	Typ varchar(19),
	Rodzaj varchar(6),
	Ocena varchar(7),
)

create table Data_(
	ID_Data date PRIMARY KEY,
	Rok integer check(Rok between 1000 and 9999),
	Miesiac varchar(11),
	Dzien integer check(Dzien between 1 and 31),
)

create table Klient(
    ID_Klienta INTEGER PRIMARY KEY IDENTITY,
    Imie_i_nazwisko varchar(100),
)

create table Junk(
    ID_Junk INTEGER PRIMARY KEY IDENTITY,
    Kwota_rachunku_przedzial varchar(14),
    Czy_widzial_reklame varchar(3),
    Czy_zarezerwowal_kolejna varchar(3),
    Czy_przyszla_z_powodu_reklamy varchar(3)
)

create table Wizyta_w_salonie(
	ID_Wizyty integer PRIMARY KEY IDENTITY,
    ID_Klienta integer references Klient,
    ID_Reklamy integer references Reklama,
    ID_Reklamodawcy integer references Reklamodawca,
    ID_Junk integer references Junk,
    Data_Rezerwacji date references Data_,
    Data_Odwolania date references Data_,
    Data_Wizyty date references Data_,
    Czy_widziala_reklame integer,
    Kwota_Rachunku float,
    Czy_Przyszla_Z_Powodu_Reklamy integer,
    Cena_Pozyskania_Klienta float,
    Czy_Zarezerwowal_kolejna integer,
    Czy_kupil_zareklamowana_usluge integer
)

