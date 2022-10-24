# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# # bs = BeautifulSoup(html.read(), 'html5lib')
# # bs = BeautifulSoup(html.read(), 'lxml')
# bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs.h1)


# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup
#
#
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(), "lxml")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
#
#
# title = getTitle("https://portal.eaeunion.org/sites/odata/_layouts/15/portal.eec.registry.ui/directoryform.aspx?viewid=1631d8b8-efd5-4a46-80d9-5e252e7986bb&listid=0e3ead06-5475-466a-a340-6f69c01b5687&itemid=231")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html.read(), "html.parser")

# nameList = bs.findAll('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())

# titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
# print([title for title in titles])
#
# nameList = bs.find_all(text='the prince')
# print(len(nameList))


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
#
# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.find('img',
#               {'src':'../img/gifts/img1.jpg'})
#       .parent.previous_sibling.get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])

# bs.find_all(lambda tag: len(tag.attrs) == 2)
# bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
# bs.find_all('', text='Or maybe he\'s only resting?')

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
#
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
#     html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#
# links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = getLinks(newArticle)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #We have encountered a new page
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks('')


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
#
#
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     try:
#         print(bs.h1.get_text())
#         print(bs.find(id='mw-content-text').find_all('p')[0])
#         print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
#     except AttributeError:
#         print('This page is missing something! Continuing.')
#
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # We have encountered a new page
#                 newPage = link.attrs['href']
#                 print('-' * 20)
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
#
# getLinks('')


# from urllib.request import urlopen
# from urllib.parse import urlparse
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
#
# pages = set()
# random.seed(datetime.datetime.now())
#
#
# # Retrieves a list of all Internal links found on a page
# def getInternalLinks(bs, includeUrl):
#     includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
#     internalLinks = []
#     # Finds all links that begin with a "/"
#     for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 if (link.attrs['href'].startswith('/')):
#                     internalLinks.append(includeUrl + link.attrs['href'])
#                 else:
#                     internalLinks.append(link.attrs['href'])
#     return internalLinks
#
#
# # Retrieves a list of all external links found on a page
# def getExternalLinks(bs, excludeUrl):
#     externalLinks = []
#     # Finds all links that start with "http" that do
#     # not contain the current URL
#     for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks:
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks
#
#
# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bs = BeautifulSoup(html, 'html.parser')
#     externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
#     if len(externalLinks) == 0:
#         print('No external links, looking around the site for one')
#         domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
#         internalLinks = getInternalLinks(bs, domain)
#         return getRandomExternalLink(internalLinks[random.randint(0,
#                                                                   len(internalLinks) - 1)])
#     else:
#         return externalLinks[random.randint(0, len(externalLinks) - 1)]
#
#
# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink(startingSite)
#     print('Random external link is: {}'.format(externalLink))
#     followExternalOnly(externalLink)
#
#
# followExternalOnly('http://oreilly.com')

