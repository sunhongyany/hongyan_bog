#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sunhongyan'
SITE_DESCRIPTION = u'Stay hungry, stay foolish'
SITENAME = u'梦与想'
SITEURL = ''

DEFAULT_PAGINATION = 3
PATH = 'content'

STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Asia/Shanghai'
THEME = "maupassant-pelican"

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
MENUITEMS = [
    ('首页', '/', 'fa-home'),
    ('文章归档', '/archives.html', 'fa-archive'),
]

# 插件目录
PLUGIN_PATHS = [u"pelican-plugins"]

YEAR_ARCHIVE_SAVE_AS = 'pages/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'pages/{date:%Y}/{date:%b}/index.html'
