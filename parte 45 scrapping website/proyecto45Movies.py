from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.get_text() for movie in all_movies]

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in reversed(movie_titles):
        file.write(f"{title}\n")
        print(title)