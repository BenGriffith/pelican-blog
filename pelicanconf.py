AUTHOR = 'Ben Griffith'
SITENAME = 'My Pelican Blog'
SITEURL = ''

MENUITEMS = [
    ('Home', '/'),
    ('Posts', '/archives.html')
]

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

THEME = 'themes/basic'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

DEFAULT_PAGINATION = 5