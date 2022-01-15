# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:30 2021

@author: pg

Class for all of the PCA reduced Raman images
"""

from Image import Image
from PrincipalComponent import PrincipalComponent
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from plotInteract import PlotInteract

class ImagePCA(Image):

    def __init__(self, array, pca):
        super().__init__(array)
        self.name = self.name + '/PCA'
        self.pca = pca
        data = self.data

        #3D Data needs to be transformed into 2D
        # 1 column - one 'slice' of 3D
        data = data.reshape(len(data) * len(data[0]), len(data[0][0]))

        self.scores = self.pca.transform(data)  # reconstructed data

    def return_Image(self, pc):  #Return reconstructed dataset
        # Used for displaying an image in the given window
        # You have to specify the pc number for which the image has to be displayed
        score = self.scores[:, pc - 1]  # get the score for chosen pc
        self.reshaped_score = np.reshape(score, (len(self.data), len(self.data[0])))
        self.img = self.reshaped_score #Updates the reconstructed image
        return self.reshaped_score

    def data_frames(self):
        col_list = []  # Used for creating column names
        for i in range(np.shape(self.scores)[1]):
            col_list.append('PC' + str(i + 1))
        # Retrieve the score values
        self.df_scores = pd.DataFrame(self.scores, columns=col_list)
        #to call: df_scores.PC1 or df_scores.["PC1"]
        self.df_loadings = pd.DataFrame(self.pca.loadings, columns=col_list)
        # Prepare the explained variance data
        explained_variance = np.insert(self.pca.explained_variance, 0, 0)
        # Prepare the cumulative variance data
        cumulative_variance = np.cumsum(np.round(explained_variance, decimals=3))
        # Combining the dataframe
        col_list.insert(0, '') #In the graph cumulative variance would start from zero, so we need first element to be blank
        # pc_df = pd.DataFrame(['','PC1','PC2','PC3'], columns=['PC'])
        pc_df = pd.DataFrame(col_list, columns=['PC'])

        explained_variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance'])
        cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=['Cumulative Variance'])
        self.df_explained_variance = pd.concat([pc_df, explained_variance_df, cumulative_variance_df], axis=1)

    def scree_plot(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Image ' + self.name)
        fig.suptitle('Scree plot')
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


    def scores_plot(self):
        if self.pca.n_components > 3:
            print('More than 3PCs')
            return True
        else:
            fig = plt.figure(1)
            fig.canvas.set_window_title('Image ' + self.name)

            fig.suptitle('Scores plot')
            if self.pca.n_components == 1: #1D scatter plot
                print('One PC')
                ax = fig.add_subplot(111)
                ax.plot(self.df_scores.PC1, ',', color='red')
                ax.set_xlabel('PC1')

                return False  # used for estimating whether there is more than 3PCs calculated
            elif self.pca.n_components == 2: #2D scatter plot
                print('Two PCs')
                ax = fig.add_subplot(111)
                ax.scatter(self.df_scores.PC1, self.df_scores.PC2,
                           c='r',
                           marker='.'
                           )
                ax.set_xlabel('PC1')
                ax.set_ylabel('PC2')

                return False
            elif self.pca.n_components == 3: #3D scatter plot
                print('Three PCs')
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(self.df_scores.PC1, self.df_scores.PC2, self.df_scores.PC3,
                           c='r',
                           marker='o'
                           )
                ax.set_xlabel('PC1')
                ax.set_ylabel('PC2')
                ax.set_zlabel('PC3')

                return False

    def scores_plt_higher_dim(self, bool, dim=2, pc_lst=['PC1', 'PC2']):
        '''
        The function would be used in the future.
        It would allow the user to create scores plot for
        principal components that he/she wants to work on

        For example:
        Instead of plotting 2D scores plot between PC1 and PC2, user can change it into 2D scores plot between PC1 and PC3.
        The same thing can applied for 3D scores plot.
        '''
        if bool == True: #That would be used when the user specifies if he wants to use this method or not
            fig = plt.figure(2)
            fig.canvas.set_window_title('Image ' + self.name)
            fig.suptitle('Scores plot')
            if dim == 2: # 2D plot
                ax = fig.add_subplot(111)
                ax.scatter(self.df_scores[pc_lst[0]], self.df_scores[pc_lst[1]],
                           c='r',
                           marker='.'
                           )
                ax.set_xlabel(pc_lst[0])
                ax.set_ylabel(pc_lst[1])

            elif dim == 3: # 3D plot
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(self.df_scores[pc_lst[0]], self.df_scores[pc_lst[1]], self.df_scores[pc_lst[2]],
                           c='r',
                           marker='o'
                           )
                ax.set_xlabel(pc_lst[0])
                ax.set_ylabel(pc_lst[1])
                ax.set_zlabel(pc_lst[2])

            else:
                print('error')

    def loadings_plot(self):
        n = self.pca.n_components  # to estimate the number of PCs
        n_columns = (n + 3 - 1) // 3  # To estimate the # of subplots (columns)
        # That would be also used for the future approach with the goal_var
        # Depending on goal_var, this may produce more than 3 loadings
        fig = plt.figure(3)
        fig.canvas.set_window_title('Image ' + self.name)
        fig.suptitle('Loadings plots')
        for pc in range(n):
            ax = fig.add_subplot(3, n_columns, pc + 1)
            PCidx = 'PC' + str(pc + 1)
            ax.plot(self.df_loadings[PCidx])
            ax.set_title(PCidx)


############################# FOR TESTING OUT ##################################
# matFile = mat73.loadmat('tissue_t3_1_workspace.mat') # .mat file must be in the same local directory
# my_data = np.array(matFile["map_t3"])
# pca_t3 = PrincipalComponent(my_data)
# image_from_pca = ImagePCA(my_data,pca_t3)
# #image_from_pca.data_frames()
# #image_from_pca.scree_plot()
# #x=image_from_pca.scores_plot()
# #image_from_pca.scores_plt_higher_dim(x)
# #image_from_pca.loadings_plot()
# #clustered_image = ImageKMCluster(image_from_pca.display(1),10)
# #clustered_image.display()
# image_from_pca.display()
# #image_from_pca.display(3)
