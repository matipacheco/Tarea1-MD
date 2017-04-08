import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df_full = pd.read_csv('beer_reviews.csv')

n_clusters = eval(raw_input("\n Ingrese la cantidad de clusters para los 12 k-means: "))

# 6 datasets para brewery_id vs un campo numerico con las primeras 100000 filas
"""
df_brewery_id_review_overall = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_overall':df_full['review_overall']})
df_brewery_id_review_overall_not_full = df_brewery_id_review_overall.loc[0:99999,:]
print df_brewery_id_review_overall_not_full.describe()
k_means1 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means1.fit(df_brewery_id_review_overall_not_full)

df_brewery_id_review_aroma = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_aroma':df_full['review_aroma']})
df_brewery_id_review_aroma_not_full = df_brewery_id_review_aroma.loc[0:99999,:]
print df_brewery_id_review_aroma_not_full.describe()
k_means2 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means2.fit(df_brewery_id_review_aroma_not_full)

df_brewery_id_review_appearance = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_appearance':df_full['review_appearance']})
df_brewery_id_review_appearance_not_full = df_brewery_id_review_appearance.loc[0:99999,:]
print df_brewery_id_review_appearance_not_full.describe()
k_means3 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means3.fit(df_brewery_id_review_appearance_not_full)

df_brewery_id_review_palate = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_palate':df_full['review_palate']})
df_brewery_id_review_palate_not_full = df_brewery_id_review_palate.loc[0:99999,:]
print df_brewery_id_review_palate_not_full.describe()
k_means4 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means4.fit(df_brewery_id_review_palate_not_full)

df_brewery_id_review_taste = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_taste':df_full['review_taste']})
df_brewery_id_review_taste_not_full = df_brewery_id_review_taste.loc[0:99999,:]
print df_brewery_id_review_taste_not_full.describe()
k_means5 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means5.fit(df_brewery_id_review_taste_not_full)

df_brewery_id_beer_abv = pd.DataFrame({'brewery_id':df_full['brewery_id'],'beer_abv':df_full['beer_abv']})
df_brewery_id_beer_abv_not_full = df_brewery_id_beer_abv.loc[0:99999,:]
df_brewery_id_beer_abv_not_full = df_brewery_id_beer_abv_not_full.fillna(0)
print df_brewery_id_beer_abv_not_full.describe()
k_means6 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means6.fit(df_brewery_id_beer_abv_not_full)

# 6 datasets para beer_beerid vs un campo numerico con las primeras 100000 filas

df_beer_beerid_review_overall = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_overall':df_full['review_overall']})
df_beer_beerid_review_overall_not_full = df_beer_beerid_review_overall.loc[0:99999,:]
print df_beer_beerid_review_overall_not_full.describe()
k_means7 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means7.fit(df_beer_beerid_review_overall_not_full)

df_beer_beerid_review_aroma = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_aroma':df_full['review_aroma']})
df_beer_beerid_review_aroma_not_full = df_beer_beerid_review_aroma.loc[0:99999,:]
print df_beer_beerid_review_aroma_not_full.describe()
k_means8 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means8.fit(df_beer_beerid_review_aroma_not_full)

df_beer_beerid_review_appearance = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_appearance':df_full['review_appearance']})
df_beer_beerid_review_appearance_not_full = df_beer_beerid_review_appearance.loc[0:99999,:]
print df_beer_beerid_review_appearance_not_full.describe()
k_means9 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means9.fit(df_beer_beerid_review_appearance_not_full)

df_beer_beerid_review_palate = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_palate':df_full['review_palate']})
df_beer_beerid_review_palate_not_full = df_beer_beerid_review_palate.loc[0:99999,:]
print df_beer_beerid_review_palate_not_full.describe()
k_means10 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means10.fit(df_beer_beerid_review_palate_not_full)

df_beer_beerid_review_taste = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_taste':df_full['review_taste']})
df_beer_beerid_review_taste_not_full = df_beer_beerid_review_taste.loc[0:99999,:]
print df_beer_beerid_review_taste_not_full.describe()
k_means11 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means11.fit(df_beer_beerid_review_taste_not_full)

df_beer_beerid_beer_abv = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'beer_abv':df_full['beer_abv']})
df_beer_beerid_beer_abv_not_full = df_beer_beerid_beer_abv.loc[0:99999,:]
df_beer_beerid_beer_abv_not_full = df_beer_beerid_beer_abv_not_full.fillna(0)
print df_beer_beerid_beer_abv_not_full.describe()
k_means12 = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means12.fit(df_beer_beerid_beer_abv_not_full)
"""
df_brewery_id_vs_6 = pd.DataFrame({'brewery_id':df_full['brewery_id'],'review_overall':df_full['review_overall'],
                                   'review_aroma':df_full['review_aroma'],'review_appearance':df_full['review_appearance'],
                                   'review_palate':df_full['review_palate'],'review_taste':df_full['review_taste'],'beer_abv':df_full['beer_abv']})
df_brewery_id_vs_6_not_full = df_brewery_id_vs_6.loc[0:99999,:]
df_brewery_id_vs_6_not_full = df_brewery_id_vs_6_not_full.fillna(0)
print df_brewery_id_vs_6_not_full.describe()
k_means_brewery_id = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means_brewery_id.fit(df_brewery_id_vs_6_not_full)

df_beer_beerid_vs_6 = pd.DataFrame({'beer_beerid':df_full['beer_beerid'],'review_overall':df_full['review_overall'],
                                   'review_aroma':df_full['review_aroma'],'review_appearance':df_full['review_appearance'],
                                   'review_palate':df_full['review_palate'],'review_taste':df_full['review_taste'],'beer_abv':df_full['beer_abv']})
df_beer_beerid_vs_6_not_full = df_beer_beerid_vs_6.loc[0:99999,:]
df_beer_beerid_vs_6_not_full = df_beer_beerid_vs_6_not_full.fillna(0)
print df_beer_beerid_vs_6_not_full.describe()
k_means1_beer_beerid = KMeans(init = "k-means++", n_clusters = n_clusters, n_init = 100)
k_means1_beer_beerid.fit(df_beer_beerid_vs_6_not_full)

