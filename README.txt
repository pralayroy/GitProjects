# GitProjects
How Days calculation program works:
-------------------------------------
1. Taken start date and end date as user input. Date formats currently supporting as follows yyyy-mm-dd, yyyy/mm/dd, dd.mm.yyyy and month day year (Jan 20 2018)
Note: We can support other date format as per the user requirement.
2. Then converting the given dates to day, month and year.
3. Checking leaper year if user input year is leaper. If yes, then adding a day to that year
4. Now calculating the start date days and similar way for end date days.
5. As this calculation will take O(n) time complexity so we need to do memorization of that function.
Once we memorize a function, it will only compute its output once for each set of parameters you call it with. Every call after the first will be quickly retrieved from a cache.
6. If end date is not greater than start date then it will print days in negative value.
7. If end date equals to start date then it will give 0 days.

How to run the program:
-------------------------
1. Using pyCharm you can import the package called "CalculateNoOfDays" then right click on "countNoOfDaysBetweenTheDates.py" and run the file.
    a. After running the file it will ask two input from user one is Start Date and second is End Date. (Follow the date format)
	b. Hit the enter button after giving all the inputs. Now you can see total number of days in between the given dates.
