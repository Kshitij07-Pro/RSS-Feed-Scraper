from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# You can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ['A What are metaclasses in Python?']

scraper = AutoScraper()

result_1 = scraper.build(url, wanted_list)
print(result_1)

# to get related topics of any stackoverflow page
result_2 = scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
print(result_2)

result_3 = scraper.get_result_exact('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
print(result_3)

# to save
scraper.save('file_path')

# to load
scraper.load('file_path')

# learn more https://gist.github.com/alirezamika/72083221891eecd991bbc0a2a2467673
