import wikipedia
from bs4 import BeautifulSoup





oregano = wikipedia.page("Oregano")


soup = BeautifulSoup(oregano.html(), 'html.parser')


taxonomy = soup.find(title='Taxonomy (biology)')

#order
orderSpan = soup.find("span", class_="order")
orderAnchor = orderSpan.find_all()
order = orderAnchor[0].contents[0];

#family
familySpan = soup.find("span", class_="family")
familyAnchor = familySpan.find_all()
family = familyAnchor[0].contents[0];

#genus
genusSpan = soup.find("span", class_="genus")
genusAnchor = genusSpan.find_all()
genus = genusAnchor[0].contents[0].contents[0]

#species
speciesSpan = soup.find("span", class_="species")
speciesAnchor = speciesSpan.find_all()
species = speciesAnchor[0].contents[0].contents[0];



# scientific name
# family = soup.find("span", class_="family")
# familyAnchor = familySpan.find_all()
# family = familyAnchor[0].contents[0];



##### printing

print ""
print ""
print 'order: ' + order
print 'family: ' + family
print 'genus: ' + genus
print 'species: ' + species


















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
