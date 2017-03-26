import scipy
import sklearn
import numpy as np
import matplotlib.pyplot as plt

from drink_beer import *

reviews = drink([])
labels, reviews = set_reviews(reviews)

print labels
print reviews[0]

# from sklearn.datasets.samples_generator import make_blobs
# np.random.seed(0)
# centers = [[1,1],[-1,-1],[1,-1]]
# X, labels_true = make_blobs(n_samples=5000, centers=centers, cluster_std=0.7)

# from sklearn.cluster import KMeans
# k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
# k_means.fit(X)
# k_means_labels = k_means.labels_
# k_means_cluster_centers = k_means.cluster_centers_

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
