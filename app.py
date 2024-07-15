from flask import Flask, render_template, request
from news_fetcher import fetch_news, filter_articles
from summarizer import summarize_article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

@app.route('/summarize', methods=['POST'])
def summarize():
    preferences = request.form.getlist('preferences')
    articles = fetch_news('YOUR_NEWS_API_KEY')
    filtered_articles = filter_articles(articles, preferences)
    summaries = [summarize_article(article['content']) for article in filtered_articles]
    return render_template('summary.html', summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)
