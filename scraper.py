import wikipedia
import csv
from bs4 import BeautifulSoup
import re


allPlants = wikipedia.page("List_of_garden_plants")
soup = BeautifulSoup(allPlants.html(), 'html.parser')

## if the link is red
## if the link title contains the word page does not exist

items = soup.find_all('li')
plants = []
for li in items:
    if li.find('i') and re.search("^\S*$", li.find('a')['title']):
        plants.append(li.find('a')['title'])


def loadPage(plant):
    print "scraping " + str(plant) #+ str(plant.index)
    plantPage = wikipedia.page(plant)
    soup = BeautifulSoup(plantPage.html(), 'html.parser')
    taxonomy = soup.find(title='Taxonomy (biology)')

    #order
    orderSpan = soup.find("span", class_="order")
    if orderSpan:
        orderAnchor = orderSpan.find_all()
        order = orderAnchor[0].contents[0];
    else:
        order = 'none'

    #family
    familySpan = soup.find("span", class_="family")
    if familySpan:
        familyAnchor = familySpan.find_all()
        family = familyAnchor[0].contents[0];
    else:
        family = 'none'

    #genus
    genusSpan = soup.find("span", class_="genus")
    if genusSpan:
        genusAnchor = genusSpan.find_all()
        if genusAnchor[0].contents[0].contents[0]:
            genus = genusAnchor[0].contents[0].contents[0]
        elif genusAnchor[0].contents[0]:
            genus = genusAnchor[0].contents[0];
        else:
            genus = 'none'
    else:
        genus = 'none'

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
    common = soup.find('th')

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
