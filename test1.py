import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.cegeprdl.ca/').read()


soup = bs.BeautifulSoup(source,'lxml')

# titre
print(soup.title)

# valeur du titre :
print(soup.title.string)

# test navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.h2)