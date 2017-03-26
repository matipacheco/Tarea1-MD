import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from drink_beer import *

reviews 		= drink([])
labels, reviews = format_reviews(reviews)

# print labels
# print reviews[0]

## Para reducir la dimensionalidad y poder dibujar los clusters
reviews = PCA(n_components=2).fit_transform(reviews)
k_means = KMeans(init = "k-means++", n_clusters = 3, n_init = 100)

k_means.fit(reviews)
k_means_labels 			= k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = 1000

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reviews[:, 0].min() - 1, reviews[:, 0].max() + 1
y_min, y_max = reviews[:, 1].min() - 1, reviews[:, 1].max() + 1
xx   , yy    = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = k_means.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation = 'nearest', extent = (xx.min(), xx.max(), yy.min(), yy.max()),
			  cmap = plt.cm.Paired, aspect = 'auto', origin = 'lower')

plt.plot(reviews[:, 0], reviews[:, 1], 'k.', markersize = 2)
# Plot the centroids as a white X
centroids = k_means.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s = 169, linewidths = 3, color = 'w', zorder = 10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()