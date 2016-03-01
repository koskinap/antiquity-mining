import sys
import os
import re
import string
import operator
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

cachedStopWords = stopwords.words("english")

PUNCT = string.punctuation

#sourceDir = './docs'
sourceDir = './docs/gap_-C0BAAAAQAAJ.txt'
#outputDir = ''


def plotOccurences(wordOccurences):
	occurList = []
	for x in wordOccurences:
		occurList.append(x[1])

	occurList.sort(reverse = True)

	plt.plot(occurList)
	plt.ylabel('some numbers')
	plt.xlabel('words')
	plt.show()

with open(sourceDir, 'r') as inputFile:
	text = inputFile.read()
	
	# Substitute everything that is not a word/number with a space and then split
	wordBag = re.sub('[^A-Za-z0-9]+', ' ', text)
	wordBagList = wordBag.split(' ')

	# make a dictionary which counts the appearances of each word
	wordDict = {}
	for word in wordBagList:
		testword = word.lower()
		if (testword in wordDict):
			wordDict[testword] += 1
		elif ((testword in cachedStopWords) or (len(testword) < 3)):
			pass
		else:
			wordDict[testword] = 1

	# Sort the Dictionary in sorted tuple(dictionaries cannot be sorted)
	wordDictSorted = sorted(wordDict.items(), key = operator.itemgetter(1))
	# print wordDictSorted

#print type(wordDictSorted)

ml = sorted(wordDictSorted, key = operator.itemgetter(1), reverse = True)

for i,x in enumerate(ml):
	if i>100:
		break
	else:
		print ml[i]

plotOccurences(wordDictSorted)
