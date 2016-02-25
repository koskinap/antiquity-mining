import sys
import os
import re
import string
from HTMLParser import HTMLParser

PUNCT = string.punctuation

#Sample input dir,needs to be generalized to take all files in every directory and produce a final document
inputDir = "./gap-html/gap_-C0BAAAAQAAJ/00000142.html"

class MyHTMLParser(HTMLParser):
	# initialize a text list which holds all the words in 
	def __init__(self):
		HTMLParser.__init__(self)
		self.__text = []

	# handle the dta,clean chars,punctuation
	def handle_data(self, data):
		# punctuation may not need to be removed, at this stage we want to clean text from html to pure text
		# data = data.replace(PUNCT, ' ')
		data = data.strip()

		dataSplit = data.split(' ')
		for w in dataSplit:
			word = w.strip()
			if word != '':
				self.__text.append(word+ ' ')

		# #Alternative
		# text = data.strip()
		# if len(text) > 0:
		# 	text = re.sub('[ \t\r\n]+', ' ', text)
		# 	self.__text.append(text + ' ')


	#If faced a html tag which signs change of line,then add newline char
	def handle_starttag(self, tag, attrs):
		if tag in ['p', 'br']:
			self.__text.append('\n')
	# join all words in text list in a string to produce the final text
	def text(self):
		print ''.join(self.__text)

	# def handle_endtag(self, tag):
	# 	print "Encountered an end tag :", tag

def main():
	parser = MyHTMLParser()
	with open(inputDir, 'r') as inputFile:
		fullDoc = inputFile.read()
		parser.feed(fullDoc)
		parser.close()
		parser.text()

if __name__ == "__main__":
	main()
