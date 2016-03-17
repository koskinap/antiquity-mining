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

# Tf_Idf implementation taken on 14/03/2016 and adjusted
# http://brandonrose.org/clustering#Visualizing-document-clusters 

stemmer = SnowballStemmer("english")

destFileTfIdf = './matrices/tfidf_matrix.txt'
featureNamesFile = './matrices/featurenames.txt'
titlesFile = './matrices/titles.txt'
sourceDir = './docs2/'
# sourceDir = './docs/'


def preprocessing(text):
	# tokenize bag of words
	tokens = [word for word in nltk.word_tokenize(text)]
	filtered_tokens = []
	# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
	for token in tokens:
		# testToken = token
		testToken = token.lower().split()
		for w in testToken:
			if (re.search('[a-zA-Z]', w) and all(ord(c) < 128 for c in w)):
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
	tfidf_vectorizer = TfidfVectorizer(max_df=0.80, max_features=50000,
                                 min_df=0.20, stop_words='english',tokenizer=preprocessing, use_idf=True, ngram_range=(1,1))
	
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