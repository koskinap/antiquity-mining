import os
import sys

docDir = './gap-html'


def main():
	dirs = os.listdir( docDir )
	for d in dirs:
		print d
		files = os.listdir(docDir + '/' + d)
		for f in files:
			print f

		print '\n'

if __name__ == '__main__':
	main()