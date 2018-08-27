#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import feedparser

url = "http://feeds.bbci.co.uk/japanese/rss.xml"
feeds = feedparser.parse(url)
title = feeds['feed'].get('title').encode('utf-8')

print(title)

file = codecs.open("test.txt", "w", "utf-8")
file.write(str(title))
file.close()