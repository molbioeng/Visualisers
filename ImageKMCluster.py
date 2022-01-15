"""
Created on Sun Jan 2 12:27 2022

@author: pg

Class for all of the Raman images reduced by K-means Clustering
"""
from Image import Image
import numpy as np
from sklearn.cluster import KMeans


class ImageKMCluster(Image):
    def __init__(self, array, n_clusters): #inputs projected data and outputs projected data that is grouped into clusters
        super().__init__(array)
        self.name = self.name + '/'+'KMCluster'+str(n_clusters)
        #The user has to specify the number of clusters for analysis. By default. it's 10
        # kmeans = KMeans(n_clusters,random_state=0).fit(np.array.reshape(-1,1))
        kmeans = KMeans(n_clusters,random_state=0).fit(np.reshape(array,(-1,1)))
        clustered_score = kmeans.labels_
        self.img=clustered_score.reshape([len(array),len(array[0])])


    def return_r_data(self):
        return self.img


