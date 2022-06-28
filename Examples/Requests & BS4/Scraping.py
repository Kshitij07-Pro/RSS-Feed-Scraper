import requests # pulling data
from bs4 import BeautifulSoup # xml parsing

# scraping function
def any_rss(URL):

    try:
        feed_url = 'URL'
        response = requests.get(feed_url)
        soup = BeautifulSoup(response.content, 'html')
        print(soup.prettify())
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

any_rss(URL_HERE)
