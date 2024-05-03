import requests
cache = dict()
def get_server_article(url):
    print("Fetching article from server")
    response = requests.get(url)
    print(response)
    return response.text

def get_article_from_cache(url):
    print('Getting article')
    if url not in cache:
        cache[url] = get_server_article(url)
    return cache[url]
get_article_from_cache('https://economictimes.indiatimes.com/?from=mdr')