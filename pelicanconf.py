AUTHOR = 'Guy Gregory'
SITENAME = 'Pedantic Journal'
SITESUBTITLE = 'Thoughts on AI and other subjects.'
SITEURL = "https://pedanticjournal.com"

MENUITEMS = [
    ('Home', '/'),
    ('About', '/about.html'),
    ('Atom', '/atom.html'),
]

PATH = "content"
OUTPUT_PATH = 'docs/'

PAGE_PATHS = ['pages']

STATIC_PATHS = ['images']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
}

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
    ("Azure AI Foundry Blog", "https://devblogs.microsoft.com/foundry/"),
    ("Microsoft Azure Blog", "https://azure.microsoft.com/blog/"),
    ("Microsoft UK Stories", "https://ukstories.microsoft.com/"),
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
