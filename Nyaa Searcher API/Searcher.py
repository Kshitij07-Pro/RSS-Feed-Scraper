# First, we are going to create a smart scraper to fetch data from Nyaa’s search results page.

from autoscraper import AutoScraper

# if you want to have same rule ids for each run
# import random
# random.seed(0)

url = 'https://nyaa.si//?page=rss&q=Naruto'
wanted_dict = {
    'Title': [

    ],
    'Link': ['https://nyaa.si/download/1547019.torrent'],
    'Size': ['196.2 MiB']
}

scraper = AutoScraper()

scraper.build(url=url, wanter_dict=wanted_dict)

# scraper.get_result_exact(url, grouped=True)
scraper.get_result_similar(url, grouped=True)

scraper.keep_rules(['rule_xxxx', 'rule_xxyy', 'rule_yyyy'])

# to save data
scraper.save('path')





Sources:
https://gist.github.com/alirezamika/72083221891eecd991bbc0a2a2467673
https://betterprogramming.pub/autoscraper-and-flask-create-an-api-from-any-website-in-less-than-5-minutes-3f0f176fc4a3
