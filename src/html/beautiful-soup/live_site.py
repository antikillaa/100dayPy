import pandas as pandas
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
# articles = {text.getText():  text.get("href") for text in soup.find_all(name="a", class_="titlelink")}
# article_upvote = int(soup.find(name="span", class_="score").getText().split(" ")[0])

article_tag = soup.find_all(name="a", class_="titlelink")
article_texts = [text.getText() for text in soup.find_all(name="a", class_="titlelink")]
article_links = [text.get("href") for text in soup.find_all(name="a", class_="titlelink")]
article_up_votes = [text.getText().split()[0] if text.getText().split()[0] else 0 for text in soup.find_all(name="span", class_="score")]

largest_number = max(article_up_votes)
max_up_votes = article_up_votes.index(largest_number)

print(article_texts[max_up_votes], article_links[max_up_votes], article_up_votes[max_up_votes])

print(article_texts)
print(article_links)
print(article_up_votes)

articles = {
    "title": article_texts,
    "link": article_links,
    # "rating": article_up_votes
}

data = pandas.DataFrame(articles)
data.to_html("articles.html", encoding="UTF-8")
data.to_excel("articles.xls", encoding="UTF-8")
