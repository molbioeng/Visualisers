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
        goal_var - amount of variance that needs to be explained.
        The goal_var would be used in the future by the program to create all PCs that would fit data
        within this percentage.

        For now, the program is set up to do PC analysis only using the first 3 most important principal components.
        '''

        self.name = array[0]
        array = np.array(array[1]) #transform into numpy array
        data = array.reshape(len(array)*len(array[0]),len(array[0][0])) #Convert 3D array to 2D array NxP

        pca = PCA(n_components=None) #first, compute all possible PCs that can explained on the given data
        fitted_pca_all =pca.fit(data)

        pca_var_ratio = fitted_pca_all.explained_variance_ratio_   #Retrieve explained variance for each PC

        # Code below will calculate the amount of PCs that need to by computed given the goal_var set by the user

        ########################################################################
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
        ########################## Hard-coded setting to 3 PCs:
        self.n_components =  3
        ##########################
        self.pca = PCA(n_components=self.n_components)
        self.fit_pca = self.pca.fit(data)


        self.loadings = self.fit_pca.components_.T #Retrieve the loadings values
        # loadings = princiapl components


        self.explained_variance = self.fit_pca.explained_variance_ratio_


    def __repr__(self): # used to print out a name of PC
        return self.name

    def transform(self,array): #Used in ImagePCA class to reconstruct data
        r_data = self.fit_pca.transform(array) #from sklearn.decomposition module
        return r_data
