import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score as NMI

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

n_clusters = int(sys.argv[1])
print "Cantidad de clusters: " + str(n_clusters)

dataset = pd.read_csv('beer_reviews.csv')

reviews = pd.DataFrame({'review_overall':dataset['review_overall'],       'review_aroma':dataset['review_aroma'],
												'review_appearance':dataset['review_appearance'], 'review_palate':dataset['review_palate'],
												'review_taste':dataset['review_taste'],           'beer_abv':dataset['beer_abv']})
reviews = reviews.fillna(0)
reviews = StandardScaler().fit_transform(reviews)
reviews = PCA(n_components = 2).fit_transform(reviews)

k_means = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 10, algorithm = "auto", verbose = 0)
k_means.fit(reviews)

breweries = pd.DataFrame({'brewery_id' :dataset['brewery_id']})
breweries = list(breweries.values.flatten())

beers = pd.DataFrame({'beer_beerid':dataset['beer_beerid']})
beers = list(beers.values.flatten())

labels = list(k_means.labels_)

print "\nIndice NMI para la etiqueta Nombre Cerveceria: " + str(NMI(breweries, labels))
print "\nIndice NMI para la etiqueta Tipo Cerveza: " + str(NMI(beers, labels))
print "\n------------------------------------------------------------\n"

# labels = k_means.labels_

# for l in np.unique(labels):
#     plt.plot(reviews[labels == l, 0], reviews[labels == l, 1], 'o', color = plt.cm.jet(np.float(l) / np.max(labels + 1)))

# plt.title("Clustering K-means con " + str(n_clusters) + " clusters (reducido utilizando PCA)")
# plt.show()