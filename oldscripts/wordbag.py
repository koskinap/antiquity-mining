import sys
import os
import re
import string
import operator
import json
import simplejson
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem.snowball import SnowballStemmer

cachedStopWords = stopwords.words("english")
stemmer = SnowballStemmer("english")
PUNCT = string.punctuation

sourceDir = './docs'
outputDir = './wordvectors/'

def makeBagOfWords(text):
	# Substitute everything that is not a word/number with a space and then split
	# Create a bag of words seperated by spaces and make a list of words
	wordBag = re.sub('[^A-Za-z0-9]+', ' ', text)
	wordBagList = wordBag.split(' ')

	#Stemming
	stemmedWordBagList = []
	stemmedWordBagList = [stemmer.stem(token) for token in wordBagList]

	# Make a dictionary which counts the appearances of each word
	wordDict = {}

	for word in stemmedWordBagList:
		# Convert current word to lower case
		testword = word.lower()

		# Check if word exists in dictionary to count occurences of each
		if (testword in wordDict):
			wordDict[testword] += 1
		elif ((testword in cachedStopWords) or (len(testword) < 3)):
			# Ignore toos short words and stopwords
			pass
		else:
			wordDict[testword] = 1

	return wordDict


def main():
	dirs = os.listdir( sourceDir )
	for d in dirs:
		fileName = sourceDir + '/' + d 
		if (fileName.endswith(".txt")):
			print("Processing book : " + d)
			with open(fileName, 'r') as inputFile:
				text = inputFile.read()			
				wordVector = makeBagOfWords(text)
			
			written_paths = d.split('.')
			d_name_without_extension = written_paths[0]
			
			f = os.path.join(outputDir, d_name_without_extension) + '.json'
			with open(f, 'w+') as out_file:
				json.dump(wordVector, out_file,indent = 4)


if __name__ == "__main__":
	main()

