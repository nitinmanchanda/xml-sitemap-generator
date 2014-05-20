import csv, sys, time, os, urllib2, json

reload(sys)
sys.setdefaultencoding("utf8")

def createFreshFile(fileName):
	os.system("rm " + fileName)
	os.system("touch " + fileName)

def getData(api):
	response = urllib2.urlopen(api)
	data = json.load(response)
	return data

def getTotalNumberOfDocs(api):
	response = urllib2.urlopen(api)
	data = json.load(response)
	return data['response']['numFound']

apis = {
	"product" : "http://54.251.33.134:8081/solr/sitename/select?q=NOT(visibility:not_show+OR+visibility:discontinued)&indent=true&wt=json&fl=id,seoUrl,type,visibility,stock&start=%s&rows=%s"
	# "category" : "http://54.251.33.134:8081/solr/sitename/select/?q=NOT(visibility:not_show+OR+visibility:discontinued)&q.op=AND&wt=json&indent=on&rows=0&facet=on&facet.field=categoryid&facet.mincount=1&facet.limit=50000",
	# "brand" : "http://54.251.33.134:8081/solr/sitename/select/?q=NOT(visibility:not_show+OR+visibility:discontinued)&q.op=AND&wt=json&indent=on&rows=2&facet=on&facet.field=brandid&facet.mincount=1&facet.limit=50000"
}

try:
	for type, api in apis.iteritems():
		fileName = "input-" + type + ".txt"
		createFreshFile(fileName)

		inputFile = open(fileName, 'r+')
		if type == "product":
			startIndex = 0
			numberOfRows = 100
			totalNumberOfDocs = getTotalNumberOfDocs(api % (startIndex, numberOfRows))

			while (startIndex < totalNumberOfDocs):
				data = getData(api % (startIndex, numberOfRows))
				print startIndex
				for row in data['response']['docs']:	
					inputFile.write("http://www.limeroad.com" + row['seoUrl'] + "\n")
				startIndex += numberOfRows
		elif type == "category":
			print type
		elif type == "brand":
			print type
finally:
	inputFile.close()
	os.system("python create-xml.py " + type + " " + fileName)
