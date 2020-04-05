from datetime import datetime
from pathlib  import Path
import yaml

import nbformat as nbf

CONTENTDIR = Path('./content')

struct = {}
struct['Title'] = input('Title: ')
struct['Slug'] = ''.join(filter(lambda s: str.isalnum(s) or s == '-', struct['Title'].lower().strip().replace(' ', '-')))
struct['Date'] = datetime.now().strftime('%Y/%m/%d %H:%M')
struct['Category'] = 'posts'
struct['author'] = input('Who is the author? ')
struct['Summary'] = input('Summary of post: ')

with open(CONTENTDIR / (struct['Slug'] + '.nbdata'), 'w') as fd:
    yaml.dump(struct, fd)

nb = nbf.v4.new_notebook()
nbf.write(nb, CONTENTDIR / (struct['Slug'] + '.ipynb'))
