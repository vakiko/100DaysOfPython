from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.prettify())
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

section_heading = soup.find(name="h3", class_="heading")

test = soup.select("ul li")
print(test)