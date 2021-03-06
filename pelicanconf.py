#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tim Robinson'
SITENAME = 'Red Green & Blog'
SITEURL = 'https://probinso.github.io/rgb'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://blog.getpelican.com/'),
#    ('Link Two', '#'),
#    ('Link Three', '#'),
#    ('Link Four', '#'),
)

# Social widget
SOCIAL = (
    ('Tim', 'https://www.linkedin.com/in/tim-robinson-95392010/'),
    ('Philip', 'https://twitter.com/timedebtor'),
    ('Philip', 'https://www.linkedin.com/in/philip-robinson-2878642a/')
#    ('Link Two', '#'),
#    ('Link Three', '#'),
#    ('Link Four', '#'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}
