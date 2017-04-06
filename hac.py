import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import AgglomerativeClustering as HAC
from sklearn.metrics import normalized_mutual_info_score as NMI

n_clusters = int(sys.argv[1])
print "Cantidad de clusters: " + str(n_clusters)

dataset = pd.read_csv('beer_reviews.csv')

reviews = pd.DataFrame({'review_overall':dataset['review_overall'],       'review_aroma':dataset['review_aroma'],
												'review_appearance':dataset['review_appearance'], 'review_palate':dataset['review_palate'],
												'review_taste':dataset['review_taste'],           'beer_abv':dataset['beer_abv']})
reviews = reviews.fillna(0)
reviews = reviews.loc[0:19999,:]
reviews = StandardScaler().fit_transform(reviews)
reviews = PCA(n_components = 2).fit_transform(reviews)

hac 		= HAC(linkage = 'complete', n_clusters = n_clusters, affinity = 'euclidean', connectivity = None)
hac.fit(reviews)

breweries = pd.DataFrame({'brewery_id' :dataset['brewery_id']})
breweries = breweries.loc[0:19999,:]
breweries = list(breweries.values.flatten())

beers = pd.DataFrame({'beer_beerid':dataset['beer_beerid']})
beers = beers.loc[0:19999,:]
beers = list(beers.values.flatten())

labels = hac.labels_

print "\nIndice NMI para la etiqueta Nombre Cerveceria: " + str(NMI(breweries, labels))
print "\nIndice NMI para la etiqueta Tipo Cerveza: " + str(NMI(beers, labels))
print "\n-----------------------------------------------------------------\n"

# for l in np.unique(label):
#     plt.plot(reviews[label == l, 0], reviews[label == l, 1], 'o', color = plt.cm.jet(np.float(l) / np.max(label + 1)))

# plt.title("Clustering HAC con " + str(n_clusters) + " clusters (reducido utilizando PCA)")
# plt.show()