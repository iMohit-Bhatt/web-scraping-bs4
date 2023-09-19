from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
result = response.text

soup = BeautifulSoup(result, "html.parser")
anchor_tags = soup.select(".titleline a")
all_score = soup.select(".score")

articles = []
article_link = []
article_score = []

for tag in anchor_tags:
    articles.append(tag.get_text())
    article_link.append(tag["href"])

for score in all_score:
    score = score.getText().split(" ")
    article_score.append(int(score[0]))

# print(articles)
# print(article_link)
# print(article_score)

max_score_index = article_score.index(max(article_score))

print(f'''
    Title: {articles[max_score_index]}
    Link: {article_link[max_score_index]}
    Upvotes: {article_score[max_score_index]}
''')

# with open("index.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.h1)

# all_anchor_tag = soup.find_all(name="a")

# for tags in all_anchor_tag:
#     print(tags.getText())