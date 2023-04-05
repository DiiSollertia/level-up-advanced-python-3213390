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
    return re.findall(r"(\d{2}:\d{2}\.?\d*)\s+(?=Jennifer Rhines)", races)


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()

    def to_dt(times):
        dt = datetime.datetime.strptime(
            times+(".000000"[len(times)-5:]), "%M:%S.%f")
        return datetime.timedelta(
            minutes=dt.minute,
            seconds=dt.second,
            microseconds=dt.microsecond
        )

    deltas = list(map(to_dt, racetimes))
    avg = sum(deltas, datetime.timedelta())/len(deltas)
    return str(avg)[2:9]
