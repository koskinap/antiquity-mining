import sys
import os
import re
import string
import operator
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


stemmer = SnowballStemmer("english")

destFileTfIdf = './matrices/tfidf_matrix.txt'
featureNamesFile = './matrices/featurenames.txt'
titlesFile = './matrices/titles.txt'
# sourceDir = './docs/'
sourceDir = './docs2/'

def preprocessing(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		subbedToken = re.sub('[^A-Za-z0-9]+', ' ', token)
		testToken = subbedToken.lower().split()
		for w in testToken:
			if (re.search('[a-zA-Z0-9]', w) and all(ord(c) < 128 for c in w) and len(w)>2):
				filtered_tokens.append(w)
	stems = [stemmer.stem(t) for t in filtered_tokens]
	return stems


def main():

	# Initialize lists with full texts of every book/document
	rawDoc = []
	# Initialize list storing titles
	docTitles = []

	dirs = os.listdir( sourceDir )
	dirs.remove('.DS_Store.txt')
	dirs.remove('.DS_Store')
	
	for d in dirs:
		fileName = sourceDir + d 
		if (fileName.endswith(".txt")):
			with open(fileName, 'rb') as f:
				rawDoc.append(f.read())
				docTitles.append(re.sub('\.txt$', '', d))

	# Initialize an object of a class which performs transform on text later
	tfidf_vectorizer = TfidfVectorizer(max_df=065, max_features=200000,
                                 min_df=0.1, stop_words='english',tokenizer=preprocessing, use_idf=True, ngram_range=(1,1))
	
	tfidf_matrix = tfidf_vectorizer.fit_transform(rawDoc)
	featureNames = tfidf_vectorizer.get_feature_names()

	# Store tf_idf matrix, feature names and book titles in files so they can be used again later without 
	# needing the costful process of computing the tfidf matrix again
	with open(destFileTfIdf, 'wb+') as f:
		pickle.dump(tfidf_matrix ,f) 

	with open(featureNamesFile, 'wb+') as f2:
		pickle.dump(featureNames ,f2)

	with open(titlesFile, 'wb+') as f3:
		pickle.dump(docTitles ,f3) 



if __name__ == "__main__":
	main()