# import requests
# from bs4 import BeautifulSoup

# terminal_command = 'python3 main.py'
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('small', class_='author')

# # print(soup)
# # print(quotes)
# authors = []
# for quote in quotes:
#   authors.append(quote.text)

# print(authors)

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('--' + authors[i].text)
#     tagsforquote = tags[i].find_all('a', class_='tag')
#     for tagforquote in tagsforquote:
#         print(tagforquote.text)
#     break

## Find first paragraph
# first_paragraph = soup.find('p')
# print(first_paragraph)
# print(first_paragraph.text)

### Find all paragraphs
# all_paragraphs = soup.find_all('p')
# print(all_paragraphs)


## Find first paragraph with get_text()
# first_paragraph = soup.find('p')
# print(first_paragraph.get_text().strip())
# print(first_paragraph.text)

# отримати значення атрибута "href" першого тегу <a> на сторінці
# first_link = soup.find("a")
# first_link_href = first_link["href"]
# print(first_link_href)# '/'


#### Get children

# first_paragraph = soup.find('p')
# body_childre = list(first_paragraph.children)
# print(body_childre)

# first_div = soup.find('div')
# first_a = first_div.find('a')
# print(first_a)


# first_a = soup.find('div').find('a')
# print(first_a)

## Find a parent

# first_paragraph = soup.find('p')
# first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

# first_paragraph = soup.find('p')
# first_paragraph_parent = first_paragraph.find_parent()
# print(first_paragraph_parent)

# container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
# print(container)

# next_sibling = soup.find('span', attrs={'class': 'tag-item'}).find_next_sibling("span")
# print(next_sibling)

# previous_sibling = next_sibling.find_previous_sibling("span")
# print(previous_sibling)


#### CSS selectors

# Find attribute p
# p = soup.select('p')
# print(p)

### Find class .text

# text_class = soup.select(".text")
# print(text_class)

### Find header

# header = soup.select('#header')
# print(header)

#Наприклад, знайдемо всі елементи <a> всередині тегу <div> з класом "container":

# a = soup.select('div.container a')
# print(a)

### Знайдемо всі елементи, у яких атрибут href починається з "https://"

# href = soup.select("[href^='https://']")
# print(href)

# text_class = soup.select("[class *= 'text']")
# print(text_class)









    



