#!/usr/bin/env python

from bs4 import BeautifulSoup
from PyRSS2Gen import RSSItem, Guid
from ScrapeNFeed import ScrapedFeed # See: http://www.crummy.com/software/ScrapeNFeed/
import parsedatetime.parsedatetime as pdt

from datetime import datetime
from time import mktime

class SMFFeed(ScrapedFeed):    
	def HTML2RSS(self, headers, body):
		soup = BeautifulSoup(body)
		items = []
		for item in soup.find_all("div", "core_posts"):
			post = item.find("div", "list_posts")
			topic_details = item.find("div", "topic_details")
			author = topic_details.find("strong").a.text
			a = topic_details.find("h5").find_all("a")[1]
			link = a['href']
			subject = a.text
			dateString = topic_details.find("em").text
			try:
				parsed = pdt.Calendar().parse(dateString)
				dt = datetime(*parsed[0][:6])
			except:
				dt = datetime.now()

			print('{}'.format(subject))
			rss = RSSItem(author = author,
			  	      title = subject,
				      link = link,
				      pubDate = dt,
				      guid = Guid(link),
				      description = post)
			items.append(rss)
		self.addRSSItems(items)

