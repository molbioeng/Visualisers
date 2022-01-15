"""
Created on Sun Jan 2 12:27 2022

@author: pg

Class for all of the Raman images reduced by K-means Clustering
"""
from Image import Image
import numpy as np
from sklearn.cluster import KMeans


class ImageKMCluster(Image):
    def __init__(self, image, n_clusters): #inputs projected data and outputs projected data that is grouped into clusters
        super().__init__((image.name, image.data))
        self.name = self.name + '/'+'KMCluster'+str(n_clusters)
        #The name would consist of number of clusters used for analysis.
        
        kmeans = KMeans(n_clusters,random_state=0).fit(np.reshape(image.img,(-1,1)))
        #Data is reshaped into one single columns for analysis
        clustered_score = kmeans.labels_
        self.img=clustered_score.reshape([len(image.img),len(image.img[0])])
        #In order to display, data has to be reshaped back

    def return_r_data(self):
        return self.img
