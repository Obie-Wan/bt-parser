import logging
logging.basicConfig(level=logging.INFO)

import smf_feed 

FORUM_PREFIX = 'https://bitcointalk.org/index.php?board=159.0'

smf_feed.SMFFeed.load("Forum Recent Posts",
                 '{}&action=recent'.format(FORUM_PREFIX),
                 'Recent posts for Forum',
                 'smf.xml', 
		 'smf.pickle',
 		 maxItems = 400)