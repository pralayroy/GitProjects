from utilities.BaseClass import Configuration
from utilities.memorization import memoize



# Inheriting the base class
class DateFunction(Configuration):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


# Here is the main function  to calculate start date and end date days
def getDaysCount(startDate, endDate):
    startDateDays = startDate.year * 365 + startDate.day
    for i in range(0, startDate.month - 1):
        startDateDays += DateFunction.monthDays[i]
    startDateDays += DateFunction.countLeaperYear(startDate)

    endDateDays = endDate.year * 365 + endDate.day
    for i in range(0, endDate.month - 1):
        endDateDays += DateFunction.monthDays[i]
    endDateDays += DateFunction.countLeaperYear(endDate)
    return endDateDays - startDateDays


if __name__ == "__main__":
    date1 = input("Enter the start date[supported format yyyy-mm-dd, yyyy/mm/dd, dd.mm.yyyy and month day year (Jan 20 "
                  "2018)]: ")
    startDate = DateFunction.convert_date(date1)
    date2 = input("Enter the end date[supported format yyyy-mm-dd, yyyy/mm/dd, dd.mm.yyyy and month day year (Jan 20 "
                  "2018)]: ")
    endDate = DateFunction.convert_date(date2)
    # Here is the memorization decorator as this calculation will take O(n) time complexity
    memorized_func = memoize(getDaysCount)
    print("Number of days between the Start Date and End Date is:", memorized_func(startDate, endDate))
