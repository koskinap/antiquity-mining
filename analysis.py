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
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = SnowballStemmer("english")

sourceDir = './wordvectors'
# documentDir = './docs/DICTIONARY GREEK AND ROMAN GEOGRAPHY VOL II.txt'
documentDir = './docs/HISTORY OF THE DECLINE AND FALL OF THE ROMAN EMPIRE GIBBONs VOL II.txt'
wordListDir = './analysisData/wordList.txt'

def preprocessing(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		testToken = token.lower()
		if (re.search('[a-zA-Z0-9]', testToken) and all(ord(c) < 128 for c in testToken) and len(testToken)>2):
			filtered_tokens.append(testToken)
	stems = [stemmer.stem(t) for t in filtered_tokens]
	return stems


def main():

	# with open(wordListDir, 'rb') as f:
	# 	wordList = pickle.load(f)

	rawDoc = []
	with open(documentDir, 'rb') as f2:
		rawDoc.append(f2.read())



	tfidf_vectorizer = TfidfVectorizer(stop_words='english',tokenizer=preprocessing, use_idf=True, ngram_range=(1,1))
	
	tfidf_matrix = tfidf_vectorizer.fit_transform(rawDoc) #fit the vectorizer to synopses

	print(tfidf_matrix.shape)
	# print(tfidf_vectorizer.get_feature_names())

	# print(tfidf_matrix.features)

	# dirs = os.listdir( sourceDir )
	# for d in dirs:
	# 	fileName = sourceDir + '/' + d 
	# 	if (fileName.endswith(".json")):
	# 		with open(fileName, 'r') as inputFile:
	# 			print("Processing book : " + d)
	# 			content = json.load(inputFile)
	# 			#print type(content)

	# 		wordDictSorted = sorted(content.items(), key = operator.itemgetter(1), reverse = True)
	# 		print(len(wordDictSorted))



if __name__ == "__main__":
	main()