import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from drink_beer import *

reviews 		= drink([])
labels, reviews = set_reviews(reviews)

# print labels
# print reviews[0]

## Para reducir la dimensionalidad y poder dibujar los clusters
reviews = PCA(n_components=2).fit_transform(reviews)
k_means = KMeans(init = "k-means++", n_clusters = 3, n_init = 100)

k_means.fit(reviews)
k_means_labels 			= k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_

# fig = plt.figure(figsize=(3,3))
# colors = ["#4EACC5","#FF9C34","#4E9A06"]
# ax = fig.add_subplot(1,1,1)
# ax.set_title("KMeans")
# for k, col in zip(range(3), colors):
# 	my_members = k_means_labels == k
# 	ax.plot(X[my_members, 0], X[my_members, 1], "w", markerfacecolor=col, marker=".")

# ax.set_xticks(())
# ax.set_yticks(())
# plt.show()
