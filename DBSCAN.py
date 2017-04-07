import time
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import normalized_mutual_info_score as nmi
import matplotlib.pyplot as plt

min_samples = eval(raw_input("\n Ingrese la cantidad de min_samples: "))
eps = eval(raw_input("\n Ingrese el valor de eps: "))
start_time = time.time()
dataset = pd.read_csv('beer_reviews.csv')

breweries = pd.DataFrame({'brewery_id': dataset['brewery_id']})
breweries = breweries.loc[0:249999, :]
breweries = list(breweries.values.flatten())
beers = pd.DataFrame({'beer_beerid': dataset['beer_beerid']})
beers = beers.loc[0:249999, :]
beers = list(beers.values.flatten())

reviews = pd.DataFrame({'review_overall': dataset['review_overall'], 'review_aroma': dataset['review_aroma'],'review_appearance': dataset['review_appearance'],
                        'review_palate': dataset['review_palate'], 'review_taste': dataset['review_taste'],'beer_abv': dataset['beer_abv']})
reviews = reviews.fillna(0)
reviews = reviews.loc[0:249999, :]
print "Comienzo de fitear DBSCAN"
print("--- %s segundos ---" % (time.time() - start_time))
reviews = StandardScaler().fit_transform(reviews)
reviews    = PCA(n_components = 2).fit_transform(reviews)
db = DBSCAN(eps=eps, min_samples=min_samples, algorithm="ball_tree").fit(reviews)
print "Termine de fitear DBSCAN"
print("--- %s segundos ---" % (time.time() - start_time))
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

labels_n = list(db.labels_)
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print "\nmin_samples: "+ str(min_samples) +" - eps: "+ str(eps) +" - numero de clusters: "+str(n_clusters_)
print "Indice NMI para la etiqueta Nombre Cerveceria: " + str(nmi(breweries, labels_n))
print "Indice NMI para la etiqueta Tipo Cerveza: " + str(nmi(beers, labels_n))
print "------------------------------------------------------------\n"

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
