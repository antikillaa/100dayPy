from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

anchor_tag = soup.find_all(name="a")

for tag in anchor_tag:
    # print(tag.getText())
    print(tag.get("href"))
heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
# print(soup.prettify())

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select(selector="#name")
print(name)

heading = soup.select(selector=".heading")
print(heading)