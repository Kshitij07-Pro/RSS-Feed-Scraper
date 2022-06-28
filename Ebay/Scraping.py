from autoscraper import AutoScraper

url = ''
wanted_list = []

scraper = AutoScraper()
result = scraper.bluid(url, wanted_list)
print(result)
