import sys
import os
import re
import string
import operator
import json
import simplejson
from nltk.corpus import stopwords

sourceDir = './docs'
outputDir = './docs2/'


def clean(text):

	# substitute every character that is no letter with a space
	removed_nonalphanumerical = re.sub("[^a-zA-Z0-9]", " ", text) 

	# convert every word to lower case and split by space to have a bag of words
	words = removed_nonalphanumerical.lower().split()                             

	# Store all stopwords in a set
	stops = set(stopwords.words("english"))                  

	# remove stop words, keep only meaningful terms with length > 2
	words_with_meaning = [w for w in words if ((not w in stops) and (len(w)>2))]   

	# concatenate words seperated by space
	return( " ".join( words_with_meaning )) 


def main():
	dirs = os.listdir( sourceDir )
	dirs.remove('.DS_Store.txt')
	dirs.remove('.DS_Store')

	for d in dirs:
		fileName = sourceDir + '/' + d
		text = None
		if (fileName.endswith(".txt") and d!='.DS_Store.txt'):
			print("Processing book : " + d)
			with open(fileName, 'r') as inputFile:
				text = inputFile.read()
			cleaned_text = clean(text)

			with open(outputDir + d, 'w+') as outputFile:
				outputFile.write(cleaned_text)



if __name__ == "__main__":
	main()