"""
Created on Wed Dec 22 17:09 2021
@author: pg

Class for all PCs calculated from an input dataset
"""

from sklearn.decomposition import PCA
import numpy as np
# #For testing:
# import mat73

class PrincipalComponent:
    def __init__(self,array):
        npArray = np.array(array) #transform into numpy array
        data = npArray.reshape(len(npArray)*len(npArray[0]),len(npArray[0][0])) #Convert 3D array to 2D array NxP
        self.pca = PCA(3) #3 PCs
        self.pca =self.pca.fit(data)
        self.loadings = self.pca.components_.T #Retrieve the loadings values
        self.explained_variance = self.pca.explained_variance_ratio_   #Retrieve explained variance for each PC
    def transform(self,array):
        r_data = self.pca.transform(array)
        return r_data 




# #TEST IT OUT
# matFile = mat73.loadmat('tissue_t3_1_workspace.mat') # .mat file must be in the same local directory
# my_data = np.array(matFile["map_t3"])
# pca_t3 = PrincipalComponent(my_data)
