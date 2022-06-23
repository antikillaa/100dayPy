import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
data = requests.get(URL)
soup = BeautifulSoup(data.text, "html.parser")
titles = [item.getText() for item in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open("cinema_list.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")

