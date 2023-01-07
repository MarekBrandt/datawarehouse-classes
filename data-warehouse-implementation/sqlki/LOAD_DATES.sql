use beauty_salon
go

-- Fill DimDates Lookup Table
-- Step a: Declare variables use in processing
Declare @StartDate date; 
Declare @EndDate date;

-- Step b:  Fill the variable with values for the range of years needed
SELECT @StartDate = '2015-01-01', @EndDate = '2020-12-31';

-- Step c:  Use a while loop to add dates to the table
Declare @DateInProcess datetime = @StartDate;

SET LANGUAGE Polish;
While @DateInProcess <= @EndDate
	Begin
	--Add a row into the date dimension table for this date
		Insert Into [dbo].[Data_] 
		( [ID_Data]
		, [Rok]
		, [Miesiac]
		, [Dzien]
		)
		Values ( 
		  @DateInProcess -- [Date]
		  , Cast( Year(@DateInProcess) as varchar(4)) -- [Year]
		  , Cast( DATENAME(month, @DateInProcess) as varchar(10)) -- [Month]
		  , Cast( DATEPART(dd, @DateInProcess) as int) -- [DayOfMonth]
		);  
		-- Add a day and loop again
		Set @DateInProcess = DateAdd(d, 1, @DateInProcess);
	End
go
Insert into [dbo].[Data_](
        [ID_Data]
        , [Rok]
        , [Miesiac]
        , [Dzien]
        )
        Values ( 
            '1000-1-1'
          , '1000'
          , 'styczeń' -- [Month]
          , 1 -- [DayOfMonth]
        );
SELECT * FROM Data_