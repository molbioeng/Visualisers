# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:30 2021

@author: thefr

Class for all of the PCA reduced Raman images
"""

from Image import Image
from PrincipalComponent import PrincipalComponent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#For testing out:
import mat73

class ImagePCA(Image):

    def __init__(self,array,pca):
        self.array = array
        self.pca = pca
        data = np.array(array)
        self.data = data.reshape(len(data)*len(data[0]),len(data[0][0]))
        self.scores = self.pca.transform(self.data)  # reconstructed data

    def display(self, pc): #You have to specify the pc for which the image has to be displayed
        score = self.scores[:,pc-1] #get the score for chosen pc
        reshaped_score =  np.reshape(score,(len(self.array), len(self.array[0])))
        plt.imshow(reshaped_score)
        plt.colorbar()
        plt.show()

    def data_frames(self):
        # Retrieve the score values
        self.df_scores = pd.DataFrame(self.scores, columns=['PC1','PC2','PC3'])
        # # to call: df_scores.PC1 or df_scores.["PC1"]
        self.df_loadings = pd.DataFrame(self.pca.loadings, columns=['PC1','PC2','PC3'])
        # Prepare the explained variance data
        explained_variance = np.insert(self.pca.explained_variance,0,0)
        # Prepare the cumulative variance data
        cumulative_variance =np.cumsum(np.round(explained_variance,decimals=3))
        # Combining the dataframe
        pc_df = pd.DataFrame(['','PC1','PC2','PC3'], columns=['PC'])
        explained_variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance'])
        cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=['Cumulative Variance'])
        self.df_explained_variance = pd.concat([pc_df,explained_variance_df,cumulative_variance_df],axis=1)
        # print(self.df_explained_variance)

    def scree_plot(self):
        fig, ax = plt.subplots()
        ax.plot(
                self.df_explained_variance['PC'],
                self.df_explained_variance['Cumulative Variance'],
                label='Cumulative Variance',
                marker='.',
                color='#458B74'
                )
        ax.bar(
                self.df_explained_variance['PC'],
                self.df_explained_variance['Explained Variance'],
                label='Explained Variance',
                color='#98F5FF'
                )
        plt.legend()
        plt.show()
    def scores_plot(self):
        fig =plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.df_scores.PC1, self.df_scores.PC2, self.df_scores.PC3,
                    c='r',
                    marker='o'
                    )
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_zlabel('PC3')
        plt.show()
    def loadings_plot(self):
        fig, (ax1,ax2,ax3) = plt.subplots(3)
        fig.suptitle('Loadings plots')
        ax1.plot(self.df_loadings.PC1)
        ax1.set_title('PC1')
        ax2.plot(self.df_loadings.PC2)
        ax2.set_title('PC2')
        ax3.plot(self.df_loadings.PC3)
        ax3.set_title('PC3')
        fig.show()
        plt.show()

######## FOR TESTING OUT #####
# matFile = mat73.loadmat('tissue_t3_1_workspace.mat') # .mat file must be in the same local directory
# my_data = np.array(matFile["map_t3"])
# pca_t3 = PrincipalComponent(my_data)
# image_from_pca = ImagePCA(my_data,pca_t3)
# image_from_pca.data_frames()
# image_from_pca.scree_plot()
# image_from_pca.scores_plot()
# image_from_pca.loadings_plot()
# image_from_pca.display(1) #display the image from projection onto PC1
# image_from_pca.display(2)
# image_from_pca.display(3)
