# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    return re.findall(r"(\d{2}:\d{2}\.?\d*)\s+(?=Jennifer Rhines)", races, re.MULTILINE)


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()

    def readfunc(times):
        _ = datetime.datetime.strptime(times+(".000000"[len(times)-5:]), "%M:%S.%f")
        return datetime.timedelta(
            minutes=_.minute,
            seconds=_.second,
            microseconds=_.microsecond
        )

    convertedtimes = list(map(readfunc, racetimes))
    avg = sum(convertedtimes, datetime.timedelta())/len(convertedtimes)
    return str(avg)[2:9]
