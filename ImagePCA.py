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
import os
import fileList as fL
from plotInteract import PlotInteract

class ImagePCA(Image):

    def __init__(self, array, pca):
        super().__init__(array)
        self.pca = pca
        data = self.data
        data = data.reshape(len(data) * len(data[0]), len(data[0][0]))
        self.scores = self.pca.transform(data)  # reconstructed data
        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]
        self.name = str(filename) + '/' + str(fL.Array_name) + '/' + 'PCA'
        self.img_name = self.name


    def __repr__(self):
        return self.img_name

    def return_Image(self, pc):  # Used for displaying an image in the given window
        # You have to specify the pc for which the image has to be displayed
        score = self.scores[:, pc - 1]  # get the score for chosen pc
        self.reshaped_score = np.reshape(score, (len(self.data), len(self.data[0])))
        self.img = self.reshaped_score
        return self.reshaped_score


    def display(self,pc_n):
        """Module allows for plot interaction"""

        pc_n_text = 'PC'+str(pc_n)

        self.img_name = self.name+'/'+pc_n_text
        #for img in self.img:

        fig, ax = plt.subplots()
        fig.suptitle(self.img_name)
        imgplt = plt.imshow(self.img)
        plt.colorbar()

        # Plot interaction and connect to event manager

        show = PlotInteract(ax, self.data)
        show.connect()
        plt.show()

    # def display(self): #For displaying image in a separate window
    #     plt.imshow(self.img)
    #     plt.colorbar()
    #     plt.show()

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
        # self.df_scores = pd.DataFrame(self.scores, columns=['PC1','PC2','PC3'])
        self.df_scores = pd.DataFrame(self.scores, columns=col_list)
        # print(self.df_scores)
        # # to call: df_scores.PC1 or df_scores.["PC1"]
        self.df_loadings = pd.DataFrame(self.pca.loadings, columns=col_list)
        # self.df_loadings = pd.DataFrame(self.pca.loadings, columns=['PC1','PC2','PC3'])
        # Prepare the explained variance data
        explained_variance = np.insert(self.pca.explained_variance, 0, 0)
        # Prepare the cumulative variance data
        cumulative_variance = np.cumsum(np.round(explained_variance, decimals=3))
        # Combining the dataframe
        col_list.insert(0, '')
        # pc_df = pd.DataFrame(['','PC1','PC2','PC3'], columns=['PC'])
        pc_df = pd.DataFrame(col_list, columns=['PC'])

        explained_variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance'])
        cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=['Cumulative Variance'])
        self.df_explained_variance = pd.concat([pc_df, explained_variance_df, cumulative_variance_df], axis=1)
        # print(self.df_explained_variance)

    def scree_plot(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Image ' + self.name)

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
        if self.pca.n_components > 3:
            print('More than 3PCs')
            return True
        else:
            fig = plt.figure()
            fig.canvas.set_window_title('Image ' + self.name)

            fig.suptitle('Scores plot')
            if self.pca.n_components == 1:
                print('One PC')
                ax = fig.add_subplot(111)
                ax.plot(self.df_scores.PC1, ',', color='red')
                ax.set_xlabel('PC1')
                plt.show()
                return False  # used for estimating whether there is more than 3PCs calculated
            elif self.pca.n_components == 2:
                print('Two PCs')
                ax = fig.add_subplot(111)
                ax.scatter(self.df_scores.PC1, self.df_scores.PC2,
                           c='r',
                           marker='.'
                           )
                ax.set_xlabel('PC1')
                ax.set_ylabel('PC2')
                plt.show()
                return False
            elif self.pca.n_components == 3:
                print('Three PCs')
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(self.df_scores.PC1, self.df_scores.PC2, self.df_scores.PC3,
                           c='r',
                           marker='o'
                           )
                ax.set_xlabel('PC1')
                ax.set_ylabel('PC2')
                ax.set_zlabel('PC3')
                plt.show()
                return False

    def scores_plt_higher_dim(self, bool, dim=2, pc_lst=['PC1', 'PC2']):
        if bool == True:
            fig = plt.figure()
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
                plt.show()
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
                plt.show()
            else:
                print('error')

    def loadings_plot(self):
        n = self.pca.n_components  # to estimate the number of PCs
        n_columns = (n + 3 - 1) // 3  # To estimate the # of subplots (columns)
        fig = plt.figure()
        fig.canvas.set_window_title('Image ' + self.name)
        fig.suptitle('Loadings plots')
        for pc in range(n):
            ax = fig.add_subplot(3, n_columns, pc + 1)
            PCidx = 'PC' + str(pc + 1)
            ax.plot(self.df_loadings[PCidx])
            ax.set_title(PCidx)
        plt.show()

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