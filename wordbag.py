import sys
import os
import re
import string
import operator

PUNCT = string.punctuation

#sourceDir = './docs'
sourceDir = './docs/gap_-C0BAAAAQAAJ.txt'
#outputDir = ''

with open(sourceDir, 'r') as inputFile:
	text = inputFile.read()
	
	# data = re.split(r'[.,;]+', text)
	# data = re.split(PUNCT, text)
	# Substitute everything that is not a word/number with a space and then split
	wordBag = re.sub('[^A-Za-z0-9]+', ' ', text)
	wordBagList = wordBag.split(' ')

	# make a dictionary which counts the appearances of each word
	wordDict = {}
	for word in wordBagList:
		testword = word.lower()
		if (testword in wordDict):
			wordDict[testword] += 1
		else:
			wordDict[testword] = 1

	# Sort the Dictionary in sorted tuple(dictionaries cannot be sorted)
	wordDictSorted = sorted(wordDict.items(), key=operator.itemgetter(1))
	print wordDictSorted