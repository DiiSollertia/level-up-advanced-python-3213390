# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data() -> str:
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt', encoding=str) as file:
        content = file.read()
    return content


def get_rhines_times() -> list:
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    # Let RegEx look ahead by itself
    return re.findall(r"(\d{2}:\d{2}\.?\d*)\s+(?=Jennifer Rhines)", races)


def get_average() -> str:
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()

    def to_dt(race: str) -> datetime.timedelta:
        # A bit hacky, but less error-prone by enforcing typing
        dt = datetime.datetime.strptime(
            race+(".000000"[len(race)-5:]), "%M:%S.%f")
        return datetime.timedelta(
            minutes=dt.minute,
            seconds=dt.second,
            microseconds=dt.microsecond
        )

    deltas = list(map(to_dt, racetimes))
    avg = sum(deltas, datetime.timedelta())/len(deltas)
    # Delay converting time data to str as much as possible
    return str(avg)[2:9]
