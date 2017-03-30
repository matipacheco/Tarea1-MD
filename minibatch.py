import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA

from drink_beer import *

print "[0] Para tomar solo los numeros del dataset"
print "[1] Para tomar solo los scores del dataset"

case 			 = eval(raw_input("\n Ingrese opcion: "))
n_clusters = eval(raw_input("\n Ingrese la cantidad de clusters: "))

reviews = drink([])

if case == 0:
	labels, reviews = get_only_review_numbers(reviews)
else:
	labels, reviews = get_only_review_scores(reviews)

## Para reducir la dimensionalidad y poder dibujar los clusters
reviews 	 = PCA(n_components = 2).fit_transform(reviews)
mini_batch = MiniBatchKMeans(init = 'k-means++', n_clusters = n_clusters,
														 batch_size = 10000, n_init = 100, max_no_improvement = 10)

mini_batch.fit(reviews)
mini_batch_labels 					= mini_batch.labels_
mini_batch_cluster_centers 	= mini_batch.cluster_centers_

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = 1000

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reviews[:, 0].min() - 1, reviews[:, 0].max() + 1
y_min, y_max = reviews[:, 1].min() - 1, reviews[:, 1].max() + 1
xx   , yy    = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = mini_batch.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation = 'nearest', extent = (xx.min(), xx.max(), yy.min(), yy.max()),
			  cmap = plt.cm.Paired, aspect = 'auto', origin = 'lower')

plt.plot(reviews[:, 0], reviews[:, 1], 'k.', markersize = 2)
# Plot the centroids as a white X
centroids = mini_batch.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s = 169, linewidths = 3, color = 'w', zorder = 10)
plt.title("Clustering MiniBatch K-means con " + str(n_clusters) + " clusters (reducido utilizando PCA)\n"
          "Los centroides estan marcados con una X")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()