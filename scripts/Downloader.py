#!/etc/python3.4

from utils import *
import sys

datalinks = open(sys.argv[1])
lines = datalinks.readlines()
dataset = open(sys.argv[2], "w")
dbsInterfaces = {"ncyc" : downloadFromNcyc}

ignoreLists = {'ncyc' : []}
hasHeader = False
for l in lines:
	database, url  = l.split(";")
	url = url.replace("\n", "")
	print("Downloading %s from %s" % (url, database))
	header, data  = dbsInterfaces[database](url, ignoreLists[database])
	if not data:
		continue
	if not hasHeader:
		print("Adding Headers!")
		dataset.write(header)
		dataset.write("\n")
		hasHeader = True
	dataset.write(data)
	dataset.write("\n")
	dataset.flush()

dataset.close()

