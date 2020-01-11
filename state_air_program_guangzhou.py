# -*- coding: utf-8 -*-
"""State Air Program Guangzhou

Import required model
"""

# !pip install feedparser
import feedparser

"""Interpret raw sources"""

rss_url = 'http://www.stateair.net/web/rss/1/3.xml'
rss = feedparser.parse(rss_url)
rss

"""Cleaning"""

# 抓取標題
print(rss['entries'][0]['title'])
print(rss.entries[0]['link'])
# 抓取摘要
print(rss.entries[0]['summary'])