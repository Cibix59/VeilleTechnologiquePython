import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://www.cegeprdl.ca/').read()
soup = bs.BeautifulSoup(source,'lxml')
# valeur du titre :
print(soup.title.string)

# titre
print(soup.title)

# test navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.h2)