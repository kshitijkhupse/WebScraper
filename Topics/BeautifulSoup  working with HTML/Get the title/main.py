import requests

from bs4 import BeautifulSoup

link = input()

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
heading = soup.find('h1')

print(heading.text)
