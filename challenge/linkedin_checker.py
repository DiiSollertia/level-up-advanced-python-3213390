from collections import namedtuple
import re

with open('specifications.txt', 'rt', encoding='utf') as file:
    specifications = file.read()

specs = namedtuple('specs', 'range regex')
# specs range builtin module
# specs regex from re.compile


def get_linkedin_dict():
    '''Convert specifications into a dict where:
       keys: feature
       values: specs namedtuple'''
    output = {}
    for line in specifications.splitlines():
        if line.startswith('feature:'):
            feature = re.match(r"feature: (\S+)", line)[1]
        elif 'requirements:' in line:
            req = re.findall(r"\d+", line)
            rng = range(int(req[0]), int(req[1])+1)
        elif 'characters:' in line:
            # Shouldn't have to check mode at this point
            char = re.findall(r"\S+", line)
            pattern = '['+''.join(char[2:])+']+'
            regex = re.compile(pattern)
        elif not line:
            output[feature] = specs(rng, regex)
    return output


ref = get_linkedin_dict()


def check_linkedin_feature(feature_text, url_or_login) -> bool:
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
    if url_or_login == 'custom_url':
        regex = re.compile(ref[url_or_login].regex.pattern + '$')
    elif url_or_login == 'login':
        pattern = ref[url_or_login].regex.pattern
        regex = re.compile(f"{pattern}@{pattern}(net|com|org)$")
    else:
        raise ValueError('Feature needs to be either login or custom_url')
    char = regex.match(feature_text)
    length = len(feature_text) in ref[url_or_login].range
    # Double check in case there is gibberish at the start of feature_text
    return length and char is not None and (len(char[0]) == len(feature_text))
