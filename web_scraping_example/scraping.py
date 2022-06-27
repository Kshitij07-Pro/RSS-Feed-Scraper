
import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files

# scraping function
def any_rss():

    try:
        feed_url = ''
        r = requests.get(feed_url)
        soup = BeautifulSoup(r.content, 'html')

    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
