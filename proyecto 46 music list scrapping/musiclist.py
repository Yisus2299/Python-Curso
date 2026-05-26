from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

all_music_list = soup.find_all(name="h3", class_="chart-entry__title")
music_titles = [music.get_text() for music in all_music_list]

with open("musiclist.txt", "w", encoding="utf-8") as file:
    for title in music_titles:
        file.write(f"{title}\n")
        print(title)

print(music_titles)