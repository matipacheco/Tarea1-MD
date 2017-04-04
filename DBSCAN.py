import time
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

print "[0] Para clusterizar por la etiqueta Nombre Cerveceria"
print "[1] Para clusterizar por la etiqueta Tipo de Cerveza"

case 			 = eval(raw_input("\n Ingrese opcion: "))

print "[0] Para clusterizar sin normalizar"
print "[1] Para clusterizar normalizando"

case_n 			 = eval(raw_input("\n Ingrese opcion: "))

min_samples = eval(raw_input("\n Ingrese la cantidad de min_samples: "))
eps = eval(raw_input("\n Ingrese el valor de eps: "))
start_time = time.time()
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
reviews = reviews.loc[100000:249999,:]
print "Comienzo de fitear DBSCAN"
print("--- %s segundos ---" % (time.time() - start_time))

if case_n == 1:
    reviews = StandardScaler().fit_transform(reviews)

reviews    = PCA(n_components = 2).fit_transform(reviews)
db = DBSCAN(eps=eps, min_samples=min_samples, algorithm="ball_tree").fit(reviews)
print "Termine de fitear DBSCAN"
print("--- %s segundos ---" % (time.time() - start_time))

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = reviews[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=5)

    xy = reviews[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=2)

plt.title('DBSCAN - Clusters estimados: %d - eps: %f - min_samples: %d' % (n_clusters_,eps,min_samples))
plt.show()