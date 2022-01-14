# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:54:13 2021

@author: FM

Updated on Sun Jan 2 13:01 2022
@author: pg

This is a database of all of the Images saved
"""


#Modules used
from ImageMean import ImageMean
from ImagePCA import ImagePCA
from ImageKMCluster import ImageKMCluster


class ImageDB(object):
    """ Image database"""

    #Constructor
    def __init__(self):
        self.images = {} #List of Images

    def addImageMean(self, currentImg):
        """Creates and adds an image to the database"""
        self.images[currentImg.name] = currentImg

    def addImagePCA(self, currentImg):
        """Creates and adds an image to the database"""
        self.images[currentImg.img_name] = currentImg

    def addImageKMCluster(self,currentImg, n_clusters):
        """Creates and adds an image to the database"""
        # self.images.append(ImageKMCluster(currentFile, n_clusters))
        pass

    def displayImage(self, img):
        """Displays image"""
        self.images[img.name].display()
