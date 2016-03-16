from __future__ import print_function
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.manifold import MDS
from scipy.cluster.hierarchy import ward, dendrogram


sourceDir = './matrices/tfidf_matrix.txt'
featureNamesFile = './matrices/featurenames.txt'
titlesFile = './matrices/titles.txt'

#set up colors per clusters using a dict
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}

#set up cluster names using a dict
cluster_names = {0: 'Cluster 1', 
                 1: 'Cluster 2', 
                 2: 'Cluster 3', 
                 3: 'Cluster 4', 
                 4: 'Cluster 5'}

def cosineSimilarity(tfidf_matrix):
	dist = 1 - cosine_similarity(tfidf_matrix)
	return dist

def kmeans(tfidf_matrix):

	num_clusters = 5

	km = KMeans(n_clusters=num_clusters)
	km.fit(tfidf_matrix)
	clusters = km.labels_.tolist()

	return clusters


def mds(dist, clusters, titles):

	MDS()
	# convert two components as we're plotting points in a two-dimensional plane
	# "precomputed" because we provide a distance matrix
	# we will also specify `random_state` so the plot is reproducible.
	mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
	pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
	xs, ys = pos[:, 0], pos[:, 1]

	#create data frame that has the result of the MDS plus the cluster numbers and titles
	df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles)) 

	#group by cluster
	groups = df.groupby('label')

	# set up plot
	fig, ax = plt.subplots(figsize=(17, 9)) # set size
	ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

	#iterate through groups to layer the plot
	#note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
	for name, group in groups:
	    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
	            label=cluster_names[name], color=cluster_colors[name], 
	            mec='none')
	    ax.set_aspect('auto')
	    ax.tick_params(\
	        axis= 'x',          # changes apply to the x-axis
	        which='both',      # both major and minor ticks are affected
	        bottom='off',      # ticks along the bottom edge are off
	        top='off',         # ticks along the top edge are off
	        labelbottom='off')
	    ax.tick_params(\
	        axis= 'y',         # changes apply to the y-axis
	        which='both',      # both major and minor ticks are affected
	        left='off',      # ticks along the bottom edge are off
	        top='off',         # ticks along the top edge are off
	        labelleft='off')
	    
	ax.legend(numpoints=1)  #show legend with only 1 point

	#add label in x,y position with the label as the film title
	for i in range(len(df)):
	    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  
    
    # Show the plot
	plt.show() 
	plt.close()

	#uncomment the below to save the plot if need be
	#plt.savefig('clusters_small_noaxes.png', dpi=200)

def hierarchical_clustering(dist, titles):

	linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

	fig, ax = plt.subplots(figsize=(15, 20)) # set size
	ax = dendrogram(linkage_matrix, orientation="right", labels=titles);

	plt.tick_params(\
	    axis= 'x',          # changes apply to the x-axis
	    which='both',      # both major and minor ticks are affected
	    bottom='off',      # ticks along the bottom edge are off
	    top='off',         # ticks along the top edge are off
	    labelbottom='off')

	plt.show()
	plt.close()
	# plt.tight_layout() #show plot with tight layout

	#uncomment below to save figure
	# plt.savefig('ward_clusters.png', dpi=200) #save figure as ward_clusters

def main():
	with open(sourceDir, 'rb') as handle:
		tfidf_matrix = pickle.load(handle)

	with open(titlesFile, 'rb') as handle2:
		titles = pickle.load(handle2)

	with open(featureNamesFile, 'rb') as handle3:
		featureNames = pickle.load(handle3)

	print(tfidf_matrix.shape)

	# Make a List of 24 lists with 24 elements each describing the cosine distance of each document to another
	cosDist = cosineSimilarity(tfidf_matrix)

	# Return a list which describes in which cluster each document belongs
	clusters = kmeans(tfidf_matrix)
	books = { 'title': titles, 'cluster': clusters}
	frame = pd.DataFrame(books, index = [clusters] , columns = ['title', 'cluster'])

	# number of books per cluster (clusters from 0 to 4)
	# print(frame['cluster'].value_counts()) 
	# # book-cluster correspondence
	# for i in xrange(0,24):
	# 	print clusters[i], titles[i]

	# For cosine similarity distance matrix
	# Apply MDS, produce two-dimensional graph
	mds(cosDist, clusters, titles)
	# Apply hierarchical clustering 
	hierarchical_clustering(cosDist,titles)



if __name__ == "__main__":
	main()