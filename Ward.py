import time
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

print "[0] Para clusterizar por la etiqueta Nombre Cerveceria"
print "[1] Para clusterizar por la etiqueta Tipo de Cerveza"

case 			 = eval(raw_input("\n Ingrese opcion: "))
n_clusters = eval(raw_input("\n Ingrese la cantidad de clusters: "))
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
reviews = reviews.loc[0:8999,:]
print "Comienzo de fitear ward"
print("--- %s segundos ---" % (time.time() - start_time))
reviews    = PCA(n_components = 2).fit_transform(reviews)
ward = AgglomerativeClustering(n_clusters = n_clusters, linkage='ward').fit(reviews)
print "Termine de fitear ward"
print("--- %s segundos ---" % (time.time() - start_time))

label = ward.labels_
for l in np.unique(label):
    plt.plot(reviews[label == l, 0], reviews[label == l, 1],'o', color=plt.cm.jet(np.float(l) / np.max(label + 1)))
plt.title('Ward con %d clusters' %n_clusters)
plt.show()