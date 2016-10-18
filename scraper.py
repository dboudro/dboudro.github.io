import wikipedia
print " "
print "100 plant searches"
print wikipedia.search("Plants", results=100)
print " "
print "Lavender summary"
print wikipedia.summary("lavender")
print " "
print "Oregano Wikipedia Page Object"
oregano = wikipedia.WikipediaPage("Oregano")

print oregano
print " "
print "Oregano categories"
print oregano.categories
print " "
print "Oregano Medical Uses"
print oregano.section("Medical Uses")

print " "
print "Oregano object and properties"
print (vars(oregano))
