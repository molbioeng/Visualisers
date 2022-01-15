"""
Created on Wed Dec 22 17:09 2021
@author: pg

Class for all PCs calculated from an input dataset
"""
import os

from sklearn.decomposition import PCA
import fileList as fL
import numpy as np


# #For testing:
# import mat73

class PrincipalComponent:
    def __init__(self, array, goal_var=0.99):
        # TODO: SET UP ERROR HANDLING FOR GOAL_VAR
        # loadings database variable
        self.name = array[0]
        npArray = np.array(array[1]) #transform into numpy array
        data = npArray.reshape(len(npArray)*len(npArray[0]),len(npArray[0][0])) #Convert 3D array to 2D array NxP
        # self.pca = PCA(3) #3 PCs
        # self.pca = PCA(n_components=0.99) #all possible PCs
        pca = PCA(n_components=None) #all possible PCs
        X_pca =pca.fit(data)

        pca_var_ratio = X_pca.explained_variance_ratio_   #Retrieve explained variance for each PC

        #Set initial variance explained so far
        total_variance = 0.0

        #Set initial number of features
        self.n_components =0

        #For the explained variance of each feature:
        for explained_variance in pca_var_ratio:
            #Add the explained variance to the total
            total_variance+=explained_variance

            #Add one to the number of components
            self.n_components+=1

            #If we reach our goal level of explained variance
            if total_variance >=goal_var:
                #End the loop
                break

        #TO REMOVE LATER##########
        self.n_components =  3
        ##########################
        self.pca = PCA(n_components=self.n_components)
        self.X_pca = self.pca.fit(data)
        self.loadings = self.X_pca.components_.T #Retrieve the loadings values
        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]

        

        self.explained_variance = self.X_pca.explained_variance_ratio_

    def __repr__(self):
        return self.name

    def transform(self,array):
        r_data = self.X_pca.transform(array)
        return r_data
