import requests

from bs4 import BeautifulSoup

index = int(input())
link_to_article = input()

r = requests.get(link_to_article)

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
sub_titles = soup.find_all('h2')
print(sub_titles[index].text)

# for sub_title in sub_titles:
#     print(sub_title.text)


