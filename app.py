import requests
from flask import Flask, render_template, request, jsonify
from summarize import summarize_article, fetch_full_article
from news_fetcher import fetch_news, filter_articles
import os
from dotenv import load_dotenv
import logging
from langchain_community.llms import OpenAI
from flask_cors import CORS

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

logging.basicConfig(level=logging.DEBUG)

ollama_ssh_key_path = os.getenv('OLLAMA_SSH_KEY_PATH')
news_api_key = os.getenv('NEWS_API_KEY')
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')

def initialize_langchain(api_key):
    client = OpenAI(api_key=api_key)
    return client

def check_ollama_api():
    try:
        response = requests.get('http://localhost:11434')
        return response.status_code == 200
    except requests.ConnectionError:
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if not check_ollama_api():
        return jsonify({"error": "Ollama API is not running. Please start it and try again."}), 500

    data = request.json
    preferences = data.get('preferences', [])
    logging.debug(f"Preferences: {preferences}")

    articles = fetch_news(news_api_key)
    logging.debug(f"Fetched Articles: {articles}")

    # Filter articles based on preferences
    filtered_articles = filter_articles(articles, preferences)
    logging.debug(f"Filtered Articles: {filtered_articles}")

    if not filtered_articles:
        return jsonify({"summaries": []})

    summaries = []
    langchain_client = initialize_langchain(langchain_api_key)

    for article in filtered_articles:
        logging.debug(f"Processing article: {article.get('title', 'No title')}")

        if 'content' in article and article['content']:
            content = article['content']
            logging.debug(f"Using content from article: {content[:100]}...")
        elif 'url' in article:
            content = fetch_full_article(article['url'])
            logging.debug(f"Fetched full article content from URL: {content[:100]}...")
        else:
            content = None
            logging.debug("No content or URL available for this article.")

        if content:
            try:
                summary_text = summarize_article(content, langchain_client)
                logging.debug(f"Summary for article '{article.get('title', 'No title')}': {summary_text}")
                summaries.append({
                    'title': article.get('title', 'No title'),
                    'description': summary_text,
                    'image': article.get('urlToImage'),
                    'url': article.get('url')
                })
            except Exception as e:
                logging.error(f"Error summarizing article '{article['title']}': {e}")
                summaries.append({
                    'title': article.get('title', 'No title'),
                    'description': f"Failed to summarize article: {e}",
                    'image': article.get('urlToImage'),
                    'url': article.get('url')
                })
        else:
            summaries.append({
                'title': article.get('title', 'No title'),
                'description': "No content available.",
                'image': article.get('urlToImage'),
                'url': article.get('url')
            })

    logging.debug(f"Generated Summaries: {summaries}")
    logging.debug(f"Number of Summaries: {len(summaries)}")

    return jsonify({"summaries": summaries})


if __name__ == '__main__':
    if check_ollama_api():
        app.run(debug=True, port=5001)
    else:
        print("Ollama API is not running. Please start it and try again.")
