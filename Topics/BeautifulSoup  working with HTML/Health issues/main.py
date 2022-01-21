import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
output_list = list()
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

hyper_links = soup.find_all('a')
# print(hyper_links[1])
for link in hyper_links:
    if len(link.text) > 1 and link.text.startswith(letter) and ("entity" in link.get('href') or "topics" in link.get('href')):
        output_list.append(link.text)
print(output_list)
