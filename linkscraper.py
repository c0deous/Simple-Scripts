from optparse import OptionParser
import commands
from bs4 import BeautifulSoup
import time
import os
import io

parser = OptionParser()
parser.add_option("-i", "--input", dest="link", help="link to scrape")
parser.add_option("-o", "--output", dest="filename", help="output filename, will default to linkscrape<date>.txt")
(options, args) = parser.parse_args()

webcontent = unicode(commands.getstatusoutput("curl -s " + str(options.link)))[5:-2]

soup = BeautifulSoup(webcontent)


links = []
for link in soup.find_all('a'):
	links.append(link.getText() + " - " + link.get("href") + "\n")

	

if options.filename:
	filename = options.filename
else:
	filename = "linkscrape" + time.strftime("%d.%m.%y") + ".txt"	
writer = io.open(filename, "w+", encoding='utf8')
for item in links:
	writer.write("%s\n" % item)

print("[+] Finished scraping links from " + str(options.link))
print("Links scraped:")
print(" ")
print(repr(links).decode("unicode_escape").encode("utf-8"))
print(" ")
print("Saved scraped links to " + filename) 
		
