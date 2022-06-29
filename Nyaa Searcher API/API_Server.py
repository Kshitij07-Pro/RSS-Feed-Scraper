from autoscraper import AutoScraper
from flask import Flask, request

scraper = AutoScraper()
scraper.load('Nyaa-search-result.txt')
app = Flask(__name__)

def get_nyaa_result(search_query):
    url = 'https://nyaa.si/?q=%s' % search_query
    result = scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    for i in range(len(list(result.values())[0])):
        final_result.append({alias: result[alias][i] for alias in result})
    return final_result

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    return dict(result=get_nyaa_result(query))

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
