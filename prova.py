import requests as rq
from bs4 import BeautifulSoup, SoupStrainer
import re

def test():
    url = 'https://pt.wikipedia.org/wiki/Blog'
    keyword = 'blogs'
    depth = 1
    search(url, keyword, depth)


def get_data():
    url = input("Digite a url: ")
    keyword = input("Digite a palavra chave: ")
    depth = int(input("Digite a profundidade: "))
    search(url, keyword, depth)


def get_links(html_with_tags):
    links = []
    for link in BeautifulSoup(html_with_tags, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            links.append(link['href'])
    return links


def search(url, keyword, depth):
    html_with_tags = rq.get(url).text
    html_pure = BeautifulSoup(html_with_tags, 'html.parser').text
    actual_links = get_links(html_with_tags)
    #print(actual_links)
    regex = '.{10}' + keyword + '\.?\s?.{10}'
    words = re.findall(regex, html_pure)

    print("URL: " + url)
    contador = 1
    for word in words:
        print('#' + str(contador) +' '+ word)
        contador += 1
    print("---- FIM ------")

    if depth > 0:
        for link in actual_links:
            if 'http' in link:
                search(link, keyword, depth-1)
            if '/' in link:
                url_completa = url + link
                search(url_completa, keyword, depth-1)


if __name__ == '__main__':
    #get_data()
    test()