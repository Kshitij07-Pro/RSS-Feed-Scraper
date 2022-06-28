# Scraping https://news.ycombinator.com/rss

import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files



# scraping function
def hackernews_rss():
    try:
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://news.ycombinator.com/rss')
        return print('The scraping job succeeded: ', r.status_code) # 200 is OK, 404 is Not Found
    except Exception as e:
            print('The scraping job failed. See exception:')
            print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')
