from datetime import datetime

# Here we can support date format according to the user requirement
# such as yyyy-mm-dd, yyyy/mm/dd, dd.mm.yyyy and month day year (Jan 20 2018)
allowed_formats = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y', '%b %d %Y']


class Configuration:
    # Class variable to calculate no of days in month of Jan to Dec
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Converting user entered date to day , month and year
    def convert_date(string):
        for formatted in allowed_formats:
            try:
                return datetime.strptime(string, formatted)
            except ValueError:
                pass

# Checking year is leaper or not
    def countLeaperYear(day):
        years = day.year
        if day.month <= 1:
            years -= 1
        return int(years / 4) - int(years / 100) + int(years / 400)





