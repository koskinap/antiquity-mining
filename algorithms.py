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

sourceDir = './matrices/tfidf_matrix.txt'


def main():
	with open(sourceDir, 'rb') as handle:
		tfidf_matrix = pickle.load(handle)

	print(tfidf_matrix.shape)
	dist = 1 - cosine_similarity(tfidf_matrix)
	print dist
	print(tfidf_vectorizer.get_feature_names())




if __name__ == "__main__":
	main()