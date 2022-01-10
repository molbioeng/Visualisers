# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:33:15 2021

@author: FM

Updated on Sun Jan 2 13:01 2022


@author: FM

Updated on Sun Jan 2 13:01 2022
@author: pg


"""

#Modules used

from ImageDB import ImageDB

import mat73


class drawing(object):
    def __init__(self):
        self.imgDB = ImageDB()

    def addImageMean(self, currentImg):
        """Adds image to ImageDB"""
        self.imgDB.addImageMean(currentImg)

    def addImagePCA(self, imgPCA):
        """Adds image to ImageDB"""
        self.imgDB.addImagePCA(imgPCA)

    def addImageKMCluster(self, currentFile, n_clusters):
        """Adds image to ImageKMClustering"""
        self.imgDB.addImageKMCluster(currentFile, n_clusters)

    def displayImage(self, img):
        self.imgDB.displayImage(img)

