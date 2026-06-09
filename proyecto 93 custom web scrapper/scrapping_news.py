import csv
import requests
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "news.csv"

url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
scores = soup.find_all(name="span", class_="score")

rows = []
for i, article_tag in enumerate(articles):
    title = article_tag.get_text()
    link = article_tag.get("href")
    score = scores[i].get_text() if i < len(scores) else "0 points"
    rows.append([title, link, score])

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "link", "score"])
    writer.writerows(rows)

print(f"CSV creado: {csv_path}")