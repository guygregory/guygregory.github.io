AUTHOR = 'Guy Gregory'
SITENAME = 'Pedantic Journal'
SITESUBTITLE = 'Thoughts on AI and other subjects.'
SITEURL = "https://pedanticjournal.com"

MENUITEMS = [
    ('Home', '/'),
    ('About', '/about.html'),
]

PATH = "content"
OUTPUT_PATH = 'docs/'

PAGE_PATHS = ['pages']


# Clean URLs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

THEME = 'pelican-themes/octopress'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://linkedin.com/in/guygregory"),
    ("GitHub", "https://github.com/guygregory"),
    ("X", "https://x.com/guygregory"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
