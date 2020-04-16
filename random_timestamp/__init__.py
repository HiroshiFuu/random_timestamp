__title__ = 'random_timestamp'
__version__ = '1.0.0'
__author__ = "FENG Hao"
__license__ = 'GPL v3.0'


from random import randint
from datetime import timedelta as td, datetime as dt, date, time
import calendar as cal


# Function which generates random datetime object
def generate_datetime(date):
    hour = randint(0, 23)
    minute = randint(0, 59)
    second = randint(0, 59)
    tm = time(hour, minute, second)
    return dt.combine(date, tm)


# Function which for users to access
def random_timestamp(year=None, month=None, day=None, part=None):
    if part == 'TIME':
        return generate_datetime(dt.now().date()).time()
    else:
        try:
            year = int(year)
            year = (1900, year)[year >= 1900]
        except:
            year = randint(1900, int(dt.now().year))

        try:
            month = int(month)
            month = (1, month)[(month >= 1) & (month <= 12)]
        except:
            month = randint(1, 12)

        try:
            day = int(day)
            day = (1, day)[(day >= 1) & (day <= 31)]
            if day > cal.monthrange(year, month)[1]:
                day = int('error')
        except:
            day = randint(1, cal.monthrange(year, month)[1])

        use_date = None
        if date(year, month, day) < dt.now().date():
            use_date = date(year, month, day)
        else:
            use_date = dt.now().date()

        if part == 'DATE':
            return use_date
        else:
            return generate_datetime(use_date)