import sys
import os
import re
from HTMLParser import HTMLParser


inputDir = "./gap-html/gap_-C0BAAAAQAAJ/00000002.html"


def main():
	#print inputDir
	parser = MyHTMLParser()
	with open(inputDir, 'r') as inputFile:
		fullDoc = inputFile.read()
		parser.feed(fullDoc) 

class MyHTMLParser(HTMLParser):
	    def handle_data(self, data):
	    	data = data.strip()
       		print "Encountered some word  :", data

	    def handle_starttag(self, tag, attrs):
	        print "Encountered a start tag:", tag
	    def handle_endtag(self, tag):
	        print "Encountered an end tag :", tag

if __name__ == "__main__":
	main()
