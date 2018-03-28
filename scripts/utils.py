import requests
from bs4 import BeautifulSoup
import collections

#On NCYC, tables may have differente names, here, 2 ID's may map to  equivalent tables
ncycTablesIds = ["product-attribute-specs-table-41", 
				 "product-attribute-specs-table-65",
				 "product-attribute-specs-table-42", 
				 "product-attribute-specs-table-64",
				 "product-attribute-specs-table-43",
				 "product-attribute-specs-table-63"]

speciesIds = {	"saccharomyces cerevisiae" 		: '0',
				"kluyveromyces marxianus"		: '1',
				"dekkera bruxellensis"			: '2',
				"brettanomyces bruxellensis"	: '2',
				"candida albicans"				: '3',
				"yarrowia lipolytica"			: '4',
				"candida tropicalis"			: '5',
				"pichia galeiformis"			: '6',
				"zygosaccharomyces fermentati"	: '7',
				"saccharomycodes ludwigii"		: '8',
				"candida pararugosa"			: '9'}

#Rever isso!
valuesDict = {	"+": '1', 
				"-":'-1', 
				"w": '0', 
				"d": '0.5',
				"delayed": '0.5', 
				"unknown": 'NaN', 
				"weak/latent": '0', 
				"weak" : '0',
				"latent" : '0',
				"veryweak" : '0',
				"no" : '0',
				"slow" : '0.5',
				"weak/slow" : '0.5',
				"slow/latent" : '0.5'}

def toCSV(row, returnHeader = False):
	csvList = []
	header = sorted(row.keys())
	for attr in header:
		csvList.append(row[attr])
	csv = ",".join(csvList)
	if returnHeader:
		return (",".join(header), csv)
	return csv

def getPageFromURL(url):
	resp = requests.get(url)
	if resp.status_code != 200:
		print("Got non 200 Response!")
	else:
		print("Got %s from NCYC" % url)
		return BeautifulSoup(resp.content, "html5lib")
	return False

def downloadFromNcyc(url, ignore, tablesIds = ncycTablesIds):
	row = {}
	code = url.split('-')[-1]
	if  code in ignore:
		print("Already downloaded, ignoring %s" % url)
		return ('', False)
	else:
		ignore.append(code)
	page = getPageFromURL(url)
	if not page:
		return (False, False)
	species = page.find("div", {"class":"product-name"}).find("h1").text
	print("Species is %s" % species)
	row["00class"] = speciesIds[species.lower().strip()]

	tables = page.findAll("table", id=tablesIds)
	for table in tables:
		rows = table.findAll("tr")
		for tr in rows:
			column, value = tr.text.replace(" ", "").replace('\n', '', 1).split("\n")[:-1]
			row[column.lower()] = valuesDict[value.lower()]
	print("%d attributes found!" % len(row))
	return toCSV(row, returnHeader=True)


def findLinksNcyc(speciesName):
	checkName = speciesName.replace(" ", '-').lower()
	pageNumber = 0
	linkLists = []
	old = 0
	while pageNumber < 10:
		old = len(linkLists)
		pageNumber += 1
		#Gerenerate query url for ncyc
		url = "https://catalogue.ncyc.co.uk/catalogsearch/result/index/?dir=desc&limit=200&order=relevance&q=%s&p=%d" % (speciesName.replace(" ", "+").lower(), pageNumber)
		print("Getting %s" % url)
		page = requests.get(url)
		#Check for non OK response
		if page.status_code == 200:
			html = BeautifulSoup(page.content, 'html5lib')
			items = html.findAll('li', {'class':'item'})
		else:
			print("Got non 200 response")
			break
		#For each Listed Item, process!
		for item in items:
			name = item.find('hgroup').text.strip().split('\n')
			name[0] = name[0].split(" ")[1].lower()
			name[1] = name[1].strip().replace(" ", '-').lower()
			if name[1] == checkName:
				#Generate specific page URL
				link = "https://catalogue.ncyc.co.uk/%s-%s"%(name[1], name[0])
				#Check if it's a repeated URL
				if not link in linkLists:
					print(link)
					linkLists.append(link)
				else:
					print("Repeated!", link)
	return linkLists

def downloadFromCBS(url):
	row = {}
	page = getPageFromURL(url)
	species = page.findAll("td", {"class":"RightColCSS"})[0].text
	print("Species is %s" % species)
	return page
