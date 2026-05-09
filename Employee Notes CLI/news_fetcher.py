import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_legal_ai_news(query="AI law legal technology", page_size=10):
    try:
        response = requests.get(
            BASE_URL,
            params={
                "q": query,
                "sortBy": "publishedAt",
                "pageSize": page_size,
                "apiKey": API_KEY,
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("articles", [])
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"HTTP error: {e.response.status_code}")
        return []
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request failed: {e}")
        return []

def display_articles(articles):
    if not articles:
        print(Fore.YELLOW + "No articles found.")
        return

    table_data = [
        [
            article.get("source", {}).get("name", "Unknown"),
            article.get("title", "No title")[:60] + "...",
            article.get("publishedAt", "")[:10]
        ]
        for article in articles
    ]

    headers = ["Source", "Title", "Date"]
    print(Fore.CYAN + tabulate(table_data, headers=headers, tablefmt="grid"))

def save_articles(articles, filename="legal_ai_news.json"):
    try:
        with open(filename, "w") as f:
            json.dump(articles, f, indent=2)
        print(Fore.GREEN + f"Saved {len(articles)} articles to {filename}")
    except IOError as e:
        print(Fore.RED + f"Error saving articles: {e}")

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "Fetching Legal AI News...\n")
    articles = fetch_legal_ai_news()
    display_articles(articles)
    save_articles(articles)

