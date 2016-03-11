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


sourceDir = './wordvectors'



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

def main():
	pass



if __name__ == "__main__":
	main()