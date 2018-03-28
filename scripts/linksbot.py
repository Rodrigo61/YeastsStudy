import utils

file = open("datalinks_bot.data", 'w')
statistics = {}
for species in utils.speciesIds.keys():	
	print("Getting links for %s" % species)
	links = utils.findLinksNcyc(species)
	print("Got %d links" % len(links))
	statistics[species] = len(links)
	for l in links:
		file.write("ncyc;")
		file.write(l)
		file.write("\n")
		file.flush()

file.close()


print(statistics)