import csv, sys, time, os, urllib2, json

response = urllib2.urlopen("url")
data = json.load(response)



pageType = "category"
lastmod = time.strftime('%Y-%m-%d')
outputFileName = 'sitemap_' + pageType +'.xml'

# dataFile = open(sys.argv[1], 'rb')
sitemap = open(outputFileName, 'w')

sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

domain = "http://www.limeroad.com"

freqMap = {"product" : "hourly", "category" : "daily", "static" : "weekly"}
priorityMap = {"product" : "0.9", "category" : "0.8", "static" : "0.7"}

changefreq = freqMap[pageType]
priority = priorityMap[pageType]
urlsCount = 0

urlInfo = '\n\t<url>\n'
urlInfo += '\t\t<loc>%s</loc>\n'
urlInfo += '\t\t<lastmod>%s</lastmod>\n'
urlInfo += '\t\t<changefreq>%s</changefreq>\n'
urlInfo += '\t\t<priority>%s</priority>\n'
urlInfo += '\t</url>'
urlInfo = urlInfo % (domain + '/test', lastmod, changefreq, priority)

try:
	sitemap.write(urlInfo)    

  #   reader = csv.reader(dataFile)
  #   for row in reader:
		# pageId = row[0]
finally:
	sitemap.write('\n</urlset>')
    # dataFile.close()
	sitemap.close()
	# os.system("gzip " + outputFileName)