import wikipedia
import csv
from bs4 import BeautifulSoup


allPlants = wikipedia.page("List_of_garden_plants")
soup = BeautifulSoup(allPlants.html(), 'html.parser')

items = soup.find_all('li')
plants = []
for li in items:
    if li.find('i'):
         plants.append(li.find('a'))


def loadPage(plant):
    print "scraping " + str(plant)
    plantPage = wikipedia.page(plant)
    soup = BeautifulSoup(plantPage.html(), 'html.parser')
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
    if speciesSpan:
        speciesAnchor = speciesSpan.find_all()
        species = speciesAnchor[0].contents[0].contents[0]
    else:
        species = "None"

    # scientific name
    scientificSpan = soup.find("span", class_="binomial")
    if scientificSpan:
        scientificAnchor = scientificSpan.find_all()
        scientific = scientificAnchor[0].contents[0]

    #common name (might not scale)
    common = soup.find_all('b')[2].contents[0]

    return ['myid', plant, genus]

csvData = []
#header
csvData.append(['id', 'name', 'genus'])

for plant in plants:
    csvData.append(loadPage(plant))
    print 'loaded ' + str(plant)

with open('plantOutput.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter= ',')
    wtr.writerows(csvData)


##### printing
# print ''
# print 'common name: ' + common
# print 'scientific name: '  + scientific
# print 'order: ' + order
# print 'family: ' + family
# print 'genus: ' + genus
# print 'species: ' + species
# print ''
# print plant.summary




















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
