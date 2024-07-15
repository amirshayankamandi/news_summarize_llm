import requests

api_key = '5c511d0e34304b92b5767903360b1016'

def fetch_news(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json()['articles']

def filter_articles(articles, preferences):
    filtered = []
    for article in articles:
        if 'title' in article and any(pref.lower() in article['title'].lower() for pref in preferences):
            filtered.append(article)
    return filtered
