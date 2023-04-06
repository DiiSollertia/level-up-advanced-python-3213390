# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import datetime
import re
from challenge.average_race_time import to_dt


def get_data() -> str:
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


# Don't really like the requirements of these 2 func
def get_event_time(line: str) -> tuple:
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    dates = re.findall(r"\d\d [A-Z][a-z]{2} \d{4}", line)
    race = re.match(r"\s{2,}(\d\d:\d\d\.?\d*)", line)[1]
    race_dt = datetime.datetime.strptime(dates[0], "%d %b %Y")
    birth_dt = datetime.datetime.strptime(dates[1], "%d %b %Y")
    age_sec = (race_dt - birth_dt).total_seconds()
    return (age_sec, race)


def get_age_slowest_times() -> tuple:
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    s_per_yr = 365.25*24*60*60
    slowest = (0, 0)
    race_slow = datetime.timedelta()
    for line in races.splitlines():
        if "Jennifer Rhines" in line:
            age_sec, race = get_event_time(line)
            race_t = to_dt(race)
            if race_t > race_slow:
                race_slow = race_t
                slowest = (age_sec, race)
    age_str = f"{int(slowest[0]//s_per_yr)}y{int(slowest[0]%s_per_yr//(s_per_yr/365.25))}d"
    return (age_str, slowest[1])
