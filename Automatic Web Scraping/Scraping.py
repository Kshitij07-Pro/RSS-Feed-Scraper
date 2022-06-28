from autoscraper import AutoScraper

url = 'https://www.analyticsvidhya.com/blog/category/machine-learning/'
wanted_list = ['Confusion Matrix: Detailed intuition and trick to learn']
scraper = AutoScraper()

proxies = {
    "http": 'http://127.0.0.1:8001',
    "https": 'https://127.0.0.1:8001',
}

result = scraper.build(url, wanted_list, request_args=dict(proxies=proxies))
print(result)

# scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
# scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/')

# to save the model
scraper.save('blogs')
# to lead the model
acraper.load('blogs')
