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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from plotInteract import PlotInteract

class ImagePCA(Image):

    def __init__(self, array, pca):
        super().__init__(array)
        self.name = self.name + '/PCA'
        self.pca = pca
        data = self.data #instantiate data for reconstruction
        data = data.reshape(len(data) * len(data[0]), len(data[0][0]))
        self.scores = self.pca.transform(data)  # reconstructed data (it consists of 3 long columns which are called scores)

    def return_Image(self, pc):  # Used for displaying an image in the given window
        # The pc number for which the image has to be displayed must be specified
        score = self.scores[:, pc - 1]  # get the score for the chosen pc
        self.reshaped_score = np.reshape(score, (len(self.data), len(self.data[0])))
        #recostructed data need to be reshaped before plotting
        self.img = self.reshaped_score #reconstructed image updated
        return self.reshaped_score


    def preview(self, pc):  # For dislaying image in a separate window (no navigation bar)
        self.img = self.return_Image(self, pc)
        import matplotlib as mpl
        mpl.rcParams['toolbar'] = 'None'
        plt.imshow(self.img)
        plt.axis('off')
        plt.show()
        mpl.rcParams['toolbar'] = 'toolbar2'

    def data_frames(self):
        col_list = []  # Used for creating column names
        for i in range(np.shape(self.scores)[1]):
            col_list.append('PC' + str(i + 1))
        # Retrieve the score values
        self.df_scores = pd.DataFrame(self.scores, columns=col_list)
        # # to call: df_scores.PC1 or df_scores.["PC1"]
        self.df_loadings = pd.DataFrame(self.pca.loadings, columns=col_list)

        # Prepare the explained variance data
        explained_variance = np.insert(self.pca.explained_variance, 0, 0)
        # Prepare the cumulative variance data
        cumulative_variance = np.cumsum(np.round(explained_variance, decimals=3))
        # Combining the dataframe
        col_list.insert(0, '') #Used to plot cumulative variance on the plot
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
            if self.pca.n_components == 1: #1D plot
                print('One PC')
                ax = fig.add_subplot(111)
                ax.plot(self.df_scores.PC1, ',', color='red')
                ax.set_xlabel('PC1')

                return False  # used for estimating whether there is more than 3PCs calculated
            elif self.pca.n_components == 2: #2D plot
                print('Two PCs')
                ax = fig.add_subplot(111)
                ax.scatter(self.df_scores.PC1, self.df_scores.PC2,
                           c='r',
                           marker='.'
                           )
                ax.set_xlabel('PC1')
                ax.set_ylabel('PC2')

                return False
            elif self.pca.n_components == 3: #3D plot
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
        This method would be used in the future approach.
        The user would select the PCs that he/she want to plot against each other

        Example:
        Instead of plotting 2D plot of scores between PC1 and PC2, he can plot PC1 against PC3
        (if # of components is greater or equal to 3 in this case)
        '''
        if bool == True:
            fig = plt.figure(2)
            fig.canvas.set_window_title('Image ' + self.name)
            fig.suptitle('Scores plot')
            if dim == 2:
                print('2D')
                ax = fig.add_subplot(111)
                ax.scatter(self.df_scores[pc_lst[0]], self.df_scores[pc_lst[1]],
                           c='r',
                           marker='.'
                           )
                ax.set_xlabel(pc_lst[0])
                ax.set_ylabel(pc_lst[1])

            elif dim == 3:
                print('3D')
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
        '''
        This would be useful in the future approach when there is more than 3 principal components.
        The method would adjust plots depending on n_components.
        '''
        fig = plt.figure(3)
        fig.canvas.set_window_title('Image ' + self.name)
        fig.suptitle('Loadings plots')
        for pc in range(n):
            ax = fig.add_subplot(3, n_columns, pc + 1)
            PCidx = 'PC' + str(pc + 1)
            ax.plot(self.df_loadings[PCidx])
            ax.set_title(PCidx)


######## FOR TESTING OUT #####
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
