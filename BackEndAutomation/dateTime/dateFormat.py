
from datetime import datetime



allowed_formats = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y', '%b %d %Y']



def convert_date(string):
    for formatted in allowed_formats:
        try:
            return datetime.strptime(string, formatted)
        except ValueError:
            pass
    return convert_date()



