#!/usr/bin/env python

from bs4 import BeautifulSoup
from PyRSS2Gen import RSSItem, Guid
from ScrapeNFeed import ScrapedFeed # See: http://www.crummy.com/software/ScrapeNFeed/
import parsedatetime.parsedatetime as pdt

import logging
from datetime import datetime
from time import mktime

class SMFFeed(ScrapedFeed):  
	def HTML2RSS(self, headers, body):
		soup = BeautifulSoup(body, 'html.parser')
		items = []
		for item in soup.find_all("tr", "titlebg2"):
			a = item.find_all("a")[-1]
			#topic_details = item.find("div", "topic_details")
			#author = topic_details.find("strong").a.text
			#a = topic_details.find("h5").find_all("a")[1]
			link = a['href']
			subject = a.text

			if 'ICO' not in subject:
				continue
			logging.info(subject)

			rss = RSSItem(author = 'x',
				title = subject,
				link = link,
				pubDate = '',
				guid = Guid(link),
				description = '')
			items.append(rss)
		self.addRSSItems(items)

