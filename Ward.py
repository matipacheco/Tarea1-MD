import time
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import normalized_mutual_info_score as nmi
import matplotlib.pyplot as plt

n_clusters = eval(raw_input("\n Ingrese la cantidad de clusters: "))
start_time = time.time()
dataset = pd.read_csv('beer_reviews.csv')

breweries = pd.DataFrame({'brewery_id': dataset['brewery_id']})
breweries = breweries.loc[0:9999, :]
breweries = list(breweries.values.flatten())
beers = pd.DataFrame({'beer_beerid': dataset['beer_beerid']})
beers = beers.loc[0:9999, :]
beers = list(beers.values.flatten())

reviews = pd.DataFrame({'review_overall': dataset['review_overall'], 'review_aroma': dataset['review_aroma'],'review_appearance': dataset['review_appearance'],
                        'review_palate': dataset['review_palate'], 'review_taste': dataset['review_taste'],'beer_abv': dataset['beer_abv']})
reviews = reviews.fillna(0)
reviews = reviews.loc[0:9999,:]
print "Comienzo de fitear ward"
print("--- %s segundos ---" % (time.time() - start_time))
reviews = StandardScaler().fit_transform(reviews)
reviews    = PCA(n_components = 2).fit_transform(reviews)
ward = AgglomerativeClustering(n_clusters = n_clusters, linkage='ward').fit(reviews)
print "Termine de fitear ward"
print("--- %s segundos ---" % (time.time() - start_time))
label = ward.labels_
labels_n = list(ward.labels_)
print "\nnumero de clusters: "+str(n_clusters)
print "Indice NMI para la etiqueta Nombre Cerveceria: " + str(nmi(breweries, labels_n))
print "Indice NMI para la etiqueta Tipo Cerveza: " + str(nmi(beers, labels_n))
print "------------------------------------------------------------\n"

for l in np.unique(label):
    plt.plot(reviews[label == l, 0], reviews[label == l, 1],'o', color=plt.cm.jet(np.float(l) / np.max(label + 1)))
plt.title('Ward con %d clusters' %n_clusters)
plt.show()