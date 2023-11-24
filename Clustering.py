#python clustering from unsupervised learning 

from sklearn.cluster import KMeans
import numpy as np

# Sample data
data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Creating a KMeans instance with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fitting the data to the KMeans algorithm
kmeans.fit(data)

# Getting the centroids and labels for the clusters
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print("Centroids:")
print(centroids)
print("Labels:")
print(labels)
