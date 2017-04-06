import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering as HAC

n_clusters = eval(raw_input("Ingrese la cantidad de clusters: "))

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

x_min, x_max = np.min(reviews, axis = 0), np.max(reviews, axis = 0)
reviews      = (reviews - x_min) / (x_max - x_min)

for i in range(reviews.shape[0]):
	plt.text(reviews[i,0], reviews[i,1], 'x',
	color    = plt.cm.spectral(hac.labels_[i] / 10.))

plt.title("Clustering HAC con " + str(n_clusters) + " clusters (reducido utilizando PCA)")
plt.show()