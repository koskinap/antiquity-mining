import sys
import os
import re
import string
import operator
import json
import simplejson
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import pickle

sourceDir = './wordvectors'
wordListOutputDir = './analysisData/wordList.txt'

def plotOccurences(wordOccurences, bookTitle):
	occurList = []
	for x in wordOccurences:
		occurList.append(x[1])

	occurList.sort(reverse = True)

	plt.plot(occurList)
	plt.ylabel('some numbers')
	plt.xlabel('words')
	plt.title(bookTitle)
	plt.show()


def printOccurTuples(ml):
	# Print top 10 words by Occurences
	print ("Number of different words in this document : ")
	print len(ml)
	print ml[0:10]

def makeDict(wordDict,listOfWords):
	for tup in wordDict:
		if(tup[0] not in listOfWords):
			listOfWords.append(tup[0])

	
	return listOfWords

def main():
	if(os.path.isfile(wordListOutputDir)):
		print("File exists")
	else:
		listOfWords = []
	
	dirs = os.listdir( sourceDir )
	for d in dirs:
		fileName = sourceDir + '/' + d 
		if (fileName.endswith(".json")):
			with open(fileName, 'r') as inputFile:
				print("Processing book : " + d)
				content = json.load(inputFile)
				#print type(content)

			# Sorted approach,this is a sorted tuple (words,occurences)
			wordDictSorted = sorted(content.items(), key = operator.itemgetter(1), reverse = True)

			# Print plot of sorted distribution 
			# printOccurTuples(wordDictSorted)
			# plotOccurences(wordDictSorted,d)


	# This Block creates a list with every different word and stores it in a file
			if (os.path.isfile(wordListOutputDir)):
				pass
			else:
				listOfWords = makeDict(wordDictSorted,listOfWords)
				print(len(listOfWords))

	with open(wordListOutputDir, 'wb') as f:
		pickle.dump(listOfWords, f)



if __name__ == "__main__":
	main()