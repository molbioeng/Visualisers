"""
Created on Wed Dec 22 17:09 2021
@author: pg

Class for all PCs calculated from an input dataset
"""
import os
from sklearn.decomposition import PCA
import fileList as fL
import numpy as np


class PrincipalComponent:
    def __init__(self, array, goal_var=0.99):
        '''
        TODO:
        For now, the program always computes the first 3 principal components
        on the given dataset

        In the future approach, user would type a goal variance.
        goal_var - amount of variance that needs to be explained
        The program would then automatically compute the exact amount of PCs
        that can fit the given variance.

        '''
        array = np.array(array) #transform into numpy array
        data = array.reshape(len(array)*len(array[0]),len(array[0][0])) #Convert 3D array to 2D array NxP

        '''
        The section below would be used in the future to
        calculate all necessary PCs that can explain the amount of variance
        specified by the user (goal_var)
        '''
        ########################################################################
        pca = PCA(n_components=None) #all possible PCs
        fit_pca_all =pca.fit(data) #fit all PCs into data

        pca_var_ratio = fit_pca_all.explained_variance_ratio_   #Retrieve explained variance for each PC

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
        ########################################################################
        ########################## hard-coded number of PCs (3)
        self.n_components =  3
        ##########################
        self.pca = PCA(n_components=self.n_components)
        self.fit_pca = self.pca.fit(data)

        self.loadings = self.fit_pca.components_.T #Retrieve the loadings values

        self.explained_variance = self.fit_pca.explained_variance_ratio_

        ######################### Create a name of this object
        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]
        self.name = str(filename)+ '/' + str(fL.Array_name)
        # The name consists of the name of the file and name of the array where
        # the dataset comes from

    def __repr__(self): # used to print out the name of the object
        return self.name

    def transform(self,array):
        r_data = self.fit_pca.transform(array) #from module sklearn.decomposition
        return r_data
