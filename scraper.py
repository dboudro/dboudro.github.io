import wikipedia
import csv
from bs4 import BeautifulSoup
import re

counter = 0

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
    global counter
    print "scraping " + str(plant) + " " + str(counter)
    counter += 1
    plantPage = wikipedia.page(plant)
    soup = BeautifulSoup(plantPage.html(), 'html.parser')
    taxonomy = soup.find(title='Taxonomy (biology)')

    #order
    orderSpan = soup.find("span", class_="order")
    if orderSpan:
        orderAnchor = orderSpan.find('a')
        orderItalic = orderSpan.find('i')
        if orderAnchor.contents:
            order = orderAnchor.contents[0];
        elif orderItalic.contents:
            order = orderItalic.contents[0];
        else:
            genus = 'none'
    else:
        order = 'none'

    #family
    familySpan = soup.find("span", class_="family")
    if familySpan:
        familyAnchor = familySpan.find('a')
        familyItalic = familySpan.find('i')
        if familyAnchor.contents:
            family = familyAnchor.contents[0]
        elif familyItalic.contents:
            family = familyItalic.contents[0]
        else:
            family = 'none'
    else:
        family = 'none'

    #genus
    genusSpan = soup.find("span", class_="genus")
    if genusSpan:
        genusAnchor = genusSpan.find('a')
        genusItalic = genusSpan.find('i')
        if genusAnchor.contents:
            genus = genusAnchor.contents[0]
        elif genusItalic.contents:
            print genusItalic
            genus = genusItalic.contents[0]
        else:
            genus = 'none'
    else:
        genus = 'none'

    #species
    speciesSpan = soup.find("span", class_="species")
    if speciesSpan:
        speciesAnchor = speciesSpan.find('a')
        speciesItalic = speciesSpan.find('i')
        if speciesAnchor.contents:
            species = speciesAnchor.contents[0]
        elif speciesItalic.contents:
            species = speciesItalic.contents[0]
        else:
            species = 'none'
    else:
        species = "none"

    # scientific name
    scientificSpan = soup.find("span", class_="binomial")
    if scientificSpan:
        scientificAnchor = scientificSpan.find('a')
        scientificItalic = scientificSpan.find('i')
        if scientificAnchor.contents:
            scientific = scientificAnchor.contents[0]
        elif scientificItalic.contents:
            scientific = scientificItalic.contents[0]
        else:
            scientific = 'none'
    else:
        scientific = 'none'

    #common name (might not scale)
    common = soup.find('th')

    return ['myid', plant, genus]

csvData = []
#header
csvData.append(['id', 'name', 'genus'])

# for testing
plants = ['Bursaria', 'Allium', 'Allosyncarpia']

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
