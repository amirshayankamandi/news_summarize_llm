import requests
import logging

def fetch_news(api_key, page_size=100):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}&pageSize={page_size}"
    logging.debug(f"Fetching news from: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.debug("Fetched data: %s", data)
        return data.get('articles', [])
    else:
        logging.error("Failed to fetch news")
        return []


def filter_articles(articles, preferences):
    # If no preferences are provided, return all articles
    if not preferences:
        return articles

    # Separate articles into those that match preferences and those that don't
    matched_articles = []
    non_matched_articles = []

    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')

        title = title.lower() if title else ''
        description = description.lower() if description else ''

        if any(pref.lower() in title or pref.lower() in description for pref in preferences):
            matched_articles.append(article)
        else:
            non_matched_articles.append(article)

    # Return both matched and non-matched articles
    return matched_articles + non_matched_articles

