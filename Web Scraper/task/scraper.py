import requests
from bs4 import BeautifulSoup
import string
import os

punctuation = string.punctuation
articles = list()
new_text = ""
article_teaser = ['News & Views', 'Correspondence']
c_article_body = ['Nature Podcast', 'News', 'News Feature', 'Book Review', 'Books & Arts']
article_section = ['Article', 'Author Correction']

def get_user_input():
    no_of_pages = int(input())
    article_type = input()
    return no_of_pages, article_type


def get_quotes(url1):
    r = requests.get(url1, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r


def get_source_content(inp_url):
    pc = requests.get(inp_url)
    return pc


def parse_article_data(request_data, a_type_2_search):
    global new_text
    global dir_name
    soup = BeautifulSoup(request_data.content, 'html.parser')
    news_article_links = soup.find_all('span', {'class': 'c-meta__type'}, text=a_type_2_search)  # replace <article_type>
    # print("No of articles: ", len(news_article_links))
    for news_article in news_article_links:
        anchor = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
        # description = news_article.find_parent('article').find('div', {'itemprop': 'description'})
        # print(anchor.text)
        article_name = anchor.text
        # print(anchor.get('href'))
        article_url = "https://www.nature.com" + anchor.get('href')
        article_content = get_source_content(article_url)
        soup1 = BeautifulSoup(article_content.content, 'html.parser')

        # article_body = soup1.find('div', {'class': 'c-article-body'})
        # News & Views, Correspondence = article__teaser;
        # Nature Podcast, News, News Feature, Book Review, Books & Arts = c-article-body;
        # Article, Author Correction = c-article-section__content
        #
        if a_type_2_search in article_teaser:
            article_body = soup1.find('div', {'class': "article__teaser"}).text.strip()
        if a_type_2_search in c_article_body:
            article_body = soup1.find('div', {'class': "c-article-body"}).text.strip()
        if a_type_2_search in article_section:
            article_body = soup1.find('div', {'class': "c-article-section__content"}).text.strip()
        # print(article_body)
        # article_paragraphs = article_body.find_all('p')
        # for a in article_paragraphs:
        #     if a.text != "":
        #         new_text = new_text + a.text.rstrip("")
        #     #  print(new_text)

        for char in punctuation:
            article_name = article_name.replace(char, '')
        article_name = article_name.replace(' ', '_')
        # print(article_name)

        filename = article_name + ".txt"
        # print(new_text)
        #  save_data_to_file(filename, description.text)
        save_data_to_file(filename, article_body, dir_name)
        articles.append(filename)


def save_data_to_file(fname, desc, dir_name):
    global new_text
    f_path = dir_name + "/" + fname
    # print(f_path)
    file = open(f_path, "w")
    # print(desc)
    file.write(desc)
    file.close()
    new_text = ""


number_of_pages, article_type_to_search = get_user_input()
cwd = os.getcwd()
for i in range(1, number_of_pages + 1):
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=" + str(i)
    # url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=" + str(number_of_pages)
    # print(url)
    page_content = get_source_content(url)
    page_number = "Page_" + str(i)
    dir_name = os.path.join(cwd, page_number)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    parse_article_data(page_content, article_type_to_search)
# print("Saved articles: ", articles)
print("Saved all articles.")



# if page_content.status_code == 200:
#     file = open('source.html', 'wb')
#     file.writelines(page_content)
#     file.close()
#     print("Content saved.")
# else:
#     print("The URL returned", page_content.status_code)
#
# print(response.text)
# try:
#     response_title, response_description = parse_data_title(response)
#     program["title"] = response_title
#     program["description"] = response_description
#     print(program)
# except AttributeError:
#     print("Invalid movie page!")
# if response.status_code == 200:
#     try:
#         print(parse_data_title(response))
#     except KeyError:
#         print("Invalid quote resource!")
# else:
#     print("Invalid movie page!")
