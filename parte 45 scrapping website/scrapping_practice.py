from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.get_text() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)





# with open("pagina.html", "w", encoding="utf-8") as f:
#     f.write(response.text)