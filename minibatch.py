import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA

print "[0] Para clusterizar por la etiqueta Nombre Cerveceria"
print "[1] Para clusterizar por la etiqueta Tipo de Cerveza"

case 			 = eval(raw_input("\n Ingrese opcion: "))
n_clusters = eval(raw_input("\n Ingrese la cantidad de clusters: "))

dataset = pd.read_csv('beer_reviews.csv')

if case == 0:
	reviews = pd.DataFrame({'brewery_id':dataset['brewery_id'],'review_overall':dataset['review_overall'],
                          'review_aroma':dataset['review_aroma'],'review_appearance':dataset['review_appearance'],
                          'review_palate':dataset['review_palate'],'review_taste':dataset['review_taste'],'beer_abv':dataset['beer_abv']})
else:
	reviews = pd.DataFrame({'beer_beerid':dataset['beer_beerid'],'review_overall':dataset['review_overall'],
                          'review_aroma':dataset['review_aroma'],'review_appearance':dataset['review_appearance'],
                          'review_palate':dataset['review_palate'],'review_taste':dataset['review_taste'],'beer_abv':dataset['beer_abv']})

reviews = reviews.fillna(0)

reviews    = PCA(n_components = 2).fit_transform(reviews)
mini_batch = MiniBatchKMeans(init = 'k-means++', n_clusters = n_clusters, batch_size = 1000,
	                           n_init = 100, max_no_improvement = 10, verbose = 0)
mini_batch.fit(reviews)

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