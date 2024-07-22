import requests
from bs4 import BeautifulSoup

def fetch_full_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        full_text = ' '.join([para.get_text() for para in paragraphs])
        return full_text
    else:
        return None

def summarize_article(content, client):
    try:
        response = client.Completions.create(
            model="text-davinci-003",  # Adjust model if needed
            prompt=f"Summarize this text:\n\n{content}",
            max_tokens=150  # Adjust based on your needs
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Failed to summarize due to unexpected error: {e}"
