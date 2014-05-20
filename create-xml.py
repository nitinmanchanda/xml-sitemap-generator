import csv, sys, time, os, urllib2, json

pageType = sys.argv[1]
lastmod = time.strftime('%Y-%m-%d')
outputFileName = 'sitemap_' + pageType +'.xml'

sitemap = open(outputFileName, 'w')

sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

freqMap = {"product" : "hourly", "category" : "daily", "static" : "weekly"}
priorityMap = {"product" : "0.9", "category" : "0.8", "static" : "0.7"}

changefreq = freqMap[pageType]
priority = priorityMap[pageType]
urlsCount = 0

try:
	for url in open(sys.argv[2], 'rb'):
		urlInfo = '\n\t<url>\n'
		urlInfo += '\t\t<loc>%s</loc>\n'
		urlInfo += '\t\t<lastmod>%s</lastmod>\n'
		urlInfo += '\t\t<changefreq>%s</changefreq>\n'
		urlInfo += '\t\t<priority>%s</priority>\n'
		urlInfo += '\t</url>'
		urlInfo = urlInfo % (url.strip(), lastmod, changefreq, priority)
		sitemap.write(urlInfo) 
		urlsCount += 1 

finally:
	print "Total URLs processed: " + str(urlsCount)
	sitemap.write('\n</urlset>')
	sitemap.close()
	os.system("gzip " + outputFileName)