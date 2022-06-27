
import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files

# scraping function
def any_rss():

    try:
        URL = ''
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html')
        print(soup.prettify())
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
