"""
Created on Sun Jan 2 12:27 2022

@author: pg

Class for all of the Raman images reduced by K-means Clustering
"""
from Image import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class ImageKMCluster(Image):
    def __init__(self,array,n_clusters): #inputs projected data and outputs projected data that is grouped into clusters
        #The user has to specify the number of clusters for analysis. By default. it's 10
        kmeans = KMeans(n_clusters,random_state=0).fit(array.reshape(-1,1))
        clustered_score = kmeans.labels_
        self.clustered_score=clustered_score.reshape([len(array),len(array[0])])

    def display(self):
        plt.imshow(self.clustered_score)
        plt.colorbar()
        plt.show()
