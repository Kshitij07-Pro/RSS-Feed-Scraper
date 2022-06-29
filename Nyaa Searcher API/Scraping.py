# First, we are going to create a smart scraper to fetch data from Nyaa’s search results page.

from autoscraper import AutoScraper

# if you want to have same rule ids for each run
# import random
# random.seed(0)

url = 'https://nyaa.si/?q=Naruto'
wanted_list = ["[YakuboEncodes] Boruto - Naruto Next Generations - 255 [1080p 10bit][x265 HEVC][Multi-Subs]", "https://nyaa.si/download/1547052.torrent", "22", "0", "196.2 MiB"]

scraper = AutoScraper()
scraper.build(url, wanted_list)

scraper.get_result_similar(url, grouped=True)

scraper.set_rule_aliases = ({"rule_c9xn": "Title", "rule_v6ms": "Torrent Link", "rule_gyyj": "Seeders", "rule_v6gu": "Leechers", "rule_n0ey": "Size"})
scraper.keep_rules(['rule_c9xn', 'rule_v6ms', 'rule_gyyj', 'rule_v6gu', 'rule_n0ey'])

# to save data
scraper.save('./Nyaa-search-result.txt')
