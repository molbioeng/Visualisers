# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:33:15 2021

@author: FM

Updated on Sun Jan 2 13:01 2022
@author: pg

"""

#Modules used

from ImageDB import ImageDB
import mat73

class drawing(object):
    def __init__(self):
        self.InputDB = ImageDB()

    def addImageMean(self, currentFile):
        """Adds image to ImageDB"""
        self.InputDB.addImageMean(currentFile)

    def addImagePCA(self, currentFile):
        """Adds image to ImageDB"""
        self.InputDB.addImagePCA(currentFile)

    def addImageKMCluster(self, currentFile, n_clusters):
        """Adds image to ImageKMClustering"""
        self.InputDB.addImageKMCluster(currentFile, n_clusters)

    def displayImage(self, index):
        """plots image of specified index in database in a new window"""
        self.InputDB.displayImage(index)


# TESTING
import mat73
mat = mat73.loadmat('./tissue_t3_1_workspace.mat')
data = mat["map_t3"]
draw = drawing()
draw.addImageMean(data)
#draw.addImagePCA(data)
#draw.addImageKMCluster(data, 3)
draw.displayImage(0)
#draw.displayImage(1)
