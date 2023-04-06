from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
                             'Event', 'Event_gender', 'Medal'])

# Complete this - medals is a list of medal namedtuples
medals = [medal(*line.split(';')) for line in olympics.splitlines()[1:]]


def get_medals(**kwargs) -> list:
    '''Return a list of medal namedtuples '''
    return [m for m in medals if all(v == getattr(m, k) for k, v in kwargs.items())]
