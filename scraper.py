import wikipedia
from bs4 import BeautifulSoup

oregano = wikipedia.page("Oregano")

soup = BeautifulSoup(oregano.html(), 'html.parser')

print(soup.find(title='Taxonomy (biology)'))

print(soup.find_all("span", class_="order"))

















# print "Oregano Wikipedia Page Object"

# print " "
# print "100 plant searches"
# print wikipedia.search("Plants", results=100)
# print " "
# print "Lavender summary"
# print wikipedia.summary("lavender")
# print " "

# print oregano
# print " "
# print "Oregano categories"
# print oregano.categories
# print " "
# print "Oregano Sections"
# print oregano.sections




# print " "
# print " "
# print " "
# print "Oregano full html page"
# print oregano.html()
