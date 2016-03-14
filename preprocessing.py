import sys
import os
import re
import string
from HTMLParser import HTMLParser

# Original MyHtmlParser classs taken and modified by
# http://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python


PUNCT = string.punctuation

#Sample input dir,needs to be generalized to take all files in every directory and produce a final document

sourceDir = './gap-html'
outputDir = './docs/'

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

class MyHTMLParser(HTMLParser):
	# initialize a text list which holds all the words in 
	def __init__(self):
		HTMLParser.__init__(self)
		self.__text = []

	# handle the data
	def handle_data(self, data):
		# punctuation may not need to be removed, at this stage we want to clean text from html to pure text

		data = data.strip()
		if (data == 'OCR Output' or is_ascii(data) == False):
			pass
		else:
			#check if needed
			dataSplit = data.split(' ')
			for w in dataSplit:
				word = w.strip()
				if word != '':
					self.__text.append(word + ' ')

	#If faced a html tag which signs change of line,then add newline char
	def handle_starttag(self, tag, attrs):
		if tag in ['p', 'br']:
			self.__text.append('\n')
	# join all words in text list in a string to produce the final text
	def text(self):
		return ''.join(self.__text)



def main():
	dirs = os.listdir( sourceDir )
	for d in dirs:
		print("Processing book : " + d)
		output = ''
		# here set the output direction and output file
		# returns a list of all html files in a directory composing a book
		filesList = os.listdir(sourceDir + '/' + d)
		# For everyfile run htmlparser and append and output which is written in a file = book/document
		for f in filesList:
			parser = MyHTMLParser()
			with open(sourceDir + '/'+ d + '/' + f, 'r') as inputFile:
				fullDoc = inputFile.read()
				parser.feed(fullDoc)
				parser.close()

				output = output + '\n\n' + str(parser.text())
		with open(outputDir + d + '.txt' ,'w') as outputFilename:
			outputFilename.write(output)

if __name__ == "__main__":
	main()
