import requests
from datetime import datetime, timedelta, timezone

query = input("What type of news are you interested in today? ").strip()
api = "5791813a44454e9786cc94639bcc9f9c"

if not query:
    print("Please enter a keyword for the news topic.")
    raise SystemExit(1)

from_date = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d")
url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)
data = r.json()

if data.get("status") != "ok":
    print("API Error:", data.get("message", "Unknown error"))
    raise SystemExit(1)

articles = data.get("articles", [])

if not articles:
    print("No articles found for this keyword.")
    raise SystemExit(0)

for index, article in enumerate(articles, start=1):
    title = article.get("title", "No title")
    url = article.get("url", "")
    print(index, title, url)
    print("\n****************************************\n")
