"""
Created on Wed Dec 22 12:46 2021
@author: pg
Program for PCA analysis
- The script's parts will be implemented separately in classes
"""

import mat73
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
np.set_printoptions(threshold=sys.maxsize)
from sklearn.decomposition import PCA
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans


###############################   WORKFLOW  ####################################
# 1) Import the file and select the data you want to work with
#   - Dimensions could be any (200x200x1024, 500x300x1000 etc.)
# 2) Transform 3D array of data into 2D array (n rows, p columns) where:
#   • Each row is an observation or sample
#   • Each column is a predictor variable
# 3) OPTIONAL BUT RECOMMENDED - standardise data before analysis
#   - User has 3 options:
#        - using z-score method
#        - using standardisation method
#        - using scaling method
# 4) Select 3 Principal Components (PCs) - by default it is set up to 3
# 5) Compute PCA to receive
#        - scores,
#        - loadings,
#        - explained variance
#        - cumulative variance
# 6) create a data frame for explained and cumulative variance for each PC
# 7) create a scree plot
# 8) create a score plot
# 9) create a loadings plot
# 10) a) [Not anymore] Set up RGB channels by combining chosen PCs and create an image
#     b) [Priority] Create an image from each PC

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
#############################  FUNCTIONS #######################################
############################  Preprocessing  ###################################
def normalization(data,normalization='standardscaler'): #User chooses which method to apply
    if normalization=='zscore': #z-score
        scaled_data = stats.zscore(data,axis=0)
         # Axis 0 will act on all the ROWS in each COLUMN
         # Axis 1 will act on all the COLUMNS in each ROW
        return scaled_data
    elif normalization=='standardscaler': # Standardizing the features
        scaled_data = StandardScaler().fit_transform(data)
        return scaled_data
    elif normalization=='scaling':
        scaled_data = scale(data) # Data scaling
        return scaled_data
    else:
        return data


##########################  PCA analysis  ####################################
def get_vector(data, numpc=3, normalization=None):
    #Convert 3D array to 2D array NxP
    # N = number of rows = number of spectra
    #       -> length(1st Dim) x length(2nd Dim)
    # P = number of columns = number of variables
    #       -> length of 3rd Dim
    data2D = data.reshape(len(data[0])*len(data), len(data[0][0]))
    # If you want to print dimensions of the array:
    # print(data2D.shape)
    if normalization != None:
        data2D = normalization(data2D,normalization)
    # 1) create the PCA instance
    pca = PCA(numpc)
    # 2) fit on data
    pca.fit(data2D)
    # Once fit, the eigenvalues and principal components can be accessed
    # on the PCA class via the explained_variance_ and components_ attributes.
    # to access values and vectors
    #   - values: pca.explained_variance_
    #   - vectors: pca.components_
    return pca

def project_data(data,pca):

    data2D = data.reshape(len(data[0])*len(data), len(data[0][0]))

    # 3) transform data
    score= pca.transform(data2D) # reconstructed data
    #dimensions should be the same as for data2D

    # 4) Retrieve the loadings values
    loading = pca.components_.T

    # 5) Retrieve explained variance for each PC
    explainedVariance = pca.explained_variance_ratio_
    return score, loading, explainedVariance

def get_PC_number_list(numpc): #used for labeling data in dataframe
    listPCs=[ 'PC'+str(number) for number in range(1,numpc+1) ]
    return listPCs

############################ Data frame  #######################################
def data_frames(score,loading,explainedVariance,numpc=3):
    pc_number_list = get_PC_number_list(numpc)
    # Retrieve the score values
    df_score = pd.DataFrame(score, columns=pc_number_list)
    # # to call: scores_df.PC1 or score_df.["PC1"]
    df_loading = pd.DataFrame(loading, columns=pc_number_list)
    # Prepare the explained variance data
    explainedVariance = np.insert(explainedVariance,0,0)
    # Prepare the cumulative variance data
    cumulativeVariance =np.cumsum(np.round(explainedVariance,decimals=3))
    # Combining the dataframe
    pc_number_list.insert(0,'')
    pc_df = pd.DataFrame(pc_number_list, columns=['PC'])
    explainedVariance_df = pd.DataFrame(explainedVariance, columns=['Explained Variance'])
    cumulativeVariance_df = pd.DataFrame(cumulativeVariance, columns=['Cumulative Variance'])
    df_explainedVariance = pd.concat([pc_df,explainedVariance_df,cumulativeVariance_df],axis=1)
    return df_score, df_loading,df_explainedVariance

##############################  Scree plot  ####################################
def scree_plot(df_explainedVariance, plot=None):
    if plot == 'separate':
        # Explained Variance + Cumulative Variance (Separate plot)
        fig = make_subplots(rows=1,cols=2)

        fig.add_trace(
            go.Scatter(
                x=df_explained_variance['PC'],
                y=df_explained_variance['Cumulative Variance'],
                marker=dict(size=15,color='LightSeaGreen')
            ), row=1,col=1
            )

        fig.add_trace(
            go.Bar(
                x=df_explained_variance['PC'],
                y=df_explained_variance['Explained Variance'],
                marker=dict(color='RoyalBlue')
            ), row=1,col=2
            )
        fig.show()
    else: #plot together
        fig = make_subplots(rows=1,cols=1)
        fig = px.bar(df_explained_variance, x='PC', y='Explained Variance',text='Explained Variance',width=800)
        fig.update_traces(texttemplate='%{text:.6f}', textposition='outside')
        fig.show()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df_explained_variance['PC'],
                y=df_explained_variance['Cumulative Variance'],
                marker=dict(size=15,color='LightSeaGreen')
            ))

        fig.add_trace(
            go.Bar(
                x=df_explained_variance['PC'],
                y=df_explained_variance['Explained Variance'],
                marker=dict(color='RoyalBlue')
            ))
        fig.show()
#############################  SCORES PLOT #####################################
def scores_plot(df_score,numpc,pc_list=[1,2,3]): #scores plot in 3D
#pc_list is used to select what PCs the user want to plot. By default, it's PC1,PC2,PC3
    if numpc >= 3: #possible only if we have at least 3 PCs
        a = (pc_list[0]-1)
        b = (pc_list[1]-1)
        c = (pc_list[2]-1)
        score_to_plot = df_score.iloc[:,pc_list[0]-1] #extract scores that the user want to plot
        score_to_plot =  np.c_[ score_to_plot, df_score.iloc[:,b] ]
        score_to_plot =  np.c_[ score_to_plot, df_score.iloc[:,c] ]
        pc_list = ['PC'+str(pc_list[0]),'PC'+str(pc_list[1]),'PC'+str(pc_list[2])]
        fig = px.scatter_3d(df_score, x=pc_list[0],y=pc_list[1],z=pc_list[2], opacity=0.5)
        fig.show()
        fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))
###########################  LOADINGS PLOT #####################################
def loadings_plot(loading,pca=[1,2,3]):
    #The use needs to specify which loadings are to going be plotted. By defaults, they are for PC1,PC2,PC3
    pcaLoadings=loading[:,pca[0]-1]
    for i in range(1,len(pca)):
        pcaLoadings = np.c_[pcaLoadings,loading[:,pca[i]-1]]
    if len(pca)==1: #when the user want to plot only one PC
        fig, ax1= plt.subplots(1)
        fig.suptitle('Loadings plots')
        ax1.plot(pcaLoadings[:,0])
        ax1.set_title('PCA'+str(pca[0]))
    elif len(pca)==2: # for two PCs
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Loadings plots')
        ax1.plot(pcaLoadings[:,0])
        ax1.set_title('PCA'+str(pca[0]))
        ax2.plot(pcaLoadings[:,1])
        ax2.set_title('PCA'+str(pca[1]))
    elif len(pca)==3:
        fig, (ax1, ax2,ax3) = plt.subplots(3)
        fig.suptitle('Loadings plots')
        ax1.plot(pcaLoadings[:,0])
        ax1.set_title('PCA'+str(pca[0]))
        ax2.plot(pcaLoadings[:,1])
        ax2.set_title('PCA'+str(pca[1]))
        ax3.plot(pcaLoadings[:,2])
        ax3.set_title('PCA'+str(pca[2]))
        fig.show()
        plt.show()
    elif len(pca)==4:
        fig, (ax1, ax2,ax3,ax4) = plt.subplots(4)
        fig.suptitle('Loadings plots')
        ax1.plot(pcaLoadings[:,0])
        ax1.set_title('PCA'+str(pca[0]))
        ax2.plot(pcaLoadings[:,1])
        ax2.set_title('PCA'+str(pca[1]))
        ax3.plot(pcaLoadings[:,2])
        ax3.set_title('PCA'+str(pca[2]))
        ax4.plot(pcaLoadings[:,3])
        ax4.set_title('PCA'+str(pca[3]))
        fig.show()
        plt.show()
    else: #when it's more than 4, plot each one after the other
        for i in range(len(pcaLoadings)):
            plt.plot(pcaLoadings[:,i])
            plt.set_title('PCA'+str(pca[i]))
            plt.show()

###########################  CREATE RGB CHANNELS ###############################
# #NOT NEEDED ANYMORE
# def rgb_channels(origin_data,scores_array,score_r=1,score_g=2,score_b=3):
#     #The user needs to choose which PCs will be rgb channels. By default it's first 3 scores
#     scoresPCAR = scores_array[:,score_r-1]
#     scoresPCAG = scores_array[:,score_g-1]
#     scoresPCAB = scores_array[:,score_b-1]
#
#     # reshape back to the original set up of data
#     scoresPCAR =  np.reshape(scoresPCAR,(len(origin_data), len(origin_data[0])))
#     scoresPCAG =  np.reshape(scoresPCAG,(len(origin_data), len(origin_data[0])))
#     scoresPCAB =  np.reshape(scoresPCAB,(len(origin_data), len(origin_data[0])))
#
#     #Code to create and show RGB channels:
#     # redChannel = np.zeros([len(origin_data),len(origin_data[0]),3])
#     # greenChannel = np.zeros([len(origin_data),len(origin_data[0]),3])
#     # blueChannel = np.zeros([len(origin_data),len(origin_data[0]),3])
#     #
#     # redChannel[:,:,0] = scoresPCAR # create an channel (X 0 0)
#     # greenChannel[:,:,1] = scoresPCAG # create an channel (0 X 0)
#     # blueChannel[:,:,2] = scoresPCAB # create an channel (0 0 X)
#     #
#     # plt.imshow(redChannel)
#     # plt.show()
#     # plt.imshow(greenChannel)
#     # plt.show()
#     # plt.imshow(blueChannel)
#     # plt.show()
#     return scoresPCAR,scoresPCAG,scoresPCAB
###########################  CREATE FULL IMAGE #################################

#NOT NEEDED ANYMORE
# def create_RGB_image(origin_data,scores_array):
#     channelRed,channelGreen,channelBlue = rgb_channels(origin_data,scores_array)
#     fullImage = np.empty([len(origin_data),len(origin_data[0]),3])
#     fullImage[:,:,0] = channelRed
#     fullImage[:,:,1] = channelGreen
#     fullImage[:,:,2] = channelBlue
#
#     plt.imshow(fullImage)
#     plt.colorbar()
#     plt.show()
#     return fullImage
def display_image(origin_data, score): #allows to display image from any 2D data (projected or clustered)
    reshaped_score =  np.reshape(score,(len(origin_data), len(origin_data[0])))
    plt.imshow(reshaped_score)
    plt.colorbar()
    plt.show()

#CHANGED
# def cluster_data(origin_data,image_to_cluster, n_clusters=10):
#     #The user has to specify the number of clusters for analysis. By default. it's 10
#     Npixels = len(origin_data)*len(origin_data[0])
#     newA = image_to_cluster.reshape([Npixels,3])
#     kmeans = KMeans(n_clusters, random_state=0).fit(newA)
#     clustered_image = kmeans.labels_
#     clustered_image = clustered_image.reshape([len(origin_data),len(origin_data[0])])
#
#     plt.imshow(clustered_image)
#     plt.colorbar()
#     plt.show()
#     return clustered_image

def cluster_data(origin_data,score_to_cluster, n_clusters=10): #inputs projected data and outputs projected data that is grouped into clusters
    #The user has to specify the number of clusters for analysis. By default. it's 10
    kmeans = KMeans(n_clusters,random_state=0).fit(score_to_cluster.reshape(-1,1))
    clustered_score = kmeans.labels_
    clustered_score=clustered_score.reshape([len(origin_data),len(origin_data[0])])
    return clustered_score

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
###########################  LOAD THE FILE  ####################################
# Load the .mat file:
matFile = mat73.loadmat('tissue_t3_1_workspace.mat')
# Select a specific data:
my_data = array(matFile["map_t3"])
# If you want to print dimensions of the array:
# print(data.shape)
principal_comp_analysis = get_vector(my_data)
scores,loadings,explained_variance = project_data(my_data, principal_comp_analysis)
df_scores, df_loadings,df_explained_variance = data_frames(scores,loadings,explained_variance)
scree_plot(df_explained_variance)
scores_plot(df_scores,numpc=3,pc_list=[1,2,3])
loadings_plot(loadings,pca=[1,2,3])
#image = create_RGB_image(my_data,scores) #NOT NEEDED ANYMORE
display_image(my_data, scores[:,0]) #projected onto PC1
display_image(my_data,scores[:,1])
display_image(my_data,scores[:,2])
#cluster_image = cluster_data(my_data,image)
cluster_score1 = cluster_data(my_data,scores[:,0])
cluster_score2 = cluster_data(my_data,scores[:,1])
cluster_score3 = cluster_data(my_data,scores[:,2])
display_image(my_data,cluster_score1) #clustered data projected onto PC1
display_image(my_data,cluster_score2)
display_image(my_data,cluster_score3)


# fig, ax = plt.subplots() #without arguments returns a Figure and a single Axes.
# ax.grid(False)
# image  = ax.imshow(data_r)
# fig.colorbar(image)
# plt.show()
