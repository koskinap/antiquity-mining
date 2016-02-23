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
	    	data.strip()
	    	if data != '':
       			print "Encountered some data  :", data


if __name__ == "__main__":
	main()
