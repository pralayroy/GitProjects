#from dateTime.dateFormat import DateFormat
from dateTime.dateFormat import convert_date


class Date:
    #conv = DateFormat.conver_date()

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        #self.day = DateFormat.convert_date(day)
        #self.month = DateFormat.convert_date(m)
        #self.year = DateFormat.convert_date()


monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def countLeaperYear(day):
    years = day.year
    if day.month <= 1:
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)


def getDaysCount(date1, date2):
    n1 = date1.year * 365 + date1.day
    for i in range(0, date1.month - 1):
        n1 += monthDays[i]
    n1 += countLeaperYear(date1)

    n2 = date2.year * 365 + date2.day
    for i in range(0, date2.month - 1):
        n2 += monthDays[i]
    n2 += countLeaperYear(date2)
    return n2 - n1


date1 = input("Start date: ")
date11 = convert_date(date1)
date2 = input("End date: ")
date22 = convert_date(date2)
#date1 = Date.convert_date('Dec 13 2018')
#date2 = Date.convert_date('Feb 25 2019')
print(getDaysCount(date11, date22), "days")
