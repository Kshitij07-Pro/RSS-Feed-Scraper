# Scraping https://news.ycombinator.com/rss

import requests
from bs4 import BeautifulSoup
import json

# declare empty var to append data
article_list = []

# save function
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)

# scraping function
def hackernews_rss():
    try:
        r = requests.get('https://news.ycombinator.com/rss')
        # return print(r.status_code) # Use this cmd to check if you're able to ping the site. 200 is OK, 404 is Not Found
        soup = BeautifulSoup(r.content, features='xml')

        articles = soup.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            pubDate = a.find('pubDate').text

            article = {
                'Title':title,
                'Link':link,
                'Published':pubDate
                }

            article_list.append(article)
        return save_function(article_list)

    except Exception as e:
            print('The scraping job failed. See exception:')
            print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')
