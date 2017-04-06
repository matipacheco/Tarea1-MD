import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import normalized_mutual_info_score

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

n_clusters = eval(raw_input("Ingrese la cantidad de clusters: "))

dataset = pd.read_csv('beer_reviews.csv')

reviews = pd.DataFrame({'review_overall':dataset['review_overall'],       'review_aroma':dataset['review_aroma'],
												'review_appearance':dataset['review_appearance'], 'review_palate':dataset['review_palate'],
												'review_taste':dataset['review_taste'],           'beer_abv':dataset['beer_abv']})

reviews = reviews.fillna(0)
reviews = StandardScaler().fit_transform(reviews)

reviews    = PCA(n_components = 2).fit_transform(reviews)
mini_batch = MiniBatchKMeans(init = 'k-means++', n_clusters = n_clusters, batch_size = 1000,
	                           n_init = 100, max_no_improvement = 10, verbose = 0)
mini_batch.fit(reviews)

label = mini_batch.labels_

for l in np.unique(label):
    plt.plot(reviews[label == l, 0], reviews[label == l, 1], 'o', color = plt.cm.jet(np.float(l) / np.max(label + 1)))

plt.title("Clustering MiniBatch K-means con " + str(n_clusters) + " clusters (reducido utilizando PCA)\n"
          "Los centroides estan marcados con una X")
plt.show()