from ollama import LLM

def summarize_article(article_text):
    llm = LLM(api_key='SHA256:NPgfBvkuZSXVbGyjMZdPBDGa2AhQSjgs+SGmxrezK0E')
    summary = llm.summarize(article_text)
    return summary

