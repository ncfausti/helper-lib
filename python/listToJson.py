import json
import os

def listToJSON(items, filename):
	jsonItems = json.dumps(items)
	f = open(filename, 'w')
	f.write(jsonItems)
	f.close()
	return ("json file: " + os.getcwd() + "/" + filename)