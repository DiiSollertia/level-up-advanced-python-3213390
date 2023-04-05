import re


def html2markdown(html):
    '''Take in html text as input and return markdown'''
    # This isn't just a dictionary, it's a lexicon!
    html2md = {
        r"<em>(.+?)</em>": r"*\1*",
        r"\s+": r" ",
        r"(?<=<p>)(.*?</p>?)(?=.*?<p>)": r"\1\n\n",
        r"</?p>": r"",
        r'<a href="(\S+?)">(.+?)</a>': r"[\2](\1)"
    }
    for key, values in html2md.items():
        html = re.compile(key).sub(values, html)
    return html
